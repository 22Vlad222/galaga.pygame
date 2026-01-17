from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class TutorialApp(App):
    def add_num(self, obj):
        if self.lab.text == "0":
            self.lab.text = obj.text
        else:
            self.lab.text += obj.text
    def build(self):
        layout = GridLayout(spacing=10,padding=7,cols=3)
        b_layout = BoxLayout(spacing=10,padding=7)
        btn1 = Button(text="1", size_hint=(.1,.1), on_press=self.add_num)
        btn2 = Button(text="2", size_hint=(.1,.1), on_press=self.add_num)
        btn3 = Button(text="3", size_hint=(.1,.1), on_press=self.add_num)
        btn4 = Button(text="4", size_hint=(.1,.1), on_press=self.add_num)
        btn5 = Button(text="5", size_hint=(.1, .1), on_press=self.add_num)
        btn6 = Button(text="6", size_hint=(.1, .1), on_press=self.add_num)
        btn7 = Button(text="7", size_hint=(.1, .1), on_press=self.add_num)
        btn8 = Button(text="8", size_hint=(.1, .1), on_press=self.add_num)
        btn9 = Button(text="9", size_hint=(.1, .1), on_press=self.add_num)
        btn10 = Button(text="0", size_hint=(.1, .1), on_press=self.add_num)
        btn11 = Button(text="-", size_hint=(.1, .1), on_press=self.add_num)
        btn12 = Button(text="+", size_hint=(.1, .1), on_press=self.add_num)
        btn13 = Button(text="*", size_hint=(.1, .1), on_press=self.add_num)
        btn14 = Button(text="/", size_hint=(.1, .1), on_press=self.add_num)
        btn15 = Button(text="=", size_hint=(.1, .1), on_press=self.add_num)
        btn16 = Button(text="C", size_hint=(.1, .1), on_press=self.add_num)
        self.lab = Label(text="0")
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)
        layout.add_widget(btn6)
        layout.add_widget(btn7)
        layout.add_widget(btn8)
        layout.add_widget(btn9)
        layout.add_widget(btn10)
        layout.add_widget(btn11)
        layout.add_widget(btn12)
        layout.add_widget(btn13)
        layout.add_widget(btn14)
        layout.add_widget(btn15)
        layout.add_widget(btn16)
      #  b_layout.add_widget(lab)
      #  layout.add_widget(b_layout)

        return layout



TutorialApp().run()
