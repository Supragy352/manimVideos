from os import linesep
from manim import *
from numpy import array

class WriteText(Scene):
    def construct(self):

        from os import linesep
from manim import *
from manim.utils.color.XKCD import ORANGERED, PIGPINK, REDORANGE
from numpy import array

class WriteText(Scene):
    def construct(self):

        intro = Text("Mitesh  here  from  Manim  Community  MITAOE. Let's  solve  a  Cartesian  Curve  problem  today",
                     font_size=20,
                     color=WHITE,
                    )
        text = Text(
            "Trace the curve: ",
            font_size=25,
            color=GREEN,
        )
        text.shift(0.5 * UP + LEFT * 2)
        formula1 = MathTex(
            "x = (y-1) (y-2) (y-3)",
            font_size=30,
            color=WHITE,
        )
        intro.shift(1.5 * UP + LEFT*0)
        formula1.shift(0.5* UP + RIGHT*1)
        self.play(Write(intro))
        self.wait(1)
        self.play(Write(text))
        self.wait(1)
        self.play(Write(formula1))
        self.wait(1)

    
        self.remove(intro,text)
        self.play(formula1.animate.scale(1).move_to(3 * UP + RIGHT * 0.6))
        self.wait(1)

        curve = Text(
            "Curve Equation : ",
            font_size=25,
           
            color=YELLOW,
        )

        curve.shift(UP * 3 , LEFT * 2.5)
        self.play(Write(curve))
        self.wait(1)
        
        text1 = Text(
            "Solution :",
            font_size=25,
            color=GREEN,
        )
        text1.shift(1.4 * UP + LEFT * 5.99)
        self.play(Write(text1))

        a = 2
        axes = ThreeDAxes(
            x_range=[-7, 7], 
            y_range=[-7, 7], 
            z_range=[-5,5],
            x_axis_config={"numbers_to_include": np.arange(-7, 8, 1)},
            y_axis_config={"numbers_to_include": np.arange(-7, 8, 1)}
        )
        axes.scale(0.45)
        labels = axes.get_axis_labels()
        # self.wait(2)

        axes.shift(0 * DOWN + 4.7 * RIGHT)
        labels.shift(0 * DOWN + 4.7*RIGHT)
        self.add(axes,labels) 
        self.wait(1)
        # self.add(labels)  # Add the axes and labels first
        # self.play(axes.animate.set_opacity(1))  # Animate to make the axes visible
        # self.play(Write(labels[0]))  # Animate to show the x-axis labels
        # self.wait(1)
        # self.play(Write(labels[1]))  # Animate to show the y-axis labels
        # self.wait(2)

        text2 = Text(
            "Symmetry : ",
            font_size=25,
            color=ORANGERED,
        )
        text2.shift(0.8 * UP + LEFT * 4.8)
        self.play(Write(text2))

        text2_a = Text(
            " Curve has no Symmetry",
            font_size=25,
            color=WHITE,
        )
        text2_a.shift(0.8 * UP + LEFT * 2)
        self.play(Write(text2_a))

        text3 = Text(
            "Points of Intersection :",
            font_size=25,
            color=BLUE,
        )
        text3.shift(0.1 * UP + LEFT * 4 )
        self.play(Write(text3))
        self.wait(1)
        formula2 = Text(
            "X-intercept : On putting y = 0 ",
            font_size=25,
            color=WHITE
        )
        formula2.shift(DOWN * 0.5 + LEFT * 1.5)
        self.play(Write(formula2))
        self.wait(1)

        formula2_a = MathTex(
            " \Longrightarrow ",
            font_size=25,
            color=YELLOW
        )
        formula2_a.shift(DOWN * 1 + LEFT * 1.5)
        self.play(Write(formula2_a))
        self.wait(1)

        formula2_b = Text(
            " x = -6",
            font_size=25,
            color=GREEN
        )
        formula2_b.shift(DOWN * 1 + LEFT * 0.25)
        self.play(Write(formula2_b))
        self.wait(1)
        formula3 = Text(
            "Y-intercept : On putting x = 0  ",
            font_size=25,
            color=WHITE
        )
        formula3.shift(DOWN * 1.5, LEFT * 1.45) 
        self.play(Write(formula3))
        self.wait(1)

        formula3_a = MathTex(
            " \Longrightarrow ",
            font_size=25,
            color=YELLOW
        )
        formula3_a.shift(DOWN * 2, LEFT * 1.5) 
        self.play(Write(formula3_a))
        self.wait(1)

        formula3_b = Text(
            " y = 1,2,3 ",
            font_size=25,
            color=GREEN
        )
        formula3_b.shift(DOWN * 2, LEFT * 0.4) 
        self.play(Write(formula3_b))
        self.wait(1)

        text4 = Text(
            "∴ (-6,0), (0,1), (0,2), (0,3) are the points of Intersection",
            font_size=25,
            color=GREEN,
        )
        text4.shift(DOWN * 2.7, LEFT * 1.3)
        self.play(Write(text4))
        self.wait(1)
        self.remove(text1,text2,text2_a,text3,text4,formula2,formula2_a,formula2_b,formula3,formula3_a,formula3_b)

        self.play(curve.animate.scale(1).move_to(3.45 * UP + LEFT * 0.1))
        self.wait(1)
        self.play(formula1.animate.scale(1).move_to(3.45 * UP + RIGHT * 3 ))
        self.wait(1)    

        # Tangents
        text5 = Text(
            "Tangents :  ",
            font_size=25,
            color=BLUE,
        )
        text5.shift(3.2 * UP + LEFT * 5)
        self.play(Write(text5))
        self.wait(1)

        deri = MathTex(
            r"\frac{dy}{dx} = \frac{1}{3y^{2} - 12{y} + 11}",
            font_size=35,
            color=YELLOW
        )
        deri.shift(UP * 2.5 , LEFT * 3) 
        self.play(Write(deri))
        self.wait(1)

        tang1_der = MathTex(
            r"1) \frac{dy}{dx}",
            font_size=25,
            color=RED
        )
        tang1_der.shift(UP * 1.5 , LEFT * 4.5) 
        self.play(Write(tang1_der))
        self.wait(1)

        tang1_a = Text(
            "at (-6 , 0) is +ve",
            font_size=20,
            color=WHITE
        )
        tang1_a.shift(UP * 1.5 , LEFT * 3.2) 
        self.play(Write(tang1_a))
        self.wait(1)

        tang1_b = Text(
            "∴ Tangent will Make 'Acute' angle with x - axis",
            font_size=20,
            color=WHITE
        )
        tang1_b.shift(UP * 0.9 , LEFT * 2) 
        self.play(Write(tang1_b))
        self.wait(1)

        tang2_der = MathTex(
            r"2) \frac{dy}{dx}",
            font_size=25,
            color=RED
        )
        tang2_der.shift(UP * 0.3 , LEFT * 4.5) 
        self.play(Write(tang2_der))
        self.wait(1)

        tang2_a = Text(
            "at (0 , 1) is +ve",
            font_size=20,
            color=WHITE
        )
        tang2_a.shift(UP * 0.3 , LEFT * 3.2) 
        self.play(Write(tang2_a))
        self.wait(1)

        tang2_b= Text(
            "∴ Tangent will Make 'Acute' angle with x - axis",
            font_size=20,
            color=WHITE
        )
        tang2_b.shift(DOWN * 0.25 , LEFT * 2) 
        self.play(Write(tang2_b))
        self.wait(1)

        tang3_der = MathTex(
            r"3) \frac{dy}{dx}",
            font_size=25,
            color=RED
        )
        tang3_der.shift(DOWN * 0.85 , LEFT * 4.5) 
        self.play(Write(tang3_der))
        self.wait(1)

        tang3_a = Text(
            "at (0 , 2) is -ve",
            font_size=20,
            color=WHITE
        )
        tang3_a.shift(DOWN * 0.85 , LEFT * 3.2) 
        self.play(Write(tang3_a))
        self.wait(1)

        tang3_b = Text(
            "∴ Tangent will Make 'Obtuse' angle with x - axis",
            font_size=20,
            color=WHITE
        )
        tang3_b.shift(DOWN * 1.5 , LEFT * 2) 
        self.play(Write(tang3_b))
        self.wait(1)

        tang4_der = MathTex(
            r"4) \frac{dy}{dx}",
            font_size=25,
            color=RED
        )
        tang4_der.shift(DOWN * 2.2 , LEFT * 4.5) 
        self.play(Write(tang4_der))
        self.wait(1)

        tang4_a = Text(
            "at (0 , 3) is +ve",
            font_size=20,
            color=WHITE
        )
        tang4_a.shift(DOWN * 2.2 , LEFT * 3.2) 
        self.play(Write(tang4_a))
        self.wait(1)

        tang4_b= Text(
            "∴ Tangent will Make 'Acute' angle with x - axis",
            font_size=20,
            color=WHITE
        )
        tang4_b.shift(DOWN * 2.73 , LEFT * 2) 
        self.play(Write(tang4_b))

        # Tangents graph
        angles_info = [
            (-6, 0, 0, 0.5),   # (x, y, angle_x, angle_y) - acute angle
            (0, 1, np.pi/4, 0.5),  # acute angle with x-axis
            (0, 2, np.pi/4, -0.5),  # obtuse angle with x-axis
            (0, 3, np.pi/4, 0.5)   # acute angle with x-axis
        ]

        lines = VGroup()
        dots = VGroup()
        labels = VGroup()

        for info in angles_info:
            line = Line(
                axes.c2p(info[0], info[1], 0), 
                axes.c2p(info[0] + np.cos(info[2]), info[1] + np.sin(info[3]), 0), 
                color=BLUE
            )
            lines.add(line)
            # Calculate the center of the line
            line_center = np.mean([line.get_start(), line.get_end()], axis=0)
            # Calculate the shift required to center the line at the specified point
            shift_vector = axes.c2p(info[0], info[1], 0) - line_center
            line.shift(shift_vector)  # Centering the line
            self.play(Create(line))

            dot = Dot(axes.c2p(info[0], info[1], 0), color=RED, radius=0.05)
            dot_label = Tex(f"({info[0]}, {info[1]})", color=WHITE, font_size=12)

            if info[:2] != (-6, 0):  # Check if the point is not (-6, 0)
                dot_label.next_to(dot, RIGHT)  # Position label to the right of the dot
            else:
                dot_label.next_to(dot, UP + RIGHT, buff=0.1)  # Position label just above and to the right of the dot with a slight buffer
            
            dots.add(dot)
            labels.add(dot_label)
            self.play(Create(dot), Write(dot_label))

        self.wait(1)

        self.remove(text5,deri,tang1_a,tang1_b,tang1_der,tang2_der,tang2_a,tang2_b,tang3_a,tang3_b,tang3_der,tang4_a,tang4_der,tang4_b)

        # Asymptote, Region of Absence
        text8 = Text(
            "Asymptote :",
            font_size=25,
            color=WHITE,
        )
        text8.shift(UP * 2, LEFT * 5.3)
        self.play(Write(text8))
        self.wait(1)

        text9 = Text(
            " No Asymptote Parallel to X & Y- axis",
            font_size=25,
            color=YELLOW,
        )
        text9.shift(UP * 2, LEFT * 1.4)
        self.play(Write(text9))
        self.wait(1)

        text10 = Text(
            "Region of Absence : ",
            font_size=25,
            color=WHITE,
        )
        text10.shift(UP * 1  , LEFT * 4.65)
        self.play(Write(text10))
        self.wait(1)

        text11 = Text(
            "Curve exist for all values",
            font_size=25,
            color=REDORANGE,
        )

        text11.shift(UP * 1 , LEFT * 1.15)
        self.play(Write(text11))
        self.wait(1)
        self.clear()

        # self.remove(text8, text9, text10, text11)

        # # Remove tangents lines and labels
        # self.remove(lines, dots, labels)

        # Final Graph
        self.play(formula1.animate.scale(1).move_to(1 * UP , LEFT * 0))
        text12 = Text(
            "Let's Plot the Final Graph",
            font_size=25,
            color=BLUE,
        )
        text12.shift(UP * 2 , LEFT * 0)
        self.play(Write(text12))
        self.wait(1)
        self.remove(text12)

        self.play(formula1.animate.scale(1).move_to(UP *3 + LEFT * 5))

        a = 2
        axes = ThreeDAxes(
            x_range=[-7, 7], 
            y_range=[-7, 7], 
            z_range=[-5,5],
            x_axis_config={"numbers_to_include": np.arange(-7, 8, 1)},
            y_axis_config={"numbers_to_include": np.arange(-7, 8, 1)}
        )
        axes.scale(0.5)
        labels = axes.get_axis_labels()
        self.add(axes, labels)
        self.wait(1)

        line_at_a = DashedLine(axes.c2p(a, -5, -5), axes.c2p(a, 5, 5), color=WHITE)
        line_at_minus_a = DashedLine(axes.c2p(-a, -5, -5), axes.c2p(-a, 5, 5), color=WHITE)

        b1 = Brace(line_at_a)
        b1text = b1.get_text("a")
        b2 = Brace(line_at_minus_a)
        b2text = b2.get_text("-a")

        def Eqn_x(y):
            return ((y-1)*(y-2)*(y-3))

        points = []

        angles_info = [
            (-6, 0, 0, 0.5),   # (x, y, angle_x, angle_y) - acute angle
            (0, 1, np.pi/4, 0.5),  # acute angle with x-axis
            (0, 2, np.pi/4, -0.5),  # obtuse angle with x-axis
            (0, 3, np.pi/4, 0.5)   # acute angle with x-axis
        ]

        graph_1_points = [(Eqn_x(y) , y) for y in np.arange(0, 5, 0.1)]

        graph_1_curve = lambda: VGroup(
            *[Line(axes.coords_to_point(x1, y1), axes.coords_to_point(min(max(x2, axes.x_range[0]), axes.x_range[1]), y2), color=YELLOW)
              for (x1, y1), (x2, y2) in zip(graph_1_points[:-1], graph_1_points[1:])
              if min(max(x1, axes.x_range[0]), axes.x_range[1]) == x1 and min(max(x2, axes.x_range[0]), axes.x_range[1]) == x2]
        )

        graph_curve = graph_1_curve()

        lines = VGroup()
        dots = VGroup()  # Group for dots
        labels = VGroup()  # Group for labels
        for info in angles_info:
            line = Line(
                axes.c2p(info[0], info[1], 0), 
                axes.c2p(info[0] + np.cos(info[2]), info[1] + np.sin(info[3]), 0), 
                color=BLUE
            )
            lines.add(line)
            line_center = np.mean([line.get_start(), line.get_end()], axis=0)
            shift_vector = axes.c2p(info[0], info[1], 0) - line_center
            line.shift(shift_vector)
            self.play(Create(line))
            
            dot = Dot(axes.c2p(info[0], info[1], 0), color=RED, radius=0.05)
            dot_label = Tex(f"({info[0]}, {info[1]})", color=WHITE, font_size=12)
            if info[:2] != (-6, 0):
                dot_label.next_to(dot, RIGHT)
            else:
                dot_label.next_to(dot, UP + RIGHT, buff=0.1)
            dots.add(dot)
            labels.add(dot_label)
            self.play(Create(dot), Write(dot_label))

        self.play(Create(graph_curve))
        self.play(graph_curve.animate.shift(2 * OUT))

        self.wait(2)
