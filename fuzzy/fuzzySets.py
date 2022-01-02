# inputs
class Inputs:
    def __init__(self, cp, cv, pa, pv):
        self.CP = self.CP(cp)
        self.CV = self.CV(cv)
        self.PA = self.PA(pa)
        self.PV = self.PV(pv)
        
    class CP:
        def __init__(self, value):
            self.value = value

        def cp_left_far(self):
            value = self.value
            if -10 <= value < -5 :
                return (((-0.2) * value) - 1)
            else:
                return 0

        def cp_left_near(self):
            value = self.value
            if -10 < value < -2.5 :
                return ((0.1333 * value) + 1.333)
            elif -2.5 <= value < 0 :
                return (((-0.4) * value))
            else :
                return 0

        def cp_stop(self):
            value = self.value
            if -2.5 < value < 0 :
                return (((0.4) * value) + 1)
            elif 0 <= value < 2.5 :
                return (((-0.4) * value) + 1)
            else :
                return 0

        def cp_right_near(self):
            value = self.value
            if 2.5 < value < 10 :
                return ((-0.1333 * value) + 1.333)
            elif 0 < value <= 2.5 :
                return (((0.4) * value))
            else :
                return 0

        def cp_right_far(self):
            value = self.value
            if 5 < value <= 10 :
                return (((0.2) * value) - 1)
            else:
                return 0
    class CV:
        def __init__(self, value):
            self.value = value

        def cv_left_fast(self):
            value = self.value
            if -5 <= value < -2.5 :
                return (((-0.4) * value) - 1)
            else :
                0
        
        def cv_left_slow(self):
            value = self.value
            if -5 < value <= -1 :
                return ((0.25 * value) + 1.25)
            elif -1 < value < 0 :
                return ((-1) * value)
            else :
                0
        
        def cv_stop(self):
            value = self.value
            if -1 < value <= 0 :
                return (value + 1)
            elif 0 < value < 1 :
                return (((-1) * value) + 1)
            else :
                0

        def cv_right_slow(self):
            value = self.value
            if 0 < value <= 1 :
                return value
            elif 1 < value < 5 :
                return (((-0.25) * value) + 1.25)
            else :
                return 0

        def cv_right_fast(self):
            value = self.value
            if 2.5 < value <= 5 :
                return ((0.4 * value) - 1)
            else :
                return 0
    class PA:
        def __init__(self, value):
            self.value = value
        
        def pa_up_more_right(self):
            value = self.value
            if 0 < value <= 30 :
                return ((0.0333) * value)
            elif 30 < value < 60 :
                return (((-0.0333) * value) + 2)
            else :
                return 0

        def pa_up_right(self):
            value = self.value
            if 30 < value <= 60 :
                return (((0.0333) * value) - 1)
            elif 60 < value < 90 :
                return (((-0.0333) * value) + 3)
            else :
                return 0

        def pa_up(self):
            value = self.value
            if 60 < value <= 90 :
                return (((0.0333) * value) - 2)
            elif 90 < value < 120 :
                return (((-0.0333) * value) + 4)
            else :
                return 0

        def pa_up_left(self):
            value = self.value
            if 90 < value <= 120 :
                return (((0.0333) * value) - 3)
            elif 120 < value < 150 :
                return (((-0.0333) * value) + 5)
            else :
                return 0

        def pa_up_more_left(self):
            value = self.value
            if 120 < value <= 150 :
                return (((0.0333) * value) - 4)
            elif 150 < value < 180 :
                return (((-0.0333) * value) + 6)
            else :
                return 0

        def pa_down_more_left(self):
            value = self.value
            if 180 < value <= 210 :
                return (((0.0333) * value) - 6)
            elif 210 < value < 240 :
                return (((-0.0333) * value) + 8)
            else :
                return 0

        def pa_down_left(self):
            value = self.value
            if 210 < value <= 240 :
                return (((0.0333) * value) - 7)
            elif 240 < value < 270 :
                return (((-0.0333) * value) + 9)
            else :
                return 0

        def pa_down(self):
            value = self.value
            if 240 < value <= 270 :
                return (((0.0333) * value) - 8)
            elif 270 < value < 300 :
                return (((-0.0333) * value) + 10)
            else :
                return 0

        def pa_down_right(self):
            value = self.value
            if 270 < value <= 300 :
                return (((0.0333) * value) - 9)
            elif 300 < value < 330 :
                return (((-0.0333) * value) + 11)
            else :
                return 0

        def pa_down_more_right(self):
            value = self.value
            if 300 < value <= 330 :
                return (((0.0333) * value) - 9)
            elif 330 < value < 360 :
                return (((-0.0333) * value) + 11)
            else :
                return 0
    class PV:
        def __init__(self, value):
            self.value = value

        def pv_cw_fast(self):
            value = self.value
            if value <= -200 :
                return 1
            elif -200 < value < -100 :
                return (((-0.01) * value) - 1)
            else :
                return 0

        def pv_cw_slow(self):
            value = self.value
            if -200 < value <= -100 :
                return ((0.01 * value) + 2)
            elif -100 < value < 0 :
                return ((-0.01) * value)
            else :
                return 0

        def pv_stop(self):
            value = self.value
            if -100 < value <= 0 :
                return ((0.01 * value) + 1)
            elif 0 < value < 100 :
                return (((-0.01) * value) + 1)
            else :
                return 0

        def pv_ccw_slow(self):
            value = self.value
            if 0 < value <= 100 :
                return (0.01 * value)
            elif 100 < value < 200 :
                return (((-0.01) * value) + 2)
            else :
                return 0

        def pv_ccw_fast(self):
            value = self.value
            if 100 < value < 200 :
                return ((0.01 * value) - 1)
            elif 200 <= value :
                return 1
            else :
                return 0

# output
