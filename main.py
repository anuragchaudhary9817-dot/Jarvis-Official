from kivy.app import App
from kivy.uix.label import Label
class JarvisApp(App):
    def build(self):
        return Label(text="Jarvis AI: Online\nBoss, model.gguf file folder ma halnuhos.")
if __name__ == "__main__":
    JarvisApp().run()
