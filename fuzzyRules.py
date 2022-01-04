import fuzzySets

class Inferrence:
    def __init__(self, inputs) :
        self.inputs = inputs
        self.left_fast_rules = self.left_fast_rules()
        self.left_slow_rules = self.left_slow_rules()
        self.stop_rules = self.stop_rules()
        self.right_slow_rules = self.right_slow_rules()
        self.right_fast_rules = self.right_fast_rules()

    def left_fast_rules(self) :
        inputs = self.inputs
        # added (1 - cv_left_fast) to the rule because we need less pushing left if we have a left velocity
        left_fast1 = min(inputs.PA.pa_up_more_left, inputs.PV.pv_cw_slow, 1 - inputs.CV.cv_left_fast)
        left_fast2 = min(inputs.PA.pa_up_more_left, inputs.PV.pv_ccw_slow, 1 - inputs.CV.cv_left_fast)
        left_fast3 = min(inputs.PA.pa_up_more_left, inputs.PV.pv_ccw_fast, 1 - inputs.CV.cv_left_fast)
        left_fast4 = min(inputs.PA.pa_down_more_left, inputs.PV.pv_cw_slow, 1 - inputs.CV.cv_left_fast)
        left_fast5 = min(inputs.PA.pa_down_left, inputs.PV.pv_cw_slow, 1 - inputs.CV.cv_left_fast)
        left_fast6 = min(inputs.PA.pa_down_left, inputs.PV.pv_ccw_slow, 1 - inputs.CV.cv_left_fast)
        left_fast7 = min(inputs.PA.pa_up_left, inputs.PV.pv_ccw_slow, 1 - inputs.CV.cv_left_fast)
        left_fast8 = min(inputs.PA.pa_up_left, inputs.PV.pv_stop, 1 - inputs.CV.cv_left_fast)
        left_fast9 = min(inputs.PA.pa_up_right, inputs.PV.pv_ccw_fast, 1 - inputs.CV.cv_left_fast)
        left_fast10 = min(inputs.PA.pa_up_left, inputs.PV.pv_ccw_fast, 1 - inputs.CV.cv_left_fast)
        left_fast11 = min(inputs.PA.pa_up, inputs.PV.pv_ccw_fast, 1 - inputs.CV.cv_left_fast)
        return max(left_fast1, left_fast2, left_fast3, left_fast4, left_fast5, left_fast6, left_fast7, left_fast8, left_fast9, left_fast10, left_fast11)#, left_fast12, left_fast13, left_fast14, left_fast15, left_fast16, left_fast17, left_fast18, left_fast19, left_fast20, left_fast21, left_fast23, left_fast24)

    def left_slow_rules(self) :
        inputs = self.inputs
        # added (1 - cv_left_slow) to the rule because we need less pushing left if we have a left velocity
        left_slow1 = min(inputs.PA.pa_up_more_right, inputs.PV.pv_ccw_fast, 1 - inputs.CV.cv_left_slow)
        left_slow2 = min(inputs.PA.pa_down_left, inputs.PV.pv_ccw_fast, 1 - inputs.CV.cv_left_slow)
        left_slow3 = min(inputs.PA.pa_up_left, inputs.PV.pv_cw_slow, 1 - inputs.CV.cv_left_slow)
        left_slow4 = min(inputs.PA.pa_up, inputs.PV.pv_ccw_slow, 1 - inputs.CV.cv_left_slow)
        # these rules are same as left fast rules plus we have a left velocity so we need less pushing
        left_slow5 = min(inputs.PA.pa_up_more_left, inputs.PV.pv_cw_slow, inputs.CV.cv_left_fast)
        left_slow6 = min(inputs.PA.pa_up_more_left, inputs.PV.pv_ccw_slow, inputs.CV.cv_left_fast)
        left_slow7 = min(inputs.PA.pa_up_more_left, inputs.PV.pv_ccw_fast, inputs.CV.cv_left_fast)
        left_slow8 = min(inputs.PA.pa_down_more_left, inputs.PV.pv_cw_slow, inputs.CV.cv_left_fast)
        left_slow9 = min(inputs.PA.pa_down_left, inputs.PV.pv_cw_slow, inputs.CV.cv_left_fast)
        left_slow10 = min(inputs.PA.pa_down_left, inputs.PV.pv_ccw_slow, inputs.CV.cv_left_fast)
        left_slow11 = min(inputs.PA.pa_up_left, inputs.PV.pv_ccw_slow, inputs.CV.cv_left_fast)
        left_slow12 = min(inputs.PA.pa_up_left, inputs.PV.pv_stop, inputs.CV.cv_left_fast)
        left_slow13 = min(inputs.PA.pa_up_right, inputs.PV.pv_ccw_fast, inputs.CV.cv_left_fast)
        left_slow14 = min(inputs.PA.pa_up_left, inputs.PV.pv_ccw_fast, inputs.CV.cv_left_fast)
        left_slow15 = min(inputs.PA.pa_up, inputs.PV.pv_ccw_fast, inputs.CV.cv_left_fast)
        return max(left_slow1, left_slow2, left_slow3, left_slow4, left_slow5, left_slow6, left_slow7, left_slow8, left_slow9, left_slow10, left_slow11, left_slow12, left_slow13, left_slow14, left_slow15)

    def stop_rules(self) :
        inputs = self.inputs
        stop1 = max(min(inputs.PA.pa_up, inputs.PV.pv_stop), min(inputs.PA.pa_up_right, inputs.PV.pv_ccw_slow), min(inputs.PA.pa_up_left, inputs.PV.pv_cw_slow))
        stop2 = min(inputs.PA.pa_down_more_right, inputs.PV.pv_cw_slow)
        stop3 = min(inputs.PA.pa_down_more_left, inputs.PV.pv_ccw_slow)
        stop4 = min(inputs.PA.pa_down_more_right, inputs.PV.pv_ccw_fast)
        stop5 = min(inputs.PA.pa_down_more_right, inputs.PV.pv_cw_fast)
        stop6 = min(inputs.PA.pa_down_more_left, inputs.PV.pv_cw_fast)
        stop7 = min(inputs.PA.pa_down_more_left, inputs.PV.pv_ccw_fast)
        stop8 = min(inputs.PA.pa_down_right, inputs.PV.pv_ccw_fast)
        stop9 = min(inputs.PA.pa_down_left, inputs.PV.pv_cw_fast)
        stop10 = min(inputs.PA.pa_down, inputs.PV.pv_cw_fast)
        stop11 = min(inputs.PA.pa_down, inputs.PV.pv_ccw_fast)
        stop12 = min(inputs.PA.pa_up, inputs.PV.pv_stop)
        # these rules are same as right slow rules plus we have a right velocity so we don't need pushing
        stop13 = min(inputs.PA.pa_up_more_left, inputs.PV.pv_cw_fast, inputs.CV.cv_right_fast)
        stop14 = min(inputs.PA.pa_down_right, inputs.PV.pv_cw_fast, inputs.CV.cv_right_fast)
        stop15 = min(inputs.PA.pa_up_right, inputs.PV.pv_ccw_slow, inputs.CV.cv_right_fast)
        stop16 = min(inputs.PA.pa_up, inputs.PV.pv_cw_slow, inputs.CV.cv_right_fast)
        # these rules are same as left slow rules plus we have a left velocity so we don't need pushing
        stop17 = min(inputs.PA.pa_up_more_right, inputs.PV.pv_ccw_fast, inputs.CV.cv_left_fast)
        stop18 = min(inputs.PA.pa_down_left, inputs.PV.pv_ccw_fast, inputs.CV.cv_left_fast)
        stop19 = min(inputs.PA.pa_up_left, inputs.PV.pv_cw_slow, inputs.CV.cv_left_fast)
        stop20 = min(inputs.PA.pa_up, inputs.PV.pv_ccw_slow, inputs.CV.cv_left_fast)
        return max(stop1, stop2, stop3, stop4, stop5, stop6, stop7, stop8, stop9, stop10, stop11, stop12, stop13, stop14, stop15, stop16, stop17, stop18, stop19, stop20)

    def right_slow_rules(self) :
        inputs = self.inputs
        # added (1 - cv_right_slow) to the rule because we need less pushing right if we have a right velocity
        right_slow1 = min(inputs.PA.pa_up_more_left, inputs.PV.pv_cw_fast, 1 - inputs.CV.cv_right_slow)
        right_slow2 = min(inputs.PA.pa_down_right, inputs.PV.pv_cw_fast, 1 - inputs.CV.cv_right_slow)
        right_slow3 = min(inputs.PA.pa_up_right, inputs.PV.pv_ccw_slow, 1 - inputs.CV.cv_right_slow)
        right_slow4 = min(inputs.PA.pa_up, inputs.PV.pv_cw_slow, 1 - inputs.CV.cv_right_slow)
        # these rules are same as right fast rules plus we have a right velocity so we need less pushing
        right_slow5 = min(inputs.PA.pa_up_more_right, inputs.PV.pv_ccw_slow, inputs.CV.cv_right_fast)
        right_slow6 = min(inputs.PA.pa_up_more_right, inputs.PV.pv_cw_slow, inputs.CV.cv_right_fast)
        right_slow7 = min(inputs.PA.pa_up_more_right, inputs.PV.pv_cw_fast, inputs.CV.cv_right_fast)
        right_slow11 = min(inputs.PA.pa_up_right, inputs.PV.pv_cw_slow, inputs.CV.cv_right_fast)
        right_slow12 = min(inputs.PA.pa_up_right, inputs.PV.pv_stop, inputs.CV.cv_right_fast)
        right_slow13 = min(inputs.PA.pa_up_right, inputs.PV.pv_cw_fast, inputs.CV.cv_right_fast)
        right_slow14 = min(inputs.PA.pa_up_left, inputs.PV.pv_cw_fast, inputs.CV.cv_right_fast)
        right_slow15 = min(inputs.PA.pa_up, inputs.PV.pv_cw_fast, inputs.CV.cv_right_fast)
        return max(right_slow1, right_slow2, right_slow3, right_slow4, right_slow5, right_slow6, right_slow7, right_slow11, right_slow12, right_slow13, right_slow14, right_slow15)

    def right_fast_rules(self) :
        inputs = self.inputs
        # added (1 - cv_right_fast) to the rule because we need less pushing right if we have a right velocity
        right_fast1 = min(inputs.PA.pa_up_more_right, inputs.PV.pv_ccw_slow, 1 - inputs.CV.cv_right_fast)
        right_fast2 = min(inputs.PA.pa_up_more_right, inputs.PV.pv_cw_slow, 1 - inputs.CV.cv_right_fast)
        right_fast3 = min(inputs.PA.pa_up_more_right, inputs.PV.pv_cw_fast, 1 - inputs.CV.cv_right_fast)
        right_fast4 = min(inputs.PA.pa_down_more_right, inputs.PV.pv_ccw_slow, 1 - inputs.CV.cv_right_fast)
        right_fast5 = min(inputs.PA.pa_down_right, inputs.PV.pv_ccw_slow, 1 - inputs.CV.cv_right_fast)
        right_fast6 = min(inputs.PA.pa_down_right, inputs.PV.pv_cw_slow, 1 - inputs.CV.cv_right_fast)
        right_fast7 = min(inputs.PA.pa_up_right, inputs.PV.pv_cw_slow, 1 - inputs.CV.cv_right_fast)
        right_fast8 = min(inputs.PA.pa_up_right, inputs.PV.pv_stop, 1 - inputs.CV.cv_right_fast)
        right_fast9 = min(inputs.PA.pa_up_right, inputs.PV.pv_cw_fast, 1 - inputs.CV.cv_right_fast)
        right_fast10 = min(inputs.PA.pa_up_left, inputs.PV.pv_cw_fast, 1 - inputs.CV.cv_right_fast)
        right_fast11 = min(inputs.PA.pa_down, inputs.PV.pv_stop, 1 - inputs.CV.cv_right_fast)
        right_fast12 = min(inputs.PA.pa_up, inputs.PV.pv_cw_fast, 1 - inputs.CV.cv_right_fast)
        return max(right_fast1, right_fast2, right_fast3, right_fast4, right_fast5, right_fast6, right_fast7, right_fast8, right_fast9, right_fast10, right_fast11, right_fast12)
