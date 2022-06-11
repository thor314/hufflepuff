from value import Value, Literal
# todo: why 95
NINETY_FIVE = 95


class MacroEnum():
    # Yikes, python enums
    def __init__(self, variant: str, **kwargs):
        if variant == "MACRO":
            self.macro = Macro(**kwargs)
        elif variant == "JUMPTABLE":
            self.JumpTable = Macro(**kwargs)
        else:
            raise NameError("Must be one of: MACRO, JUMPTABLE")


class Macro():
    def __init__(self, name: str, idx: int, args: list[str], content: list[Value]):
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
