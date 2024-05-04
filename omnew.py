from manim import *

class curve(Scene):
    def construct(self):
        a = 1

        question_text = Text("Trace the Curve : y^2 * (2a - x) = x^3").scale(0.6)
        question_text.move_to(ORIGIN)
        self.play(Write(question_text))
        self.play(question_text.animate.shift(UP*3))
        self.wait(1.5)
        
        symmetry_text = Text("Symmetry : ").scale(0.5).to_edge(LEFT * 3)
        text = Text("equation contains even powers of y").scale(0.5).next_to(symmetry_text, DR)
        text2 = Text("Therefore, Symmetric about x-axis").scale(0.5).next_to(text, DOWN)
        self.play(Write(symmetry_text))
        self.wait(0.3)
        self.play(Write(text))
        self.wait(0.3)
        self.play(Write(text2))
        self.wait(1)

        axes = Axes(x_range=[-6,6], y_range=[-6,6], axis_config={"color":WHITE}, x_length=5, y_length=5)
        axes.to_edge(RIGHT, buff=0.5)
        area_above_x_axis = Polygon(axes.c2p(-6,6), axes.c2p(6,6), axes.c2p(6,0), axes.c2p(-6,0), fill_color=BLUE, fill_opacity=0.5)
        area_below_x_axis = Polygon(axes.c2p(-6,-6), axes.c2p(6,-6), axes.c2p(6,0), axes.c2p(-6,0), fill_color=BLUE, fill_opacity=0.5)
        self.play(Create(axes))
        self.play(FadeIn(area_above_x_axis))
        self.wait(0.5)
        self.play(FadeOut(area_above_x_axis))
        self.wait(0.5)
        self.play(FadeIn(area_below_x_axis))
        self.wait(0.5)
        self.play(FadeOut(area_below_x_axis))
        self.wait(0.5)

        self.play(Unwrite(symmetry_text))
        self.play(Unwrite(text))
        self.play(Unwrite(text2))

        poi_text = Text("Point of Intersection : ").scale(0.5).to_edge(LEFT * 3)
        intercept = Text("x = 0 --> y=0 and y = 0 --> x = 0").scale(0.5).next_to(poi_text, DR)
        origin = Text("Therefore, Passing through origin").scale(0.5).next_to(intercept, DOWN)
        self.play(Write(poi_text))
        self.wait(0.3)
        self.play(Write(intercept))
        self.wait(0.3)
        self.play(Write(origin))
        self.wait(1)

        intersection_point = Dot(color=RED)
        intersection_point.move_to(axes.c2p(0,0))
        intersection_label = Tex("(0, 0)").scale(0.4).next_to(intersection_point, DR)
        self.play(Create(intersection_point),Write(intersection_label))
        self.wait(1.5)

        self.play(Unwrite(poi_text))
        self.play(Unwrite(intercept))
        self.play(Unwrite(origin))

        tangent = Text("Tangent : ").scale(0.5).to_edge(LEFT * 3)
        lowest = Text("Equating the lowest degree term to Zero").scale(0.5).next_to(tangent, DR)
        equ = Text("2ay^2 - y^2x - x^3 = 0").scale(0.5).next_to(lowest, DOWN)
        equ2 = Text("2ay^2 = 0 --> y^2 = 0 --> y=0 & y=0").scale(0.5).next_to(equ, DOWN)
        equ3 = Text("Two real and coincident tangents").scale(0.5).next_to(equ2, DOWN)
        final_equ = Text("(0,0) is a cusp").scale(0.5).next_to(equ3, DOWN)
        self.play(Write(tangent))
        self.wait(0.2)
        self.play(Write(lowest))
        self.wait(0.2)
        self.play(Write(equ))
        self.wait(0.2)
        self.play(Write(equ2))
        self.wait(0.2)
        self.play(Write(equ3))
        self.wait(0.2)
        self.play(Write(final_equ))
        self.wait(1)

        x_axis = Line(start=axes.c2p(-6,0), end=axes.c2p(6,0), color=BLUE)  
        self.play(FadeIn(x_axis))  
        self.wait(1)
        
        self.play(Unwrite(tangent))
        self.play(Unwrite(lowest))
        self.play(Unwrite(equ))
        self.play(Unwrite(equ2))
        self.play(Unwrite(equ3))
        self.play(Unwrite(final_equ))

        asymptote = Text("Asymptote :").scale(0.4).to_edge(LEFT * 3)
        asym_xaxis = Text("||el to x-axis : coefficient of highest degree term of x equal to Zero").scale(0.4).next_to(asymptote, DR)
        asymp_x = Text("Coefficient of x^3 is 1, but 1 not equal to zero").scale(0.4).next_to(asym_xaxis, DOWN)
        x_final = Text("Therefore, no asymptote ||el to x-axis").scale(0.4).next_to(asymp_x, DOWN)
        self.play(Write(asymptote))
        self.wait(0.1)
        self.play(Write(asym_xaxis))
        self.wait(0.1)
        self.play(Write(asymp_x))
        self.wait(0.1)
        self.play(Write(x_final))
        self.wait(1)

        self.play(Unwrite(asymptote))
        self.play(Unwrite(asym_xaxis))
        self.play(Unwrite(asymp_x))
        self.play(Unwrite(x_final))

        asymp_y = Text("||el to y-axis : Coefficient of highest degree term of y equal to Zero").scale(0.4).to_edge(LEFT * 2)
        y2 = Text("coefficient of y^2 is (2a-x) --> 2a-x = 0 --> x=2a").scale(0.4).next_to(asymp_y, DOWN)
        y_final = Text("Therefore, asymptote ||el to y-axis is x=2a").scale(0.4).next_to(y2, DOWN)

        self.play(Write(asymp_y))
        self.wait(0.1)
        self.play(Write(y2))
        self.wait(0.1)
        self.play(Write(y_final))
        self.wait(0.1)

        x_2a = Line(start=axes.c2p(2*a,-6), end=axes.c2p(2*a,6), color=GREEN)
        asymptote_label = Tex("x=2a").scale(0.5).next_to(x_2a, UR)
        self.play(Create(x_2a), Write(asymptote_label))
        self.wait(1.2)

        self.play(Unwrite(asymp_y))
        self.play(Unwrite(y2))
        self.play(Unwrite(y_final))

        region = Text("Region of Absence : ").scale(0.4).to_edge(LEFT * 2.2)
        curve_exists = Text("When x<0 & x>2a curve does not exists").scale(0.4).next_to(region, DOWN)
        presence = Text("The curve exists in region 0<x<2a").scale(0.4).next_to(curve_exists, DOWN)
        
        self.play(Write(region))
        self.play(Write(curve_exists))
        self.play(Write(presence))

        area_between = Polygon(axes.c2p(0,0), axes.c2p(2*a,0), axes.c2p(2*a,6), axes.c2p(0,6), fill_color=BLUE, fill_opacity=0.5)
        area_below = Polygon(axes.c2p(0,0), axes.c2p(2*a,0), axes.c2p(2*a,-6), axes.c2p(0,-6), fill_color=BLUE, fill_opacity=0.5)
        self.play(FadeIn(area_between), FadeIn(area_below))
        self.wait(0.5)
        self.play(FadeOut(area_between), FadeOut(area_below))
        self.wait(0.5)

        self.play(Unwrite(region))
        self.play(Unwrite(curve_exists))
        self.play(Unwrite(presence))

        self.play(Uncreate(axes))
        self.play(Uncreate(intersection_point),Unwrite(intersection_label))
        self.play(FadeOut(x_axis))
        self.play(Uncreate(x_2a), Unwrite(asymptote_label))
        self.play(question_text.animate.shift(LEFT*3.5))

        def implicit_function(x, y):
            return y**2 * (2 * a - x) - x ** 3
        
        curve = ImplicitFunction(
            implicit_function,
            color=YELLOW)

        axes = Axes(x_range=[-6,6], y_range=[-6,6], axis_config={"color":WHITE})
        self.play(Create(axes))

        intersection_point = Dot(color=RED)
        intersection_label = Tex("(0, 0)").scale(0.4).next_to(intersection_point, DL)
        self.play(Create(intersection_point),Write(intersection_label))

        tangent_POI = Line(start=LEFT * 6, end=RIGHT * 6, color=GREEN)
        tangent_label = Tex("y=0").scale(0.5).next_to(tangent_POI, UL)
        self.play(Create(tangent_POI))

        asymptote = Line(start=DOWN * 6, end=UP * 6, color=RED).shift(RIGHT * 2*a)
        asymptote_label = Tex("x = 2a").scale(0.6).next_to(asymptote, LEFT, buff=0.1).shift(UP * 0.5)
        self.play(Create(asymptote),Create(asymptote_label),run_time = 5)

        self.play(Create(curve), run_time=5) 