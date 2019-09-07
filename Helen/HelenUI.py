import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
import helen_math

class HelenUI(App):
    def build(self):
        gl = GridLayout(spacing=5, rows=3, padding=10)
        gl.add_widget(TextInput(text="HI", size_hint_y=0.3))
        gl.add_widget(TextInput(text="HI", size_hint_y=0.3))
        gl.add_widget(Button(text="HI"))
        return gl

if __name__ == "__main__":
    HelenUI().run()