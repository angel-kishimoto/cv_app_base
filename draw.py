from typing import Tuple

import cv2
import numpy as np

Color = Tuple[int, int, int]
Point = Tuple[int, int]


class Draw:
    @staticmethod
    def circle(
        canvas: np.ndarray,
        center: Point,
        color: Color = (255, 255, 255),
        radius: int = 20,
        thickness: int = 2,
    ) -> np.ndarray:
        return cv2.circle(canvas, center, radius, color, thickness)
