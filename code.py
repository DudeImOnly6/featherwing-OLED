# Import the needed modules
import board
import adafruit_ssd1306
import displayio
import time
import random
import adafruit_imageload
import adafruit_displayio_ssd1306
# import fontstuffs

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
displayio.release_displays()
displaybus = displayio.I2CDisplay(board.I2C(), device_address=0x3c)

rockdisplay = adafruit_displayio_ssd1306.SSD1306(displaybus, width=128, height=32)

bitmap, palette = adafruit_imageload.load("/Rock.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)

tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

group = displayio.Group()
group.append(tile_grid)

rockdisplay.show(group)

while True:
    pass
