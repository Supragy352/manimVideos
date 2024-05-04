from manim import *

class PlotCurve(Scene):
    def construct(self):
        # CONSTANTS
        a = 1

        # The curve equation function
        def curve_equation(x, y):
            return y**2 * (a**2 - x**2) - a**3 * x
        
        # Adjust and write Text
        def adjust_write_Text(Text):

            Text[0].next_to(curve_eqn_text, DR, aligned_edge=LEFT, buff=0.5).shift(DOWN * 1)
            for i in range(1, len(Text)):
                Text[i].next_to(Text[i-1], DOWN, aligned_edge=LEFT, buff=0.3)

        
            for sentence in Text:
                self.play(Write(sentence), run_time=1)

        # Remove Text
        def removeText(Text):

            self.play(*[Unwrite(text_obj) for text_obj in Text], run_time=3, lag_ratio=0.5)
            self.wait()

        # Create the curve equation graph
        curve = ImplicitFunction(
            curve_equation,
            color=YELLOW
        )
        
        #Introduction
        curve_eqn_text = Tex("Trace the curve : $y^2 (a^2 - x^2) = a^3 x$")
        self.play(Write(curve_eqn_text),run_time = 3)

        self.play(
            curve_eqn_text.animate.scale(0.7).shift(UP* 3.2),
            run_time=2
        )


        # Add the axes at the original position
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=6,
            y_length=6,
            axis_config={
            "color": BLUE,
            "include_tip": True,  # Add arrowheads on both sides
            "tip_length": 0.1,    # Adjust the length of the arrowheads
            },
        )

        # Add x and y axis labels
        x_axis_label = Tex("x-axis").scale(0.6)
        x_axis_label.next_to(axes.x_axis.get_end(), DOWN)

        y_axis_label = Tex("y-axis").scale(0.6)
        y_axis_label.next_to(axes.y_axis.get_end(), DL).shift(UP * 0.3)

        self.play(Create(axes), Create(x_axis_label), Create(y_axis_label), run_time=2)

        axis_labels = [x_axis_label, y_axis_label]

        # Define the scaling and shifting parameters
        scale_factor = 0.85  # Scaling factor
        shift_distance = 4  # Distance to shift to the right

        # Animate scaling down and shifting to the side
        self.play(
            axis_labels[0].animate.shift(LEFT * shift_distance),
            axis_labels[1].animate.shift(LEFT * shift_distance),
            axes.animate.scale(scale_factor).shift(LEFT * shift_distance),
            run_time=2
        )

        # Check the Symmetry
        symmetry_texts = [
            Tex("Symmetry :").scale(0.7) ,
            Tex("As the power of $y$ is even and $x$ is odd").scale(0.7) ,
            Tex("Curve is symmetric about the $x$-axis only").scale(0.7)
        ]

        # Adjust Symmetry text position
        adjust_write_Text(symmetry_texts)
        
        # Highlight the x axis to show its symmetry
        original = axes.x_axis.get_color()
        x_axis_color_change = axes.x_axis.animate.set_color(RED)
        self.play(x_axis_color_change, run_time=3)
        self.play(axes.x_axis.animate.set_color(original), run_time=2)

        # Remove the Symmetry text
        removeText(symmetry_texts)
        
        # Point of Intersection
        intersection_texts = [
            Tex("Point of Intersection :").scale(0.7),
            Tex("At $x = 0$, equation becomes").scale(0.7) ,
            Tex("$y^2 (a^2 - x^2) = a^3 x$").scale(0.7),
            Tex("$y^2 (a^2 - 0) = a^3 * 0$").scale(0.7),
            Tex("$y^2 (a^2) = 0$").scale(0.7),
            Tex("$y = 0$").scale(0.7),
            Tex("So the point of intersection is Origin $(0,0)$").scale(0.7)
        ]

        # Setting Text Position
        adjust_write_Text(intersection_texts)
        
        # Draw dot at (0, 0)
        dot = Dot(color=YELLOW)
        dot.move_to(axes.coords_to_point(0, 0))
        dot_label = Tex("$(0, 0)$").scale(0.6)
        dot_label.next_to(dot, UR, buff=0.1)
        self.play(Create(dot),Write(dot_label))

        intersection_texts.append(dot_label)

        # Unwrite the intersection texts
        removeText(intersection_texts)

        # Tangent to POI
        tangent_texts = [
            Tex("Tangent At POI :").scale(0.7) ,
            Tex("Here, the tangent at orign").scale(0.7),
            Tex("Lowest degree term = 0").scale(0.7),
            Tex("$a^3x = 0$").scale(0.7),
            Tex("$x=0$").scale(0.7),
            Tex("Thus the tangent is y-axis").scale(0.7)
        ]

        adjust_write_Text(tangent_texts)

        # Draw tangent line on y-axis
        self.play(FadeOut(dot))
        y_axis_point_bottom = axes.coords_to_point(0, -2)  # Bottom point on y-axis
        y_axis_point_top = axes.coords_to_point(0, 2)  # Top point on y-axis
        tangent_line = Line(y_axis_point_bottom, y_axis_point_top, color=RED)
        tangent_label = Tex("$x = 0$").scale(0.6)
        tangent_label.next_to(tangent_line, UL, buff=0.1)
        self.play(Create(tangent_line),Create(tangent_label))
        self.play(FadeIn(dot))
        
        tangent_texts.append(tangent_label)

        removeText(tangent_texts)


        # Asymptotes Of curves

        asymptote_text_x_axis= [
            Tex("Asymptotes of curve:").scale(0.7),
            Tex("Along x-axis:").scale(0.7),
            Tex("\tCoefficient of highest degree term of x,").scale(0.7),
            Tex("\t$y^2 = 0$").scale(0.7),
            Tex("$y=0$ ").scale(0.7),
            Tex("x-axis is the asymptote").scale(0.7)
        ]

        asymptote_text_y_axis= [
            Tex("Asymptotes of curve:").scale(0.7),
            Tex("Along y-axis:").scale(0.7),
            Tex("\tCoefficient of highest degree term of y,").scale(0.7),
            Tex("\t$x^2 = a^2$").scale(0.7),
            Tex("$x=a$, $x=-a$ are the asymptotes").scale(0.7)
        ]

        adjust_write_Text(asymptote_text_x_axis)

        # Draw asymptote y = 0
        asymptote_bottom = Line(
            axes.coords_to_point(axes.x_range[0], 0),
            axes.coords_to_point(axes.x_range[1], 0),
            color=GREEN
        )

        self.play(FadeOut(dot))
        self.play(Create(asymptote_bottom))
        self.play(FadeIn(dot))


        removeText(asymptote_text_x_axis)

        adjust_write_Text(asymptote_text_y_axis)

        # Draw asymptote x = -a
        asymptote_left = Line(
            axes.coords_to_point(-a, axes.y_range[0]),
            axes.coords_to_point(-a, axes.y_range[1]),
            color=GREEN
        )
        asymptote_left_label = Tex("$x = -a$").scale(0.6)
        asymptote_left_label.next_to(asymptote_left, LEFT).shift(UP * 0.5)
        self.play(Create(asymptote_left),Create(asymptote_left_label))

        # Draw asymptote x = a
        asymptote_right = Line(
            axes.coords_to_point(a, axes.y_range[0]),
            axes.coords_to_point(a, axes.y_range[1]),
            color=GREEN
        )

        asymptote_right_label = Tex("$x = a$").scale(0.6)
        asymptote_right_label.next_to(asymptote_right, RIGHT).shift(UP * 0.5)
        self.play(Create(asymptote_right),Create(asymptote_right_label))

        asymptote_text_y_axis.append(asymptote_left_label)
        asymptote_text_y_axis.append(asymptote_right_label)

        removeText(asymptote_text_y_axis)

        region_texts = [
            Tex("Region :").scale(0.7),
            Tex("When $x < -a$, y is real thus curve exist ").scale(0.7),
            Tex("When $0 < x < a$, y is real thus curve exist ").scale(0.7),
            Tex("Therefore, Region of absence :").scale(0.7),
            Tex("$x \in (-a, 0) \cup (a, \infty)$").scale(0.7)
        ]

        adjust_write_Text(region_texts)

        # Highlight Region of Absence
        region_of_absence_right = Rectangle(
            width=a * (0.85 **3),
            height=(axes.y_range[1] + 2) * 0.85,
            color=BLUE,
            fill_opacity=0.3
        )

        region_of_absence_left = Rectangle(
            width=(axes.y_range[1] - a) * (0.85 **3),
            height=(axes.y_range[1] + 2) * 0.85,
            color=BLUE,
            fill_opacity=0.3
        )

        # Shift the region to the left half of the y-axis range
        region_of_absence_right.shift(axes.coords_to_point(-a / 2, 0))
        region_of_absence_left.shift(axes.coords_to_point((axes.y_range[1]+a)/2,0))

        self.play(Create(region_of_absence_right),Create(region_of_absence_left))
        self.wait(2)
        self.play(FadeOut(region_of_absence_left),FadeOut(region_of_absence_right))
        self.wait(2)

        # Add the curve to the scene
        curve.scale(0.645).shift(LEFT * 2.91)
        self.play(Create(curve),run_time = 4)
        self.wait(2)

        removeText(region_texts)

        to_fade_out = VGroup(
            curve,
            dot,
            tangent_line,
            axes,
            x_axis_label,
            y_axis_label,
            asymptote_bottom,
            asymptote_left,
            asymptote_right,
            curve_eqn_text
        )

        self.play(FadeOut(to_fade_out),run_time = 2)
        
        # Final Result
        new_axes = Axes(

            x_length=11,          
            y_length=7,          
            axis_config={
                "color": BLUE,
                "include_tip": True,
                "tip_length": 0.1,
            },
        )
        # Create a new curve
        new_curve = ImplicitFunction(
            curve_equation,
            color=YELLOW
        )

        new_curve.scale(0.8).shift(RIGHT * 0.62)

        # Add the new axes and curve to the scene
        curve_eqn_text.to_edge(UL)
        self.play(Write(curve_eqn_text))
        self.play(Create(new_axes), run_time=2)
        self.play(Create(new_curve), run_time=5)
        self.wait(3)