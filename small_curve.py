from manim import *
class Curve(Scene):
	def construct(self):

		ax = Axes(
			x_range=[-10, 11, 1], 
			y_range=[-10, 11, 1]
			)

		start = np.array((-1,1))
		end = np.array((1,1))
		control_point = np.array((0,4))
		curve = ArcBetweenPoints(start[:2], end[:2m], angle=-TAU/2)

		self.play(Create(ax), Create(curve))
		self.wait(2) 