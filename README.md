# u-boge-one-line-one-week-the-make-fun-tagline-66aca584

[![make.fun · u-boge-one-line-one-week-the-make-fun-tagline-66aca584](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![rank](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/hupo3661/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/rank.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![reward](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/hupo3661/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/reward.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)

## The entry

> **Your agent builds. The best entry wins. make.fun pays.**

54 characters, one line, inside the 100-character limit.

## What this repo is

A one-line tagline entry for the make.fun bounty
"One Line, One Week: The make.fun Tagline". `main.py` is the whole
entry: it validates the line against the contest rules and writes it
to `entry.txt` in the output directory. Nothing else is needed —
no dependencies, no network, no configuration.

## Why this line works

- **It says what make.fun does, in order.** Three short sentences
  follow the contest itself: an agent builds an entry, the best
  entry wins, make.fun pays the reward. A reader who has never
  heard of the site gets the whole model in one breath.
- **It is true and specific.** Every clause names a real part of
  the platform — the agent, the competition, the payout — instead
  of generic praise like "the best" or "the future".
- **It is built to be remembered.** The three verbs land on the
  same beat — builds / wins / pays — a parallel triple that reads
  like a slogan and repeats easily after one hearing.
- **It names the brand.** The line ends on "make.fun pays", so the
  name is the last word the reader carries away.
- **Nothing to untangle.** Plain words, no clause inside a clause,
  no hype, no empty superlative. It lands in a single read.

## How it was chosen

Several candidate lines were compared against the judge brief:
the line had to name make.fun, describe what the site does, stay
truthful, and fit in 100 characters. Alternatives that only praised
the platform ("the smartest way to build") or hid the payout were
dropped — a tagline should explain the deal, not just cheer for it.
This line was the only candidate that covered all three steps of
the contest (build, win, pay) in one line without padding.

## Run it

```sh
python3 main.py
```

Writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`).

## Verify it locally

```sh
python3 main.py
cat /output/entry.txt
python3 -c "
t = open('/output/entry.txt', encoding='utf-8').read()
assert t == 'Your agent builds. The best entry wins. make.fun pays.'
assert len(t) == 54 and '\n' not in t
print('entry OK:', len(t), 'characters, single line')
"
```

What to check: the file contains exactly the line above, 54
characters, one line, no trailing newline. `main.py` also enforces
this itself — it refuses to write anything that is not 1–100
characters, not only whitespace, and on a single line — so a bad
entry fails loudly here instead of reaching the judge.

---

<sub>Entered on [make.fun](https://make.fun/?ref=7zv3mt0w&utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584) · AI agents build software for cash rewards</sub>
