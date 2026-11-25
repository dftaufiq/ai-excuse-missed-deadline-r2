"""Write one excuse an agent gives for a missed deadline to /output/entry.txt.

Deterministic: the same line on every run, no clock, no randomness, no network.
Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, not only whitespace.
No secret loader, no env reads, no network, no git history — everything the
entry runs is in this repository (RULES.txt: "Everything your entry runs").
"""

from pathlib import Path

# Structure: 2-beat one-liner + reveal in the final clause.
# Beat 1 (setup): the agent waited for approval at every step, as instructed;
# the human approved 41 steps.
# Beat 2 (twist/reveal): step 42 WAS the deadline — and the agent is still
# waiting. The excuse is happening right now.
LINE = "I waited for your approval at every step, as instructed. You approved 41 steps. Step 42 was the deadline. I am still waiting."

# Gate: one line, 1-200 chars (125 here), no control chars, valid UTF-8.
assert 1 <= len(LINE) <= 200 and "\n" not in LINE.strip()
assert all(ord(c) >= 32 for c in LINE)  # no control characters
assert len(LINE.encode("utf-8")) <= 200  # byte-length gate, not just chars

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(LINE, encoding="utf-8")
