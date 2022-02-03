"""
Parameter Tuner
"""
import sys
from pathlib import Path

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


from twiddler.runner import Runner


class Twiddler(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        runner = Runner(base_args=[sys.executable, "sample_cli.py", "imaginary-argument"], path, arguments)

        name_label = toga.Label(
                'Your name: ',
                style=Pack(padding=(0, 5))
            )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
                'Say Hello!',
                on_press=self.say_hello,
                style=Pack(padding=5)
            )

        slider_box = toga.Box()

        slider = toga.Slider(range=(0, 100), on_release=self.onchange, style=Pack(flex=.75))
        slider_box.add(toga.Label('Slider', style=Pack(flex=.25)))
        slider_box.add(slider)

        main_box.add(name_box)
        main_box.add(button)
        main_box.add(slider_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    def say_hello(self, widget):
        print("Hello", self.name_input.value)

    def onchange(self, x):
        print(x.value)


def main():
    return Twiddler()
