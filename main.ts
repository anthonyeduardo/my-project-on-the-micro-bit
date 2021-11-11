input.onButtonPressed(Button.A, function () {
    music.playMelody("E A B - - - - - ", 120)
    basic.showLeds(`
        . . # . .
        . # # # .
        # . # . #
        . . # . .
        . . # . .
        `)
})
input.onButtonPressed(Button.AB, function () {
    music.playMelody("B A E D E A B - ", 120)
    basic.showLeds(`
        . . # . .
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        `)
})
input.onButtonPressed(Button.B, function () {
    music.playMelody("B A E - - - - - ", 120)
    basic.showLeds(`
        . . # . .
        . . # . .
        # . # . #
        . # # # .
        . . # . .
        `)
})
music.playMelody("B A E - - - - - ", 120)
basic.showString("Hello!")
basic.forever(function () {
	
})
