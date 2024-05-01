from manim import *

class LineSymmetry(Scene):
	def construct(self):
		start = np.array((0,-7,0))
		end = np.array((0,7,0))
		line = Line(start, end, color=BLUE)

		self.play(Create(line), color = BLUE)
		self.wait(2)