from manim import *

class SineGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 11, 1],
            y_range=[-10, 11, 1],
            axis_config={"color": BLUE},
        )

        self.add(axes)
        self.wait()
