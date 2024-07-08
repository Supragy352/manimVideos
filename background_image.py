from manim import *

class Background(Scene):
	config.pixel_width = 1920
	config.pixel_height = 1080
	config.frame_width = 32
	config.frame_height = 18
	def construct(self):

		x = ImageMobject("C:\\Users\\Anooj Dilip Archana\\Downloads\\fantasy-style-galaxy-background.jpg")
		self.add(x)

		y = Text("HELLO", font_size=200, stroke_width=8)
		self.play(Write(y))

