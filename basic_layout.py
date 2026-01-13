from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.image import Image
countries={
    "USA":{"currency":"USD","pos":(0.215,0.46)},
    "CANADA":{"currency":"CAD","pos":(0.2,0.57)},
    "EUROPE":{"currency":"EUR","pos":(0.55,0.52)},
    "JAPAN":{"currency":"YEN","pos":(0.84,0.4)},
    "INDIA":{"currency":"INR","pos":(0.72,0.385)}
    }

# USA["currency"] -> USD
# USA.keys() -> currency,pos 
# USA.values() -> "USD",(0.14,0.41)
# USA.items() -> "currency":"USD","pos":(0.14,0.41)


class CurrencyApp(App):
    def build(self):
        layout1=FloatLayout()
        label1=Label(text="Real Time Currency App",pos_hint={"center_x":0.5, "y":0.9},size_hint=(1,None),height=40)
        image=Image(source="world_map.png",pos_hint={"center_x":0.5,"y":0.05},size_hint=(1,0.7),allow_stretch=True)

        input_box=BoxLayout(pos_hint={"center_x":0.5, "y":0.8},size_hint=(0.8,None),height=80)
        self.text_amount = TextInput(hint_text="Enter amount of dollars",font_size=15)
        self.spinner = Spinner(values=["USD","CAD","EUR","YEN","INR"])
        button1 = Button(text="Convert",font_size=20,on_press=self.convert_and_show)
        button2 = Button(text="Reset",font_size=20)

        input_box.add_widget(self.text_amount)
        input_box.add_widget(self.spinner)
        input_box.add_widget(button1)
        input_box.add_widget(button2)
        layout1.add_widget(label1) 
        layout1.add_widget(input_box)
        layout1.add_widget(image)
        self.labels={}
        for country, data in countries.items():
            label = Label(
                text=country,
                pos_hint={"center_x": data["pos"][0], "center_y": data["pos"][1]}
            )
            self.labels[country] = label
            layout1.add_widget(label)

        return layout1 
    
    # PART 1 of Next Class
    def convert_and_show(self):
        amount_text=self.text_amount.text.strip()
        base_currency=self.spinner.text


if __name__ =="__main__":
    CurrencyApp().run()
