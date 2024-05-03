from manim import *
from moderngl_window.meta import scene

class SecondExample(Scene):
	def construct(self):
		ax = Axes(x_range=(3,-3),y_range=(3,-3))
		self.add(ax)

