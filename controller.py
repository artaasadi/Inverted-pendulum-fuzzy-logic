# -*- coding: utf-8 -*-

# python imports
from math import degrees
import Fuzzy

# pyfuzzy imports
from fuzzy.storage.fcl.Reader import Reader


class FuzzyController:

    def __init__(self, fcl_path):
        self.system = Reader().load_from_file(fcl_path)


    def _make_input(self, world):
        return dict(
            cp = world.x,
            cv = world.v,
            pa = degrees(world.theta),
            pv = degrees(world.omega)
        )


    def _make_output(self):
        return dict(
            force = 0.
        )


    def decide(self, world):
        output = self._make_output()
        #self.fuzzification(self._make_input(world))
        self.system.calculate(self._make_input(world), output)
        print("force", output['force'])
        print("myforce", Fuzzy.calculate(self._make_input(world)))
        print(self._make_input(world))
        #return output['force']
        return Fuzzy.calculate(self._make_input(world))




