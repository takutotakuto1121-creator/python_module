#!/usr/bin/env python3


from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.creature import TransformCapability, HealCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Battle error, aborting tournament: "
                f"Invalide Creature '{creature._name}'"
                "for this agressive strategy"
             )
        else:
            return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AgressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                f"Battle error, aborting tournament: "
                f"Invalide Creature '{creature._name}'"
                "for this agressive strategy"
            )
        else:
            result = (
                f"{creature.transform()}\n"
                f"{creature.attack()}\n{creature.revert()}"
                )
            return result

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(
                f"Battle error, aborting tournament: "
                f"Invalide Creature '{creature._name}'"
                "for this sefensive strategy"
            )
        else:
            result = f"{creature.attack()}\n{creature.heal()}\n"
            return result

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
