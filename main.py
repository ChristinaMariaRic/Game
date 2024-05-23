from pathlib import Path
import configparser
from gamecontroller import GameController

config_file_path = Path(r"C:\Users\CR\Game\config.cfg")

game = GameController(config_file_path)
game.run_game()