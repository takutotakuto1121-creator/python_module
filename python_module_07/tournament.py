#!/usr/bin/env python3


from ex0.creature import Creature
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy, AgressiveStrategy, DefensiveStrategy,
    BattleStrategy, InvalidStrategyError
)


def single_battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    number = len(opponents)
    print(f"{number} opponents involved")
    print()

    fighters: list[tuple[Creature, BattleStrategy]] = []
    for factory, strategy in opponents:
        fighters.append((factory.create_base(), strategy))

    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            try:
                creature_a, strategy_a = fighters[i]
                creature_b, strategy_b = fighters[j]
                print("* Battle *")
                print(creature_a.describe())
                print(" vs.")
                print(creature_b.describe())
                print(" now fight!")
                print(strategy_a.act(creature_a))
                print(strategy_b.act(creature_b))
                print()
            except InvalidStrategyError as e:
                print(f"{e}")


if __name__ == "__main__":
    print("=== Tournament ===")
    single_battle([
        (FlameFactory(), NormalStrategy()),
        (AquaFactory(), NormalStrategy()),
    ])
    single_battle([
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AgressiveStrategy()),
    ])
    tournament = [
        (FlameFactory(), NormalStrategy()),
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AgressiveStrategy()),
    ]
    single_battle(tournament)
    single_battle([
        (FlameFactory(), NormalStrategy()),
        (AquaFactory(), AgressiveStrategy()),
    ])
