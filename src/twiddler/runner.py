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


class Runner:
    def __init__(self, base_args: tp.Iterable[str], path: Path, arguments: tp.Iterable[Argument]):
        """Corresponds to a program cli."""
        self.base_args = list(base_args)
        self.path = path
        self.arguments = tuple(arguments)
        self.running_task = None

    async def launch(self):
        """Start the command running, and return immediately"""
        args = " ".join(str(a) for a in self.arguments).split()
        cmd = self.base_args + args
        self.running_task = await asyncio.create_subprocess_exec(*cmd)
        return self.running_task
