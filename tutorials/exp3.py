from functools import reduce
from manim import *
from numpy import number, square, squeeze


class Positioning(Scene):
	def construct(self):
		plane = NumberPlane()
		self.add(plane)

		red_dot = Dot(color=RED)
		green_dot = Dot(color=GREEN)
		green_dot.next_to(red_dot, RIGHT + UP)
		self.add(red_dot,green_dot)

		s = Square(color = RED)
		s.shift(2 * UP + 4 * RIGHT)
		self.add(s)