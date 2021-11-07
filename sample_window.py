import image_util
from draw import Draw
from key import Key
from mouse import Mouse
from window import Window

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
