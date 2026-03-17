from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class JarvisApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.lbl = Label(text="Hello Boss!\nJarvis is ready to serve.", 
                         halign="center", font_size='20sp')
        
        btn = Button(text="Tap to Start", size_hint=(1, 0.2),
                     background_color=(0, 0.7, 1, 1))
        btn.bind(on_press=self.on_click)
        
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        return layout

    def on_click(self, instance):
        self.lbl.text = "Listening to Boss..."

if __name__ == "__main__":
    JarvisApp().run()
