from manim import *

class ManimCELogo(Scene):
    def construct(self):
        # Text equation
        eqn = Text("Equation :->", font_size=30,color = RED)
        eqn.shift(3 * UP)
        equation = MathTex("xy^{2}=a^{2}\\left(x^{2}-a^{2}\\right)", font_size=60)
        equation.shift( 2 * UP)
        self.play(Write(eqn),Write(equation))
        self.wait()
        self.play(FadeOut(eqn))

        equation.shift(1 * UP + 4 * RIGHT)
        self.play(Write(equation))
        self.wait(2)

        # Symmetry
        sy = Text("Symmetry :->", font_size=30,color=RED)
        sy.shift(3 * RIGHT + 1 * UP)
        sy_1 = Text("As all powers of y are even", font_size=25)
        sy_1.shift(3 * RIGHT )
        sy_2 = Text("Therefore Symmetry is about X-axis",font_size=25)
        sy_2.shift(3 * RIGHT - 1 * UP)
        self.play(Write(sy))
        self.play(Write(sy_1))
        self.play(Write(sy_2))
        self.wait(1)


        # Axes and labels
        a = 2
        axes = ThreeDAxes(
            x_range=[-5, 5], y_range=[-5, 5], z_range=[-5, 5],
            x_axis_config={"numbers_to_include": [a,-a]},
            y_axis_config={"numbers_to_include": []}
        )
        axes.scale(0.5)
        axes.shift(4 * LEFT )  # Adjusted position to center at (0, 0)
        labels = axes.get_axis_labels()
        line = Line(axes.c2p(8, 20, 20), axes.c2p(8, -20, -20), color=WHITE)

        label_symmetry_x = Tex("Symmetry", color=WHITE, font_size=30)
        label_symmetry_x.next_to(axes.get_x_axis(), RIGHT, buff=SMALL_BUFF)
        self.play(Create(axes),Write(label_symmetry_x),Create(line))
        self.wait(2)
        self.play(FadeOut(sy),FadeOut(sy_1),FadeOut(sy_2))

        #some points on curve
        some_points_on_curve = Text("Some Points on the curve :->",font_size=30,color = RED)
        some_points_on_curve.shift(3 * RIGHT + 1 * UP )

        some_points_on_curve_1 = Text("x-intercept :-> Put y = 0 in equation",font_size=20)
        some_points_on_curve_1.shift(3 * RIGHT -1 * UP)

        some_points_on_curve_2 = Text("(a,0) and (-a,0)",font_size=25)
        some_points_on_curve_2.shift(3 * RIGHT - 1.5 * UP)

        self.play(Write(some_points_on_curve))
        self.play(Write(some_points_on_curve_1))
        self.play(Write(some_points_on_curve_2))
        self.play(FadeOut(some_points_on_curve),FadeOut(some_points_on_curve_1),FadeOut(some_points_on_curve_2))
        self.wait()

        tangent = Text("Tangents :->",font_size=30,color=RED)
        tangent.shift(3 * RIGHT + 1.5 * UP)
        tangent_1 = Text("At (a,0) parallel to Y-axis",font_size=30)
        tangent_1.shift(3 * RIGHT + 0.8 * UP)
        tangent_2 = Text("At (-a,0) parallel to Y-axis",font_size=30)
        tangent_2.shift(3 * RIGHT)
        self.play(Write(tangent))
        self.play(Write(tangent_1))
        self.play(Write(tangent_2))
        self.wait()
        
        # Lines and braces
        a = 2
        line_at_a = DashedLine(axes.c2p(a, -5, -5), axes.c2p(a, 5, 5), color=WHITE)
        line_at_minus_a = DashedLine(axes.c2p(-a, -5, -5), axes.c2p(-a, 5, 5), color=WHITE)
        b1 = Brace(line_at_a)
        b1text = b1.get_text("tangent").set_color(YELLOW)
        b2 = Brace(line_at_minus_a)
        b2text = b2.get_text("tangent").set_color(YELLOW)
        self.play(Create(line_at_a),Create(line_at_minus_a),Write(b1text),Write(b2text))
        self.wait()
        self.play(FadeOut(tangent),FadeOut(tangent_1),FadeOut(tangent_2))
        
        # Asymptotes
        asymptote = Text("asymptote :->",font_size=40,color=RED)
        asymptote.shift(3 * RIGHT + 2 * UP)
        asymptote_1 = Text("asymptote parallel to Y-axis :" , font_size=30)
        asymptote_1.shift(3 * RIGHT + 1 * UP )
        asymptote_2 =Text("(X = 0)",font_size=30)
        asymptote_2.shift(3 * RIGHT)
        
        line_at_right_y = Line(axes.c2p(0.8, 3.5, 3.5), axes.c2p(0.8, 5, 5), color=RED)
        line_at_minus_right_y = Line(axes.c2p(0.8, -3.5, -3.5), axes.c2p(0.8, -5, -5), color=RED)
        line_at_left_y = Line(axes.c2p(-0.8, 3.5, 3.5), axes.c2p(-0.8, 5, 5), color=RED)
        line_at_minus_left_y = Line(axes.c2p(-0.8, -3.5, -3.5), axes.c2p(-0.8, -5, -5), color=RED)

        b4 = Brace(line_at_left_y)
        b4text = b4.get_text("asymptote").scale(0.5).next_to(b4, 4.5*UP+0.5*RIGHT).set_color(RED)

        self.play(Write(asymptote))
        self.play(Write(asymptote_1))
        self.play(Write(asymptote_2))
        self.play(Create(line_at_right_y),Create(line_at_minus_right_y),Create(line_at_left_y),Create(line_at_minus_left_y),Write(b4text))
        self.wait(2)
        self.play(FadeOut(asymptote),FadeOut(asymptote_1),FadeOut(asymptote_2))

        # Region of absence
        roa = Text("Region of absence:->",font_size=40,color=RED)
        roa.shift(3 * RIGHT + 2 * UP)
        roa_1 = Text("ROA for Y :-> ",font_size=30)
        roa_1.shift(3 * RIGHT + 1 * UP)
        roa_2 = Text("(x < -a) and (0 < x < a)",font_size=30)
        roa_2.shift(3 * RIGHT )

        rectangle_roa = Rectangle(height=5, width=1, color=WHITE, fill_opacity=0.2).move_to(axes.c2p(1, 0, 0))
        rectangle = Rectangle(height=5, width=1.5, color=WHITE, fill_opacity=0.2).move_to(axes.c2p(-3.5, 0, 0))
        
        self.play(Write(roa))
        self.play(Write(roa_1))
        self.play(Write(roa_2))
        self.play(Create(rectangle_roa), Create(rectangle))
        self.wait()
        self.play(FadeOut(roa),FadeOut(roa_1),FadeOut(roa_2))

        draw = Text("Lets connect points on graph",font_size=30,color=YELLOW)
        draw.shift(3 * RIGHT - 2 * UP)
        self.play(Write(draw))

        # Editing graph of implicit function
        graph = ImplicitFunction(
            lambda x, y: x * y ** 2 - a ** 2 * (x ** 2 - a ** 2),
            color=YELLOW
        )
        
        # Example of editing graph (you can modify this)
        graph.scale(0.5)  # Scale down the graph
        graph.shift(4.7 * LEFT)  # Shift the graph
        graph.set_color(GREEN)  # Change color of the graph
        
        self.play(Create(graph))
        self.wait(4)

