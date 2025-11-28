from dataclasses import dataclass
from typing import Optional


@dataclass
class Environment:
    """
    Beskriver verden Alex går i.

    Koordinater:
        left  = 0  (E6)
        right = 100 (jernbanen)
    """

    left: int = 0
    right: int = 100
    pentagon_pos: int = 20
    audmax_pos: int = 50
    kaia_pos: int = 80
    p_pentagon: float = 0.5
    p_kaia: float = 0.5

    def start_position(self) -> int:
        """Startposisjonen til Alex (AudMax)."""
        return self.audmax_pos

    def check_arrival(self, position: int, rng) -> Optional[str]:
        """
        Sjekk om Alex går inn i Pentagon eller Kaia.

        Returnerer:
            "pentagon", "kaia" eller None
        """
        if position == self.pentagon_pos:
            if rng.random() < self.p_pentagon:
                return "pentagon"

        if position == self.kaia_pos:
            if rng.random() < self.p_kaia:
                return "kaia"

        return None
