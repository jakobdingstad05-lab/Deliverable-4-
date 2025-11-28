import random
from dataclasses import dataclass
from typing import Optional, Dict, Any

from .alex import Alex
from .environment import Environment


@dataclass
class SimulationResult:
    destination: Optional[str]  # "pentagon", "kaia" eller None
    seconds: int
    steps: int


class Simulation:
    """Kjører simulering av Alex sin vei hjem."""

    def __init__(
        self,
        environment: Optional[Environment] = None,
        step_prob: float = 0.2,
        rng: Optional[random.Random] = None,
    ) -> None:
        self.environment = environment or Environment()
        self.step_prob = step_prob
        self.rng = rng or random.Random()

    def run_once(self) -> SimulationResult:
        """Kjør én simulering til Alex havner i Pentagon eller Kaia."""
        env = self.environment
        alex = Alex(position=env.start_position())

        destination: Optional[str] = None

        while destination is None:
            alex.tick(
                rng=self.rng,
                step_prob=self.step_prob,
                left_boundary=env.left,
                right_boundary=env.right,
            )
            destination = env.check_arrival(alex.position, self.rng)

        return SimulationResult(
            destination=destination,
            seconds=alex.n_seconds,
            steps=alex.n_steps,
        )

    def run_many(self, n_runs: int = 1000) -> Dict[str, Any]:
        """Kjør mange simuleringer og returner enkel statistikk."""
        results = [self.run_once() for _ in range(n_runs)]

        n_pentagon = sum(r.destination == "pentagon" for r in results)
        n_kaia = sum(r.destination == "kaia" for r in results)

        avg_seconds = sum(r.seconds for r in results) / n_runs
        avg_steps = sum(r.steps for r in results) / n_runs

        return {
            "n_runs": n_runs,
            "n_pentagon": n_pentagon,
            "n_kaia": n_kaia,
            "p_pentagon_emp": n_pentagon / n_runs,
            "p_kaia_emp": n_kaia / n_runs,
            "avg_seconds": avg_seconds,
            "avg_steps": avg_steps,
        }


def main() -> None:
    """Eksempel: kjør mange simuleringer og skriv ut statistikk."""
    env = Environment(
        left=0,
        right=100,
        pentagon_pos=20,
        audmax_pos=50,
        kaia_pos=80,
        p_pentagon=0.6,
        p_kaia=0.7,
    )
    sim = Simulation(environment=env, step_prob=0.2, rng=random.Random(42))
    stats = sim.run_many(n_runs=1000)

    print("Simulerte Alex sin vei hjem:")
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
