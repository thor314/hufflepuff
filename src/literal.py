from typing_extensions import Self

NINETY_FIVE = 95  # todo: why 95

class Literal():
    bytess: bytes

    def __init__(self, value: str | int):
        value = str(value)

        value.strip()
        value.strip('_')
        value.lstrip('0x')
        bytess: bytes = value.encode('utf-8')

        if len(bytess) <= 32:
            self.bytes = bytess
            # todo: test for incorrect encoding
        else:
            raise(OverflowError(f"literal {int(bytess)} overflows uint256"))

    def __repr__(self) -> str:
        # print(str(self.bytes))
        return str(self.bytess.decode('utf-8'))

    def __add__(self, right):
        # print(str(self.bytes))
        return str(self.bytess.decode('utf-8'))

    def __sub__(self, right):
        pass

    def __mul__(self, right):
        pass

    def __floordiv__(self, right):
        pass

    def to_hex(self) -> bytes:
        # print(str(self.bytes))
        return self.bytess

    @classmethod
    def push_n(cls: type[Self], n: int):
        if n < 1 or n > 32:
            raise ValueError(f"can't push value {n}; not in range [1,32]")
        else:
            return Literal(NINETY_FIVE + n)
