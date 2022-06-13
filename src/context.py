from typing_extensions import Self
from macros import MacroEnum
from value import ValueEnum

class Context:
    jumptables: list[tuple[str, list[str], None | int]]
    jumptabledests: dict[str, int]
    jumptablestarts: dict[str, list[int]]
    macros: dict[str, MacroEnum]
    constants: dict[str, ValueEnum]
    compiles_at_idx: dict[tuple[str, int], int]

    def __init__(self):
        self.jumptables = []
        self.jumptabledests = {}
        self.jumptablestarts = {}
        self.macros = {}
        self.constants = {}
        self.compiles_at_idx = {}

    def __repr__(self) -> str:
        s = ""
        for c in self.constants:
            s += f"constant: {c[0]} {c[1]}\n"
        for c in self.macros:
            s += f"macro:    {c[0]} {c[1]}\n"
        return s

    def exists(self, s: str) -> bool:
        s.strip()
        if self.constants[s] != None or self. macros[s] != None or s in self.jumptables:
            return True
        return False

    def resolve_constant(self, s: str) -> None|ValueEnum:
        s.strip()
        try:
            return self.constants[s]
        except KeyError:
            return None

    def resolve_macro(self, s: str) -> None|MacroEnum:
        s.strip()
        try:
            return self.macros[s]
        except KeyError:
            return None

    def resolve_jumptabledest(self, s: str) -> None|int:
        s.strip()
        try:
            return self.jumptabledests[s]
        except KeyError:
            return None