from literal import Literal
from value import ValueEnum

NINETY_FIVE = 95  # todo: why 95


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


def push_n(n: int):
    if n < 1 or n > 32:
        raise ValueError(f"can't push value {n}; not in range [1,32]")
    else:
        return Literal(NINETY_FIVE+n)


# Yikes, python enums
class MacroEnum():
    variant: str
    enum: ValueEnum | Macro | JumpTable

    def __init__(self, variant: str, **kwargs):
        self.variant = variant
        self.enum = {"VALUES": ValueEnum(**kwargs),
                     "MACRO": Macro(**kwargs),
                     "JUMPTABLE": JumpTable(**kwargs)}[variant]
