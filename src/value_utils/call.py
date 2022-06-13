
from value import ValueEnum
from value_utils.types import JumpTable

class MacroCall:
    name: str
    args: None | list[ValueEnum]

class SizeCallEnum:
    macro = None
    jumptable = None

    def __init__(self, name: str,
                 macro: None | MacroCall,
                 jumptable: None | JumpTable):
        assert name in ["MACRO", "JUMPTABLE"]
        assert macro is not None or jumptable is not None
        self._name_ = name
        match name:
            case "MACRO": self.macro = macro
            case "JUMPTABLE": self.jumptable = jumptable


class StartCall:
    # not documented yet
    pass


class JumpTableCall:
    jumptablecall: JumpTable
