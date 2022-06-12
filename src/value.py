import enum
from typing_extensions import Self
from value_constant import Constant, Quote
from value_mathops import MathOp
from literal import Literal
from value_call import *

# Expecc bugs
class ValueEnum(enum.Enum):
    LABEL = 1
    JUMPDEST = 2
    JUMPTABLEDEST = 3

    def __new__(cls: type[Self], variant: str, **kwargs) -> Self:
        cls._name_ = variant
        {
            "LABEL": cls.label_init(**kwargs),
            "JUMPDEST": cls.jd_init(**kwargs),  # do nothing
            "JUMPTABLEDEST": cls.jtd_init(**kwargs),
            "CONSTANT": cls.constant_init(**kwargs),
            "OPCODE": cls.opcode_init(**kwargs),
            "LITERAL": cls.literal_init(**kwargs),
            "QUOTE": cls.quote_init(**kwargs),
            "MATHOP": cls.mathop_init(**kwargs),
            "SIZECALL": cls.sizecall_init(**kwargs),
            "STARTCALL": cls.startcall_init(**kwargs),
            "MACROCALL": cls.macrocall_init(**kwargs),
            "JUMPTABLECALL": cls.jtcall_init(**kwargs),
        }[variant]

        return cls

    @classmethod
    def label_init(cls, **kwargs):
        cls.name_ = kwargs["name"]
        cls.ns = kwargs["ns"]

    @classmethod
    def jd_init(cls, **kwargs):
        cls.name_ = kwargs["name"]

    @classmethod
    def jtd_init(cls, **kwargs):
        cls.name_ = kwargs["name"]

    @classmethod
    def constant_init(cls, **kwargs):
        cls.name_ = kwargs["name"]
        cls._value_: type[Self] = kwargs["value"]

    @classmethod
    def opcode_init(cls, **kwargs):
        cls.op = kwargs["op"]

    @classmethod
    def literal_init(cls, **kwargs):
        cls.literal: Literal = kwargs["literal"]

    @classmethod
    def quote_init(cls, **kwargs):
        cls._value_: type[Self] = kwargs["value"]

    # todo
    @classmethod
    def mathop_init(cls, **kwargs):
        cls.mathop = kwargs["mathop"]

    # todo
    @classmethod
    def sizecall_init(cls, **kwargs):
        # macro|jt
        cls._value_ = kwargs["value"]

    @classmethod
    # todo
    def startcall_init(cls, **kwargs):
        cls._value_ = kwargs["value"]

    @classmethod
    def macrocall_init(cls, **kwargs):
        cls._name = kwargs["name"]
        cls.args = kwargs["args"]

    @classmethod
    def jtcall_init(cls, **kwargs):
        cls._name = kwargs["name"]
