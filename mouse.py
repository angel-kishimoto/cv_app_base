from dataclasses import dataclass

import cv2


@dataclass
class Mouse:
    x: int = -1
    y: int = -1
    event: int = -1
    is_down: bool = False
    is_rdown: bool = False

    def __call__(self, event, x, y, flag, params):
        self.x, self.y, self.event = x, y, event

        if self.lbutton_down:
            self.is_down = True
        if self.lbutton_up:
            self.is_down = False
        if self.rbutton_down:
            self.is_rdown = True
        if self.rbutton_up:
            self.is_rdown = False

    @property
    def lbutton_down(self) -> bool:
        return self.event == cv2.EVENT_LBUTTONDOWN

    @property
    def lbutton_up(self) -> bool:
        return self.event == cv2.EVENT_LBUTTONUP

    @property
    def button_move(self) -> bool:
        return self.event == cv2.EVENT_MOUSEMOVE

    @property
    def rbutton_up(self) -> bool:
        return self.event == cv2.EVENT_RBUTTONUP

    @property
    def rbutton_down(self) -> bool:
        return self.event == cv2.EVENT_RBUTTONDOWN
