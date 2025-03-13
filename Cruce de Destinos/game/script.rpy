# Definir el juego

define config.name = "Cruce de Destinos"

# Definir personajes

define aiko = Character("Aiko", color="#ff5d5d")
define hana = Character("Hana", color="#FFD700")
define saki = Character("Saki", color="#90EE90")
define rika = Character("Rika", color="#808080")

# Iniciar la historia
label start:
    scene bg apartment_hallway
    show aiko normal

    aiko "Aquí estoy... Mi primera vez viviendo sola en una ciudad nueva. Se siente extraño."

    "El sonido del tráfico en la calle y el murmullo de la gente en los pasillos me recuerdan que ya no estoy en casa."

    show hana happy at left
    show saki shy at right

    hana "¡Así que tú eres la nueva! Me llamo Hana. Si necesitas algo, solo dime. ¡Incluso si es una fiesta para celebrar tu llegada!"

    saki "Ah... umm... soy Saki. Trabajo en la biblioteca. Si necesitas ayuda con los libros o... o cualquier cosa académica, estaré por ahí."

    show rika neutral at center

    rika "Soy Rika. Vivo en el departamento de al lado. Si necesitas algo... no toques mi puerta."

    "Rika dice esto con voz tranquila, pero su mirada me da la sensación de que no lo dice en serio."

    aiko "Parece que no voy a estar sola después de todo..."

    jump decision_1

label decision_1:
    menu:
        "Ir a una fiesta con Hana":
            $ rel_hana += 1
            $ rel_saki -= 1
            jump fiesta_hana

        "Estudiar con Saki en la biblioteca":
            $ rel_saki += 1
            $ rel_hana -= 1
            jump biblioteca_saki

        "Quedarme en casa y hablar con Rika":
            $ rel_rika += 1
            $ rel_hana -= 1
            $ rel_saki -= 1
            jump casa_rika

label fiesta_hana:
    scene bg party
    show hana excited

    hana "¡Sabía que aceptarías! Vamos, la música nos llama."

    "El lugar está lleno de estudiantes, luces de neón y un ritmo que hace temblar el suelo."

    hana "Vamos a bailar, ¡quiero ver qué tal te mueves!"

    aiko "¿Eh? Yo no soy muy buena en eso..."

    hana "No importa, solo déjate llevar. Es la regla número uno de la diversión."

    "Reímos juntas mientras nos movemos al ritmo de la música."

    jump decision_2

label biblioteca_saki:
    scene bg library
    show saki neutral

    saki "Oh... No pensé que vendrías."

    aiko "¿Molesto tu tranquilidad?"

    saki "No... es agradable tener compañía aquí."

    "Nos sentamos en una mesa, y mientras Saki lee, noto que de vez en cuando me observa de reojo."

    aiko "Saki, ¿por qué siempre vienes aquí?"

    saki "Me gusta la calma... aquí no necesito hablar mucho. Pero... contigo, es diferente."

    "Saki sonríe levemente antes de volver la vista a su libro."

    jump decision_2

label casa_rika:
    scene bg apartment
    show rika neutral

    rika "No muchos deciden quedarse en casa. ¿Por qué tú sí?"

    aiko "Supongo que no me gusta tanto el ruido..."

    rika "Entonces somos iguales."

    "Rika me mira en silencio, como si estuviera evaluándome."

    rika "Si quieres quedarte aquí un rato, no me molesta."

    "Nos quedamos en la sala, en una tranquilidad casi reconfortante."

    jump decision_2

label decision_2:
    "La lluvia comienza a caer mientras Aiko camina por el campus."

    show hana sad at left
    show saki shy at right
    show rika neutral at center

    hana "¡Uf! No traje paraguas. ¡Aiko, vamos a refugiarnos en la cafetería!"

    saki "La biblioteca está cerca... y tengo un libro que quiero mostrarte."

    rika "Mi departamento está aquí. Puedes esperar a que pare la lluvia."

    menu:
        "Ir con Hana a la cafetería":
            $ rel_hana += 1
            $ rel_rika -= 1
            jump cafeteria_hana

        "Ir con Saki a la biblioteca":
            $ rel_saki += 1
            $ rel_hana -= 1
            jump biblioteca_saki_2

        "Esperar en el departamento de Rika":
            $ rel_rika += 1
            $ rel_saki -= 1
            jump departamento_rika

