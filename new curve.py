from manim import *

class PlotCurve(Scene):
    def construct(self):
        # Create axes with appropriate ranges based on your function's behavior
        axes = Axes(
            x_range=(-2, 4),  # Adjust based on function's domain
            y_range=(-2, 3),  # Adjust based on function's range
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": range(-2, 5)},
            y_axis_config={"numbers_to_include": range(-2, 4)},
        )

        # Improved equation (a^2)(y^2) = x^2(2a - x)(x - a)
        equation = MathTex("(a^2)(y^2) = x^2(2a - x)(x - a)").scale(0.8).to_edge(UP)

        # Step 1: Symmetry about x-axis with visual confirmation
        step1_text = Text("Step 1: Symmetry about x-axis").shift(UP * 3)
        reflected_equation = equation.copy().reflect(DOWN)

        self.play(Write(equation))
        self.wait()

        self.play(
            Create(axes),
            Write(equation),
            run_time=2
        )
        self.wait()

        self.play(
            Write(step1_text),
            Create(reflected_equation),
            run_time=2
        )
        self.wait(2)  # Hold frame for better visualization

        # Step 2: Points of intersection
        intersection_points_text = Text("Points of Intersection: (0, 0), (a, 0), (2a, 0)").next_to(step1_text, DOWN)
        intersection_points = [Dot(axes.c2p(0, 0), color=RED), Dot(axes.c2p(1, 0), color=RED), Dot(axes.c2p(2, 0), color=RED)]

        self.play(Write(intersection_points_text))
        self.play(FadeIn(intersection_points[0]))
        self.wait(0.5)
        self.play(FadeIn(intersection_points[1]))
        self.wait(0.5)
        self.play(FadeIn(intersection_points[2]))
        self.wait(2)  # Hold frame to show intersection points

        # Step 3: Tangents at (a, 0) and (2a, 0) parallel to y-axis
        tangents_text = Text("Step 3: Tangents at (a, 0) and (2a, 0) parallel to y-axis").next_to(intersection_points_text, DOWN)
        tangents = [Line(axes.c2p(1, 0), UP, color=GREEN), Line(axes.c2p(2, 0), UP, color=GREEN)]

        self.play(Write(tangents_text))
        self.play(Create(tangents[0]))
        self.wait(1)
        self.play(Create(tangents[1]))
        self.wait(2)  # Hold frame to show tangents

        # ... Complete the remaining steps for your analysis (optional)

        self.wait()  # Hold
