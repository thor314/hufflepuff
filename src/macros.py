from literal import Literal
from value import ValueEnum
from value_utils.types import JumpTable


class MacroEnum():
    class Macro:
        name: str
        idx: int
        args: list[str]
        content: list[ValueEnum]

    values: None | list[ValueEnum] = None
    macro: None | Macro = None
    jumptable: None | JumpTable = None

    def __init__(self,
                 name: str,
                 values: list[ValueEnum] | None = None,
                 macro: None | Macro = None,
                 jumptable: None | JumpTable = None):
        assert name in ["VALUES", "MACRO", "JUMPTABLE"]
        assert values is not None or macro is not None or jumptable is not None
        self._name_ = name
        self.values = values
        self.macro = macro
        self.jumptable = jumptable

