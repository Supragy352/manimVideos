from PIL import Image
from typing_extensions import runtime
from manim import * 

class First(Scene):
	config.pixel_width = 1920
	config.pixel_height = 1080
	config.frame_width = 32
	config.frame_height = 18
	def construct(self):

		ax = Axes(
			x_range=[-10,11,1],
			y_range=[-10,11,1],
			x_length=15,
			y_length=15,
			).add_coordinates()

		image = ImageMobject("C:\\Users\\Anooj Dilip Archana\\Downloads\\Earth.jpeg").move_to(ax.coords_to_point(5,0))
		image.scale(0.06)

		self.play(Create(ax), runtime=3)
		self.add(image)
		self.wait(3)