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


if __name__ == "__main__":
    import image_util
    from draw import Draw
    from key import Key
    from mouse import Mouse

    canvas_size = (1000, 1000)
    canvas = image_util.zeros(canvas_size)

    mouse = Mouse()

    with Window("test") as window:
        window.set_mouse_callback(mouse)

        while True:
            window.imshow(canvas)
            canvas = image_util.zeros(canvas_size)

            key = Key.wait_key()
            if key in [Key.q, Key.ESC]:
                break

            center = mouse.x, mouse.y

            if mouse.is_rdown:
                Draw.circle(canvas, center, color=(0, 0, 255), radius=60)

            Draw.circle(canvas, center)
