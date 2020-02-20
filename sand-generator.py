import board
import adafruit_ssd1306
import time
import random
import displayio

displayio.release_displays()
display = adafruit_ssd1306.SSD1306_I2C(128, 32, board.I2C(), addr=0x3c)
WIDTH = 128
HEIGHT = 56
# loop that randomly generates the 'sand'
while True:
    for _ in range(325):
        x = random.randrange(WIDTH)
        y = random.randrange(HEIGHT//10) + HEIGHT//2
        display.pixel(x, y, 1)
    display.show()
    time.sleep(0)
    display.fill(0)
