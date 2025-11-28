from dataclasses import dataclass


@dataclass
class Alex:
    """Representerer Alex som går i en 1D-verden."""

    position: int
    n_steps: int = 0
    n_seconds: int = 0

    def tick(self, *, rng, step_prob: float, left_boundary: int, right_boundary: int) -> None:
        """
        Simuler ett sekund.

        - Med sannsynlighet step_prob tar Alex ett steg.
        - Hvis han går utenfor grensen, blir han stående på grensepunktet.
        """
        self.n_seconds += 1

        # Ingen bevegelse dette sekundet
        if rng.random() >= step_prob:
            return

        # 50 % sjanse venstre, 50 % sjanse høyre
        step = -1 if rng.random() < 0.5 else 1
        new_pos = self.position + step

        # Hold Alex innenfor grensene
        if new_pos < left_boundary:
            new_pos = left_boundary
        if new_pos > right_boundary:
            new_pos = right_boundary

        self.position = new_pos
        self.n_steps += 1
