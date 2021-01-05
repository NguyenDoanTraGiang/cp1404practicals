from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    label_text = StringProperty()

    def __init__(self, **kwargs):
        # List containing names to display
        super().__init__(**kwargs)
        self.names = ["James", "Mary", "John", "Lizzy", "Robert", "Linda"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        # Create labels using the names in the list
        for name in self.names:
            label = Label(text=name, id=name)
            label.bind(on_release=self.press_entry)
            self.root.ids.display_box.add_widget(label)

    def press_entry(self, instance):
        # Get label text from Label's text
        label = instance.text
        self.label_text = label


DynamicLabelsApp().run()
