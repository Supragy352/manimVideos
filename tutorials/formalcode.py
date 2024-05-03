from typing_extensions import runtime
from manim import *
from numpy import array

class IsolatedPoint(Scene):
	def construct(self):
		plane = Axes(x_range=(-6,6), y_range=(-6,6))
		a=2
		b=3
		c = Circle(radius= 0.1 , color= RED , fill_opacity = 0.1)
		line1 = DoubleArrow(start=array([1.0 , -3.9 , 0.0]), end=array([1.0 , 3.9 , 0.0]), color= RED)
		line2 = DoubleArrow(start=array([-1.0 , -3.9 , 0.0]), end=array([-1.0 , 3.9 , 0.0]), color= RED)
		line3 = DoubleArrow(start=array([-5.9 , 0.5 , 0.0]), end=array([5.9 ,0.5 , 0.0]), color= RED)
		line4 = DoubleArrow(start=array([-5.9 , -0.5 , 0.0]), end=array([5.9 , -0.5 , 0.0]), color= RED)
		curve = ImplicitFunction(lambda x, y: (x ** 2 - 1 ** 2) * (y ** 2 - 1 ** 2)  - (1 ** 2)*(1 ** 2))
		graph = VGroup(plane,curve,line1,line2,line3,line4,c).scale(0.4).shift(RIGHT * 4.5 + DOWN * 1.5)
		self.play(Create(plane))	
		self.wait(3)
		self.clear()
		