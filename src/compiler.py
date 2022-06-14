
from tkinter.font import names
from context import Context
from literal import Literal
from macros import MacroEnum
from value import ValueEnum
from value_utils.mathops import MathOpsEnum
from value_utils.types import Opcode

def compile(main: str, c: Context) -> str:
    main.strip()
    macro_enum: MacroEnum = c.macros[main]
    if macro_enum.macro != None and macro_enum.macro.args != "":
        vv = macro_enum.macro.content
    else:
        raise Exception("bad macro in compile")

    (s,h) =  compile_macro(":", 0, vv, c, {}, {})
    if h == []:
        return s
    else:
        raise Exception("bad compilation result")

def compile_value(
    namespace: str,
    idx: int,
    macro_start_idx: int,
    s: str,
    v: ValueEnum,
    c: Context,
    arg_values: dict[str, ValueEnum],
    jumpdests: dict[str, tuple[bool, int]],
    missed_labels: list[tuple[str, int]],
    time_machine: dict[tuple[str, int], tuple[str, ValueEnum]]
) -> tuple[str, bool]:
    key = (str(v),idx) 
    try:
        count = c.compiles_at_idx[key]
    except KeyError:
        count = 0
    c.compiles_at_idx[key] = count+1
    if count > 100:
        raise Exception("compile value count oveflow")
    
    tm_v = time_machine[(str(namespace), macro_start_idx+idx)]

    if v.opcode != None:
        out = Literal(v.opcode.value)
    elif v.literal != None:
        out = hex(v.literal)
        
    match v._name_:
        case "OPCODE": 
            opcode: Opcode = v.opcode
            out=Literal(v.opcode.value)
    # switch = {
    # } 


def append_macro_start(m: str, i: int) -> str:
    pass

def compile_label(
    namespace: str,
    idx: int,
    macro_start_idx: int,
    s: str,
    v: ValueEnum,
    c: Context,
    arg_values: dict[str, ValueEnum],
    jumpdests: dict[str, tuple[bool, int]],
    missed_labels: list[tuple[str, int]],
    time_machine: dict[tuple[str, str], tuple[str, ValueEnum]]
):
    pass

def insert_missed_label(missed: list[tuple[str, int]], label: str, idx: int):
    pass

def prepare_compile_macro(
    name: str,
    namespace: str,
    c: Context,
    parent_arg_values: dict[str, ValueEnum],
    arg_values: None | list[ValueEnum],
    jumpdests: dict[str, tuple[bool, int]],
    time_machine: dict[tuple[str, str], tuple[str, ValueEnum]]
):
    pass

def compile_macro(
    namespace: str,
    start_idx: int,
    vv: list[ValueEnum],
    c: Context,
    arg_values: dict[str, ValueEnum],
    time_machine: dict[tuple[str, str], tuple[str, ValueEnum]]
) -> tuple[str, list[tuple[str, int]]]:
    pass

def compile_mathop(
    op: MathOpsEnum,
    namespace: str,
    c: Context,
    parent_arg_values: dict[str, ValueEnum],
    idx: int,
    jumpdests: dict[str, tuple[bool, int]],
    left: ValueEnum,
    right: ValueEnum,
    time_machine: dict[tuple[str, str], tuple[str, ValueEnum]]
):
    pass
