from manim import *

class ConicsAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Curve Tracing", font_size=48, color=RED)
        title.shift(3 * UP)
        self.play(Write(title), run_time = 2)
        self.wait(0.2)

        text = Text("Hello, today we will learn how to plot the curve :", font_size = 36)
        text.shift(1 * UP)
        self.play(Write(text), run_time = 2)
        self.wait(0.2)

        eqn = MathTex("x^{3} + y^{3} = 3axy", font_size=50)
        self.play(Write(eqn))
        self.wait(1)
        self.play(FadeOut(eqn))

        self.play(FadeOut(title), FadeOut(text))

        eqn.shift(2.8 * UP + 4 * LEFT)
        self.play(Write(eqn))
        self.wait(1)

        # Axes and labels
        a = 1.5
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
        symm_line = DashedLine(start=axes.coords_to_point(-4.5, -4.5), end=axes.coords_to_point(4.5, 4.5), color=YELLOW)

        self.play(Create(symm_line))
        self.wait(1)

        label_symmetry = Text("Symmetry", color=YELLOW, font_size=18)
        label_symmetry.next_to(symm_line, UP+RIGHT, buff=SMALL_BUFF)

        self.play(Create(label_symmetry))
        self.wait(1)


        self.play(FadeOut(sy),FadeOut(sy_1),FadeOut(sy_2),FadeOut(sy_3))


        #Points of Intersection

        points = Text("2] Points of intersection :-",font_size=30,color = RED)
        points.shift(4 * LEFT + 2 * UP)

        points_1 = MathTex("x-intercept \Rightarrow Put", "\quad", "y = 0", "\quad", "in", "\quad", "equation",font_size=26)
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

        points_9 = Text("We get (3a/2,3a/2) as a point",font_size=30, color=YELLOW)
        points_9.shift(3 * LEFT - 2 * UP)

        points_10 = Text("Hence (0,0) and (3a/2, 3a/2) are the points on the curve",font_size=23, color=YELLOW)
        points_10.shift(3 * LEFT + 1 * UP)


        #Arranging the points of intersection in sequence

        self.play(Write(points))
        self.play(Write(points_1))
        self.play(Write(points_2))
        self.play(Write(points_3))
        self.play(Write(points_4))
        self.wait(1)

        #Animation for origin

        origin_dot = Dot(color=BLUE, radius=0.07)
        origin_dot.move_to(axes.coords_to_point(0, 0))

        label_dot = Text("(0,0)", color=WHITE, font_size=18)
        label_dot.next_to(origin_dot, DOWN+RIGHT, buff=SMALL_BUFF)

        self.play(Create(origin_dot))
        self.wait(1)

        self.play(Create(label_dot))
        self.wait(1)

        self.play(FadeOut(points_1),FadeOut(points_2), FadeOut(points_3), FadeOut(points_4))
        self.wait(1)

        self.play(Write(points_5))
        self.play(Write(points_6))
        self.play(Write(points_7))
        self.play(Write(points_8))
        self.play(Write(points_9))
        self.wait(1)


        dot2 = Dot(color=BLUE, radius=0.07)
        dot2.move_to(axes.coords_to_point(3*a/2, 3*a/2))

        self.play(Create(dot2))
        self.wait(1)

        label_dot2 = Text("(3a/2,3a/2)", color=WHITE, font_size=18)
        label_dot2.next_to(dot2, RIGHT, buff=SMALL_BUFF)

        self.play(Create(label_dot2))
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

        def tangent1(y):
            return 0

        def tangent2(x):
            return 0

        Tangent_1_points = [(x, tangent1(x)) for x in np.arange(-5, 5, 0.1)]
        Tangent_2_points = [(tangent2(y), y) for y in np.arange(-5, 5, 0.1)]

        Tangent_1_curve = VGroup(
            *[Line(axes.coords_to_point(x1, y1), axes.coords_to_point(x2, y2), color=RED)
              for (x1, y1), (x2, y2) in zip(Tangent_1_points[:-1], Tangent_1_points[1:])]
        )

        Tangent_2_curve = VGroup(
            *[Line(axes.coords_to_point(x1, y1), axes.coords_to_point(x2, y2), color=RED)
              for (x1, y1), (x2, y2) in zip(Tangent_2_points[:-1], Tangent_2_points[1:])]
        )

        self.play(Create(Tangent_1_curve), Create(Tangent_2_curve))
        self.wait(1)

        label_tangent = Text("Tangent", color=RED, font_size=18)
        label_tangent1 = Text("x=0", color=RED, font_size=18)
        label_tangent2 = Text("y=0", color=RED, font_size=18)
        label_tangent3 = Text("Tangent", color=RED, font_size=18)

        label_tangent.next_to(Tangent_1_curve, UP+RIGHT, buff=SMALL_BUFF)
        label_tangent1.next_to(Tangent_1_curve, UP+LEFT, buff=SMALL_BUFF)
        label_tangent2.next_to(Tangent_2_curve, DOWN+RIGHT, buff=SMALL_BUFF)
        label_tangent3.next_to(Tangent_2_curve, UP+RIGHT, buff=SMALL_BUFF)

        self.play(Create(label_tangent1), Create(label_tangent))
        self.play(Create(label_tangent2), Create(label_tangent3))
        self.wait(1)


        self.play(Write(tangent_7))
        self.play(Write(tangent_8))
        self.wait(2)

        self.play(FadeOut(tangent_7),FadeOut(tangent_8),FadeOut(tangents))



        #Asymptotes

        Asymptotes = Text("4] Asymptotes :-",font_size=30,color = RED)
        Asymptotes.shift(4 * LEFT + 2 * UP)

        Asymptote_1 = Text("To find the asymptote parallel to x-axis,",font_size=24)
        Asymptote_1.shift(3 * LEFT + 1 * UP)

        Asymptote_2 = Text("we have to equate the coefficient of the ",font_size=24)
        Asymptote_2.shift(3 * LEFT + 0.5 * UP)

        Asymptote_3 = Text("highest degree term x to zero",font_size=24)
        Asymptote_3.shift(3 * LEFT)

        self.play(Create(Asymptotes))
        self.play(Create(Asymptote_1))
        self.play(Create(Asymptote_2))
        self.play(Create(Asymptote_3))
        self.wait(2)

        self.play(FadeOut(Asymptote_1),FadeOut(Asymptote_2), FadeOut(Asymptote_3))

        

        Asymptote1 = MathTex("Highest", "\quad", " degree", "\quad", " term", "\quad", " of", "\quad", " x", "\quad", " is", "\quad", " x^{3}",font_size=35)
        Asymptote1.shift(3 * LEFT + 1 * UP)

        Asymptote2 = MathTex("Coeffient", "\quad", " of", "\quad", " x^{3} ", "\quad", "is", "\quad", " 1",font_size=35)
        Asymptote2.shift(3 * LEFT + 0.4 * UP)

        Asymptote3 = MathTex("1 = 0 \Rightarrow", "\quad", " doesn't", "\quad", " yield", "\quad", " any", "\quad", " value",font_size=35)
        Asymptote3.shift(3 * LEFT - 0.2 * UP)

        Asymptote4 = Text("There is no asymptote parallel to x-axis",font_size=27, color=YELLOW)
        Asymptote4.shift(3 * LEFT - 1.4 * UP)

        self.play(Create(Asymptote1))
        self.play(Create(Asymptote2))
        self.play(Create(Asymptote3))
        self.play(Create(Asymptote4))
        self.wait(2)

        self.play(FadeOut(Asymptote1),FadeOut(Asymptote2), FadeOut(Asymptote3), FadeOut(Asymptote4))


        Asymptote_4 = Text("To find the asymptote parallel to y-axis,",font_size=22)
        Asymptote_4.shift(3 * LEFT + 1 * UP)

        Asymptote_5 = Text(" we have to equate the coefficient of the ",font_size=22)
        Asymptote_5.shift(3 * LEFT + 0.5 * UP)

        Asymptote_6 = Text("highest degree term of y to zero",font_size=22)
        Asymptote_6.shift(3 * LEFT)

        self.play(Create(Asymptote_4))
        self.play(Create(Asymptote_5))
        self.play(Create(Asymptote_6))
        self.wait(2)

        self.play(FadeOut(Asymptote_4),FadeOut(Asymptote_5), FadeOut(Asymptote_6))


        Asymptote5 = MathTex("Highest", "\quad", " degree", "\quad", " term ", "\quad", "of", "\quad", " y", "\quad", " is ", "\quad", "y^{3}",font_size=35)
        Asymptote5.shift(3 * LEFT + 1 * UP)

        Asymptote6 = MathTex("Coeffient ", "\quad", "of", "\quad", " y^{3}", "\quad", " is", "\quad", " 1",font_size=35)
        Asymptote6.shift(3 * LEFT + 0.4 * UP)

        Asymptote7 = MathTex("1 = 0 \Rightarrow", "\quad", " doesn't", "\quad", " yield ", "\quad", "any", "\quad", " value",font_size=35)
        Asymptote7.shift(3 * LEFT - 0.2 * UP)

        Asymptote8 = Text("There is no asymptote parallel to y-axis",font_size=27, color=YELLOW)
        Asymptote8.shift(3 * LEFT - 1.4 * UP)

        self.play(Create(Asymptote5))
        self.play(Create(Asymptote6))
        self.play(Create(Asymptote7))
        self.play(Create(Asymptote8))
        self.wait(2)

        self.play(FadeOut(Asymptote5),FadeOut(Asymptote6), FadeOut(Asymptote7), FadeOut(Asymptote8))

        
        #Oblique Asymptote

        obl1 = Text("To find the oblique asymptote, put y = mx + c in given eqn",font_size=22)
        obl1.shift(3 * LEFT + 1 * UP)

        obl2 = MathTex("x^{3} + (mx + c)^{3} = 3ax(mx + c)",font_size=30)
        obl2.shift(3 * LEFT)

        obl11 = Text("Coefficient of",font_size=20)
        obl11.shift(5 * LEFT - 0.8 * UP)

        obl3 = MathTex(" x^{3}", "\quad" ,"is","\quad" , "1 + m^{3} = 0 \Rightarrow m = -1",font_size=30)
        obl3.shift(1.9 * LEFT - 0.8 * UP)

        obl22 = Text("Coefficient of",font_size=20)
        obl22.shift(5 * LEFT - 1.5 * UP)

        obl4 = MathTex("x^{2}", "\quad" ,"is","\quad" , "3m^{2}c - 3am = 0",font_size=30)
        obl4.shift(2.3 * LEFT - 1.5 * UP)

        obl5 = MathTex("3m^{2}c = 3am \Rightarrow c = -a (m = -1)",font_size=30)
        obl5.shift(3 * LEFT - 2.3 * UP)

        self.play(Write(obl1))
        self.play(Write(obl2))
        self.play(Write(obl11))
        self.play(Write(obl3))
        self.wait(1)

        self.play(Write(obl22))
        self.play(Write(obl4))
        self.play(Write(obl5))
        self.wait(2)


        def obl_asymptote(x):
            y = -x -a
            return y

        obl_asymp_points = [(x , obl_asymptote(x)) for x in np.arange(-5, 4, 0.1)]

        obl_asymptote_curve = VGroup(
            *[Line(axes.coords_to_point(x1, y1), axes.coords_to_point(x2, y2), color=GREEN)
              for (x1, y1), (x2, y2) in zip(obl_asymp_points[:-1], obl_asymp_points[1:])]
        )

        self.play(Create(obl_asymptote_curve))
        self.wait(2)
        
        obliq1 = Text("Asymptote", color=WHITE, font_size=18)
        obliq1.next_to(obl_asymptote_curve, DOWN+RIGHT, buff=SMALL_BUFF)

        obliq2 = Text("x+y+a=0", color=WHITE, font_size=18)
        obliq2.next_to(obl_asymptote_curve, UP+LEFT, buff=SMALL_BUFF)

        self.play(Create(obliq1), Create(obliq2))
        self.wait(2)

        self.play(FadeOut(obl1),FadeOut(obl2), FadeOut(obl11), FadeOut(obl3))

        self.play(FadeOut(obl22),FadeOut(obl4), FadeOut(obl5))

        self.play(FadeOut(Asymptotes))



        #Last Tangent

        Another_tangent = Text("4] Another tangent :-",font_size=30,color = RED)
        Another_tangent.shift(4 * LEFT + 2 * UP)

        tang1 = Text("Therefore",font_size=20)
        tang1.shift(3 * LEFT + 0.5 * UP)

        tang2 = MathTex("y = mx + c = -x -a" , "\quad" ,"or","\quad" ,"x + y + a = 0",font_size=30)
        tang2.shift(3 * LEFT)

        tang3 = Text("is the oblique asymptote",font_size=20)
        tang3.shift(3 * LEFT - 0.5 * UP)

        tang4 = MathTex(" x + y + a = 0",font_size=30)
        tang4.shift(3 * LEFT + 0.5 * UP)

        tang5 = Text("Differentiating the eqn w.r.t. to x",font_size=20)
        tang5.shift(3 * LEFT - 0.1 * UP)

        tang6 = MathTex("3x^{2} + 3y^{2} dy/dx = 3a (y + x dy/dx)",font_size=30)
        tang6.shift(3 * LEFT - 0.7 * UP)

        tang7 = Text("Therefore",font_size=20)
        tang7.shift(3 * LEFT - 1.4 * UP)

        tang8 = MathTex("dy/dx = (ay - x^{2})/(y^{2} - ax)",font_size=30)
        tang8.shift(3 * LEFT - 1.9 * UP)

        tang9 = Text("At (3a/2, 3a/2),  dy/dx = -1",font_size=24, color=YELLOW)
        tang9.shift(3 * LEFT - 2.6 * UP)

        self.play(Write(Another_tangent))
        self.play(Write(tang1))
        self.play(Write(tang2))
        self.play(Write(tang3))
        self.wait(1)

        self.play(FadeOut(tang1),FadeOut(tang2), FadeOut(tang3))
        self.wait(1)

        self.play(Write(tang4))
        self.play(Write(tang5))
        self.play(Write(tang6))
        self.wait(1)
        self.play(Write(tang7))
        self.play(Write(tang8))
        self.play(Write(tang9))
        self.wait(1)

        def tangent3(x):
            y = -1 * (x - 3*a/2) + 3*a/2
            return y

        tang3_points = [(x , tangent3(x)) for x in np.arange(-2, 6, 0.1)]

        tang3_curve = VGroup(
            *[Line(axes.coords_to_point(x1, y1), axes.coords_to_point(x2, y2), color=RED)
              for (x1, y1), (x2, y2) in zip(tang3_points[:-1], tang3_points[1:])]
        )

        self.play(Create(tang3_curve))
        self.wait(2)

        label_tangent4 = Text("Tangent", color=RED, font_size=18)
        label_tangent4.next_to(tang3_curve, UP+LEFT, buff=SMALL_BUFF)

        self.play(Create(label_tangent4))
        self.wait(1)

        self.play(FadeOut(tang4),FadeOut(tang5), FadeOut(tang6),FadeOut(tang7), FadeOut(tang8),FadeOut(tang9))
        self.wait(1)

        self.play(FadeOut(Another_tangent))


        Final_curve = Text("Let's finally plot the curve", font_size=35, color=RED)
        Final_curve.shift(3 * LEFT )

        self.play(Write(Final_curve))
        self.wait(1)

        curve = self.get_curve(a)
        curve.scale(0.4)
        curve.shift(4.81 * RIGHT + 0.02 * UP)

        # Add curve to scene
        self.play(Create(curve), run_time=5)
        self.wait(2)

    def get_curve(self,a):
        def curve_func(x,y):
            return x ** 3 + y ** 3 - 3 * a * x * y

        curve = ImplicitFunction(lambda x, y: curve_func(x, y), color=YELLOW)

        return curve

        self.play(FadeOut(Final_curve))
        self.wait(1)