import image_util
from key import Key
from window import Window

red = image_util.zeros((100, 200))
red[:, :, 2] = 255

blue = image_util.zeros((200, 200))
blue[:, :, 0] = 255

a = image_util.hconcat([red, blue])
b = image_util.vconcat([red, blue])

c = image_util.hconcat([a, b])


with Window("test") as window:
    while True:
        window.imshow(c)
        key = Key.wait_key()
    
        if key == Key.q:
            break
