import fuzzySets

class fuzzy_rules:
    def __init__(self, inputs : fuzzySets.Inputs) :
        self.inputs = inputs

    def left_fast_rules(self) :
        inputs = self.inputs
        left_fast1 = min(inputs.PA.pa_up_more_left, inputs.PV.pv_cw_slow)
        left_fast2 = min(inputs.PA.pa_up_more_left, inputs.PV.pv_ccw_slow)
        left_fast3 = min(inputs.PA.pa_up_more_left, inputs.PV.pv_ccw_fast)
        left_fast4 = min(inputs.PA.pa_down_more_left, inputs.PV.pv_cw_slow)
        left_fast5 = min(inputs.PA.pa_down_left, inputs.PV.pv_cw_slow)
        left_fast6 = min(inputs.PA.pa_down_left, inputs.PV.pv_ccw_slow)
        left_fast7 = min(inputs.PA.pa_up_left, inputs.PV.pv_ccw_slow)
        left_fast8 = min(inputs.PA.pa_up_left, inputs.PV.pv_stop)
        left_fast9 = min(inputs.PA.pa_up_right, inputs.PV.pv_ccw_fast)
        left_fast10 = min(inputs.PA.pa_up_left, inputs.PV.pv_ccw_fast)
        left_fast11 = min(inputs.PA.pa_up, inputs.PV.pv_ccw_fast)
        return max(left_fast1, left_fast2, left_fast3, left_fast4, left_fast5, left_fast6, left_fast7, left_fast8, left_fast9, left_fast10, left_fast11)

    def left_slow_rules(self) :
        inputs = self.inputs
        left_slow1 = min(inputs.PA.pa_up_more_right, inputs.PV.pv_ccw_fast)
        left_slow2 = min(inputs.PA.pa_down_left, inputs.PV.pv_ccw_fast)
        left_slow3 = min(inputs.PA.pa_up_left, inputs.PV.pv_cw_slow)
        left_slow4 = min(inputs.PA.pa_up, inputs.PV.pv_ccw_slow)
        return max(left_slow1, left_slow2, left_slow3, left_slow4)

    def stop_rules(self) :
        inputs = self.inputs
        stop1 = max()