from value import ValueEnum

class Label:
    name: str
    ns: None | str

class JumpDest:
    name: str

class JumpTableDest:
    name: str

class Opcode:
    value: int

class Constant:
    name: str
    value: ValueEnum

class Quote:
    value: ValueEnum

class JumpTable:
    def __init__(self, name: str, labels: list[str]):
        self.name = name
        self.labels = labels
