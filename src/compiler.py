
from context import Context
from value import ValueEnum

def compile(main: str, c: Context) -> str:
    pass

def compile_value(
    namespace: str,
    idx: int,
    macro_start_idx:int,
    s: str,
    v: ValueEnum,
    c: Context,
    arg_values: dict[str,ValueEnum],
    jumpdests: dict[str, tuple[bool,int]],
    missed_labels: list[tuple[str,int]],
    time_machine: dict[tuple[str,str],tuple[str,ValueEnum]]
)-> tuple[str,bool]:
    pass

def append_macro_start(m: str, i:int)-> str:
    pass
    
def compile_label(
    namespace: str,
    idx: int,
    macro_start_idx:int,
    s: str,
    v: ValueEnum,
    c: Context,
    arg_values: dict[str,ValueEnum],
    jumpdests: dict[str, tuple[bool,int]],
    missed_labels: list[tuple[str,int]],
    time_machine: dict[tuple[str,str],tuple[str,ValueEnum]]
):
    pass

def insert_missed_label(missed: list[tuple[str,int]], label: str, idx: int):
    pass

def prepare_compile_macro(
    name: str,
    namespace: str,
    c: Context,
    parent_arg_values: dict[str,ValueEnum],
    arg_values: None|list[ValueEnum],
    jumpdests: dict[str, tuple[bool,int]],
    time_machine: dict[tuple[str,str],tuple[str,ValueEnum]]
):
    pass

def compile_macro(
    namespace: str,
    idx: int,
    start_idx:int,
    vv: list[ValueEnum],
    c: Context,
    arg_values: dict[str,ValueEnum],
    jumpdests: dict[str, tuple[bool,int]],
    missed_labels: list[tuple[str,int]],
    time_machine: dict[tuple[str,str],tuple[str,ValueEnum]]
): pass

def compile_mathop(
    op: MathOps,
    namespace: str,
    c: Context,
    parent_arg_values: dict[str,ValueEnum],
    idx: int,
    jumpdests: dict[str, tuple[bool,int]],
    left: ValueEnum,
    right: ValueEnum,
    time_machine: dict[tuple[str,str],tuple[str,ValueEnum]]
):
    pass
