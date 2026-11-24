"""The Robot Pickup Line Championship — make.fun entry.

A robot pickup line with a twist: the robot has to prove it is NOT a robot.
The captcha joke flipped around — instead of the human proving they're human,
the robot is the one begging to be believed.

Writes one robot pickup line (81 characters) to /output/entry.txt.
"""

import os

MAX_LEN = 200

# Chosen line (81 characters). The joke flips the captcha: the robot,
# not the human, has to prove it is not a robot.
LINE = "Are you a captcha? Because every time I see you, I have to prove I'm not a robot."

assert 1 <= len(LINE) <= MAX_LEN, "line out of gate"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    assert f.read() == LINE
