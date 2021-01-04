from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class MilesToKilometersApp(App):
    default = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_mi_km(self, miles):
        kilometers = miles * 1.609
        self.root.ids.output_label.text = str(kilometers)

    def handle_convert(self):
        self.default = self.root.ids.input_number.text

    def handle_increment(self, change):
        self.root.ids.input_number.text = str(float(self.root.ids.input_number.text) + change)

MilesToKilometersApp().run()
