<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
<img src="imgs/logo.png" alt="logo" style="display: block; margin: 0 auto; width: 50%">
</p>

Git Gud is the best assistant for Vibe Coders 💪.

With Git Gud, you won't have to worry anymore about Claude generating wrong code: Git Gud will check your codebase and remove any mistake that it finds, leaving your project clean and lean.

## Installation

Getting started with Git Gud is easy: in your favorite AI Editor (e.g. Cursor, Windsurf), ask it to install `pre-commit`.

For instance you can write:

```txt
Cursor, please install `pre-commit` in the current project.
```

> [!TIP]
> If you don't know what "Pre-commit" is, imagine like a suite of checks to make sure your code stays always clean and organized. It's like checking if you have the keys and phone before leaving the house.

Once `pre-commit` is installed, all you have to do is create a new file in the project called `.pre-commit-config.yaml` (mind the dot! 😊), and copy-paste the following content in it:

```yml
repos:
  - repo: https://github.com/wtfzambo/gitgud
    rev: 1.0.0
    hooks:
      - id: gitgud
        args: ["--test-command", "<insert test command here>"]
```

That's it, you're done! You can now continue working as usual.

🚀 Happy coding!
