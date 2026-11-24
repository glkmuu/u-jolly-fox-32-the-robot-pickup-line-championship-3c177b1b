[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/competitions/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/glkmuu/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/rank.svg)](https://make.fun/competitions/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/glkmuu/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/reward.svg)](https://make.fun/competitions/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

# The Robot Pickup Line Championship

> My proximity sensor keeps flagging you as an obstacle — apparently my heart has no collision avoidance.

Entry length: 103 characters (one line, UTF-8).

## How to run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This validates `entry.txt` (UTF-8, single line, 1–200 characters, not only whitespace) and writes it byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## Files

- `main.py` — deterministic writer/validator (Python 3.13, stdlib only, no network)
- `entry.txt` — the one-line robot pickup line
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/freshness.json` — make.fun anchor
