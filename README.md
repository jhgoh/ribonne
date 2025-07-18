# ribonne

A minimal project skeleton demonstrating the use of [MuJoCo](https://mujoco.org/).

## Setup

1. Create the Conda environment:

```bash
conda env create -f environment.yml
```

2. Activate the environment:

```bash
conda activate ribonne
```

The environment file installs the required `mujoco` package. If you prefer
using `pip` in another environment, run:

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