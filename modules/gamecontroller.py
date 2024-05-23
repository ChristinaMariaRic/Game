import configparser
from pathlib import Path
from universe import Universe
from ruleset import Ruleset


class GameController:
    """
    Klasse zur Steuerung des Spiels "Game of Life".

    Attribute:
        config (configparser.ConfigParser): Die gelesene Konfigurationsdatei.
        universe (Universe): Das Universum des Spiels.
    """

    def __init__(self, config_file: Path):
        """
        Initialisiert den GameController mit den Parametern aus der Konfigurationsdatei.

        """
        self.config = self._read_config(config_file)
        self.universe = self._setup_game()

    def _read_config(self, config_file: Path) -> configparser.ConfigParser:
        """
        Liest die Konfigurationsdatei ein.

        Args:
            config_file (Path): Pfad zur Konfigurationsdatei.

        Returns:
            configparser.ConfigParser: Die gelesene Konfiguration.
        """
        config = configparser.ConfigParser()
        config.read(config_file)
        return config

    def _setup_game(self) -> Universe:

        height = int(self.config["GAME"]["height"])
        width = int(self.config["GAME"]["width"])
        ruleset = Ruleset(self.config["GAME"]["ruleset"])
        p_cell_alive = float(self.config["GAME"]["p_cell_alive"])
        char_alive = str(self.config["VISUAL"]["char_alive"])
        char_dead = str(self.config["VISUAL"]["char_dead"])

        return Universe(height, width, ruleset, p_cell_alive, char_alive, char_dead)

    def run_game(self) -> None:

        iteration_delay = float(self.config["VISUAL"]["iteration_delay"])
        iterations = int(self.config["GAME"]["iterations"])
        for _ in range(iterations):
            self.universe.print_universe()
            self.universe.run_one_iteration()
            time.sleep(iteration_delay)

        user_input = input("Möchten Sie das Spiel fortsetzen? (j/n): ")
        if user_input.lower() == "n":
            return
        else:
            self.run_game()

