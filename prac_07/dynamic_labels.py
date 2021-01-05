from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        # List containing names to display
        super().__init__(**kwargs)
        self.names = ["James", "Mary", "John", "Lizzy", "Robert", "Linda"]
