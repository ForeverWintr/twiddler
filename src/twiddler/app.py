"""
Parameter Tuner
"""
import sys
from pathlib import Path

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


from twiddler.runner import Runner, Argument


class Twiddler(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        runner = Runner(
            base_args=[sys.executable, "sample_cli.py", "imaginary-argument"],
            path=Path("."),
            arguments=(
                Argument(
                    0,
                    name="sleep",
                ),
            ),
        )

        control_box = toga.Box(style=Pack(direction=COLUMN))
        for arg in runner.arguments:
            s = toga.Slider(
                range=(arg.min, arg.max), on_change=self.slider_changed, style=Pack(flex=2)
            )
            label = toga.Label(arg.name, style=Pack(flex=0.1))
            slider_box = toga.Box(children=(label, s))
            control_box.add(slider_box)

        main_box.add(control_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def slider_changed(self, x):
        print(x.value)


def main():
    return Twiddler()
