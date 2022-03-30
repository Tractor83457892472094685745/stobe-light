basic.show_icon(IconNames.YES)
strip = neopixel.create(DigitalPin.P16, 3, NeoPixelMode.RGB)
strip.show()

def on_forever():
    strip.rotate(1)
    basic.pause(200)
    strip.set_pixel_color(0,
        neopixel.rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
    basic.pause(200)
    strip.set_pixel_color(1,
        neopixel.rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
    basic.pause(200)
    strip.set_pixel_color(2,
        neopixel.rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
    basic.pause(200)
basic.forever(on_forever)
