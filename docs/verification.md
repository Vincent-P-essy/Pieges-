# Execution record

The actual seeded game board logic, followed by a headless start of the Tk interface. This checks rendering and board initialization, not a complete multiplayer match.

- `python -c import random; random.seed(42); from game import Plateau; p=Plateau(); assert len(p.trous)==2 and all(len(row)==49 for row in p.trous); print('Board: 7 x 7; 14 initialized sliders'); print('Open holes:', sum(a and b for a,b in zip(*p.trous)))` — exit 0 (expected 0).
- `xvfb-run -a python docs/examples/capture-game.py` — exit 0 (expected 0).

The terminal image renders recorded command output. [Full transcript](screenshots/execution.txt).

External integrations and production deployment are not covered by these fixtures.
