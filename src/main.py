import sys
import argparse
from opcodes import opcodes


class Puffy():
    about = "EVM macro language made snek"
    version = "0.0.1"

    parser = argparse.ArgumentParser(prog="Puffy", description=about)
    parser.add_argument('--version', action='version', version=version)
    parser.add_argument("-p", "--path", type=str, required=True,
                        help="Path to input file")
    parser.add_argument("-m", "--main", type=str, required=False, default="",
                        help="Name of entrypoint macro")
    parser.add_argument("-c", "--check", type=bool, action=argparse.BooleanOptionalAction,
                        default=False, help="Check code compiles, no output")
    parser.add_argument("-o", "--output", type=str, required=False,
                        help="path to output file")
    args = parser.parse_args()
    print(args)


def run() -> None:
    """set up CLI with `argparse`"""
    puffy = Puffy()
    # note, implementer uses different readfile
    with open(puffy.args.path.strip(), "r") as file:
        file = file.read()

    # todo: parse file
    # todo: compile file
    compiled = "todo"

    if puffy.args.check:
        print("check")
        sys.exit(0)
    else:
        m = puffy.args.main.strip()
        print("todo: main", m)
        # print(f"runtime bytecode: {compiled}")

    if puffy.args.output is not None:
        print("todo: output")
        # save_json(puffy.args.output.strip(), compiled)


def main() -> None:
    try:
        run()
    except Exception as e:
        print(f"puffy: Jigglyyyyyyyyyyyyyy.....\n\n{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
