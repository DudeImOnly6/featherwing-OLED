import board
import adafruit_displayio_ssd1306
import displayio
import time
import random

displayio.release_displays()

display_bus = displayio.I2CDisplay(board.I2C(), device_address=0x3c)

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

bitmap = displayio.Bitmap(128, 32, 2)
palette = displayio.Palette(2)
palette[0] = 0x000000
palette[1] = 0xffffff
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
group = displayio.Group()
group.append(tile_grid)
display.show(group)
bitmap[20, 10] = 1

while True:
    pass
