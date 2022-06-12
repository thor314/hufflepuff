import enum
from literal import Literal
from value import ValueEnum

class MathOpsEnum(enum.Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4

    def apply(self, left: Literal, right: Literal) -> Literal:
        # todo: checked
        return Literal({"ADD": left + right,
                        "SUB": left - right,
                        "MUL": left * right,
                        "DIV": left // right,
                        }[self.name])

class MathOp:
    op: MathOpsEnum
    left: ValueEnum
    right: ValueEnum
