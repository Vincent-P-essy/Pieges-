"""Start the real Tk game in a temporary display and capture its initial board."""
import pathlib,subprocess,sys,time
from PIL import ImageGrab
p=subprocess.Popen([sys.executable,"piege.py"])
try:
    time.sleep(5)
    if p.poll() is not None:
        raise RuntimeError("The game stopped before the capture")
    destination=pathlib.Path("docs/screenshots/game.png")
    destination.parent.mkdir(parents=True,exist_ok=True)
    ImageGrab.grab().save(destination)
    print("Captured the running game:",destination)
finally:
    p.terminate()
    try:p.wait(timeout=5)
    except subprocess.TimeoutExpired:p.kill()
