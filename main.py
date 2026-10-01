from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config

# جلوگیری از باز شدن کیبورد مجازی
Config.set('kivy', 'keyboard_mode', 'system')

class CalculatorApp(App):
    def build(self):
        self.title = "ماشین حساب ساده"
        self.expression = ""

        # لایه اصلی عمودی
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # نمایشگر
        self.display = Label(
            text="0",
            font_size=50,
            halign="right",
            valign="middle",
            size_hint=(1, 0.3)
        )
        self.display.bind(size=self.display.setter('text_size'))
        main_layout.add_widget(self.display)

        # دکمه‌ها
        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '⌫'],
        ]

        grid = GridLayout(cols=4, spacing=5, size_hint=(1, 0.7))
        for row in buttons:
            for label in row:
                btn = Button(text=label, font_size=30)
                btn.bind(on_press=self.on_button_press)
                grid.add_widget(btn)

        main_layout.add_widget(grid)
        return main_layout

    def on_button_press(self, instance):
        text = instance.text

        if text == 'C':
            self.expression = ""
            self.display.text = "0"

        elif text == '⌫':
            self.expression = self.expression[:-1]
            self.display.text = self.expression if self.expression else "0"

        elif text == '=':
            try:
                # جایگزینی نمادها برای eval
                result = str(eval(self.expression))
                self.display.text = result
                self.expression = result
            except Exception:
                self.display.text = "خطا"
                self.expression = ""

        else:
            self.expression += text
            self.display.text = self.expression


if __name__ == '__main__':
    CalculatorApp().run()