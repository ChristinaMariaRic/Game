import pytest
import sys
from copy import deepcopy
if r"C:\Users\CR\Game\modules" not in sys.path:
    sys.path.append(r"C:\Users\CR\Game\modules")


# Testfall für die Initialisierung des Universums
from ruleset import Ruleset
from cell import Cell
from universe import Universe

class TestUniverse:
    def test_init(self):
        ruleset = Ruleset("23/3")
        universe = Universe(10, 10, ruleset, 0.5, '*', '.')
        assert universe.height == 10
        assert universe.width == 10
        assert universe.ruleset == ruleset
        assert universe.p_cell_alive == 0.5
        assert universe.char_alive == '*'
        assert universe.char_dead == '.'
        assert len(universe._cells) == 12
        assert len(universe._cells[0]) == 12

    def test_create_empty_universe(self):
        ruleset = Ruleset("23/3")
        universe = Universe(5, 5, ruleset, 0.5, '*', '.')
        empty_universe = universe._create_empty_universe()
        for row in empty_universe:
            assert len(row) == 7  # Überprüfen Sie die Länge jeder Zeile, um sicherzustellen, dass sie mit der erwarteten Breite übereinstimmt
    def test_initialize_visible_universe(self):
        ruleset = Ruleset("23/3")
        universe = Universe(5, 5, ruleset, 0.5, '*', '.')
        visible_universe = universe._initialize_visible_universe(universe._create_empty_universe())
        assert len(visible_universe) == 7
        assert len(visible_universe[0]) == 7

    def test_add_neighbors_to_cells(self):
        ruleset = Ruleset("23/3")
        universe = Universe(5, 5, ruleset, 0.5, '*', '.')
        universe_with_neighbors = universe._add_neighbors_to_cells(universe._create_empty_universe())
        assert len(universe_with_neighbors) == 7
        assert len(universe_with_neighbors[0]) == 7

    def test_create_universe(self):
        ruleset = Ruleset("23/3")
        universe = Universe(5, 5, ruleset, 0.5, '*', '.')
        created_universe = universe._create_universe()
        assert len(created_universe) == 7
        assert len(created_universe[0]) == 7

    def test_print_universe(self, capsys):
        ruleset = Ruleset("23/3")
        universe = Universe(5, 5, ruleset, 0.5, '*', '.')
        universe.print_universe()
        captured = capsys.readouterr()
        assert len(captured.out.split('\n')) == 7

    def test_run_one_iteration(self):
        ruleset = Ruleset("23/3")
        universe = Universe(5, 5, ruleset, 0.5, '*', '.')
        initial_state = deepcopy(universe._cells)  # Tiefere Kopie des initialen Zustands erstellen
        universe.run_one_iteration()
        assert universe._cells != initial_state  # Überprüfen, ob sich der Zustand des Universums nach einer Iteration ändert