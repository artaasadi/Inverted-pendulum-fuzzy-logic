# -*- coding: utf-8 -*-

# python imports
from math import degrees
from fuzzy.fuzzySets import CP, CV, PA, PV

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
        cp = CP(input['cp'])
        cv = CV(input['cv'])
        pa = PA(input['pa'])
        pv = PV(input['pv'])
        print('==============' + str(cp.cp_left_near()))
        print('==============' + str(pv.pv_stop()))
        print('==============' + str(cv.cv_left_slow()))
        print('==============' + str(pa.pa_up()))

    def decide(self, world):
        output = self._make_output()
        self.fuzzification(self._make_input(world))
        self.system.calculate(self._make_input(world), output)
        return output['force']
    
    #def decide(self, world):
    #    self.fuzzification(self._make_input(world))



