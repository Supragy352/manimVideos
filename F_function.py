from manim import * 

class Function(Scene):

	config.pixel_height = 1080
	config.pixel_width = 1920
	config.frame_height = 18
	config.frame_width = 32

	def construct(self):

		axes1 = Axes(
			x_range=[0, 10, 1],
			y_range=[0, 10, 1],
			x_length=10,
			y_length=10,
			axis_config={"color":BLUE, "include_ticks": True, 'tip_shape': StealthTip}
			).add_coordinates(color=BLUE).add_background_rectangle(color=WHITE, opacity=0.2)

		self.play(Create(axes1), run_time=2)
		self.wait(10)

		return super().construct()