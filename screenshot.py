import pyscreenshot as ImageGrab
import time as t

im = ImageGrab.grab()
im.save("before.png")
t.sleep(1)
im = ImageGrab.grab()
im.save("after.png")
