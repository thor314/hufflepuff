
import enum
from macros import JumpTable

class SizeCallEnum(enum.Enum):
    MACROCALL = 1
    JUMPTABLE = 2
    def __new__(cls, variant: str):

        pass
        # return super().__new__(value)
    # variant: str
    # val: MacroCall | JumpTable


class SizeCall:
    sizecall: SizeCallEnum

# class StartCall:
#     startcall: StartCall

# class MacroCall:
#     macrocall: MacroCall

# class JumpTableCall:
#     jumptablecall: JumpTableCall
