from logging import currentframe
from manim import *

class IntegrationIntro(Scene):

	def construct(self):

		# CONSTANTS
		X = 9
		Y = 6 
		
		# def curve_equation(x,y):
		# 	return x**2 + y**2 - 1

		# curve = ImplicitFunction(
		# 	curve_equation,
		# 	color=YELLOW
		# )

		axes = Axes(
			x_range=[0,X + 1,1],
			y_range=[0,Y,1],
			x_length= X + 1,
			y_length= Y,
			axis_config={"color":BLUE , "include_ticks": False}
		)

		curve = axes.plot(
			lambda x: 0.2 * x * (X - x),
			x_range = [0,X],
			color = YELLOW
		)

		graph = VGroup(axes,curve)
		graph.move_to(ORIGIN).shift(UP * 0.5)
		self.play(Create(axes),Create(curve))
		self.wait(3)

		def makeRect(num_rects):
			rectangles = VGroup()
			dx = X / num_rects

			for i in range(1, num_rects):
				x = i * dx
				height = 0.2 * x * (X - x)
				rect = Rectangle(
					width = dx,
					height = height,
					color = RED,
					fill_color = RED,
					fill_opacity = 0.5,
					stroke_width = 0.5
				)
				rect.move_to(axes.c2p(x , height / 2))
				rectangles.add(rect)

			return rectangles
				
		# rects_set = VGroup()

		for i in range(1,4):
			num_rects = 6 ** i
			rectangles = makeRect(num_rects)
			# rects_set.add(rectangles)

			self.play(Create(rectangles),run_time = 2)
			self.wait(1)
			self.play(FadeOut(rectangles))