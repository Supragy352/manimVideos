from manim import*

class Graph(Scene):
	def construct(self):

		Title = Text("Curve Tracing", color=BLUE, font_size=48)
		self.play(Write(Title))
		self.wait(10)