import pytest
import coverage
import warnings
import sys

if r"C:\Users\CR\Game\modules" not in sys.path:
    sys.path.append(r"C:\Users\CR\Game\modules")
from cell import Cell
from ruleset import Ruleset

def test_cell_initialization():
    ruleset = Ruleset("23/3")
    cell = Cell(1, ruleset)
    assert cell.state == 1
    assert cell._state_next_iteration is None
    assert cell.neighbors == []

def test_cell_from_string():
    ruleset = Ruleset("23/3")
    cell = Cell.from_string("1", ruleset)
    assert cell.state == 1

def test_add_neighbor():
    ruleset = Ruleset("23/3")
    cell1 = Cell(1, ruleset)
    cell2 = Cell(0, ruleset)
    cell1.add_neighbor(cell2)
    assert cell1.neighbors == [cell2]

def test_calculate_state_of_next_iteration():
    ruleset = Ruleset("23/3")
    cell1 = Cell(1, ruleset)
    cell2 = Cell(1, ruleset)
    cell3 = Cell(1, ruleset)
    cell1.add_neighbor(cell2)
    cell1.add_neighbor(cell3)
    cell1.calculate_state_of_next_iteration()
    assert cell1._state_next_iteration == 1

def test_update_state():
    ruleset = Ruleset("23/3")
    cell = Cell(1, ruleset)
    cell._state_next_iteration = 0
    cell.update_state()
    assert cell.state == 0
    assert cell._state_next_iteration is None
