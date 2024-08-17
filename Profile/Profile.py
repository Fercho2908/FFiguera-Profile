import reflex as rx
from rxconfig import config

def index() -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.vstack(
                rx.center(
                    rx.avatar(
                        src="profile1.webp",
                        radius="full",
                        size="9",
                    ),
                    rx.heading("Fernando Figuera", margin_top="0.4em"),
                    width="100%",
                    direction="column",
                ),
                rx.center(
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
                    padding_top="2.2em",
                ),
                
                
                bg="rgb(56,68,77)",
                min_width="20em",
                min_height="65vh",
                border_radius="1.5rem 0 0 1.5rem",
                justify="center",
            ),
            rx.vstack(
                rx.markdown(
                  """
¡Hola👋🏽, bienvenido a mi página web!

Soy Fernando Figuera, Técnico Superior Universitario en Informática y actualmente estudiante de Ingeniería en Sistemas en el [IUP Santiago Mariño](http://psmmaturin.edu.ve/).

Soy un apasionado de la tecnología y la programación en constante crecimiento. Esta página es mi proyecto inicial en [Reflex](https://reflex.dev) desarrollado completamente desde cero a partir de su documentación.

Si te interesan mis servicios, no dudes en contactarme. 🚀

                  """  
                ),
                rx.flex(
                    rx.hstack(
                        rx.link(
                            rx.button(
                                rx.icon(tag="mail"),
                                "Contactar",
                                size="3",
                                variant="solid",
                                cursor="pointer"
                            ),
                            href="mailto:fefc2908@gmail.com",
                        ),
                        rx.button(
                            rx.icon(tag="file-down"),
                            "Descargar CV",
                            on_click=rx.download(url="/CV Fernando.zip"),
                            size="3",
                            variant="surface",
                            cursor="pointer",
                        ),
                        spacing="2"
                    ),
                    rx.hstack(
                        rx.link(
                            rx.icon(tag="Github"),
                            href="https://github.com/fercho2908",
                            size="9",
                            alt="GitHub",
                            cursor="pointer",
                        ),
                        rx.link(
                            rx.icon(tag="phone"),
                            href="https://wa.me/584249246863",
                            size="9",
                            alt="Whatsapp",
                            cursor="pointer",
                        ),
                        rx.link(
                            rx.icon(tag="Instagram"),
                            href="https://instagram.com/fercho.2908",
                            size="9",
                            alt="Instagram",
                            cursor="pointer",
                        ),
                        spacing="2",
                        padding_right="1em"
                    ),
                    width="100%",
                    align="end",
                    justify="between",
                ),
                padding="0.8em",
            ),
            
            bg="rgb(29,42,53)",
            min_height="65vh",
            min_width="70vw",
            margin_top="13vh",
            margin_bottom="9vh",
            border_radius="1.5rem",
        ),
        rx.logo(),
    )

app = rx.App(
    theme=rx.theme(
        appearance="dark",
    )
)
app.add_page(index)
