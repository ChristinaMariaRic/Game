import pytest
import coverage
import os
import sys

# Sicherstellen, dass der Pfad zu den Modulen im sys.path enthalten ist
if r"C:\Users\CR\Game-of-Life\modules" not in sys.path:
    sys.path.append(r"C:\Users\CR\Game-of-Life\modules")
from ruleset import Ruleset

def test_parse_rules():
    """Testet die Erstellung eines Ruleset-Objekts mit einer gültigen Regelset-Kurznotation."""
    ruleset = Ruleset("23/3")
    assert ruleset.cell_survives == [2, 3]
    assert ruleset.cell_born == [3]

def test_invalid_rules():
    """Testet, ob eine TypeError ausgelöst wird, wenn das Regelset kein string ist,
    und ob eine ValueError ausgelöst wird, wenn das Regelset in einer falschen Schreibweise angegeben ist."""
    with pytest.raises(TypeError):
        Ruleset(123)

    with pytest.raises(ValueError):
        Ruleset("Rules: 23/3 ")

def test_calculate_next_state():
    """Testet die Berechnung des nächsten Zustands der Zelle basierend auf verschiedenen Szenarien."""
    ruleset = Ruleset("23/3")

    # Lebende Zelle mit 2 oder 3 lebenden Nachbarn sollte leben
    assert ruleset.calculate_next_state(1, 2) == 1
    assert ruleset.calculate_next_state(1, 3) == 1

    # Lebende Zelle mit weniger als 2 oder mehr als 3 lebenden Nachbarn sollte sterben
    assert ruleset.calculate_next_state(1, 1) == 0
    assert ruleset.calculate_next_state(1, 4) == 0

    # Tote Zelle mit genau 3 lebenden Nachbarn sollte lebendig werden
    assert ruleset.calculate_next_state(0, 3) == 1

    # Tote Zelle mit weniger als 3 oder mehr als 3 lebenden Nachbarn sollte tot bleiben
    assert ruleset.calculate_next_state(0, 2) == 0
    assert ruleset.calculate_next_state(0, 4) == 0

def test_calculate_next_state_invalid_dtypes():
    """Testet die Berechnung des nächsten Zustands der Zelle mit ungültigen Datentypen und Werten."""
    ruleset = Ruleset("23/3")

    # Ungültige Datentypen und Werte sollten entsprechende Fehler auslösen
    with pytest.raises(TypeError):
        ruleset.calculate_next_state("False", 3)
    with pytest.raises(TypeError):
        ruleset.calculate_next_state(0, 3.5)
    with pytest.raises(ValueError):
        ruleset.calculate_next_state(1, -4)
    with pytest.raises(ValueError):
        ruleset.calculate_next_state(4, 2)