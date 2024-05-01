from manim import *

class FirstTex(Scene):
	def construct(self):
		text = Tex(r"1. Symmetry \\ xyz", color=BLUE, font_size=32)
		text_1 = Text("2. Origin", color=BLUE, font_size=32)
		text_2 = Text("3. Tangent", color=BLUE, font_size=32)
		text_3 = Text("4. Assymptots", color=BLUE, font_size=32)
		
		text.to_edge(UP+LEFT)
		text_1.next_to(text, DOWN)
		text_2.next_to(text_1, DOWN)
		text_3.next_to(text_2, DOWN)
		
		self.play(Write(text),Write(text_1), Write(text_2), Write(text_3), run_time=3)  
		#self.play(, run_time=3)
		self.wait(3)