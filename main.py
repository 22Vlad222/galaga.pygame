from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
Window.size = (300, 500)
Window.clearcolor = (0, 0.5, 0, 1)

class Delivery(Widget):
    pass

class FiguresApp(App):
    def build(self):
        return Delivery()


FiguresApp().run()
