from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button 

class CurrencyApp(App):
    def build(self):
        layout1=FloatLayout()
        label1=Label(text="Real Time Currency App",pos_hint={"center_x":0.5, "y":0.9},size_hint=(1,None),height=40)
        layout1.add_widget(label1)

        layout2=BoxLayout(pos_hint={"center_x":0.5, "y":0.8},size_hint=(0.8,None),height=80)
        text_amount = TextInput(hint_text="Enter amount of dollars",font_size=15)
        spinner = Spinner(values=["USD","CAD","PESO","YEN","INR"])
        button1 = Button(text="Convert",font_size=20)
        button2 = Button(text="Reset",font_size=20)

        layout2.add_widget(text_amount)
        layout2.add_widget(spinner)
        layout2.add_widget(button1)
        layout2.add_widget(button2)
        layout1.add_widget(layout2)

        return layout1 
        



if __name__ =="__main__":
    CurrencyApp().run()
