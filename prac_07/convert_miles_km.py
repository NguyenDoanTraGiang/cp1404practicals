from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class MilesToKilometersApp(App):
    default = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_mi_km(self):
        """Convert miles into kilometers"""
        miles = self.validate_miles()
        kilometers = miles * 1.609
        self.root.ids.output_label.text = str(kilometers)

    def handle_convert(self):
        """Update the input field automatically"""
        self.default = self.root.ids.input_number.text

    def handle_increment(self, change):
        """Change the value in the input field by change parameter"""
        self.root.ids.input_number.text = str(self.validate_miles() + change)

    def validate_miles(self):
        """If input field is empty or not a number then return 0"""
        try:
            miles = float(self.root.ids.input_number.text)
            return miles
        except ValueError:
            return 0

MilesToKilometersApp().run()
