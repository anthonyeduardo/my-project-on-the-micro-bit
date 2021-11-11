def on_button_pressed_a():
    music.play_melody("B A E - - - - - ", 120)
    basic.show_leds("""
        . . # . .
                . # # # .
                # . # . #
                . . # . .
                . . # . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music.play_melody("B A E D E A B - ", 120)
    basic.show_leds("""
        . . # . .
                . # # # .
                # # # # #
                . # # # .
                . . # . .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.play_melody("E A B - - - - - ", 120)
    basic.show_leds("""
        . . # . .
                . . # . .
                # . # . #
                . # # # .
                . . # . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

music.play_melody("B A E - - - - - ", 120)
basic.show_string("Hello!")

def on_forever():
    pass
basic.forever(on_forever)
