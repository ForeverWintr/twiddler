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

        self.text_display = toga.MultilineTextInput(readonly=True, style=Pack(flex=2))
        main_box.add(self.text_display)
        main_box.add(self.build_control_box(runner))

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def build_control_box(self, runner: Runner) -> toga.Box:
        control_box = toga.Box(style=Pack(direction=COLUMN, flex=1))
        for name, arg in runner.arguments.items():
            s = toga.Slider(
                range=(arg.min, arg.max),
                on_change=self.slider_changed,
                style=Pack(flex=2),
                id=name,
            )
            label = toga.Label(arg.name, style=Pack(flex=1))
            slider_box = toga.Box(children=(label, s))
            control_box.add(slider_box)
        return control_box

    def slider_changed(self, x):
        self.text_display.value = f"{x.id}: {x.value:.2f}\n"


def main():
    return Twiddler()
