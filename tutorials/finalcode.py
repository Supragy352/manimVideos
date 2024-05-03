from click import clear
from manim import *
from manim.mobject import graph
from manim.utils.color.X11 import LIGHTBLUE
from manim.utils.color.XKCD import DARKBLUE
from numpy import array

class WriteText(Scene):
	def construct(self):
		banner = ManimBanner()
		self.play(banner.create())
		self.play(banner.expand())
		self.wait()
		self.play(Unwrite(banner))
		self.clear()

		plane = Axes(x_range=(-6,6), y_range=(-6,6))
		c = Circle(radius= 0.1 , color= RED , fill_opacity = 0.1)
		line1 = DoubleArrow(start=array([1.0 , -3.9 , 0.0]), end=array([1.0 , 3.9 , 0.0]), color= RED)
		line2 = DoubleArrow(start=array([-1.0 , -3.9 , 0.0]), end=array([-1.0 , 3.9 , 0.0]), color= RED)
		line3 = DoubleArrow(start=array([-5.9 , 0.5 , 0.0]), end=array([5.9 ,0.5 , 0.0]), color= RED)
		line4 = DoubleArrow(start=array([-5.9 , -0.5 , 0.0]), end=array([5.9 , -0.5 , 0.0]), color= RED)
		curve = ImplicitFunction(lambda x, y: (x ** 2 - 1 ** 2) * (y ** 2 - 1 ** 2)  - (1 ** 2)*(1 ** 2))
		graph = VGroup(plane,curve,line1,line2,line3,line4,c).scale(0.4).shift(RIGHT * 4.5 + DOWN * 1.5)

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
			FadeIn(intro),
			Create(plane)
			)
		self.play(Indicate(text))
		self.play(Write(formula1))
		self.wait(1)
		text1 = Text(
			"Solution :",
			font_size=30,
			font="Arial",
			color= RED,
			)
		text1.shift(1.4 * UP + LEFT * 5)
		self.play(Write(text1))
		text2 = Text(
			"Symmetry: About X-axis , Y-axis and Origin",
			font_size=25,
			font="Arial",
			color= GREEN,
			)
		text2.shift(0.8 * UP + LEFT * 2)
		self.play(Write(text2))
		text3 = Text(
			"Point of Intersection :",
			font_size=25,
			font="Arial",
			color= LIGHTBLUE,
			)
		text3.shift(0.1 * UP + LEFT * 3.3 )
		self.play(Write(text3))
	
		formula2 = MathTex(
			"x = 0 ==> -a^{2}y^{2} + a^{2}b^{2} = a^{2}b^{2}",
			font_size = 35,
			color= WHITE
			)
		formula2.shift(DOWN * 0.3 + LEFT * 0.2)
		self.play(Write(formula2))

		formula4 = MathTex(
			"==> y = 0",
			font_size = 35,
			color= WHITE
			)
		formula4.shift(DOWN * 0.8 + LEFT * 0.2)
		self.play(Write(formula4))
		self.wait(1)
		formula3 = MathTex(
			"y = 0 ==> -b^{2}x^{2}+a^{2}b^{2} = a^{2}b^{2} ",
			font_size = 35,
			color= WHITE
			)
		formula3.shift(DOWN * 1.3, LEFT * 0.2) 
		self.play(Write(formula3))

		formula5 = MathTex(
			"==> x = 0 ",
			font_size = 35,
			color= WHITE
			)
		formula5.shift(DOWN * 1.8, LEFT * 0.2) 
		self.play(Write(formula5))
		text4 = Text(
			"(0,0) is the only point of Intersection",
			font_size=30,
			font="Arial",
			color= WHITE,
			)
		text4.shift(DOWN * 2.3)
		self.play(Write(text4))
		self.wait(1)
		text5 = Text(
			"Tangets :  \n \n At (0,0): Equating the Lowest Degree Term to Zero we get",
			font_size=25,
			font="Arial",
			color= WHITE,
			)
		text5.shift(3.2 * DOWN + LEFT * 0.5 )
		self.play(Write(text5))
		self.clear()
		formula6 = MathTex(
			"=> -b^{2}x^{2} - a^{2}y^{2} = 0 ",
			font_size = 35,
			color= WHITE
			)
		formula6.shift(UP * 3.5 ) 
		self.play(Write(formula6))
		formula7 = MathTex(
			"=> y^{2} = -x^{2} ",
			font_size = 35,
			color= WHITE
			)
		formula7.shift(UP * 3, LEFT * 0.5) 	
		self.play(Write(formula7))
		text6 = Text(
			"=> y is Imaginary",
			font_size=25,
			font="Arial",
			color= WHITE,
			)
		text6.shift(UP * 2.45, LEFT * 0.1)
		self.play(Write(text6))
		
		text7 = Text(
			"=> There exist no real Tangets at (0,0) \n \n ∴(0,0) is the only point of Intersection",
			font_size=20,
			font="Arial",
			color= WHITE,
			)
		text7.shift(UP * 1.5, LEFT * 4)
		self.play(Write(text7))
		self.wait(1)
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




		

		text11 = Text(
			"Plotting the Graph to understand the Region of Absence : ",
			font_size=30,
			font="Arial",
			color= LIGHTBLUE,
			)
		text11.shift(DOWN * 1 , LEFT * 1.3)
		self.play(Write(text11))

		self.clear() 

		#GRAPH




		#TEXT AFTER GRAPH
		text13 = Text(
            "Region of Absence : ",
            font_size=30,
            font="Arial",
            color= LIGHTBLUE,
            )
		text13.shift(UP * 3  , LEFT * 5)
		self.play(Write(text13))
		formula11 = MathTex(
            " x^{2} = a^{2} + (a^{2}b^{2})/(y^{2}-b^{2}) ",
            font_size = 40,
            color= WHITE
            )
		formula11.shift(UP * 2.3 , LEFT * 4.6) 
		self.play(Write(formula11))

		formula12 = MathTex(
			" y < -b : x^{2} ",
            font_size = 40,
            color= WHITE
            )
		formula12.shift(UP * 2.4 ) 
		self.play(Write(formula12))
		text14 = Text(
            "is +ve => Curve exists ",
            font_size=30,
            font="Arial",
            color= WHITE,
            )

		text14.shift(UP * 2.4 , RIGHT * 3.3)
		self.play(Write(text14))


		formula13 = MathTex(
            "-b < y < 0 : x^{2} ",
            font_size = 40,
            color= WHITE
            )
		formula13.shift(UP * 1.8 ) 
		self.play(Write(formula13))
		text15 = Text(
            "is -ve => Curve does not exist ",
            font_size=30,
            font="Arial",
            color= WHITE,
            )

		text15.shift(UP * 1.8 , RIGHT * 4.3)
		self.play(Write(text15))


		formula14 = MathTex(
            "0 < y < b : x^{2} ",
            font_size = 40,
            color= WHITE
            )

		formula14.shift(UP * 1.2 ) 
		self.play(Write(formula14))

		text16 = Text(
            "is -ve => Curve does not exist ",
            font_size=30,
            font="Arial",
            color= WHITE,
            )
		text16.shift(UP * 1.2 , RIGHT * 4.2)
		self.play(Write(text16))

		formula15 = MathTex(
            " y > b : x^{2} ",
            font_size = 40,
            color= WHITE
            )

		formula15.shift(UP * 0.6 ) 
		self.play(Write(formula15))
		text17 = Text(
            "is +ve => Curve exists ",
            font_size=30,
            font="Arial",
            color= WHITE,
            )
		text17.shift(UP * 0.6 , RIGHT * 3)
		self.play(Write(text17))
		self.wait(1)

		text18 = Text(
            "For any value of y , ",
            font_size=30,
            font="Arial",
            color= WHITE,
            )
		text18.shift(DOWN * 0.5,LEFT * 5)
		self.play(Write(text18))

		formula16 = MathTex(
            " x^{2}= a^{2} + (a^{2}b^{2})/(y^{2}-b^{2}) ",
            font_size = 40,
            color= WHITE
            )
		formula16.shift(DOWN * 0.5 , LEFT * 0.6) 
		self.play(Write(formula16))
		

		text19 = Text(
            "Curve does not exist for -a < x < a ",
            font_size=30,
            font="Arial",
            color= WHITE,
            )
		text19.shift(DOWN * 1.3,LEFT * 1)
		self.play(Write(text19))
		














		

