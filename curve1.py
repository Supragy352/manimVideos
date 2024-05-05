from manim import *

class PlotCurve(Scene):
    def construct(self):
        # Introduction text
        intro_text = Text("Hello I am Sujal Ravindra Sonawane\nToday we are going to trace a curve using manim\nwhich is python library").scale(0.6).shift(UP)
        question_text = Text("Question is:").scale(0.6)

        # Equation
        equation = MathTex("xy^2 = a^2(a-x)").scale(0.8).shift(DOWN)

        # Add and display intro text, question, and equation
        self.add(intro_text, question_text, equation)
        self.wait(3)
        self.play(FadeOut(intro_text), FadeOut(question_text), FadeOut(equation))

        # Create axes
        axes = Axes(
            x_range=(-5, 5),
            y_range=(-6, 6),
            axis_config={"color": BLUE},
            x_axis_config={
                "numbers_to_include": [],
                "tick_size": 0.05,
            },
            y_axis_config={
                "numbers_to_include": [],
                "tick_size": 0.05,
            },
        )

        # Scale and shift axes
        axes.scale(0.5)  
        axes.shift( RIGHT * 4)
        self.add(axes)
        self.wait(2)

        # Add equation
        equation = MathTex("xy^2 = a^2(a-x)").scale(0.8).to_edge(UP)

        # Add point (a, 0) on the axis
        a_point = Dot(axes.coords_to_point(2, 0), color=RED)
        a_label = MathTex("(a, 0)").next_to(a_point, DOWN)

        # Step 1: Symmetry about x-axis
        step1_text = Text("Step 1: Symmetry  \nAs equation has even power of y\nTherefore, curve is symmetric about x axis").scale(0.4).to_edge(LEFT, UP).shift(UP)
        self.play(Create(axes), Write(equation), run_time=2)
        self.wait()
        self.play(Write(step1_text), run_time=1)
        self.wait(1)

        # Step 2: Point of intersection
        step2_text = Text("Step 2: Point of intersection \n= a(x-a) = 0 \n= x = a \nTherefore, y = 0 \nTherefore, point of intersection is  (a, 0)").scale(0.4).to_edge(LEFT, UP).shift(UP)
        self.wait(2)
        self.play(FadeOut(step1_text), Create(a_point), Write(a_label), run_time=1)
        self.wait(1)
        self.play(Write(step2_text), run_time=1)
        self.wait(1)

        # Step 3: Tangent at (a,0) parallel to y-axis
        step3_text = MathText("Step 3: Tangent \nat  point (a, 0) \ndy/dx at point (a,0) is infinite \nTherefore, tangent at (a,0) is parallel to y-axis").scale(0.4).to_edge(LEFT, UP).shift(UP)
        a = 2
        tangent_line = Line(axes.coords_to_point(a, -3), axes.coords_to_point(a, 3), color=GREEN)
        tangent_line.scale(0.8)
        self.wait(2)
        self.play(FadeOut(step2_text))
        self.wait(1)
        self.play(Write(step3_text), Create(tangent_line), run_time=2)
        self.wait(1)

        # Step 4: x=0 line is an asymptote
        step4_text = Text("Step 4: Asymptote \nequating coeffincient of highest power to zero\nTherefore, x=0 line is an asymptote").scale(0.4).to_edge(LEFT, UP).shift(UP)
        asymptote_line = DashedLine(axes.coords_to_point(0, -3), axes.coords_to_point(0, 3), color=RED)
        asymptote_line.scale(0.8)
        self.wait(2)
        self.play(FadeOut(step3_text))
        self.wait(1)
        self.play(Write(step4_text), Create(asymptote_line), run_time=2)
        self.wait(1)

        # Step 5: Region of absence
        step5_text = Text("Step 5: Region of absence").scale(0.4).to_edge(LEFT, UP).shift(UP)
        equation_text = MathTex("xy^2 = a^2(a-x)").scale(0.8).to_edge(LEFT, UP)
        region_text = Text("Therefore x<0 and x>a \nRegion of absence is x<0 and x>a").scale(0.4).to_edge(LEFT, UP).shift(DOWN)
        step5_text = VGroup(step5_text, equation_text, region_text)

        region_of_absence, region_of_absence_text = self.get_region_of_absence(axes, a)
        region_of_absence.scale(0.8)
        self.play(FadeOut(step4_text))
        self.wait(1)
        self.play(Write(step5_text), Create(region_of_absence), Write(region_of_absence_text), run_time=2)
        self.wait(3)

        # Fade out equation
        FadeOut(equation)
         
        # Final curve
        final_curve = self.get_final_curve(axes, a)
        self.wait(2)
        final_curve_text = Text("Final Curve").scale(0.6).to_edge(LEFT, UP).shift(UP)
        self.play(FadeOut(step5_text), FadeOut(region_of_absence) , FadeOut(region_of_absence_text) )
        self.wait(1)
        self.play(Create(final_curve), Write(final_curve_text), run_time=5)
        self.wait(3)

        self.play(FadeOut(final_curve,a_point,a_label),FadeOut(tangent_line,asymptote_line),FadeOut(axes),FadeOut(final_curve_text),FadeOut(equation))

        # End text
        end_text = Text("Thank you")
        self.add(end_text)
        self.wait(1)

    def get_region_of_absence(self, axes, a):
        # Define coordinates for the shaded region of absence
        region_left = Rectangle(
            width=axes.coords_to_point(-5, 0)[0] - axes.coords_to_point(0, 0)[0],
            height= 5,
            color=YELLOW,
            fill_opacity=0.2,
        ).move_to(axes.coords_to_point(-2.0, 0))

        region_right = Rectangle(
            width=axes.coords_to_point(10, 2)[0] - axes.coords_to_point(7, 0)[0],
            height= 4,
            color=YELLOW,
            fill_opacity=0.2,
        ).move_to(axes.coords_to_point(3.5, 0))

        region_of_absence = VGroup(region_left, region_right)
         
        return region_of_absence 

    def get_final_curve(self, axes, a):
        curve_points_top = []
        curve_points_bottom = []
        for x in np.linspace(0.01, a, 100):  # Start from 0.01 to avoid division by zero
            y = np.sqrt(abs(a**2 * (a - x) / x))
            curve_points_top.append(axes.coords_to_point(x, y))
            curve_points_bottom.append(axes.coords_to_point(x, -y))
        curve_points = curve_points_top + curve_points_bottom[::-1]  # Combine top and bottom points
        curve = VMobject().set_points_smoothly(curve_points)
        curve.set_color(PINK)
        return curve
