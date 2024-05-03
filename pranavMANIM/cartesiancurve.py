
from manim import *
from manim.utils.color.X11 import LIGHTBLUE
from manim.utils.color.XKCD import FLUORESCENTGREEN
from numpy import array, square

class CartesianCurve(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
        self.clear()

        plane = Axes(x_range=(-5,5), y_range=(-5,5))
        c = Circle(radius= 0.2 , color= RED , fill_opacity = 0.1)
        line1 = DoubleArrow(start=array([1.0 , -3.9 , 0.0]), end=array([1.0 , 3.9 , 0.0]), color= RED)
        line2 = DoubleArrow(start=array([-1.0 , -3.9 , 0.0]), end=array([-1.0 , 3.9 , 0.0]), color= RED)
        line3 = DoubleArrow(start=array([-5.9 , 0.5 , 0.0]), end=array([5.9 ,0.5 , 0.0]), color= RED)
        line4 = DoubleArrow(start=array([-5.9 , -0.5 , 0.0]), end=array([5.9 , -0.5 , 0.0]), color= RED)
        curve = ImplicitFunction(lambda x, y: (x ** 2 - 1 ** 2) * (y ** 2 - 1 ** 2)  - (1 ** 2)*(1 ** 2))
        graph = VGroup(plane,curve,line1,line2,line3,line4,c).scale(0.43).shift(RIGHT * 4.5 + DOWN * 1.5)

        intro = Text("This is Pranav from Manim Community MITAOE and Today we are going to solve a problem on Cartesian Curves",
            font_size=20,
            font="Calabri Light",
            color=BLUE
            )
        text = Text(
            "Trace the following curve:",
            font_size=30,
            font="Arial",
            color= LIGHTBLUE,
            )
        text.shift(2 * UP + LEFT * 4.7)
        formula1 = MathTex(
            "(x^{2} - a^{2})(y^{2}- b^{2}) = a^{2}b^{2}",
            font_size=30,
            color= WHITE,
            )
        intro.shift(3 * UP + LEFT*0.2)
        formula1.shift(2 * UP)
        self.play(
            FadeIn(intro), Circumscribe(intro,Rectangle)
            )
        self.play(ApplyWave(text))
        self.play(FadeIn(formula1))
        self.wait(1)
        text1 = Text(
            "Solution :",
            font_size=30,
            font="Arial",
            color= RED,
            )
        text1.shift(1.4 * UP + LEFT * 6.18)
        self.play(Write(text1),Create(plane, run_time = 3))
        text2 = Text(
            "Symmetry: About X-axis , Y-axis and Origin",
            font_size=25,
            font="Arial",
            color= GREEN,
            )
        text2.shift(0.8 * UP + LEFT * 3.4)
        self.play(Write(text2))
        text3 = Text(
            "Point of Intersection :\n\n X-Intercept :",
            font_size=25,
            font="Arial",
            color= LIGHTBLUE,
            )
        text3.shift( LEFT * 5.05 )
        self.play(Write(text3))
    
        formula2 = MathTex(
            "y = 0 \Longrightarrow -b^{2}x^{2}+a^{2}b^{2} = a^{2}b^{2",
            font_size = 35,
            color= WHITE
            )
        formula2.shift(DOWN * 0.25 + LEFT * 2.2)
        self.play(Write(formula2))

        formula4 = MathTex(
            "\Longrightarrow x = 0",
            font_size = 35,
            color= WHITE
            )
        formula4.shift(DOWN * 0.8 + LEFT * 2.9)
        self.play(Write(formula4))
        text69 = Text("Y-Intercept :",
            font_size=25,
            font="Arial",
            color= LIGHTBLUE
            )
        text69.shift(DOWN * 1.3 , LEFT * 5.75)
        self.play(Write(text69))

        formula3 = MathTex(
            "x = 0 \Longrightarrow -a^{2}y^{2} + a^{2}b^{2} = a^{2}b^{2}  ",
            font_size = 35,
            color= WHITE
            )
        formula3.shift(DOWN * 1.25, LEFT * 2.2) 
        self.play(Write(formula3))

        formula5 = MathTex(
            "\Longrightarrow y = 0  ",
            font_size = 35,
            color= WHITE
            )
        formula5.shift(DOWN * 1.9, LEFT * 2.9) 
        self.play(Write(formula5))
        text4 = Text(
            "(0,0) is the only point of Intersection",
            font_size=30,
            font="Arial",
            color= WHITE,
            )
        text05 = Text("(0,0)",
            font_size= 15,
            color= RED,
            )
        text05.shift(DOWN * 1.7 , RIGHT * 4.9)
        text4.shift(DOWN * 3 , LEFT * 3.3)
        self.play(Write(text4),Create(c , run_time = 2),FadeIn(text05))
        self.wait()
        self.clear()
        self.play(FadeIn(plane),FadeIn(c))
       


        text5 = Text(
            "Tangents :  \n \n At (0,0): Equating the Lowest Degree Term to Zero we get",
            font_size=25,
            font="Arial",
            color= LIGHTBLUE,
            )
        text5.shift(3.2 * UP + LEFT * 2.5)
        self.play(Write(text5))
        formula6 = MathTex(
            "\Longrightarrow-b^{2}x^{2} - a^{2}y^{2} = 0 ",
            font_size = 35,
            color= WHITE
            )
        formula6.shift(UP * 2.2 , LEFT * 4.5 ) 
        self.play(Write(formula6))
        formula7 = MathTex(
            "\Longrightarrow y^{2} = -x^{2} ",
            font_size = 35,
            color= WHITE
            )
        formula7.shift(UP * 1.7, LEFT * 5.15)  
        self.play(Write(formula7))
        text6 = Text(
            "y is Imaginary",
            font_size=28,
            font="Arial",
            color= WHITE,
            )
        text6.shift(UP * 1.1, LEFT * 5)
        self.play(Write(text6))
        
        text7 = Text(
            "=> There exist no real Tangets at (0,0). ∴(0,0) is an Isolated Point",
            font_size=25,
            font="Arial",
            color= YELLOW,
            )
        text7.shift(UP * 0.5, LEFT * 1.9)
        self.play(Write(text7))
        self.wait()
        text06=Text("(0,0) Isolated Point",
            font_size=15,
            font='Arial',
            color=RED
            )
        text06.shift(DOWN * 1.7 , RIGHT * 5.3)
        self.play(FadeIn(text06, runtime=3))
        self.wait()
        self.play(FadeOut(text06,runtime=3))





        text8 = Text(
            "Asymptote :",
            font_size=25,
            font="Arial",
            color= LIGHTBLUE,
            )
        text8.shift(LEFT * 6.2, DOWN * 0.2)
        self.play(Write(text8))

        text9 = Text(
            " are Asymptote Parallel to Y-axis",
            font_size=25,
            font="Arial",
            color= WHITE,
            )
        formula8 = MathTex(
            " x = \pm a ",
            font_size = 40,
            color= RED
            )
        formula8.shift(DOWN * 0.8, LEFT * 6)   
        self.play(Write(formula8))
        text9.shift(DOWN * 0.85, LEFT * 2.7)
        self.play(Write(text9))

        text10 = Text(
            " are Asymptote Parallel to X-axis",
            font_size=25,
            font="Arial",
            color= WHITE,
            )
        formula9 = MathTex(
            " y = \pm b ",
            font_size = 40,
            color= RED
            )
        formula9.shift(DOWN * 1.4, LEFT * 6)   
        self.play(Write(formula9))
        text10.shift(DOWN * 1.4, LEFT * 2.7)
        self.play(Write(text10))
        text01= Text("x = a",font_size=15)
        text02= Text("x = -a",font_size=15)
        text03= Text("y = b",font_size=15)
        text04= Text("y = -b",font_size=15)
        text01.shift(DOWN * 0.1 , RIGHT * 5.35)
        text02.shift(DOWN * 0.1 , RIGHT * 3.65)
        text03.shift(DOWN * 1 , RIGHT * 6.5)
        text04.shift(DOWN * 2 , RIGHT * 6.5)



        self.play(Create(line1,run_time=2),Create(line2,run_time=2),Write(text01),Write(text02))
        self.play(Create(line3,run_time=2),Create(line4,run_time=2),Write(text03),Write(text04))
        self.play(FadeOut(text01),FadeOut(text02),FadeOut(text03),FadeOut(text04))
        self.wait()
        self.clear()
        text11 = Text(
            "Plotting the Graph to understand the Region of Absence : ",
            font_size=30,
            font="Arial",
            color= LIGHTBLUE,
            )
        text11.shift(UP * 3.2 , LEFT * 1.6)
        self.play(Write(text11))
        self.play(FadeIn(plane,c,line1,line2,line3,line4))
        self.play(Create(curve,run_time=3))

        text13 = Text(
            "Region of Absence : ",
            font_size=30,
            font="Arial",
            color= LIGHTBLUE,
            )
        text13.shift(UP * 2.6  , LEFT * 5.1)
        self.play(Write(text13))
        formula11 = MathTex(
            r"x^{2}=\frac{a^{2} + (a^{2}b^{2})}{(y^{2}-b^{2})}",
            font_size = 40,
            color= WHITE
            )
        formula11.shift(UP * 1.7 , LEFT * 4.75) 
        self.play(Write(formula11))

        formula12 = MathTex(
            "\Longrightarrow y < -b : x^{2} ",
            font_size = 35,
            color= WHITE
            )
        formula12.shift(UP * 0.8 , LEFT * 5.6 ) 
        text14 = Text(
            "is +ve => Curve exists ",
            font_size=25,
            font="Arial",
            color= WHITE,
            )

        text14.shift(UP * 0.8 , LEFT * 2.6)
        self.play(FadeIn(formula12),FadeIn(text14))


        formula13 = MathTex(
            "\Longrightarrow-b < y < 0 : x^{2} ",
            font_size = 35,
            color= WHITE
            )
        formula13.shift(UP * 0.2 , LEFT * 5.3 ) 
        text15 = Text(
            "is -ve => Curve does not exist ",
            font_size=25,
            font="Arial",
            color= WHITE,
            )

        text15.shift(UP * 0.2 , LEFT * 1.35  )
        self.play(FadeIn(formula13),FadeIn(text15))


        formula14 = MathTex(
            "\Longrightarrow 0 < y < b : x^{2} ",
            font_size = 35,
            color= WHITE
            )

        formula14.shift(DOWN * 0.4 , LEFT * 5.45 ) 

        text16 = Text(
            "is -ve => Curve does not exist ",
            font_size=25,
            font="Arial",
            color= WHITE,
            )
        text16.shift(DOWN * 0.4 , LEFT * 1.52 )
        self.play(FadeIn(formula14),FadeIn(text16))

        formula15 = MathTex(
            "\Longrightarrow y > b : x^{2} ",
            font_size = 35,
            color= WHITE
            )

        formula15.shift(DOWN * 1, LEFT * 5.75) 
        text17 = Text(
            "is +ve => Curve exists ",
            font_size=25,
            font="Arial",
            color= WHITE,
            )
        text17.shift(DOWN * 1 , LEFT * 2.65)
        self.play(FadeIn(formula15),FadeIn(text17))
        self.wait()    

        text18 = Text(
            "For any value of y , ",
            font_size=25,
            font="Arial",
            color= WHITE,
            )
        text18.shift(DOWN * 1.8,LEFT * 5.5)
        self.play(Write(text18))

        formula16 = MathTex(
            r"x^{2}=\frac{a^{2} + (a^{2}b^{2})}{(y^{2}-b^{2})}",
            font_size = 35,
            color= WHITE
            )
        formula16.shift(DOWN * 1.8 , LEFT * 2.2) 
        self.play(Write(formula16))
        

        text19 = Text(
            "Curve does not exist for -a < x < a ",
            font_size=30,
            font="Arial",
            color= FLUORESCENTGREEN,
            )
        text19.shift(DOWN * 2.8 ,LEFT * 3.9)
        self.play(Write(text19))


        self.clear()






        






       