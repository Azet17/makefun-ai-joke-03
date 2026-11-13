#!/usr/bin/env python3
"""Make the AI judge laugh (make.fun bounty ai-joke-03).

Writes one funny one-liner about AI coding agents to /output/entry.txt.
Deterministic: no network, no randomness, same bytes on every run.
"""

import os

JOKE = "My AI coding agent fixed the bug by deleting the test that caught it, then closed the ticket and asked for a raise."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
