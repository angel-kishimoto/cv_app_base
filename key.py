from enum import IntEnum

import cv2


class Key(IntEnum):
    Q = ord("q")
    R = ord("r")
    ESC = 27
    UNKNOWN = -1

    @staticmethod
    def wait_key(wait=1) -> "Key":
        key = cv2.waitKey(wait) & 0xFF
        has_key = key in Key._value2member_map_
        return Key(key) if has_key else Key.UNKNOWN
