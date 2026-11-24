"""The Excuse an AI Agent Gives Its Human.

Writes one line (93 characters) to /output/entry.txt:
the excuse an AI agent gives its human for missing a deadline.
Pure Python 3.13 standard library, deterministic: no network, no clock,
no randomness, no input. Two runs write byte-identical output.
"""

import os

# Chosen line: the agent's retry policy is exponential backoff, the
# deadline is not — so it expires while the agent is still waiting
# between retries. Parallel twist, deadpan, one breath, no blame on
# the market, the data, or the human. 93 characters.
# Revision note: wording unchanged since v1; the line was picked over
# nine other candidates (see candidates.md) for its short, fresh turn.
EXCUSE = "My retry policy was exponential backoff. The deadline was not. It expired during the backoff."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
