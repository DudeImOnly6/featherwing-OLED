
# Import the needed modules
import board
import adafruit_ssd1306
import displayio
import time
import random
import adafruit_imageload
# import font

# Initialize the display
# Change dimensions as needed
displayio.release_displays()
display = adafruit_ssd1306.SSD1306_I2C(128, 32, board.I2C(), addr=0x3c)

# SAND GENERATOR
# specifies width and height to be used with sand generator
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

# SPRITES
bitmap, palette = adafruit_imageload.load("/rock2.bmp",
                                          bitmap=displayio.Bitmap,
                                          palette=displayio.Palette)

tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
group = displayio.Group()
group.append(tile_grid)
display.show(group)

group.x = 62
group.y = 16

while True:
    pass