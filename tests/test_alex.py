import random

from walking_home.alex import Alex


def test_alex_does_not_move_when_step_prob_zero():
    rng = random.Random(0)
    alex = Alex(position=10)

    alex.tick(rng=rng, step_prob=0.0, left_boundary=0, right_boundary=100)

    # Ett sekund har gått, men ingen steg
    assert alex.n_seconds == 1
    assert alex.n_steps == 0
    assert alex.position == 10


def test_alex_moves_with_step_prob_one():
    rng = random.Random(0)
    alex = Alex(position=10)

    alex.tick(rng=rng, step_prob=1.0, left_boundary=0, right_boundary=100)

    # Her vet vi at han må ha tatt ett steg
    assert alex.n_seconds == 1
    assert alex.n_steps == 1
    # Med seed 0 og koden over blir dette alltid 9 eller 11
    assert alex.position in (9, 11)
