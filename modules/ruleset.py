class Ruleset:
    """
    Diese Klasse definiert die Regeln für das Conway's Game of Life.

    Attribute:
        cell_survives (list): Eine Liste von Zahlen, die bestimmen, wann eine Zelle überlebt.
        cell_born (list): Eine Liste von Zahlen, die bestimmen, wann eine neue Zelle entsteht.
    """

    def __init__(self, rules: str):
        """
        Initialisiert ein neues Ruleset-Objekt.

        Args:
            rules (str): Das Regelset in der Kurzschreibweise (z.B. "23/3").
        """
        if not isinstance(rules, str):
            raise TypeError("Die Regeln müssen als String angegeben werden")
        self.cell_survives, self.cell_born = self._parse_rules(rules)

    def _parse_rules(self, rules: str) -> tuple:
        """
        Zerlegt die Regeln in separate Listen für Überleben und Geburt.

        Args:
            rules (str): Die Regeln in der Kurzschreibweise (z.B. "23/3").

        Returns:
            tuple: Ein Tupel mit zwei Listen: Überlebensregeln und Geburtsregeln.
        """
        try:
            survives, is_born = rules.split("/")
            cell_survives = [int(num) for num in survives]
            cell_born = [int(num) for num in is_born]
            return cell_survives, cell_born
        except ValueError:
            raise ValueError("Die Regelnotation ist ungültig")

    def calculate_next_state(self, _current_state: int, num_alive_neighbors: int) -> int:
        """
        Bestimmt den zukünftigen Zustand einer Zelle basierend auf dem aktuellen Zustand und der Anzahl der lebenden Nachbarn.

        Args:
            current_state (int): Der momentane Zustand der Zelle (1 = lebendig, 0 = tot).
            num_alive_neighbors (int): Die Anzahl der lebenden Nachbarn.

        Returns:
            int: Der zukünftige Zustand der Zelle (1 = lebendig, 0 = tot).
        """
        if not isinstance(_current_state, int):
            raise TypeError("Der aktuelle Zustand muss eine ganze Zahl sein")
        if _current_state not in (1, 0):
            raise ValueError("Der aktuelle Zustand muss entweder 1 (lebendig) oder 0 (tot) sein")
        if not isinstance(num_alive_neighbors, int):
            raise TypeError("Die Anzahl der Nachbarn muss eine ganze Zahl sein")
        if num_alive_neighbors < 0:
            raise ValueError("Die Anzahl der Nachbarn darf nicht negativ sein")

        if _current_state:
            return int(num_alive_neighbors in self.cell_survives)
        else:
            return int(num_alive_neighbors in self.cell_born)

