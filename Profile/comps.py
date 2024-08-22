import reflex as rx
import googletrans

PROFILE_INFO = [
    "¡Hola👋🏽, bienvenido a mi página web!",
    "Soy Fernando Figuera, Técnico Superior Universitario en Informática y actualmente estudiante de Ingeniería en Sistemas en el [IUP Santiago Mariño](http://psmmaturin.edu.ve/).",
    "Soy un apasionado de la tecnología y la programación en constante crecimiento. Esta página es mi proyecto inicial en [Reflex](https://reflex.dev) desarrollado completamente desde cero a partir de su documentación.",
    "Si te interesan mis servicios, no dudes en contactarme. 🚀",
]

UI_TEXT = [
    "Habilidades:",
    "Contactar",
    "Descargar CV"
]

SKILLS = ["Python", "Java", "C#", "Visual Basic", "Git", "MySQL", "Access"]
translator = googletrans.Translator()

class State(rx.State):
    skills = SKILLS.copy()
    profile_info = PROFILE_INFO.copy()
    ui_text = UI_TEXT.copy()
    language: str = "es"
    
    def translate_text(self, text: str) -> str:
        return translator.translate(text, dest=self.language).text
    
    def translate(self):
        self.language = "es" if self.language == "en" else "en"
        self.profile_info = [self.translate_text(text) for text in self.profile_info]
        self.ui_text = [self.translate_text(text) for text in self.ui_text]

def select_language():
    return rx.hstack(
        rx.icon(tag="languages"),
        rx.select(
            ["Español", "English"],
            default_value="Español",
            on_change= State.translate()
        ),
        width="100%",
        align="center",
        justify="end"
    )

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
    
def display_skills(skills: str):
    return rx.badge(skills, size="2", variant="outline")

def skills_cards():
    return rx.center(
        rx.text(State.ui_text[0], size="1"),
        rx.flex(
            rx.foreach(State.skills, display_skills),
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
    
def display_profile_info(info: str):
    return rx.box(rx.markdown(info))
    
def profile_description():
    return rx.vstack(
        rx.foreach(State.profile_info, display_profile_info)
    )
    
def contact_button():
    return rx.link(
        rx.button(
            rx.icon(tag="mail"),
            State.ui_text[1],
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
        State.ui_text[2],
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
        is_external=True,
    )
    
def social_links():
    return rx.hstack(
        social_icon("github", "https://github.com/fercho2908"),
        social_icon("Phone", "https://wa.me/584249246863"),
        social_icon("Instagram", "https://instagram.com/fercho.2908"),
        spacing="2",
        padding=rx.breakpoints(
            initial="0.8em 0 0 0",
            xs="0.8em 0 0 0",
            sm="0 1em 0 0"
        ),
        padding_right="1em"
    )