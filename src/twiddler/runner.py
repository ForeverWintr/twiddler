import dataclasses
import typing as tp
import asyncio
from pathlib import Path


@dataclasses.dataclass(frozen=True)
class Argument:
    value: float
    name: str
    max: float = 100
    min: float = 0
    step: float = 1

    def __str__(self):
        return f"--{self.name} {self.value}"

    @property
    def tick_count(self):
        """Number of ticks for a slider"""
        return ((self.max - self.min) // self.step) + 1


class Runner:
    def __init__(self, base_args: tp.Iterable[str], path: Path, arguments: tp.Iterable[Argument]):
        """Corresponds to a program cli."""
        self.base_args = list(base_args)
        self.path = path
        self.arguments = {a.name: a for a in arguments}
        self.running_task = None

    def args_list(self) -> list[str]:
        args = " ".join(str(a) for a in self.arguments.values()).split()
        return self.base_args + args

    def command_line(self) -> str:
        """Return the command line for this runner"""
        return " ".join(self.args_list())

    async def launch(self):
        """Start the command running, and return immediately"""
        self.running_task = await asyncio.create_subprocess_exec(*self.args_list())
        return self.running_task
