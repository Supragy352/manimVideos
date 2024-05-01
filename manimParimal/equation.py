from manim import *

import numpy as np

last_entry = None

def curve_eqn(t, a, above, First, y_range):
    global last_entry
    x = t
    y_min , y_max = y_range
    if First or (x**2 < a**2):
        denominator = a**2 - x**2
        if denominator != 0: 
            value_inside_sqrt = (a**3 * x) / denominator
            if value_inside_sqrt >= 0:
                y = np.sqrt(value_inside_sqrt) if above else -np.sqrt(value_inside_sqrt)
                if y_min <= y <= y_max:
                    last_entry = [x,y,0]
                    # print("current points",x,y,0)
                    return np.array([x, y, 0])
    # print("last entry",last_entry)
    return np.array(last_entry)

class PlotCurve(Scene):
    def construct(self):

        # Constants
        a = 0.6
        transition_length = 0.0005
        x_range = [-6, 6]
        y_range = [-3, 3]

        # Axes
        axes = Axes(
            x_range=(tuple(x_range)),
            y_range=(tuple(y_range)),
            axis_config={"color": WHITE},
        )

        # Highlight Symmetry
        axes_symmetry = axes.copy()

        # Text
        curve_eqn_text = Text("Curve Equation: y^2(a^2 - x^2) = a^3 * x").scale(0.5).to_edge(UL)
        symmetry_text = Text("Symmetry: about x-axis").scale(0.5).next_to(curve_eqn_text, DOWN, aligned_edge=LEFT)
        intersection_text = Text("Point of Intersection: Origin").scale(0.5).next_to(symmetry_text, DOWN, aligned_edge=LEFT)
        tangent_text = Text("Tangent at Origin: x = 0").scale(0.5).next_to(intersection_text, DOWN, aligned_edge=LEFT)
        asymptote_text = Text("Asymptote: x = +/- a , y = 0").scale(0.5).next_to(tangent_text, DOWN, aligned_edge=LEFT)

        # Highlight x-axis
        self.play(Create(axes), Create(curve_eqn_text), run_time=3)
        self.play(Write(symmetry_text))
        self.play(axes_symmetry[0].animate.set_color("#000080"))
        self.wait(2)
        self.play(axes_symmetry[0].animate.set_color(WHITE))
        self.wait(1)

        # Origin and Tangent
        self.play(Write(intersection_text))
        origin_dot = Dot(point=[0, 0, 0], color=BLUE)
        self.play(Create(origin_dot))
        self.play(Write(tangent_text))
        tangent_line = Line(start=[0, 1, 0], end=[0, -1, 0], color="#00008B")
        self.play(Create(tangent_line))
        self.wait(1)

        # Asymptotes
        self.play(Write(asymptote_text))
        asymptote1 = Line(start=[-a, y_range[0], 0], end=[-a, y_range[1], 0], color=YELLOW)
        asymptote2 = Line(start=[a, y_range[0], 0], end=[a, y_range[1], 0], color=YELLOW)
        asymptote3 = Line(start=[0, 0, 0], end=[-6, 0, 0], color=YELLOW)
        self.play(Create(asymptote1), Create(asymptote2), Create(asymptote3))
        self.wait(1)

        # Plot Curve
        curveFirst1 = ParametricFunction(lambda t: curve_eqn(t, a,True,True,y_range), t_range=[x_range[0], -a - transition_length], color = RED)
        curveFirst2 = ParametricFunction(lambda t: curve_eqn(t, a,False,True,y_range), t_range=[x_range[0], -a - transition_length], color = RED)

        curveSecond1 = ParametricFunction(lambda t: curve_eqn(t, a,True,False,y_range), t_range=[transition_length, a-transition_length], color = RED)
        curveSecond2 = ParametricFunction(lambda t: curve_eqn(t, a,False,False,y_range), t_range=[transition_length, a-transition_length], color = RED)

        self.play(Create(curveFirst1), Create(curveFirst2), Create(curveSecond1), Create(curveSecond2), run_time=8)
        self.wait(2)
