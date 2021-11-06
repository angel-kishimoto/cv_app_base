from typing import List, Tuple

import cv2
import numpy as np


class Image:
    @staticmethod
    def to_rgb(image: np.ndarray) -> np.ndarray:
        if len(image.shape) == 3:
            return image
        return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    @staticmethod
    def to_gray(image: np.ndarray) -> np.ndarray:
        if len(image.shape) == 2:
            return image
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def zeros(size: Tuple[int, int]) -> np.ndarray:
        height, width = size
        return np.zeros((height, width, 3), np.uint8)

    @staticmethod
    def hconcat(images: List[np.ndarray]) -> np.ndarray:
        if not images:
            return cv2.hconcat([])

        max_h = max([image.shape[0] for image in images])

        def padding(image: np.ndarray) -> np.ndarray:
            h, w = image.shape[:2]
            canvas = Image.zeros((max_h, w))
            canvas[:h, :w, :] = image
            return canvas

        return cv2.hconcat([padding(image) for image in images])

    @staticmethod
    def vconcat(images: List[np.ndarray]) -> np.ndarray:
        if not images:
            return cv2.vconcat([])

        max_w = max([image.shape[1] for image in images])

        def padding(image: np.ndarray) -> np.ndarray:
            h, w = image.shape[:2]
            canvas = Image.zeros((h, max_w))
            canvas[:h, :w, :] = image
            return canvas

        return cv2.vconcat([padding(image) for image in images])


if __name__ == "__main__":

    red = Image.zeros((100, 200))
    red[:, :, 2] = 255

    blue = Image.zeros((200, 200))
    blue[:, :, 0] = 255

    a = Image.hconcat([red, blue])
    b = Image.vconcat([red, blue])

    c = Image.hconcat([a, b])

    cv2.namedWindow("test", cv2.WINDOW_NORMAL)

    from key import Key

    while True:
        cv2.imshow("test", c)
        key = Key.wait_key()

        if key == Key.Q:
            break
    cv2.destroyAllWindows()
