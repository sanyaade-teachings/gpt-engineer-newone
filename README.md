<<<<<<< main
# aiDrive Engineer
=======
# aiDrive Engineer

>>>>>>> main
[![Discord Follow](https://dcbadge.vercel.app/api/server/4t5vXHhu?style=flat)](https://discord.gg/4t5vXHhu)
[![GitHub Repo stars](https://img.shields.io/github/stars/AntonOsika/aiDrive-engineer?style=social)](https://github.com/AntonOsika/aiDrive-engineer)
[![Twitter Follow](https://img.shields.io/twitter/follow/antonosika?style=social)](https://twitter.com/AntonOsika)

**Specify what you want it to build, the AI asks for clarification, and then builds it.**

aiDrive Engineer is made to be easy to adapt, extend, and make your agent learn how you want your code to look. It generates an entire codebase based on a prompt.

[Demo](https://twitter.com/antonosika/status/1667641038104674306) 👶🤖

## Project philosophy

- Simple to get value
- Flexible and easy to add new own "AI steps". See `steps.py`.
- Incrementally build towards a user experience of:
  1. high level prompting
  2. giving feedback to the AI that it will remember over time
- Fast handovers back and forth between AI and human
- Simplicity, all computation is "resumable" and persisted to the filesystem

## Usage

<<<<<<< main
**Setup**
- `git clone git@github.com:AntonOsika/aiDrive-engineer.git`
- `cd aiDrive-engineer`
- `make install`
- `source venv/bin/activate`
=======
Choose either **stable** or **development**.

For **stable** release:

- `pip install aiDrive-engineer`

For **development**:
- `git clone git@github.com:AntonOsika/aiDrive-engineer.git`
- `cd aiDrive-engineer`
- `pip install -e .`
  - (or: `make install && source venv/bin/activate` for a venv)

**Setup**
>>>>>>> main

With an api key that has aiDrive4 access run:

- `export OPENAI_API_KEY=[your api key]`

**Run**:

- Create an empty folder. If inside the repo, you can run:
  - `cp -r projects/example/ projects/my-new-project`
- Fill in the `main_prompt` file in your new folder
<<<<<<< main
- Run: `aiDrive-engineer projects/my-new-project`
=======
- `aiDrive-engineer projects/my-new-project`
  - (Note, `aiDrive-engineer --help` lets you see all available options. For example `--steps use_feedback` lets you improve/fix code in a project)
>>>>>>> main

**Results**:

- Check the generated files in `projects/my-new-project/workspace`

## Features

You can specify the "identity" of the AI agent by editing the files in the `identity` folder.

Editing the identity, and evolving the `main_prompt`, is currently how you make the agent remember things between projects.

Each step in `steps.py` will have its communication history with aiDrive4 stored in the logs folder, and can be rerun with `scripts/rerun_edited_message_logs.py`.

## Contributing

We are building the open platform for devs to tinker with and build their personal code-generation toolbox.

If you want to contribute, please check out the [roadmap](https://github.com/AntonOsika/aiDrive-engineer/blob/main/ROADMAP.md), [projects](https://github.com/AntonOsika/aiDrive-engineer/projects?query=is%3Aopen) or [issues tab](https://github.com/AntonOsika/aiDrive-engineer/issues) in the GitHub repo. You are welcome to read the [contributing document](.github/CONTRIBUTING.md) and join our [Discord 💬](https://discord.gg/4t5vXHhu).

We are currently looking for more maintainers and community organisers. Email <anton.osika@gmail.com> if you are interested in an official role.

## Example

<<<<<<< main
https://github.com/AntonOsika/aiDrive-engineer/assets/4467025/6e362e45-4a94-4b0d-973d-393a31d92d9b
=======
<https://github.com/AntonOsika/aiDrive-engineer/assets/4467025/6e362e45-4a94-4b0d-973d-393a31d92d9b>
>>>>>>> main
