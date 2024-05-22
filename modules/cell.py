import warnings
from ruleset import Ruleset


class Cell:
    """
      Die Klasse Cell repräsentiert eine Zelle im Game of Life.

      Attribute:
      - _current_state (int): Der aktuelle Zustand der Zelle (0 = tot, 1 = lebendig).
      - _state_next_iteration (Optional[int]): Der Zustand der Zelle in der nächsten Iteration.
      - neighbors (list[Cell]): Liste der Nachbarzellen.
      - ruleset (Ruleset): Das verwendete Regelwerk.
      """

    def __init__(self, initial_state: int, ruleset: Ruleset) -> None:
        """
        Initialisiert die Cell-Instanz

        Argumente:
            initial_state (int): Der Anfangszustand der Zelle (0 für tot, 1 für lebendig).
            ruleset (Ruleset): Das verwendete Regelwerk

        Raises:
            ValueError: Wenn der initial_state weder 0 noch 1 ist.
        """
        if initial_state not in (0, 1):
            raise ValueError("initial_state muss 0 (tot) oder 1 (lebendig) sein.")
        if not isinstance(ruleset, Ruleset):
            raise TypeError("Ruleset ist nicht vom type Ruleset")
        self._current_state = initial_state
        self._state_next_iteration = None
        self.neighbors = []
        self.ruleset = ruleset

    @classmethod
    def from_string(cls, state_string: str, ruleset: Ruleset) -> 'Cell':
        """
               Erstellt eine Cell-Instanz aus einem String.

               Argumente:
               - initial_state (str): Der Startzustand der Zelle als String ("0" oder "1").
               - ruleset (Ruleset): Das verwendete Regelwerk.

               Rückgabe:
               - Cell: Eine neue Cell-Instanz.
        """
        if state_string not in ('0', '1'):
            raise ValueError("Der initial_state muss '0' (tot) oder '1' (lebendig) sein.")
        initial_state = int(state_string)
        return cls(initial_state, ruleset)

    @property
    def state(self) -> int:
        """
        Gibt den aktuellen Zustand der Zelle zurück.

        Returns:
            int: Der aktuelle Zustand der Zelle (0 für tot, 1 für lebendig).
        """
        return self._current_state

    @state.setter
    def state(self, value: int) -> None:
        """Verhindert das Setzen des Zustands von außen."""
        warnings.warn("Man darf den Zustand einer Zelle nicht ändern")

    def add_neighbor(self, neighbor_cell: 'Cell') -> None:
        """
        Fügt eine Nachbarzelle hinzu.

        Args:
            neighbor_cell (Cell): Die hinzugefügte Nachbarzelle.

        Raises:
            OverflowError: Wenn bereits 8 Nachbarn vorhanden sind.
        """
        if len(self.neighbors) >= 8:
            warnings.warn("Eine Zelle kann nicht mehr als 8 Nachbarn haben.")
        self.neighbors.append(neighbor_cell)

    def calculate_state_of_next_iteration(self) -> None:
        """
        Berechnet den Zustand der Zelle in der nächsten Iteration.
        """
        num_alive_neighbors = sum([neighbor_cell._current_state for neighbor_cell in self.neighbors])
        self._state_next_iteration = self.ruleset.calculate_next_state(self._current_state, num_alive_neighbors)

    def update_state(self):
        """
        Aktualisiert den Zustand der Zelle auf den nächsten Zustand, falls verfügbar.
        """
        if self._state_next_iteration is None:
            warnings.warn("Zustand wird jetzt berechnet")
            self.calculate_state_of_next_iteration()
        self._current_state = self._state_next_iteration
        self._state_next_iteration = None

    def __str__(self) -> str:
        """Gibt aktuellen Zustand zurück"""

        return str(self._current_state)
