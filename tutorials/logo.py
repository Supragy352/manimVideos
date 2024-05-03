from manim import *

class  Graphplotting(Scene):
    def construct(self):
        override_animation(FadeIn)
        ax = Axes()
        tan = ax.plot(np.tan , color = BLUE)
        alpha = ValueTracker(0)
        self.add(ax, tan)
        self.play(FadeIn(tan))