label decision_3:
    scene bg campus_evening

    show hana determined at left
    show saki nervous at right
    show rika serious at center

    hana "Mañana hay una competencia de baile en la universidad. Si vienes, lo pasaremos genial."

    saki "Yo... estaré en la biblioteca. Estoy organizando una lectura de poesía. Me gustaría que vinieras."

    rika "Tengo algo que mostrarte. Pero solo si realmente quieres saber más sobre mí."

    menu:
        "Ir a la competencia con Hana":
            $ rel_hana += 1
            $ rel_saki -= 1
            $ rel_rika -= 1
            jump final_hana

        "Ir a la lectura con Saki":
            $ rel_saki += 1
            $ rel_hana -= 1
            $ rel_rika -= 1
            jump final_saki

        "Descubrir lo que Rika quiere mostrar":
            $ rel_rika += 1
            $ rel_hana -= 1
            $ rel_saki -= 1
            jump final_rika

label final_hana:
    scene bg stage
    show hana happy

    hana "¡No puedo creer que estés aquí! Sabía que elegirías la opción más divertida."

    aiko "¿Qué puedo decir? Tu energía es contagiosa."

    "La música llena el aire, y la multitud aplaude mientras nos preparamos para bailar."

    hana "Vamos a hacerlo inolvidable. No se trata de ganar, se trata de divertirnos."

    aiko "¡Exacto! Pero no estaría mal ganar también."

    show hana excited
    "Hana sonríe ampliamente antes de tomar mi mano. La pista de baile se ilumina mientras la música empieza."

    hana "Después de esto, quiero que sigamos disfrutando juntas. Hay tanto por hacer, tantos lugares a los que ir."

    aiko "¿Quieres decir… seguir compartiendo nuestras locuras después de la universidad?"

    hana "¡Por supuesto! El mundo es nuestro escenario, Aiko."

    "Nos lanzamos a la pista, moviéndonos con sincronía perfecta. En este momento, el resto del mundo desaparece. Solo estamos nosotras, bailando hacia un futuro brillante."

    return


label final_saki:
    scene bg library
    show saki shy

    saki "Honestamente... no pensé que vendrías."

    aiko "¿Por qué no? Sabes que me encanta escucharte leer."

    saki "Lo sé... pero es algo tan simple comparado con lo que los demás hacen."

    "Saki me mira con una mezcla de gratitud e inseguridad. Me acerco y tomo suavemente su mano."

    aiko "No hay nada simple en compartir algo que amas. Cada palabra que lees me hace sentir más cerca de ti."

    show saki surprised
    "Por un instante, Saki se queda sin palabras. Luego, con un leve rubor en las mejillas, saca un pequeño libro y lo abre."

    saki "Entonces... esta será la última lectura del día."

    "Se aclara la garganta y empieza a leer. Su voz es suave pero firme, llena de emoción. Me pierdo en las palabras, en el sonido de su voz."

    saki "Aiko... ¿te quedarás conmigo después de la universidad? Sé que soy reservada, pero cuando estoy contigo... todo parece más fácil."

    aiko "No hay otro lugar donde preferiría estar."

    "Saki sonríe y me aprieta la mano con fuerza. En este momento, entre las páginas de un libro y la calidez de su compañía, encuentro mi hogar."

    return


label final_rika:
    scene bg rooftop
    show rika serious

    "El viento nocturno sopla suavemente mientras Rika y yo estamos sentadas en la azotea. Desde aquí, las luces de la ciudad parpadean como estrellas caídas."

    rika "Siempre vengo aquí cuando necesito pensar."

    aiko "Y ahora compartes este lugar conmigo."

    show rika soft
    "Rika me mira de reojo, con una expresión que nunca le había visto antes. No es frialdad, ni distancia... es vulnerabilidad."

    rika "Contigo... es diferente. No siento que deba poner barreras."

    aiko "Nunca tuviste que hacerlo conmigo."

    "El silencio entre nosotras no es incómodo. Es una conversación en sí misma, un lenguaje hecho de miradas y pequeños gestos."

    rika "Aiko... Si te quedas a mi lado, prometo que algún día te contaré todo sobre mí. No quiero secretos entre nosotras."

    aiko "No tienes que apresurarte. Estaré aquí cuando estés lista."

    "Rika me toma de la mano, entrelazando nuestros dedos. Su agarre es firme, como si temiera que pudiera desaparecer."

    rika "Gracias... por no rendirte conmigo."

    "La ciudad sigue su curso debajo de nosotras, pero aquí arriba, en esta pequeña azotea, todo se siente más claro. Un nuevo comienzo, con Rika a mi lado."

    return


