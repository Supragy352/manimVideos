from math import sin
from manim import *
from numpy import dtype
from svgelements import Length

class  Graphplotting(Scene):
    def construct(self):
        override_animation(FadeIn)
        dt = 1.5
        ax = Axes()
        cose = ax.plot(np.cos , color = BLUE)
        sine = ax.plot(np.sin, color=RED)
        sine = always_redraw(
            lambda: ParametricFunction(
                si,
                alpha = alpha.get_value(),
                color = YELLOW,
                Length = 5,
                )
            )
        alpha = ValueTracker(0)
        self.add(ax)
        self.play(alpha.animate.set_value(1),FadeIn(cose),FadeIn(sine), rate_func=linear, run_time=2) 