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
        a = 3
        axes = ThreeDAxes(
            x_range=[-5, 5], y_range=[-5, 5], z_range=[-5, 5],
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []}
        )
        axes.scale(0.4)
        axes.shift(4 * RIGHT)  # Adjusted position to center at (0, 0)
        labels = axes.get_axis_labels()
        line = Line(axes.c2p(8, 20, 20), axes.c2p(8, -20, -20), color=WHITE)

        self.play(Create(axes),Create(line))
        self.wait(2)

        # Symmetry

        sy = Text("1] Symmetry", font_size=30,color=RED)
        sy.shift(4 * LEFT + 2 * UP)
        sy_1 = Text("As after replacing x by y and y by x,", font_size=25)
        sy_1.shift(3 * LEFT + 1 * UP)
        sy_2 = Text("the equation doesn't change", font_size=25)
        sy_2.shift(3 * LEFT + 0.4 * UP)
        sy_3 = Text("Therefore Symmetry is about the line x=y",font_size=25, color=YELLOW)
        sy_3.shift(3 * LEFT - 0.4 * UP)
        self.play(Write(sy))
        self.play(Write(sy_1))
        self.play(Write(sy_2))
        self.play(Write(sy_3))
        self.wait(1)



        
        #Animation for Symmetry 
        symm_line = DashedLine(start=axes.coords_to_point(-5, -5), end=axes.coords_to_point(5, 5), color=YELLOW)

        self.play(Create(symm_line))
        self.wait(1)

        label_symmetry = Text("Symmetry", color=WHITE, font_size=18)
        label_symmetry.next_to(symm_line, UP+RIGHT, buff=SMALL_BUFF)

        self.play(Create(label_symmetry))
        self.wait(1)


        self.play(FadeOut(sy),FadeOut(sy_1),FadeOut(sy_2),FadeOut(sy_3))


        #Points of Intersection

        points = Text("2] Points of intersection :-",font_size=30,color = RED)
        points.shift(4 * LEFT + 2 * UP)

        points_1 = MathTex("x-intercept \Rightarrow Put y = 0  in equation",font_size=26)
        points_1.shift(3 * LEFT + 1 * UP)

        points_2 = MathTex("x^{3} + 0^{3} = 3ax(0)",font_size=40)
        points_2.shift(3 * LEFT)

        points_3 = MathTex("x^{3} = 0 \Rightarrow (x = 0)",font_size=40)
        points_3.shift(3 * LEFT - 0.5 * UP)

        points_4 = Text("We get (0,0) as a point",font_size=30, color=YELLOW)
        points_4.shift(3 * LEFT - 1.5 * UP)

        points_5 = Text("Also.. as the curve passes through x=y, put y=x in equation",font_size=22)
        points_5.shift(3 * LEFT + 1 * UP)

        points_6 = MathTex("x^{3} + x^{3} = 3ax(x)",font_size=40)
        points_6.shift(3 * LEFT)

        points_7 = MathTex("2x^{3} = 3ax^{2}",font_size=40)
        points_7.shift(3 * LEFT - 0.5 * UP)

        points_8 = MathTex("2x = 3a \Rightarrow (x = 3a/2)",font_size=40)
        points_8.shift(3 * LEFT - 1 * UP)

        points_9 = MathTex("we get (3*a/2,3*a/2) as a point",font_size=30, color=YELLOW)
        points_9.shift(3 * LEFT - 2 * UP)

        points_10 = Text("Hence (0,0) and (3a/2, 3a/2) are the points on the curve",font_size=24, color=YELLOW)
        points_10.shift(3 * LEFT + 1 * UP)


        #Arranging the points of intersection in sequence

        self.play(Write(points))
        self.play(Write(points_1))
        self.play(Write(points_2))
        self.play(Write(points_3))
        self.play(Write(points_4))
        self.wait(1)

        #Animation for origin

        origin_dot = Dot(color=GREEN, radius=0.1)
        origin_dot.move_to(axes.coords_to_point(0, 0))

        self.play(Create(origin_dot))
        self.wait(1)

        self.play(FadeOut(points_1),FadeOut(points_2), FadeOut(points_3), FadeOut(points_4))
        self.wait(1)

        self.play(Write(points_5))
        self.play(Write(points_6))
        self.play(Write(points_7))
        self.play(Write(points_8))
        self.play(Write(points_9))
        self.wait(1)




        dot2 = Dot(color=GREEN, radius=0.1)
        dot2.move_to(axes.coords_to_point(3*a/2, 3*a/2))

        self.play(Create(dot2))
        self.wait(1)




        self.play(FadeOut(points_5),FadeOut(points_6),FadeOut(points_7),FadeOut(points_8),FadeOut(points_9))
        self.wait(1)

        self.play(Write(points_10))
        self.wait(1)

        self.play(FadeOut(points_10),FadeOut(points))

        #Tangents

        tangents = Text("3] Tangents :-",font_size=30,color = RED)
        tangents.shift(4 * LEFT + 2 * UP)

        tangent_1 = Text("To find the tangent, we have to equate the lowest ",font_size=26)
        tangent_1.shift(3 * LEFT + 1 * UP)

        tangent_2 = Text("degree term of the equation to zero",font_size=26)
        tangent_2.shift(3 * LEFT + 0.5 * UP)

        self.play(Write(tangents))
        self.play(Write(tangent_1))
        self.play(Write(tangent_2))
        self.wait(2)

        self.play(FadeOut(tangent_1),FadeOut(tangent_2))
        self.wait(1)

        tangent_3 = Text("In this eqn, Equating the Lowest Degree Term to zero, we get",font_size=20)
        tangent_3.shift(3 * LEFT + 1 * UP)

        tangent_4 = MathTex("3axy = 0",font_size=40)
        tangent_4.shift(3 * LEFT)

        tangent_5 = MathTex("xy = 0",font_size=40)
        tangent_5.shift(3 * LEFT - 0.5 * UP)

        tangent_6 = Text("x=0 & y=0 are tangents at origin",font_size=27, color=YELLOW)
        tangent_6.shift(3 * LEFT - 1.5 * UP)

        tangent_7 = Text("Since there are 2 tangents at origin",font_size=27, color=YELLOW)
        tangent_7.shift(3 * LEFT + 1 * UP)

        tangent_8 = Text("Therefore, the origin is a node",font_size=27, color=YELLOW)
        tangent_8.shift(3 * LEFT + 0.4 * UP)

        self.play(Write(tangent_3))
        self.play(Write(tangent_4))
        self.play(Write(tangent_5))
        self.play(Write(tangent_6))
        self.wait(2)

        self.play(FadeOut(tangent_3),FadeOut(tangent_4),FadeOut(tangent_5),FadeOut(tangent_6))


        #Animation to draw Tangents

        tangent1 = Line(start=axes.coords_to_point(-5, 0), end=axes.coords_to_point(5, 0), color=RED)

        self.play(Create(tangent1))
        self.wait(1)

        label_tangent = Text("Tangent", color=WHITE, font_size=18)
        label_tangent.next_to(tangent1, UP+RIGHT, buff=SMALL_BUFF)

        label_tangent1 = Text("x=0", color=WHITE, font_size=18)
        label_tangent1.next_to(tangent1, UP+LEFT, buff=SMALL_BUFF)

        self.play(Create(label_tangent1))
        self.play(Create(label_tangent))
        self.wait(1)

        tangent2 = Line(start=axes.coords_to_point(0, -5), end=axes.coords_to_point(0, 5), color=RED)

        self.play(Create(tangent2))
        self.wait(1)

        label_tangent2 = Text("y=0", color=WHITE, font_size=18)
        label_tangent2.next_to(tangent2, DOWN+RIGHT, buff=SMALL_BUFF)

        label_tangent3 = Text("Tangent", color=WHITE, font_size=18)
        label_tangent3.next_to(tangent2, UP+RIGHT, buff=SMALL_BUFF)
        
        self.play(Create(label_tangent2))
        self.play(Create(label_tangent3))
        self.wait(1)


        self.play(Write(tangent_7))
        self.play(Write(tangent_8))
        self.wait(2)

        self.play(FadeOut(tangent_7),FadeOut(tangent_8),FadeOut(tangents))