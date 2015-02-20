# You can place the script of your game in this file.

init:
    # Declare images below this line, using the image statement.
    image bg 01 = "images/bg01.png"
    image bg 02 = "images/bg02.png"
    image bg 03 = "images/bg03.png"
    image bg 04 = "images/bg04.png"
    image bg 05 = "images/bg05.png"
    image bg 06 = "images/bg06.png"
    image bg 07 = "images/bg07.png"
    image bg 08 = "images/bg08.png"
    image bg 09 = "images/bg09.png"
    image bg 10 = "images/bg10.png"
    image bg 11 = "images/bg11.png"
    image bg 12 = "images/bg12.png"
    image bg 13 = "images/bg13.png"
    image bg 14 = "images/bg14.png"
    image bg 15 = "images/bg15.png"
    image bg 16 = "images/bg16.png"
    
    image nino 01 = "images/kid01.png"
    image nino 02 = "images/kid02.png"
    image nino 03 = "images/kid03.png"
    image nino 04 = "images/kid04.png"
    
    image end = "images/end.png"
    


    $_game_menu_screen = "_quit_prompt"

# The game starts here.
label start:
    scene bg 01 with pixellate
    "Eres un pez."
    $ config.rollback_enabled = False
    show bg 02
    "De alguna forma estas tirado en la playa."
    show bg 03
    "Hace mucho calor."
    show bg 04
    "Sientes que te quemas!"
    show bg 05
    "No sabes como terminaste allí..."
    show bg 06
    "...deseas regresar al mar."
    show bg 07
    "El calor..."
    show bg 08
    "La marea esta bajando."
    menu:
        "Muevete un poco sacudiendo.":
            show bg 09
            "Te mueves."
            show bg 10
            "No pasa nada."
        
        "No hacer nada.":
            show bg 09
            "No haces nada."
            show bg 10
            "Sigue haciendo calor."
            
    show bg 11
    "Piensalo con calma..."
    show bg 12
    "...Te has divertido ya bastante en el agua."
    show bg 13
    "El sol te seca las branquias."
    show bg 14
    "Pero te sientes bien... Hasta donde se puede!"
    show bg 15
    "Hace calor."
    show bg 16
    "Deseas volver al mar."
    menu:
        "Sacudete hacia al el oceano.":
            show bg 01
            "Te sacudes."
            show bg 02
            "Te mueves un poco!"
            show bg 03
            "Pero nunca has estado tan lejos del agua."
        
        "No hacer nada.":
            show bg 01
            "No haces nada."
            show bg 02
            "Te rindes?"
            show bg 03
            "Aun hace calor..."

    show bg 04
    "La arena te hace sentir más seco."
    show bg 05
    "Nada de agua..."
    show bg 06
    "La brisa te tira granos de arena en los ojos."
    menu:
        "Sacudirse.":
            show bg 07
            "Te sacudiste un poco."
            show bg 08
            "Te cubristes de arena nada mas."
        
        "No hacer nada.":
            show bg 07
            "No haces nada."
            show bg 08
            "La arena aun obstruye tus branquias."
            
    show bg 09
    "Hace calor"
    show bg 10
    "Por unos momentos ves con claridad..."
    show bg 11
    "... Entiendes el significado de la existencia."
    show bg 12
    "..."
    show bg 13
    "Te sofocas, hace calor"
    show bg 14
    "Oh, pasos!"
    show bg 15
    "Quizas alguien ayude!"
    show bg 16
    "Volveras al oceano."
    show bg 01
    show nino 01
    "Oh, es un nino."
    show bg 02
    show nino 02
    "Huh?"
    show bg 03
    show nino 03
    "Que es eso"
    show bg 04
    show nino 04
    "!!!"
    scene black
    "Ahhhhh..."
    
    label end:
    $ renpy.pause(0)
    scene black

    show end
    with pixellate
    with Pause(2.0)

    scene black
    with pixellate
    with Pause(1.0)

    return

