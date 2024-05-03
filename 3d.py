from manim import *
from moderngl_window.meta import scene
from numpy import array

class ThreeDGraph(Scene):
	def construct(self):

		ax = ThreeDAxes(
			x_range=[-10, 10, 1],
			y_range=[-10, 10, 1],
			z_range=[-10, 10, 1]
			)
		graph = ax.get_graph()

		self.add((ax))
		self.wait(5)