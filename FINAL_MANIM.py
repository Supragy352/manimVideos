from manim import *

class ManimCELogo(Scene):
    def construct(self):
        # Sovling Equation ka TEXT


        # ***********************INTRO************************
        intro = Text(" Problem on Cartesian Curves ",
            font_size=40,
            font="Arial",
             color= BLUE
            )
        text = Text(
            "Question:",
            font_size=30,
            font="Arial",
            color= BLUE
            )
        text.shift(0.5 * UP + LEFT * 2.75)
        formula1 = MathTex(
            "x^{2} y^{2} = a^{2}(y^{2}- x^{2})  ",
            font_size=40,
            # font="Arial",
            color= WHITE,
            )
        intro.shift(1.5 * UP + LEFT*0.2)
        formula1.shift(0.5 * UP + RIGHT * 0)
        self.play(
            Write(intro)
            )
        self.wait(1)
        self.play(Write(text))
        self.wait(1)
        self.play(Write(formula1))
        self.wait(1)

        lets_text = Text(
            "Let's Solve It",
            font_size=30,
            font="Arial",
            color= RED
            )
        lets_text.shift(0.5 * DOWN + LEFT * 0.5)
        self.play(Write(lets_text))
        self.wait(1)

        self.remove(lets_text,intro,text)
        self.play(formula1.animate.scale(1).move_to(3 * UP + LEFT * 0))
        self.wait(1)

        # ***********************SYYMENTRY************************



        text1 = Text(
            "Solution :",
            font_size=30,
            font="Arial",
            color= RED,
            )
        text1.shift(2 * UP + LEFT *6)
        self.play(Write(text1))

        a = 2
        axes = ThreeDAxes(x_range=[-5, 5], y_range=[-5, 5], z_range=[-5,5],x_axis_config={"numbers_to_include": []},y_axis_config={"numbers_to_include": []})
        axes.scale(0.3)
        labels = axes.get_axis_labels()

        axes.shift(2.15 * DOWN + 4.3 * RIGHT)
        labels.shift(2.15 * DOWN + 4.3 * RIGHT)

        self.add(axes,labels)
        self.wait(2)

        text2 = Text(
            "1) Symmetry :",
            font_size=30,
            font="Arial",
            color= BLUE,
            )
        text2.shift(1.25 * UP + LEFT * 5.5)
        self.play(Write(text2))
        self.wait(1)

        text2_b = Text(
            "About X-axis , Y-axis and Opposite Quadrant",
            font_size=23,
            font="Arial",
            color= WHITE,
            )
        text2_b.shift(0.5* UP + LEFT * 3)
        self.play(Write(text2_b))
        self.wait(1)

        # Adding blue lines for y=0 and x=0
        line_y_equals_0 = Line(start=axes.coords_to_point(-5, 0), end=axes.coords_to_point(5, 0), color=BLUE)
        line_x_equals_0 = Line(start=axes.coords_to_point(0, -5), end=axes.coords_to_point(0, 5), color=BLUE)

        self.play(Create(line_y_equals_0), Create(line_x_equals_0))
        # self.add(axes, labels)  # Add axes and labels after animation for smoother appearance
        self.wait(2)

        label_symmetry_x = Tex("Symmetry", color=WHITE, font_size=18)
        label_symmetry_x.next_to(axes.get_x_axis(), RIGHT, buff=SMALL_BUFF)  # Position label to the right of x-axis

        label_symmetry_y = Tex("Symmetry", color=WHITE, font_size=18)
        label_symmetry_y.next_to(axes.get_y_axis(), DOWN, buff=SMALL_BUFF)

        self.play(Create(label_symmetry_x), Create(label_symmetry_y))
        self.wait(1)


        text3 = Text(
            "2) Point of Intersection :",
            font_size=30,
            font="Arial",
            color= BLUE,
            )
        text3.shift( 0.25*DOWN + LEFT * 4.7)
        self.play(Write(text3))
        self.wait(1)
        formula2 = MathTex(
            "x = 0 \Rightarrow 0 = a^{2}(y^{2} - 0) ",
            font_size = 35,
            color= WHITE
            )
        formula2.shift(DOWN * 0.8 + LEFT * 3.25)
        self.play(Write(formula2))
        self.wait(1)
        formula4 = MathTex(
            r"\therefore y = 0",
            font_size = 35,
            color= WHITE
            )
        formula4.shift(DOWN * 1.3 + LEFT * 3.25)
        self.play(Write(formula4))
        self.wait(1)
        formula3 = MathTex(
            "y = 0 \Rightarrow 0 = a^{2}(0 - x^{2})",
            font_size = 35,
            color= WHITE
            )
        formula3.shift(DOWN * 1.8, LEFT * 3.25) 
        self.play(Write(formula3))
        self.wait(1)
        formula5 = MathTex(
            r"\therefore x = 0 ",
            font_size = 35,
            color= WHITE
            )
        formula5.shift(DOWN * 2.3, LEFT * 3.25) 
        self.play(Write(formula5))
        self.wait(1)

        text4 = Text(
            "(0,0) Origin is the only point of Intersection",
            font_size=23,
            font="Arial",
            color= WHITE,
            )
        text4.shift(DOWN * 3 ,LEFT *2.5)
        self.play(Write(text4))
        self.wait(1)

        #GLOWING the origin
        origin_dot = Dot(color=RED, radius=0.1)
        origin_dot.move_to(axes.coords_to_point(0, 0))

        self.play(Create(origin_dot))
        self.wait(1)

        self.remove(formula2,formula3,formula4,formula5,text1,text2,text2_b,text3,text4)

        #************************TANGENT****************************************

        text_t = Text(
            "3) Tangets :",
            font_size=30,
            font="Arial",
            color= BLUE,
            )
        text_t.shift(2.5 * UP, LEFT * 6 )
        self.play(Write(text_t))
        self.wait(1)

        text5 = Text(
            "At (0,0) : Equating the Lowest Degree Term to Zero we get",
            font_size=23,
            font="Arial",
            color= WHITE,
            )
        text5.shift(2 * UP, LEFT * 2)
        self.play(Write(text5))
        self.wait(1)

        formula6 = MathTex(
            "\Rightarrow -a^{2}(y^{2} - x^{2}) = 0 ",
            font_size = 35,
            color= WHITE
            )
        formula6.shift(UP * 1.5 , LEFT * 2.5 ) 
        self.play(Write(formula6))
        self.wait(1)
        formula7 = MathTex(
            "\Rightarrow y^{2} = x^{2} ",
            font_size = 35,
            color= WHITE
            )
        formula7.shift(UP * 1, LEFT * 3.275)  
        self.play(Write(formula7))
        self.wait(1)
        text6 = MathTex(
            "\Rightarrow y = \pm x",
            font_size=35,
            # font="Arial",
            color= WHITE,
            )
        text6.shift(UP * 0.5, LEFT * 3.275)
        self.play(Write(text6))
        self.wait(1)
        text7 = Text(
            "There exist two real Tangets at (0,0)",
            font_size=20,
            font="Arial",
            color= WHITE,
            )
        text7.shift(UP * 0, LEFT * 2.5)
        self.play(Write(text7))
        self.wait(1)

        #Tangent
        def Tan1_Equn(x):
            y = x
            return y

        def Tan2_Equn(x):
            y = -x
            return y

        Tangent_1_points = [(x , Tan1_Equn(x)) for x in np.arange(-5, 5, 0.1)]
        Tangent_2_points = [(x , Tan2_Equn(x)) for x in np.arange(-5, 5, 0.1)]

        Tangent_1_curve = VGroup(
            *[DashedLine(axes.coords_to_point(x1, y1), axes.coords_to_point(x2, y2), color=WHITE)
              for (x1, y1), (x2, y2) in zip(Tangent_1_points[:-1], Tangent_1_points[1:])]
        )

        Tangent_2_curve = VGroup(
            *[DashedLine(axes.coords_to_point(x1, y1), axes.coords_to_point(x2, y2), color=WHITE)
              for (x1, y1), (x2, y2) in zip(Tangent_2_points[:-1], Tangent_2_points[1:])]
        )

        tangent_text1 = Text("Tangent", color=WHITE ,font_size=14).next_to(Tangent_1_curve[-1], UP,buff=SMALL_BUFF)
        tangent_text2 = Text("Tangent", color=WHITE, font_size=14).next_to(Tangent_2_curve[-1], UP,buff=SMALL_BUFF).shift(0.5*DOWN) 

        self.play(Create(Tangent_1_curve),Create(Tangent_2_curve))
        self.play(Write(tangent_text1), Write(tangent_text2))
        self.wait(1)



        # *****************ASSYMPTOTE***********

        text8 = Text(
            "4) Asymptote :",
            font_size=30,
            font="Arial",
            color= BLUE,
            )
        text8.shift(DOWN * 1, LEFT * 5.5)
        self.play(Write(text8))
        self.wait(1)

        text9 = Text(
            " are Asymptote Parallel to Y-axis",
            font_size=23,
            font="Arial",
            color= WHITE,
            )
        formula8 = MathTex(
            " x = \pm a ",
            font_size = 35,
            color= WHITE
            )
        formula8.shift(DOWN * 1.75, LEFT * 5.5)   
        self.play(Write(formula8))
        text9.shift(DOWN * 1.75, LEFT * 2.2)
        self.play(Write(text9))
        self.wait(1)

        text10 = Text(
            " No Asymptote Parallel to X-axis",
            font_size=23,
            font="Arial",
            color= WHITE,
            )
        formula9 = MathTex(
            " y^{2} =-a^{2} ",
            font_size = 35,
            color= WHITE
            )
        formula9.shift(DOWN *2.25, LEFT * 5.4)   
        self.play(Write(formula9))
        text10.shift(DOWN *2.25, LEFT * 2)
        self.play(Write(text10))
        self.wait(1)

        #Lines At a And -a

        line_at_a = DashedLine(axes.c2p(a, -5, -5), axes.c2p(a, 5, 5), color=WHITE)
        line_at_minus_a = DashedLine(axes.c2p(-a, -5, -5), axes.c2p(-a, 5, 5), color=WHITE)
        self.wait(1)


        b1 = Brace(line_at_a)
        b1text = b1.get_text("a")
        b2 = Brace(line_at_minus_a)
        b2text = b2.get_text("-a")


        # Add labels for asymptotes with reduced text size
        label_asymptote_a = Tex("asymptote", color=WHITE, font_size=18)
        label_asymptote_a.next_to(line_at_a, UP, buff=SMALL_BUFF)  # Position label above the line

        label_asymptote_minus_a = Tex("asymptote", color=WHITE, font_size=18)
        label_asymptote_minus_a.next_to(line_at_minus_a, UP, buff=SMALL_BUFF)  # Position label above the line
        

        self.wait(1)

        self.play(
            Create(line_at_a), Create(line_at_minus_a),
            Create(label_asymptote_a), Create(label_asymptote_minus_a),
            Create(label_symmetry_x), Create(label_symmetry_y)
        )

        self.wait(1)

        # Red Line With asymptote
        line_at_right_y = DashedLine(axes.c2p(2.2,4 ,4), axes.c2p(2.2, 5, 5), color=RED)
        line_at_minus_right_y = DashedLine(axes.c2p(2.2,-4 ,-4), axes.c2p(2.2, -5, -5), color=RED)

        line_at_right_y2 = Line(axes.c2p(1.8,4 ,4), axes.c2p(1.8, 5, 5), color=RED)
        line_at_minus_right_y2 = Line(axes.c2p(1.8,-4 ,-4), axes.c2p(1.8, -5, -5), color=RED)

        line_at_left_y = DashedLine(axes.c2p(-2.2,4 ,4), axes.c2p(-2.2, 5, 5), color=RED)
        line_at_minus_left_y = DashedLine(axes.c2p(-2.2,-4 ,-4), axes.c2p(-2.2, -5, -5), color=RED)

        line_at_left_y2 = Line(axes.c2p(-1.8,4 ,4), axes.c2p(-1.8, 5, 5), color=RED)
        line_at_minus_left_y2 = Line(axes.c2p(-1.8,-4 ,-4), axes.c2p(-1.8, -5, -5), color=RED)
        
        self.play(Create(line_at_right_y),Create(line_at_left_y),Create(line_at_right_y2),Create(line_at_left_y2),Create(line_at_minus_right_y),Create(line_at_minus_right_y2),Create(line_at_minus_left_y),Create(line_at_minus_left_y2))
        self.wait(2)
        # self.clear(intro,text5,text6,text7,text8,text9,text10,)
        self.remove(text5,text_t, text6, text7, text8, text9, text10,formula6,formula7,formula8,formula9)




        # ***********************ROA************************

        text11 = Text(
            "5) Region of Absence : ",
            font_size=30,
            font="Arial",
            color= BLUE,
            )
        text11.shift(UP * 2.5  , LEFT * 4.8)
        self.play(Write(text11))
        self.wait(1)

        formula10 = MathTex(
            r"x^{2} = \frac{a^{2}y^{2}}{a^{2}+y^{2}} ",
            font_size = 35,
            color= WHITE
            )
        formula10.shift(UP * 1.5 , LEFT * 4) 
        self.play(Write(formula10))
        self.wait(1)

        text12 = Text(
            "For Any Value of y, ",
            font_size=23,
            font="Arial",
            color= WHITE,
            )

        text12.shift(UP * 0.5 , LEFT * 3.8)
        self.play(Write(text12))
        self.wait(1)

        text12_b = MathTex(
            " x^{2} ",
            font_size=35,
            # font="Arial",
            color= WHITE,
            )

        text12_b.shift(UP * 0.55 , LEFT * 2.1)
        self.play(Write(text12_b))
        self.wait(1)

        text12_c = Text(
            " is possitive ",
            font_size=23,
            font="Arial",
            color= WHITE,
            )

        text12_c.shift(UP * 0.5 , LEFT * 1.1)
        self.play(Write(text12_c))
        self.wait(1)

        text13 = Text(
            "Hence,No Region Of Absence For x",
            font_size=23,
            font="Arial",
            color= WHITE,
            )

        text13.shift(0*DOWN, LEFT * 2.5)
        self.play(Write(text13))
        self.wait(1)

        formula11 = MathTex(
            r"y^{2}= \frac{a^{2}x^{2}}{a^{2}-x^{2}} ",
            font_size = 35,
            color= WHITE
            )
        formula11.shift(DOWN* 1 , LEFT * 4) 
        self.play(Write(formula11))
        self.wait(1)

        formula12 = MathTex(
            "y^{2} ",
            font_size = 35,
            color= WHITE
            )
        formula12.shift(DOWN * 1.95 , LEFT * 4.9) 
        self.play(Write(formula12))
        self.wait(1)

        text14 = Text(
            "is -ve, When : ",
            font_size=23,
            font="Arial",
            color= WHITE,
            )
        text14.shift(DOWN * 2 , LEFT * 3.5)
        self.play(Write(text14))
        self.wait(1)

        formula13 = MathTex(
            "x^{2} < a^{2}",
            font_size = 35,
            color= WHITE
            )
        formula13.shift(DOWN * 1.95 , LEFT * 1.8) 
        self.play(Write(formula13))
        self.wait(1)

        text15 = Text(
            "Region of Absence is : ",
            font_size=23,
            font="Arial",
            color= WHITE,
            )
        text15.shift(DOWN * 2.5 , LEFT * 3.4)
        self.play(Write(text15))
        self.wait(1)

        text15_b = Text(
            " x > a And x < -a ",
            font_size=23,
            font="Arial",
            color= RED,
            )
        text15_b.shift(DOWN * 2.45 , LEFT * 0.4)
        self.play(Write(text15_b))
        self.wait(1)
        #ROA label
        label_ROA_4 = Text("ROA", color=BLUE, font_size=16)
        label_ROA_4.next_to(axes.coords_to_point(4, 0), UP, buff=SMALL_BUFF)

        label_ROA_minus_4 = Text("ROA", color=BLUE, font_size=16)
        label_ROA_minus_4.next_to(axes.coords_to_point(-4, 0), UP, buff=SMALL_BUFF)

        self.play(Write(label_ROA_4), Write(label_ROA_minus_4))
        self.wait(1)


        self.remove(text11,text12,text13,text14,text15,text15_b,text12_b,text12_c,formula10,formula11,formula12,formula13,axes)
        self.remove(line_at_right_y,line_at_minus_right_y,line_at_left_y,line_at_minus_left_y,line_at_right_y2,line_at_minus_right_y2,line_at_left_y2,line_at_minus_left_y2)
        self.remove(label_asymptote_a,label_asymptote_minus_a,line_at_minus_a,line_at_a,tangent_text1,tangent_text2,Tangent_1_curve,Tangent_2_curve,origin_dot)
        self.remove(label_symmetry_x,label_symmetry_y,line_y_equals_0,line_x_equals_0,labels,label_ROA_minus_4,label_ROA_4)


        self.play(formula1.animate.scale(1).move_to(1 * UP , LEFT * 0))
        text16 = Text(
            "Let's Plot The Final Graph ",
            font_size=25,
            font="Arial",
            color= RED,
            )
        text16.shift(DOWN*0 , LEFT * 0)
        self.play(Write(text16))
        self.wait(2)

        self.remove(text16)
        self.play(formula1.animate.scale(1).move_to(UP *3 + LEFT * 5))

        # ******************PLoTING GRAPH******************


        a = 2
        axes = ThreeDAxes(x_range=[-5, 5], y_range=[-5, 5], z_range=[-5,5],x_axis_config={"numbers_to_include": []},y_axis_config={"numbers_to_include": []})
        axes.scale(0.5)
        labels = axes.get_axis_labels()

        self.add(axes,labels)
        self.wait(2)


        #Tangent
        def Tan1_Equn(x):
            y = x
            return y

        def Tan2_Equn(x):
            y = -x
            return y

        Tangent_1_points = [(x , Tan1_Equn(x)) for x in np.arange(-5, 5, 0.1)]
        Tangent_2_points = [(x , Tan2_Equn(x)) for x in np.arange(-5, 5, 0.1)]

        Tangent_1_curve = VGroup(
            *[DashedLine(axes.coords_to_point(x1, y1), axes.coords_to_point(x2, y2), color=WHITE)
              for (x1, y1), (x2, y2) in zip(Tangent_1_points[:-1], Tangent_1_points[1:])]
        )

        Tangent_2_curve = VGroup(
            *[DashedLine(axes.coords_to_point(x1, y1), axes.coords_to_point(x2, y2), color=WHITE)
              for (x1, y1), (x2, y2) in zip(Tangent_2_points[:-1], Tangent_2_points[1:])]
        )

        tangent_text1 = Text("Tangent", color=WHITE ,font_size=14).next_to(Tangent_1_curve[-1], UP,buff=SMALL_BUFF)
        tangent_text2 = Text("Tangent", color=WHITE, font_size=14).next_to(Tangent_2_curve[-1], UP,buff=SMALL_BUFF).shift(0.5*DOWN) 

        self.play(Create(Tangent_1_curve),Create(Tangent_2_curve))
        self.play(Write(tangent_text1), Write(tangent_text2))


        #Lines At a And -a

        line_at_a = DashedLine(axes.c2p(a, -5, -5), axes.c2p(a, 5, 5), color=WHITE)
        line_at_minus_a = DashedLine(axes.c2p(-a, -5, -5), axes.c2p(-a, 5, 5), color=WHITE)
        self.wait(2)


        b1 = Brace(line_at_a)
        b1text = b1.get_text("a")
        b2 = Brace(line_at_minus_a)
        b2text = b2.get_text("-a")


        # Add labels for asymptotes with reduced text size
        label_asymptote_a = Tex("asymptote", color=WHITE, font_size=18)
        label_asymptote_a.next_to(line_at_a, UP, buff=SMALL_BUFF)  # Position label above the line

        label_asymptote_minus_a = Tex("asymptote", color=WHITE, font_size=18)
        label_asymptote_minus_a.next_to(line_at_minus_a, UP, buff=SMALL_BUFF)  # Position label above the line
        

        # Add labels for symmetry
        label_symmetry_x = Tex("Symmetry", color=WHITE, font_size=18)
        label_symmetry_x.next_to(axes.get_x_axis(), RIGHT, buff=SMALL_BUFF)  # Position label to the right of x-axis

        label_symmetry_y = Tex("Symmetry", color=WHITE, font_size=18)
        label_symmetry_y.next_to(axes.get_y_axis(), DOWN, buff=SMALL_BUFF)  # Position label at the bottom of y-axis

        self.wait(3)

        self.play(
            Create(line_at_a), Create(line_at_minus_a),
            Create(label_asymptote_a), Create(label_asymptote_minus_a),
            Create(label_symmetry_x), Create(label_symmetry_y)
        )

        self.wait(3)

        # Red Line With asymptote
        line_at_right_y = DashedLine(axes.c2p(2.2,4 ,4), axes.c2p(2.2, 5, 5), color=RED)
        line_at_minus_right_y = DashedLine(axes.c2p(2.2,-4 ,-4), axes.c2p(2.2, -5, -5), color=RED)

        line_at_right_y2 = Line(axes.c2p(1.8,4 ,4), axes.c2p(1.8, 5, 5), color=RED)
        line_at_minus_right_y2 = Line(axes.c2p(1.8,-4 ,-4), axes.c2p(1.8, -5, -5), color=RED)

        line_at_left_y = DashedLine(axes.c2p(-2.2,4 ,4), axes.c2p(-2.2, 5, 5), color=RED)
        line_at_minus_left_y = DashedLine(axes.c2p(-2.2,-4 ,-4), axes.c2p(-2.2, -5, -5), color=RED)

        line_at_left_y2 = Line(axes.c2p(-1.8,4 ,4), axes.c2p(-1.8, 5, 5), color=RED)
        line_at_minus_left_y2 = Line(axes.c2p(-1.8,-4 ,-4), axes.c2p(-1.8, -5, -5), color=RED)
        
        self.play(Create(line_at_right_y),Create(line_at_left_y),Create(line_at_right_y2),Create(line_at_left_y2),Create(line_at_minus_right_y),Create(line_at_minus_right_y2),Create(line_at_minus_left_y),Create(line_at_minus_left_y2))
        self.wait(1)

        #ROA Label

        label_ROA_4 = Text("ROA", color=BLUE, font_size=18)
        label_ROA_4.next_to(axes.coords_to_point(4, 0), UP, buff=SMALL_BUFF)

        label_ROA_minus_4 = Text("ROA", color=BLUE, font_size=18)
        label_ROA_minus_4.next_to(axes.coords_to_point(-4, 0), UP, buff=SMALL_BUFF)

        self.play(Write(label_ROA_4), Write(label_ROA_minus_4))
        self.wait(1)


        #Defining the equation of y
        def Eqn_y(x,a):
            return (a*x /(np.sqrt((a*a) - (x*x))))


        points = []

        graph_1_points = [(x , Eqn_y(x,a)) for x in np.arange(0, 5, 0.1)]
        graph_1_neg_points = [(x , -Eqn_y(x,a)) for x in np.arange(0, 5, 0.1)]

        graph_1_curve = VGroup(
            *[Line(axes.coords_to_point(x1, y1), axes.coords_to_point(x2, y2), color=GREEN)
              for (x1, y1), (x2, y2) in zip(graph_1_points[:-1], graph_1_points[1:])]
        )

        graph_1_neg_curve = VGroup(
            *[Line(axes.coords_to_point(x1, y1), axes.coords_to_point(x2, y2), color=GREEN)
              for (x1, y1), (x2, y2) in zip(graph_1_neg_points[:-1], graph_1_neg_points[1:])]
        )


        graph_2_points = [(-x , y) for x,y in graph_1_points]
        graph_2_neg_points = [(-x ,y) for x,y in graph_1_neg_points]

        graph_2_curve = VGroup(
            *[Line(axes.coords_to_point(x1, y1), axes.coords_to_point(x2, y2), color=GREEN)
              for (x1, y1), (x2, y2) in zip(graph_2_points[:-1], graph_2_points[1:])]
        )

        graph_2_neg_curve = VGroup(
            *[Line(axes.coords_to_point(x1, y1), axes.coords_to_point(x2, y2), color=GREEN)
              for (x1, y1), (x2, y2) in zip(graph_2_neg_points[:-1], graph_2_neg_points[1:])]
        )
        self.wait(1)

        self.play(Create(graph_1_curve),Create(graph_1_neg_curve) ,Create(graph_2_curve),Create(graph_2_neg_curve))
        self.wait(3)




