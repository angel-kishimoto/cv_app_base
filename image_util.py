from typing import List, Tuple

import cv2
import numpy as np


def to_rgb(image: np.ndarray) -> np.ndarray:
    if len(image.shape) == 3:
        return image
    return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

def to_gray(image: np.ndarray) -> np.ndarray:
    if len(image.shape) == 2:
        return image
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def zeros(size: Tuple[int, int]) -> np.ndarray:
    height, width = size
    return np.zeros((height, width, 3), np.uint8)

def padding(image: np.ndarray, max_h: int = 0, max_w: int = 0):
    im_h, im_w = image.shape[:2]
    dst_h, dst_w = max(im_h, max_h), max(im_w, max_w)

    canvas = zeros((dst_h, dst_w))
    canvas[:im_h, :im_w, :] = image
    return canvas

def hconcat(images: List[np.ndarray]) -> np.ndarray:
    if not images:
        return cv2.hconcat([])

    max_h = max([image.shape[0] for image in images])

    return cv2.hconcat([padding(image, max_h=max_h) for image in images])

def vconcat(images: List[np.ndarray]) -> np.ndarray:
    if not images:
        return cv2.vconcat([])

    max_w = max([image.shape[1] for image in images])

    return cv2.vconcat([padding(image, max_w=max_w) for image in images])
