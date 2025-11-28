from walking_home.environment import Environment
from walking_home.simulation import Simulation
import random
import matplotlib.pyplot as plt

def run_grid(p_values, n_runs=500, seed=0):
    probs_kaia = []
    avg_steps = []

    for p in p_values:
        env = Environment(p_pentagon=p, p_kaia=p)
        sim = Simulation(environment=env, step_prob=0.2, rng=random.Random(seed))
        stats = sim.run_many(n_runs)

        # run_many returnerer en dict, så vi henter ut verdier derfra
        probs_kaia.append(stats["p_kaia_emp"])
        avg_steps.append(stats["avg_steps"])

    return probs_kaia, avg_steps

p_vals = [0.1 * i for i in range(1, 10)]  # 0.1, 0.2, ..., 0.9
probs_kaia, avg_steps = run_grid(p_vals, n_runs=500)

fig, ax = plt.subplots(1, 2, figsize=(12, 4))

ax[0].plot(p_vals, probs_kaia, marker="o")
ax[0].set_xlabel("p_pentagon = p_kaia")
ax[0].set_ylabel("Empirisk sannsynlighet for å ende på Kaia")
ax[0].set_title("Destinasjonssannsynlighet")

ax[1].plot(p_vals, avg_steps, marker="o")
ax[1].set_xlabel("p_pentagon = p_kaia")
ax[1].set_ylabel("Gjennomsnittlig antall steg")
ax[1].set_title("Hvor langt Alex går i snitt")

plt.tight_layout()
plt.show()
