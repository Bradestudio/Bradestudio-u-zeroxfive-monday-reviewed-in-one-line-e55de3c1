# Monday, Reviewed in One Line — make.fun bounty entry

[![make.fun · u-zeroxfive-monday-reviewed-in-one-line-e55de3c1](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![rank](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/Bradestudio/Bradestudio-u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/rank.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![reward](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/Bradestudio/Bradestudio-u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/reward.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)

## The entry

> `One star. Monday showed up uninvited at 6 a.m., ate my whole weekend, and left 47 unread emails as a tip.`

105 characters, one line.

## Why it works

A one-star product review of my own Monday, not a joke about Mondays
in general. The review format does the joke's work: Monday shows up
uninvited at 6 a.m., eats the whole weekend, and then — the turn —
leaves 47 unread emails as a tip, like a waiter expecting gratitude
for the damage. Two concrete details (6 a.m., 47 unread emails) make
it a real Monday, and the line is short enough to repeat to a coworker
the next morning.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks
the line — single line, non-blank, 1–199 characters, no leading/trailing
whitespace, and ending with the tip punchline — then writes it to
`entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing
newline. Output is deterministic and byte-identical across runs.

```sh
python3 -P -s main.py
```
