from svgelements import Curve
from typing_extensions import runtime
from manim import *
import numpy as np

class title(Scene):
	config.pixel_height=1080
	config.pixel_width=1920
	config.frame_height=18
	config.frame_width=32

	def construct(self):

		Title_1 = Text("Differentiation", gradient=[RED, BLUE], font_size=110)
		self.play(Write(Title_1), runtime=3)
		self.wait(1)

class Graph(Scene):
	config.pixel_height=1080
	config.pixel_width=1920
	config.frame_height=18
	config.frame_width=32

	def construct(self):
		ax = Axes(
			x_range=[0,11,1],
			y_range=[0,11,1],
			x_length=6,
			y_length=6,
			axis_config={"color":BLUE, "include_ticks": False}
			).add_coordinates(color=BLUE).to_edge(UL)
		ax.add_background_rectangle(color=WHITE, opacity=0.2)

		self.play(Create(ax), runtime=3)
		self.wait(1)

		point1 = ax.coords_to_point(3,0)
		point2 = ax.coords_to_point(0,4)
		point3 = ax.coords_to_point(8,6.8)

		line1 = Line(point1, point2, color=YELLOW)
		line2 = Line(point3, point1, color=YELLOW)

		parametric_function = ParametricFunction(
            lambda t: ax.c2p(t, np.sqrt(t) + 4),
            t_range=np.array([0, 8]),  
            color=YELLOW)

		self.play(Create(line1), Create(line2),Create(parametric_function), run_time=1)
		self.wait(2)

					#########################################################

		ax2 = Axes(
			x_range=[0,11,1],
			y_range=[0,11,1],
			x_length=6,
			y_length=6,
			axis_config={"color":BLUE, "include_ticks": False}
			).add_coordinates(color=BLUE).next_to(ax).shift(RIGHT)
		ax2.add_background_rectangle(color=WHITE, opacity=0.2)

		self.play(Create(ax2), runtime=3)
		self.wait(1)


		x_start, y_start = 0, 8
		x_end, y_end = 10, 8
		x_mid = (x_start + x_end) / 2
		y_mid = 2

		a = (y_start - y_mid) / ((x_start - x_mid) ** 2)

		curve = ParametricFunction(
            lambda t: ax2.c2p(t, a * (t - x_mid) ** 2 + y_mid),
            t_range=np.array([x_start, x_end]),
            color=YELLOW
        )

		self.play(Create(curve))

		point4 = Dot(color=RED).move_to(ax2.coords_to_point(7,3))
		point5 = Dot(color=RED).move_to(ax2.coords_to_point(9.5,7))
		line3 = Line(point4, point5, color=PINK)
		self.play(Create(point4), Create(point5), colour=RED)
		self.play(Create(line3))

		self.wait(20)
		return super().construct()