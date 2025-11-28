import random

from walking_home.environment import Environment


def test_environment_pentagon_always_accepts_when_p_is_one():
    rng = random.Random(0)
    env = Environment(pentagon_pos=10, kaia_pos=90, p_pentagon=1.0, p_kaia=0.0)
    dest = env.check_arrival(10, rng)
    assert dest == "pentagon"


def test_environment_no_arrival_if_not_on_special_position():
    rng = random.Random(0)
    env = Environment()
    dest = env.check_arrival(42, rng)
    assert dest is None
