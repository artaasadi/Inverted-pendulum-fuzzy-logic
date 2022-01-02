# -*- coding: utf-8 -*-

# python imports
from math import degrees
from fuzzySets import Inputs

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

    def fuzzification(self, input):
        fuzzy_input = Inputs(input['cp'], input['cv'], input['pa'], input['pv'])
        print('==============' + str(fuzzy_input.CP.cp_left_near()))
        print('==============' + str(fuzzy_input.PV.pv_stop()))
        print('==============' + str(fuzzy_input.CV.cv_left_slow()))
        print('==============' + str(fuzzy_input.PA.pa_up()))

    def decide(self, world):
        output = self._make_output()
        self.fuzzification(self._make_input(world))
        self.system.calculate(self._make_input(world), output)
        return output['force']
    
    #def decide(self, world):
    #    self.fuzzification(self._make_input(world))



