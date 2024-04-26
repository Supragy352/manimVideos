from manim import *
class Cartesian(Scene):
    def construct(self):
        axes = Axes(
            x_range = [-10, 11, 1],
            y_range = [-10,11, 1],
            x_length=12,
            y_length=12,
            axis_config={"color": BLUE},
            x_axis_config={"color": RED}
            )

        self.add(axes)
        point = Dot().move_to(axes.coords_to_point(2, 3))
        point_1 = Dot(). move_to(axes.coords_to_point(5, 7))
        self.play(Create(point))
        self.play(Create(point_1))

        # Add label to the point
        label = MathTex("(2, 3)").next_to(point, DOWN + RIGHT)
        label_1 = MathTex("(5, 7)").next_to(point_1, DOWN + RIGHT)
        self.play(Write(label))
        self.play(Write(label_1))

        self.wait()
