import enum
from context import Context
from value import ValueEnum

def remove_comments(s: str) -> str:
    data = s
    formatted = ""
    while data.strip() is not "":
        idx_multi = data.find("/*")
        idx_single = data.find("//")
        if idx_multi != -1:  # found some string
            formatted += data[0:idx_multi]

            idx_multiend = data.find("*/")
            if idx_multiend == -1:
                raise Exception("multiline comment end not found")
            else:
                formatted += data[idx_multiend]
        elif idx_single != -1:
            formatted += (data[0:idx_single])
            end = data.find("\n")
            if end == 0:
                formatted += " " * len(data)  # todo: this is suss
            elif end != -1:
                formatted += " " * end
            else:
                break
        else:
            formatted += data
            break
    return formatted

def is_label_char(c: str) -> bool:
    return c.isalnum() or c == '_'

def parse_value(s: str, c: Context) -> ValueEnum:
    s.strip()
    if s == "":
        raise Exception("attempted to parse empty value")
    pass

def parse_sizecall(s: str, c: Context) -> ValueEnum:
    pass

def parse_startcall(s: str, c: Context) -> ValueEnum:
    pass

def parse_math(s: str, c: Context) -> ValueEnum:
    pass

def parse_macro(s: str, c: Context) -> ValueEnum:
    pass

def parse_macro_call(s: str, c: Context) -> MacroCall:
    pass

def split_call_args(s: str) -> list[str]:
    pass

def parse_expression(s: str, c: Context) -> Macro:
    pass

def macro_to_value(m: Macro) -> ValueEnum:
    pass

def parse_top_level(s: str) -> Context:
    pass

def find_math(s: list[str], start: int) -> int:
    pass


# Probably want to move these

class Num:
    s: str

    def __repr__(self) -> str:
        return self.s
    pass

class Parsable(enum.Enum):
    Macro = 1
    Constant = 2
    SizeCall = 3
    StartCall = 4
    MacroCall = 5
    JumpTable = 6
    WhiteSpace = 7

    def rgx(self) -> str:
        match self._name_:
            case "WhiteSpace": return r"^\s+"
            case "Macro": return r"^\s*(\w+)\s*=\s*\((.*)\)\s*\{\s*([^}]*)\s*}"
            case "Constant": return r"^\s*(\w+)\s*=\s*([^=\n]*)"
            case "SizeCall": return r"^\s*size\s*\(\s*(.+)\s*\)"
            case "StartCall": return r"^\s*start\s*\(\s*(.+)\s*\)"
            case "MacroCall": return r"^\s*(\w+)\(\s*(.*)\s*\)"
            case "JumpTable": return r"^\s*(\w+)\s*=\s*\{\s*([\w\s]*)\s*\}"
            case _: raise NameError("unknown Parsable")
