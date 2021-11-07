from typing import Callable

import cv2
import numpy as np


class Window:
    def __init__(self, id: str, option: int = None):
        self.__id = id
        self.__option: int = option if option is not None else cv2.WINDOW_NORMAL
        self.__title: str = self.__id

    def __enter__(self):
        cv2.namedWindow(self.__id, self.__option)
        self.set_window_title(self.__title)
        return self

    def __exit__(self, *_):
        cv2.destroyWindow(self.__id)

    def imshow(self, image: np.ndarray):
        cv2.imshow(self.__id, image)

    def set_window_title(self, title: str):
        self.__title = title
        cv2.setWindowTitle(self.__id, title)

    def set_mouse_callback(self, callback: Callable, params=None):
        """
        callback(event: int, x: int, y: int, flags: int, param)
        """
        cv2.setMouseCallback(self.__id, callback, params)
