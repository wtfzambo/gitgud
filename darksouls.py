import argparse
import enum
import os
import subprocess

os.system("color")

RED_DARK = "\033[31m"
END = "\033[0m"

YOU_DIED = """
⢰⣶⣶⣤⣤⡄⠀⠀⠀⠀⢰⣶⣶⣶⣶⠀⢀⣠⣶⣿⡆⣿⣷⣦⣄⠀⠀⠀⠀⢶⣶⣶⣶⣶⡆⠀⠀⠀⠀⣶⣶⣶⣶⡆⠀⠀⠀⠀⢶⣶⣶⣶⢠⣶⣶⣶⣶⣦⣄⠀⠀⠀⠀⣶⣶⣶⣶⣶⠰⣿⣷⣶⣶⣶⣶⣶⣶⡶⢶⣶⣶⡆⣶⣶⣶⣶⣶⣤⣄⠀⠀⠀⠀
⠀⠈⢿⣿⣿⣇⠀⠀⠀⠀⠀⣽⣿⡿⠉⣴⣿⣿⠟⠋⠀⠀⠈⠛⣿⣷⣆⠀⠀⠀⢻⣿⣿⠁⠀⠀⠀⠀⠀⠈⣿⣿⡏⠀⠀⠀⠀⠀⠀⢹⣿⣿⠈⠉⠉⠙⠻⣿⣿⣷⣆⠀⠀⠈⣿⣿⣿⠁⠀⠀⣿⣿⣿⠉⠙⢻⣿⡅⠀⣿⣿⡇⠙⠛⠛⠻⢿⣿⣿⣷⣄⠀⠀
⠀⠀⠀⠻⣿⣿⡄⠀⠀⠀⣼⣿⠟⠀⣼⣿⣿⠋⠀⠀⠀⠀⠀⠀⠈⢿⣿⣆⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠹⣿⣿⣦⠀⠀⢻⣿⡇⠀⠀⠀⣿⣿⣿⠀⠀⠈⠉⠁⠀⣿⣿⡇⠀⠀⠀⠀⠀⠈⢻⣿⣿⣆⠀
⠀⠀⠀⠀⠹⣿⣿⡀⠀⣸⣿⠏⠀⢰⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡄⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡇⠀⢸⣿⡇⠀⠀⠀⣿⣿⡟⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡄
⠀⠀⠀⠀⠀⢻⣿⣷⣰⣿⠏⠀⠀⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⢸⣿⡇⠀⠀⠀⣿⣿⣷⣤⣤⣾⣿⠇⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇
⠀⠀⠀⠀⠀⠈⢻⣿⣿⡿⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⢿⣿⡇⠀⠀⠀⣿⣿⣿⠛⠻⣿⣿⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⢹⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⠀⢸⣿⡿⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⣸⣿⡇⠀⠀⠀⣿⣿⡇⠀⠀⠘⠛⠀⠀⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠃
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠈⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠇⠀⠸⣿⣿⠀⠀⠀⠀⠀⠀⢀⣿⣿⠃⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⣿⣿⡇⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⠀
⠀⠀⠀⠀⠀⠀⢈⣿⣿⡇⠀⠀⠀⠀⠈⠻⣿⣧⡀⠀⠀⠀⠀⠀⢀⣾⣿⠏⠀⠀⠀⢻⣿⣧⡀⠀⠀⠀⢀⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡆⠀⠀⠀⠀⢀⣴⣿⣿⠇⠀⠀⣿⣿⣧⠀⠀⠀⣿⣿⣧⠀⠀⠀⢰⣦⠀⢿⣿⣿⠀⠀⠀⠀⠀⢀⣼⣿⣿⠃⠀
⠀⠀⠀⠀⠀⠀⣼⣿⣿⣷⣄⠀⠀⠀⠀⠀⠙⢿⣿⣶⣦⣤⣴⣶⣿⡿⠋⠀⠀⠀⠀⠀⠻⣿⣿⣶⣶⣶⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣷⣦⣤⣴⣶⣿⣿⠟⠁⠀⠀⣴⣿⣿⣿⣄⡀⣴⣿⣿⣿⣷⣤⣶⣿⡇⣠⣿⣿⣿⣷⣶⣶⣶⣶⣿⡿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠋⠉⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠛⠋⠉⠉⠀⠀⠀⠀⠀⠉⠉⠉⠙⠛⠁⠉⠉⠉⠙⠛⠛⠛⠉⠁⠉⠉⠛⠛⠛⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀
"""


class ExitCode(enum.IntEnum):
    SUCCESS = 0
    FAILURE = 1
    NOT_REPO = 0


def find_repo_root(path: str = ".") -> str | None:
    current_path = os.path.abspath(path)
    while True:
        if os.path.isdir(os.path.join(current_path, ".git")):
            return current_path
        parent_path = os.path.dirname(current_path)
        if parent_path == current_path:
            return None
        current_path = parent_path


def you_died():
    print(RED_DARK + YOU_DIED + END)


def run_tests(test_command: str):
    repo_root = find_repo_root(os.getcwd())
    if not repo_root:
        print("Not in a git repository.")
        return ExitCode.NOT_REPO

    print(f"Dark Souls: Running test command '{test_command}' in {repo_root}")

    try:
        command_parts = test_command.split()
        result = subprocess.run(
            command_parts,
            cwd=repo_root,  # Run the command from the repo root
            check=False,  # Don't raise CalledProcessError on non-zero exit
        )

        if result.returncode == ExitCode.SUCCESS:
            print("Dark Souls: Tests passed! Your code is safe... this time.")
            return ExitCode.SUCCESS
        else:
            print("Dark Souls: Tests failed. You died.")
            return ExitCode.FAILURE

    except Exception as e:
        print(f"Dark Souls: An error occurred: {e}")
        return ExitCode.FAILURE


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames (ignored)")
    parser.add_argument(
        "--test-command",
        required=True,
        type=str,
        help="The command to execute to run tests (e.g. 'npm test', 'pytest', etc.)",
    )

    args = parser.parse_args()
    exit_code = run_tests(args.test_command)  # pyright: ignore[reportAny]

    if exit_code is ExitCode.FAILURE:
        you_died()
    else:
        print("Dark Souls: You have proven yourself worthy.")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
