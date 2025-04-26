##CODIGO SIN USAR##

#show dad confused at Transform(xpos=-0.5, xalign=1.0, alpha=1.0)with dissolve

define b = Character("Hombre misterioso", color="#ff0000")

define d = Character("Padre", color="#ad008a")

define t = Character("Yuu", color="#ffffff")


image box base = "box.png"

image box confused = "box2.png"

image dad base = "dad.png"

image dad confused = "dad2.png"

image lighter = "lighter.png"

default encendedor = False 

label start:
    
    $ nom = renpy.input("¿Cual es tu nombre?")
    $ nombre = nom.strip().capitalize()

    $ player =  Character(nombre, color="#ffffff")

    scene dark

    b"Estas teniendo un terrible sueño . . .  no?"

    show box base at Transform(yoffset=5.0, xalign=0.5)with vpunch

    b"{cps=20}. . .{/cps}"

    b"{bt=5}Ni hao{/bt} {cps=20}. . .{/cps} soy el hombre de tus sueños"

    b"No te preocupes [nombre] no sere un problema para ti, {cps=5}...{/cps} {bt=5}por ahora{/bt}"

    show dad confused at Transform(xpos=-0.5, xalign=1.0)with vpunch
    hide box base with dissolve
    pause 0.2
    show dad confused at Transform(xpos=1.0, xalign=0.5)with moveinright
    
    
    d"...."
    d"{sc=5}estas bien??{/sc}"
    d"Estabas {sc=2}temblando{/sc}"
    d"paresias casi {cps=5}. . .{/cps} {bt=5}poseido{/bt}"
    show dad base with vpunch
    d"te dije que no faltaras a misa la semana pasada"

    hide dad base
    show dad confused at Transform(xalign=0.5)
    d"bueno, terngo que ir a una reunion de trabajo"
    d"ni se te ocurra invitar esos {bt=5}amiguitos{/bt} "
    
    jump cuarto

    
    label cuarto:
        scene cuartoduerme with dissolve

        player"tengo que ir por mi desayuno"

        jump cuartopreguntas 

    
    label cuartopreguntas:
        scene cuartoduerme with dissolve
        menu:
            "Ir al piso de abajo":
                jump abajo
            "Inspecionar cuarto":
                call encendedor
                jump cuartopreguntas
            "Ir al baño":
                call baño
                jump cuartopreguntas
                
    label encendedor:
        show lighter at Transform(yalign=0.5,xalign=0.5) with moveintop
        "encontraste un encendedor"
        
        $ encendedor = True
        return
    label abajo:
        scene princhouse
        player"el desayundo deberia estar en el refrigerador" 
        return

    label baño:
        scene bathomb
        player"eres tu"
        player"te ves {bt=5}descente{/bt}"
        return