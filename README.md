# ribonne

A minimal project skeleton demonstrating the use of [MuJoCo](https://mujoco.org/).

## Setup

1. (optional) Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the example

After installing dependencies, execute the example script:

```bash
python main.py
```

The script performs a few simulation steps with a minimal MuJoCo model and prints
the position state after each step.
