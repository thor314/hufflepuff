import enum
from literal import Literal
from value import ValueEnum

class Macro():
    def __init__(self, name: str, idx: int, args: list[str], content: list[ValueEnum]):
        if len(args) == 1 and args[0] == "":
            self.args = []
        else:
            self.args = args
        self.name = name
        self.idx = idx
        self.content = content


class JumpTable():
    def __init__(self, name: str, labels: list[str]):
        self.name = name
        self.labels = labels


# Yikes, python enums
class MacroEnum(enum.Enum):
    VALUES = 1
    MACRO = 2
    JUMPTABLE: JumpTable

    def __new__(cls, variant: str, **kwargs):
        cls._name_ = variant
        cls._value_ = {"VALUES": ValueEnum(**kwargs),
                       "MACRO": Macro(**kwargs),
                       "JUMPTABLE": JumpTable(**kwargs)
                       }[variant]
