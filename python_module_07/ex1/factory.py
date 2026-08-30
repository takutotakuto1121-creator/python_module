#!/usr/bin/env python3


from ex0.factory import CreatureFactory
from ex1.creature import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformingFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
