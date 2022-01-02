import dataclasses
import typing as tp
import subprocess


@dataclasses.dataclass(frozen=True)
class Argument:
    value: float
    name: str
    max: float = 100
    min: float = 0
    step: float = 1


class Runner:
    def __init__(self, cli_template: str, arguments: tp.Iterable[Argument, ...]):
        self.cli_template = cli_template
        self.arguments = tuple(arguments)
