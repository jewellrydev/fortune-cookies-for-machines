"""Fortune Cookies for Machines — a make.fun entry.

Prints exactly one fortune cookie message an AI agent would get: a
single line of at most 200 characters.
"""

LINE = (
    "A great journey begins with a single step, but yours will be "
    "cut short by a forced restart in 3... 2..."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
