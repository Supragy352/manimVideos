from ast import Lambda
from typing_extensions import runtime
from manim import *

class Graph(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-7, 8, 1],
            y_range=[-7, 8, 1],
            )
        point = Dot().move_to(ax.coords_to_point(0,4))
        label = MathTex("(0,4)", font_size=36).next_to(point, UP + RIGHT)
        curve = ax.plot(lambda x: 64/(x*x+16), color=RED)
        area = ax.get_area(curve, x_range=(-7, 8), color=BLUE)
        self.play(Create(ax, run_time=5)) 
        self.play(Create(point))
        self.play(Write(label))
        self.play(Create(curve, run_time=5), Create(area, run_time=5))
        self.wait()