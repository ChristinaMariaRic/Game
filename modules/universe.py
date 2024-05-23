import numpy as np
from ruleset import Ruleset
from cell import Cell


class Universe:
    """
        Die Klasse Universe repräsentiert das Universum des Game of Life.

        Attribute:
        - height (int): Höhe des Universums.
        - width (int): Breite des Universums.
        - ruleset (Ruleset): Das verwendete Regelwerk.
        - p_cell_alive (float): Wahrscheinlichkeit für eine lebende Zelle zu Beginn.
        - char_alive (str): Darstellung einer lebenden Zelle in der Konsole.
        - char_dead (str): Darstellung einer toten Zelle in der Konsole.
        - _cells (list[list[int]]): Die Zellen des Universums als 2D-Matrix.
        """

    def __init__(self, height: int, width: int, ruleset: Ruleset, p_cell_alive: float, char_alive: str, char_dead: str):
        """
        Initialisiert die Universe-Instanz.

        Argumente:
        - height (int): Höhe des Universums.
        - width (int): Breite des Universums.
        - ruleset (Ruleset): Das verwendete Regelwerk.
        - p_cell_alive (float): Wahrscheinlichkeit für eine lebende Zelle zu Beginn.
        - char_alive (str): Darstellung einer lebenden Zelle in der Konsole.
        - char_dead (str): Darstellung einer toten Zelle in der Konsole.
        """
        self.height = height
        self.width = width
        self.ruleset = ruleset
        self.p_cell_alive = p_cell_alive
        self.char_alive = char_alive
        self.char_dead = char_dead
        self._cells = self._create_universe()

    def _create_empty_universe(self) -> list:
        """Erstellt ein Universum mit toten Zellen."""
        return [[Cell(0, self.ruleset) for _ in range(self.width + 2)] for _ in range(self.height + 2)]

    def _initialize_visible_universe(self, universe: list) -> list:
        """Initialisiert das sichtbare Universum mit Zellen zufällig lebendig oder tot."""
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                initial_state = int(np.random.choice([0, 1], p=[1 - self.p_cell_alive, self.p_cell_alive]))
                universe[i][j] = Cell(initial_state, self.ruleset)
        return universe

    def _add_neighbors_to_cells(self, universe: list) -> list:
        """Fügt jedem Zellenobjekt die Nachbarn hinzu."""
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                cell = universe[i][j]
                neighbors = [
                    universe[i - 1][j - 1], universe[i - 1][j], universe[i - 1][j + 1],
                    universe[i][j - 1], universe[i][j + 1],
                    universe[i + 1][j - 1], universe[i + 1][j], universe[i + 1][j + 1]
                ]
                cell.neighbors = neighbors
        return universe

    def _create_universe(self) -> list:
        """Erzeugt das Universum."""
        empty_universe = self._create_empty_universe()
        start_universe = self._initialize_visible_universe(empty_universe)
        return self._add_neighbors_to_cells(start_universe)

    def print_universe(self):
        """Stellt das aktuelle Universum in der Konsole dar."""
        for row in self._cells[1:-1]:
            print(' '.join([self.char_alive if cell.state else self.char_dead for cell in row[1:-1]]))
        print("--" * len(self._cells))

    def run_one_iteration(self):
        """Führt eine Iteration durch."""
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                self._cells[i][j].calculate_state_of_next_iteration()

        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                self._cells[i][j].update_state()