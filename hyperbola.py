from manim import *

class ConicsAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Curve Tracing", font_size=48)
        title.shift(3 * UP)
        self.play(Write(title), run_time = 2)
        self.wait(0.2)

        text = Text("Hello, today we will learn how to plot the curve :", font_size = 36)
        text.shift(1 * UP)
        self.play(Write(text), run_time = 2)
        self.wait(0.2)

        eqn = MathTex("x^{3} + y^{3} = 3axy", font_size=45)
        self.play(Write(eqn))
        self.wait()
        self.play(FadeOut(eqn))

        self.play(FadeOut(title), FadeOut(text))

        eqn.shift(3 * UP + 4 * LEFT)
        self.play(Write(eqn))
        self.wait(1)

        # Axes and labels
        a = 2
        axes = ThreeDAxes(
            x_range=[-5, 5], y_range=[-5, 5], z_range=[-5, 5],
            x_axis_config={"numbers_to_include": [a,-a]},
            y_axis_config={"numbers_to_include": []}
        )
        axes.scale(0.4)
        axes.shift(4 * RIGHT)  # Adjusted position to center at (0, 0)
        labels = axes.get_axis_labels()
        line = Line(axes.c2p(8, 20, 20), axes.c2p(8, -20, -20), color=WHITE)

        self.play(Create(axes),Create(line))
        self.wait(2)

        # Symmetry

        sy = Text("Lets check the Symmetry", font_size=30,color=RED)
        sy.shift(4 * LEFT + 2 * UP)
        sy_1 = Text("As after replacing x by y and y by x,", font_size=25)
        sy_1.shift(3 * LEFT + 1 * UP)
        sy_2 = Text("the equation doesn't change", font_size=25)
        sy_2.shift(3 * LEFT)
        sy_3 = Text("Therefore Symmetry is about the line x=y",font_size=25, color=YELLOW)
        sy_3.shift(3 * LEFT - 1 * UP)
        self.play(Write(sy))
        self.play(Write(sy_1))
        self.play(Write(sy_2))
        self.play(Write(sy_3))
        self.wait(1)

        self.play(FadeOut(sy),FadeOut(sy_1),FadeOut(sy_2),FadeOut(sy_3))

        #some points on curve
        points = Text("Some Points on the curve :->",font_size=30,color = RED)
        points.shift(4 * LEFT + 2 * UP)

        points_1 = Text("x-intercept :-> Put y = 0  in equation",font_size=26)
        points_1.shift(3 * LEFT + 1 * UP)

        points_2 = MathTex("x^{3} + 0^{3} = 3ax(0)",font_size=40)
        points_2.shift(3 * LEFT)

        points_3 = MathTex("x^{3} = 0 --> (x = 0)",font_size=40)
        points_3.shift(3 * LEFT - 0.5 * UP)

        points_4 = Text("We get (0,0) as a point",font_size=30)
        points_4.shift(3 * LEFT - 1.5 * UP)

        points_5 = Text("Also.. as the curve passes through x=y, put y=x in equation",font_size=22)
        points_5.shift(3 * LEFT + 1 * UP)

        points_6 = MathTex("x^{3} + x^{3} = 3ax(x)",font_size=40)
        points_6.shift(3 * LEFT)

        points_7 = MathTex("2x^{3} = 3ax^{2}",font_size=40)
        points_7.shift(3 * LEFT - 0.5 * UP)

        points_8 = MathTex("2x = 3a --> (x = 3a/2)",font_size=40)
        points_8.shift(3 * LEFT - 1 * UP)

        points_9 = Text("we get the point (3a/2,3a/2)",font_size=40)
        points_9.shift(3 * LEFT - 2 * UP)

        points_10 = Text("Hence (0,0) and (3a/2, 3a/2) are the points on curve",font_size=24, color=YELLOW)
        points_10.shift(3 * LEFT + 1 * UP)

        self.play(Write(points))
        self.play(Write(points_1))
        self.play(Write(points_2))
        self.play(Write(points_3))
        self.play(Write(points_4))
        self.wait(1)

        self.play(FadeOut(points_1),FadeOut(points_2), FadeOut(points_3), FadeOut(points_4))
        self.wait(1)

        self.play(Write(points_5))
        self.play(Write(points_6))
        self.play(Write(points_7))
        self.play(Write(points_8))
        self.play(Write(points_9))
        self.wait(1)

        self.play(FadeOut(points_5),FadeOut(points_6),FadeOut(points_7),FadeOut(points_8),FadeOut(points_9))
        self.wait(1)

        self.play(Write(points_10))
        self.wait(1)

        self.play(FadeOut(points_10),FadeOut(points))