light.set_brightness(10)
while True:
    light.set_pixel_color(0, light.rgb(255,0,0))
    pause(300)
    light.set_pixel_color(1, light.rgb(204,255,0))
    pause(300)
    light.set_pixel_color(2, light.rgb(0,255,0))
    pause(300)
    light.set_pixel_color(3, light.rgb(44,238,144))
    pause(300)
    light.set_pixel_color(4, light.rgb(0,255,255))
    pause(300)
    light.set_pixel_color(5, light.rgb(51,190,255))
    pause(300)
    light.set_pixel_color(6, light.rgb(0,0,255))
    pause(300)
    light.set_pixel_color(7, light.rgb(238,130,238))
    pause(300)
    light.set_pixel_color(8, light.rgb(128,0,128))
    pause(300)
    light.set_pixel_color(9, light.rgb( 254,44,84))
    pause(300)
    light.clear()
    pause(3000)
    light.clear()
    pause(2000)