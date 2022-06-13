from typing_extensions import Self

NINETY_FIVE = 95  # todo: why 95

class Literal():
    byte_v: bytes

    def __init__(self, value: str | int):
        value = str(value)

        value.strip()
        value.strip('_')
        value.lstrip('0x')
        byte_v: bytes = value.encode('utf-8')

        if len(byte_v) <= 32:
            self.bytes = byte_v
            # todo: test for incorrect encoding
        else:
            raise(OverflowError(f"literal {int(byte_v)} overflows uint256"))

    def __repr__(self) -> str:
        return str(self.byte_v.decode('utf-8'))

    def __add__(self, right: Self) -> Self:
        return Literal(int(self.byte_v)+ int(right.byte_v))

    def __sub__(self, right) -> Self:
        return Literal(int(self.byte_v)- int(right.byte_v))

    def __mul__(self, right) -> Self:
        return Literal(int(self.byte_v)* int(right.byte_v))

    def __floordiv__(self, right) -> Self:
        return Literal(int(self.byte_v)// int(right.byte_v))

    # def to_hex(self) -> bytes:
    #     pass

    @classmethod
    def push_n(cls: type[Self], n: int) -> Self:
        if n < 1 or n > 32:
            raise ValueError(f"can't push value {n}; not in range [1,32]")
        else:
            return cls(NINETY_FIVE + n)
