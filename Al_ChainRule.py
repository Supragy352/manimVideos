from typing_extensions import runtime
from manim import *
from moderngl_window.meta import scene

class AxesPlot(Scene):
	config.pixel_height=1080
	config.pixel_width=1920
	config.frame_height=18
	config.frame_width=32
	def construct(self, font_size=50):

		Title_1 = Text("Chain Rule", gradient=[RED, BLUE], font_size=110)
		Title_2 = Text("Chain Rule", gradient=[RED, BLUE], font_size=110).to_edge(UP)

		self.play(GrowFromCenter(Title_1),
			run_time=3)
		self.wait(2)

		self.play(
			ReplacementTransform(Title_1,Title_2),
			run_time=3
			)
		self.wait()


		text=MathTex("\\frac{d}{dx}f(x)g(x)=",
		"f(x)\\frac{d}{dx}g(x)",
		"+",
		"g(x)\\frac{d}{dx}f(x)", font_size=100)
		self.play(Write(text))

		brace1 = Brace(text[1], UP, buff = SMALL_BUFF, color=BLUE, stroke_width=6)
		brace2 = Brace(text[3],  buff = SMALL_BUFF, color=RED, stroke_width=6)
		t1 = brace1.get_text("$g'f$").scale(1.5)
		t2 = brace2.get_text("$f'g$").scale(1.5)
		self.play(
			GrowFromCenter(brace1),
			FadeIn(t1)
			)
		self.wait()
		self.play(
			ReplacementTransform(brace1,brace2),
			ReplacementTransform(t1,t2)
			)
		self.play(FadeIn(t2))
		self.wait(1)
		self.wait(5)
        