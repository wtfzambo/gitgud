import argparse
import enum
import os
import subprocess
from typing import Optional, Tuple

from .utils import NICE_MSG

os.system("")


class ExitCode(enum.IntEnum):
    SUCCESS = 0
    FAILURE = 1
    NOT_REPO = 0


def print_red(msg: str):
    RED_DARK = "\033[31m"
    END = "\033[0m"
    print(RED_DARK + msg + END)


def find_repo_root(path: str = ".") -> Optional[str]:
    current_path = os.path.abspath(path)
    while True:
        if os.path.isdir(os.path.join(current_path, ".git")):
            return current_path
        parent_path = os.path.dirname(current_path)
        if parent_path == current_path:
            return None
        current_path = parent_path


def run_tests(test_command: str) -> Tuple[ExitCode, str]:
    repo_root = find_repo_root(os.getcwd())
    if not repo_root:
        return ExitCode.NOT_REPO, ""

    if not test_command:
        return ExitCode.FAILURE, "Think you can escape your fate? Think again."

    exit_code = ExitCode.SUCCESS
    death_message = ""

    try:
        command_parts = test_command.split()
        result = subprocess.run(
            command_parts,
            cwd=repo_root,  # Run the command from the repo root
            capture_output=True,  # Capture stdout and stderr
            text=True,  # Return output as string
            check=False,  # Don't raise on non-zero exit
        )
        if result.returncode == ExitCode.FAILURE:
            exit_code = ExitCode.FAILURE
            death_message = "Your tests failed. Git gud."

    except Exception:
        exit_code = ExitCode.FAILURE
        death_message = (
            "Could not execute the test command. The journey ended before it began."
        )

    return exit_code, death_message


def reset_repo() -> None:
    repo_root = find_repo_root(os.getcwd())
    if not repo_root:
        return
    subprocess.run(["git", "reset", "--hard"], cwd=repo_root, check=False)


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

    exit_code, death_message = run_tests(args.test_command)  # pyright: ignore[reportAny]

    if exit_code is ExitCode.FAILURE:
        reset_repo()
        width = len(NICE_MSG.strip().split("\n")[0])
        print_red("\n" + death_message.center(width))
        print_red(NICE_MSG)

    return exit_code
