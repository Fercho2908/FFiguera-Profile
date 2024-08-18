import reflex as rx

def profile_image():
    return rx.center(
        rx.avatar(
            src="profile1.webp",
            radius="full",
            size="9",
        ),
        rx.heading("Fernando Figuera", margin_top="0.4em"),
        direction="column",
    )
    
def skills():
    return rx.center(
        rx.text("Habilidades:", size="1"),
        rx.flex(
            rx.badge("Python", size="2", variant="outline"),
            rx.badge("Java", size="2", variant="outline"),
            rx.badge("C#", size="2", variant="outline"),
            rx.badge("Visual Basic", size="2", variant="outline"),
            rx.badge("Git", size="2", variant="outline"),
            rx.badge("MySQL", size="2", variant="outline"),
            rx.badge("Access", size="2", variant="outline"),
            width="80%",
            spacing="2",
            flex_wrap="wrap",
            align="center",
            justify="center",
            padding_top="0.2em",
        ),
        width="100%",
        direction="column",
        padding_top=rx.breakpoints(
            initial="1.4em",
            sm="2.2em"
        ),
    )
    
def profile_info():
    return rx.markdown(
        """
¡Hola👋🏽, bienvenido a mi página web!

Soy Fernando Figuera, Técnico Superior Universitario en Informática y actualmente estudiante de Ingeniería en Sistemas en el [IUP Santiago Mariño](http://psmmaturin.edu.ve/).

Soy un apasionado de la tecnología y la programación en constante crecimiento. Esta página es mi proyecto inicial en [Reflex](https://reflex.dev) desarrollado completamente desde cero a partir de su documentación.

Si te interesan mis servicios, no dudes en contactarme. 🚀

        """  
    )
    
def contact_button():
    return rx.link(
        rx.button(
            rx.icon(tag="mail"),
            "Contactar",
            size=rx.breakpoints(
                initial="2",
                xs="3"
            ),
            variant="solid",
            cursor="pointer"
        ),
        href="mailto:fefc2908@gmail.com",
    )
    
def download_cv():
    return rx.button(
        rx.icon(tag="file-down"),
        "Descargar CV",
        on_click=rx.download(url="/CV Fernando.zip"),
        size=rx.breakpoints(
                initial="2",
                xs="3"
            ),
        variant="surface",
        cursor="pointer",
    )
    
def social_icon(icon, link):
    return rx.link(
        rx.icon(icon),
        href=link,
    )
    
def social_links():
    return rx.hstack(
        social_icon("github", "https://github.com/fercho2908"),
        social_icon("Phone", "https://wa.me/584249246863"),
        social_icon("Instagram", "https://instagram.com/fercho.2908"),
        spacing="2",
        padding=rx.breakpoints(
            initial="0.8em 0 0 0",
            xs="0.8 0.4em 0 0",
            sm="0 1em 0 0"
        ),
        padding_right="1em"
    )