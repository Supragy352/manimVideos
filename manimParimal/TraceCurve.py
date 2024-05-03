from manim import *

class PlotCurve(Scene):
    def construct(self):
        # CONSTANTS
        a = 1

        # The curve equation function
        def curve_equation(x, y):
            return y**2 * (a**2 - x**2) - a**3 * x

        # Create the curve equation graph
        curve = ImplicitFunction(
            curve_equation,
            color=YELLOW
        )

        #Text
        curve_eqn_text = MathTex("The Curve Equation is: y^2 (a^2 - x^2) = a^3 x").scale(0.6).to_edge(UL)
        symmetry_text = Tex("Symmetry: about x-axis").scale(0.6).next_to(curve_eqn_text, DOWN, aligned_edge=LEFT)
        intersection_text = Tex("Point of Intersection: Origin").scale(0.6).next_to(symmetry_text, DOWN, aligned_edge=LEFT)
        tangent_text = Tex("Tangent at Origin: x = 0").scale(0.6).next_to(intersection_text, DOWN, aligned_edge=LEFT)
        asymptote_text = Tex("Asymptote: x = a, x = -a , y = 0").scale(0.6).next_to(tangent_text, DOWN, aligned_edge=LEFT)
        

        #Add the number plane 
        self.add(NumberPlane())
        self.play(Write(curve_eqn_text))

        #Highlight the line of symmetry
        self.play(Write(symmetry_text))
        x_axis = Line(start=LEFT * 10, end=RIGHT * 10, color=RED)  
        self.play(FadeIn(x_axis))  
        self.wait(1)
        self.play(FadeOut(x_axis))

        #Point of intersection
        self.play(Write(intersection_text))
        intersection_point = Dot(color=RED)
        intersection_label = MathTex("(0, 0)").scale(0.6).next_to(intersection_point, UR)
        self.play(Create(intersection_point),Write(intersection_label))

        #Draw the tangent
        self.play(Write(tangent_text))
        tangent_POI = Line(start=UP * 3, end=DOWN * 3, color=RED)
        tangent_label = Tex("x=0").scale(0.6).next_to(tangent_POI, RIGHT).shift(UP * 1.5)
        self.play(Create(tangent_POI),Create(tangent_label))

        #Draw Asymptotes
        self.play(Write(asymptote_text))
        asymptote1 = Line(start=DOWN * 10, end=UP * 10, color=GREEN).shift(LEFT * a)
        asymptote1_label = MathTex("x = -a").scale(0.6).next_to(asymptote1, LEFT, buff=0.1).shift(UP * 0.5)
        
        asymptote2 = Line(start=DOWN * 10, end=UP * 10, color=GREEN).shift(RIGHT * a)
        asymptote2_label = MathTex("x = a").scale(0.6).next_to(asymptote2, RIGHT, buff=0.1).shift(UP * 0.5)
        
        asymptote3 = Line(start=RIGHT * 0, end=LEFT * 10, color=GREEN)
        asymptote3_label = MathTex("y = 0").scale(0.6).next_to(asymptote3, UP, buff=0.1).shift(RIGHT * 1)

        self.play(Create(asymptote1),Create(asymptote1_label),Create(asymptote2),Create(asymptote2_label),Create(asymptote3),Create(asymptote3_label),run_time = 5)

        # Region Of the Curve
        region1 = Rectangle(
            width=1,
            height=40,
            stroke_color=BLUE,
            stroke_width=1,
            fill_color=BLUE,
            fill_opacity=0.2,
        ).move_to(LEFT * 0.5*a).shift(DOWN * 10)

        region2 = Rectangle(
            width=8,
            height=40,
            stroke_color=BLUE,
            stroke_width=1,
            fill_color=BLUE,
            fill_opacity=0.2,
        ).move_to(RIGHT * 5 * a).shift(DOWN * 10)


        region_absence = Tex("Region of Absence: (-a < x < 0)  ,  x > a").scale(0.6).to_edge(UR)
        self.play(Write(region_absence))
        self.play(Create(region1),Create(region2))

        region_presence = MathTex("Region of Presence: x < -a ,  0 < x < a").scale(0.6).next_to(region_absence,DOWN)
        self.play(Write(region_presence))

        # Add graph to the scene
        self.play(Create(curve), run_time=5)