# from manim import *

# class Ax(ThreeDScene):
# 	def construct(self):

# 		axes = ThreeDAxes(
# 			x_range = [-6,7,1],
# 			y_range = [-6,7,1],
# 			z_range = [-6,7,1],
# 			# x_lenght = 6,
# 			y_length = 6,
# 			# z_lenght = 6
# 			)

# 		# graph = axes.get_graph(lambda x: x ** 2)
# 		# rect = axes.get_rieman_rectangles(
# 		# 	graph=graph, x_range=[-2,2], dx=0.1, stroke_color=WHITE
# 		# 	)

# 		# graph2 = axes.gt_parametric_curve(
# 		# 	lambda t: np.array([np.cos(t), np.sin(t), t]),
# 		# 	t_range=[-2*PI, 2*PI],
# 		# 	colour=RED
# 		# 	)

# 		self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
# 		self.add(axes)
# 		self.begin_ambient_camera_rotation(rate=0.1)
# 		self.wait()
# 		self.stop_ambient_camera_rotation()
# 		self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
# 		self.wait()

# 		curve = axes.plot(ImplicitFunction())

# 		self.add(axes)
# 		self.wait(5)

# 		


from manim import *

class Function(Scene):
	def construct(self):

		axes = ThreeDAxes(
			x_range=[-10, 10, 1],
			y_range=[-10, 10, 1],
			z_range=[-10,10,1]
			)
		
		curve = ImplicitFunction(lambda x, y: x + y**2 - 4)
		curve_1 = ImplicitFunction(lambda x, y: -x + y**2 - 4)

		area = axes.get_area(curve, x_range=(-10, 10), y_range=(-10, 10), color=BLUE)

		self.play(Create(curve), Create(curve_1), run_time=3)
		self.wait(4)