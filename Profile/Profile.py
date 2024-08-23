import reflex as rx
from rxconfig import config
from Profile.comps import *

def index() -> rx.Component:
    return rx.container(
        container_language(),
        rx.flex(
            rx.vstack(
                rx.center(
                    profile_image(),
                    width="100%"
                ),
                skills_cards(),
                
                bg="rgb(56,68,77)",
                min_width="20em",
                height="auto",
                padding="0.8em",
                border_radius=rx.breakpoints(
                    initial="1.5rem 1.5rem 0 0",
                    sm="1.5rem 0 0 1.5rem"
                ),
                justify="center",
            ),
            rx.vstack(
                profile_description(),
                rx.flex(
                    rx.hstack(
                        contact_button(),
                        download_cv(),
                        spacing="2"
                    ),
                    social_links(),
                    width="100%",
                    align=rx.breakpoints(
                        initial="center",
                        xs="end"
                    ),
                    justify=rx.breakpoints(
                        initial="center",
                        xs="between"
                    ),
                    direction=rx.breakpoints(
                        initial="column",
                        xs="row"
                    )
                ),
                padding="0.8em",
            ),
            
            bg="rgb(29,42,53)",
            height="100%",
            min_width="70vw",
            margin_top=rx.breakpoints(initial="2vh", xs="2vh", sm="13vh"),
            margin_bottom="9vh",
            border_radius="1.5rem",
            direction=rx.breakpoints(
                initial="column",
                sm="row"
            )
        ),
        rx.logo(),
    )

app = rx.App(
    theme=rx.theme(
        appearance="dark",
    )
)
app.add_page(index)
