basic.showIcon(IconNames.Rollerskate)
let strip = neopixel.create(DigitalPin.P16, 3, NeoPixelMode.RGB_RGB)
strip.setPixelColor(0, neopixel.colors(NeoPixelColors.White))
strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Black))
strip.setPixelColor(2, neopixel.colors(NeoPixelColors.White))
strip.setBrightness(255)
strip.show()
basic.forever(function () {
    strip.rotate(1)
})
basic.forever(function () {
    strip.rotate(1)
    strip.show()
})
