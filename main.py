import mujoco

XML = """
<mujoco>
  <worldbody>
    <geom name="floor" type="plane" size="10 10 0.1" pos="0 0 0" condim="3" />
    <body name="ball" pos="0 0 1">
      <geom type="sphere" size="0.1" rgba="1 0 0 1" />
    </body>
  </worldbody>
</mujoco>
"""

def run_steps(steps: int = 10) -> None:
    """Run a simple MuJoCo simulation and print the object position."""
    model = mujoco.MjModel.from_xml_string(XML)
    data = mujoco.MjData(model)
    for _ in range(steps):
        mujoco.mj_step(model, data)
        print("position:", data.qpos)


if __name__ == "__main__":
    run_steps()
