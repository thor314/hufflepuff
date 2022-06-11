
class Literal():
    bytess: bytes = bytes()

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

    def to_hex(self) -> bytes:
        # print(str(self.bytes))
        return self.bytess

