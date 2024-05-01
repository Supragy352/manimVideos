from manim import *
class Tex(Scene):
	def construct(self):
		text = MathTex(r"y= \frac{8a^3}{x^2+4a^3}")
		self.play(Write(text))		
		self.wait()
		
		transform_text = MathTex(r"y= \frac{8a^3}{x^2+4a^3}", font_size=40, color=BLUE)
		transform_text.to_corner(UP+LEFT)

		self.play(Transform(text, transform_text))
		self.wait(1)
		rtarrow0 = MathTex(r"\xrightarrow{   a=2   }", font_size=40)
		rtarrow0.next_to(transform_text)
		self.play(Write(rtarrow0))

		text_1 = Text(">>To plot on graph, put a=2", font_size=24)
		text_1.next_to(text, RIGHT+DOWN)

		self.play(Write(text_1))
		self.wait(0)

		text_2 = MathTex(r"y= \frac{8*2*2*2}{x^2+4*2*2}")
		self.play(Write(text_2))
		self.wait()		
		
		transform_text_2 = MathTex(r"y= \frac{64}{x^2+32}", font_size=40, color=RED)
		transform_text_2.to_corner(UP+LEFT)
		transform_text_2.next_to(rtarrow0)

		self.play(Transform(text_2, transform_text_2))
		self.wait(5)
		self.remove(text_2)
		self.wait(1)
		



		text_3 = Text("1. Symmetry:", font_size=28)
		text_3.next_to(transform_text_2, DOWN)
		text_4 = Text("About x-axis: The terms have even power of y.", font_size=24)
		text_4.next_to(text_3, RIGHT+DOWN)

		self.play(Write(text_3), Write(text_4))
	


		text_5 = Text("2. Point Of Intersection", font_size=24)
		text_5.next_to(text_4, LEFT+DOWN, aligned_edge=RIGHT+DOWN)

		self.play(Write(text_5))
		self.wait(10)
		
