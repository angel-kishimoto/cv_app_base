from typing import Callable

import cv2
import numpy as np

from draw import Draw
from key import Key
from mouse import Mouse


class Window:
    def __init__(self, id: str, option=None):
        self.__id = id

        self.__option = option if option is not None else cv2.WINDOW_NORMAL
        self.__title: str = self.__id

    def __enter__(self):
        cv2.namedWindow(self.__id, self.__option)
        self.set_title(self.__title)
        return self

    def __exit__(self, *_):
        cv2.destroyWindow(self.__id)
        del self

    def imshow(self, image: np.ndarray):
        cv2.imshow(self.__id, image)

    def set_title(self, title: str):
        self.__title = title
        cv2.setWindowTitle(self.__id, title)

    def set_callback(self, callback: Callable, params=None):
        """
        callback(event: int, x: int, y: int, flags: int, param)
        """
        cv2.setMouseCallback(self.__id, callback, params)


if __name__ == "__main__":

    def null(shape=(1000, 1000, 3)):
        return np.zeros(shape, np.uint8)

    canvas = null()

    mouse = Mouse()
    with Window("test") as window:
        window.set_callback(mouse)

        while True:
            window.imshow(canvas)
            canvas = null()

            key = Key.wait_key()
            if key in [Key.Q, Key.ESC]:
                break

            if key == Key.R:
                canvas = null()

            center = mouse.x, mouse.y
            Draw.circle(canvas, center)

            if mouse.is_rdown:
                Draw.circle(canvas, center, color=(0, 0, 255), radius=60)
