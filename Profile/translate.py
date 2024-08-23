from deep_translator import GoogleTranslator

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

translator = GoogleTranslator(source="auto")

class State():
    profile_info = PROFILE_INFO.copy()
    ui_text = UI_TEXT.copy()
    language:str = "es"
        
    def translate_text(self, text: str) -> str:
        translator.target = self.language
        return translator.translate(text)
    
    def translate(self):
        self.language = "es" if self.language == "en" else "en"
        self.profile_info = [self.translate_text(text) for text in self.profile_info]
        self.ui_text = [self.translate_text(text) for text in self.ui_text]