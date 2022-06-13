from value_utils.mathops import MathOpsEnum
from literal import Literal
from value_utils.call import SizeCallEnum, StartCall, MacroCall, JumpTableCall
from value_utils.types import *

class ValueEnum():
    name: str
    label: None | Label = None
    jumpdest: None | JumpDest = None
    jumptabledest: None | JumpTableDest = None
    constant: None | Constant = None
    opcode: None | Opcode = None
    literal: None | Literal = None
    quote: None | Quote = None
    mathop: None | MathOpsEnum = None
    sizecall: None | SizeCallEnum = None
    startcall: None | StartCall = None
    macrocall: None | MacroCall = None
    jumptablecall: None | JumpTableCall = None

    def __init__(self,
                 name: str,
                 label: None | Label = None,
                 jumpdest: None | JumpDest = None,
                 jumptabledest: None | JumpTableDest = None,
                 constant: None | Constant = None,
                 opcode: None | Opcode = None,
                 literal: None | Literal = None,
                 quote: None | Quote = None,
                 mathop: None | MathOpsEnum = None,
                 sizecall: None | SizeCallEnum = None,
                 startcall: None | StartCall = None,
                 macrocall: None | MacroCall = None,
                 jumptablecall: None | JumpTableCall = None,
                 ):
        assert name in ["LABEL", "JUMPDEST", "LABEL", "JUMPDEST", "JUMPTABLEDEST", "CONSTANT ",
                        "OPCODE ", "LITERAL", "QUOTE", "MATHOP", "SIZECALL", "STARTCALL", "MACROCALL", "JUMPTABLECALL"]
        self._name_ = name
        match name:
            case "LABEL": self.label = label
            case "JUMPDEST": self.jumpdest = jumpdest
            case "JUMPTABLEDEST": self.jumptabledest = jumptabledest
            case "CONSTANT": self.constant = constant
            case "OPCODE": self.opcode = opcode
            case "LITERAL": self.literal = literal
            case "QUOTE": self.quote = quote
            case "MATHOP": self.mathop = mathop
            case "SIZECALL": self.sizecall = sizecall
            case "STARTCALL": self.startcall = startcall
            case "MACROCALL": self.macrocall = macrocall
            case "JUMPTABLECALL": self.jumptablecall = jumptablecall
