import time
from manim import *
from manim.utils.color.X11 import BLUE1, PLUM, RED4, SALMON, THISTLE
import numpy as numpy

class VObject(Scene):
	def construct(self):
		config.pixel_height = 2160
		config.pixel_width = 4096
		config.frame_height = 0.1
		config.frame_width = 0.1
		
		# self.camera.background_color = WHITE

		axes = Axes(
            x_range = [-10, 11, 1],
            y_range = [-10,11, 1],
            x_length=12,
            y_length=12,
            y_axis_config={"color": ORANGE},
             x_axis_config={"color": BLUE1}
            )
		# self.play(Create(axes))

		text1 =  Text("C", font_size=500)
		self.play(Create(text1))
		text2 = Text("Calculus", font_size = 100)
		self.play(Transform(text1, text2))
		self.wait()
		self.remove(text1)
		text3 = Text("Calculus")
		self.play(Transform(text2, text3))
