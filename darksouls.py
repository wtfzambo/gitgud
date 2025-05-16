# 1. Find if test exists at all
#    1.1. If not, you died
# 2. Run tests
#    2.1. If all pass, you died
#    2.x. If any fail, you died
# 3. Return output

import argparse


def run_tests():
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames (ignored)")
    parser.add_argument(
        "--test-command",
        required=True,
        help="The command to execute to run tests (e.g. 'npm test', 'pytest', etc.)",
    )

    args = parser.parse_args()

    print("Hello from darksouls!")
    print(f"{args=}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
