from manim import *

class FirstText(Scene):
	def construct(self):
		background_rect = Rectangle(
            width=FRAME_WIDTH,
            height=FRAME_HEIGHT,
            fill_color=BLUE,
            fill_opacity=1,  # Set fill_opacity to 1 for solid color
            stroke_width=0,  # Set stroke_width to 0 to remove border
        )
        self.add(background_rect)

        self.camera.frame_width = 32
		self.camera.frame_height = 18


		text = MathTex(r"y= \frac{8a^3}{x^2+4a^3}", font_size=45)
		self.play(Write(text))
		self.wait()

		transform_text = MathTex(r"y= \frac{8a^3}{x^2+4a^3}", font_size=40, color=BLUE)
		transform_text.to_corner(UP+LEFT)

		self.play(Transform(text, transform_text))
		self.wait()



		text_1 = Text("(To plot a Graph on Cartesian Plan, let's put a = 2)", font_size=28)
		text_1.next_to(transform_text, RIGHT+DOWN)
		self.play(Write(text_1))
		self.wait(2)
		self.remove(text_1)
		self.wait(1)




		arrow =	MathTex(r"\xrightarrow{....a = 2....}", font_size=50)
		arrow.next_to(transform_text)

		self.play(Write(arrow))
		self.wait()




		text_2 = MathTex(r"y= \frac{8*2*2*2}{x^2+4*2*2}")
		self.play(Write(text_2))
		self.wait()		
		
		transform_text_2 = MathTex(r"y= \frac{64}{x^2+32}", font_size=40, color=RED)
		transform_text_2.to_corner(UP+LEFT)
		transform_text_2.next_to(arrow)

		self.play(Transform(text_2, transform_text_2))
		self.wait()
		



		text_3 = Text("1. Symmetry:", font_size=36)
		text_3.next_to(arrow, DOWN-3)
		self.play(Write(text_3))
		self.wait()


		text_4 = Text("Condition:-", font_size=28)
		text_5 = Text(" If x is replace by -x and equation is unchanged then, the graph is symmetric about y axis.", font_size=28)
		text_4.next_to(text_3, DOWN)
		text_5.next_to(text_4, DOWN+RIGHT)

		text_6 = MathTex(r"y= \frac{64}{(-x)^2+32}", font_size=40)
		text_6.next_to(text_5, DOWN)
		text_7 = MathTex(r" = \frac{64}{x^2+32}", font_size=40)
		text_7.next_to(text_6,DOWN)

		text_8 = Text("Hence, The graph is symmetric about x-axis", font_size=50)
		text_8.next_to(text_7,DOWN)

		self.play(Write(text_4), Write(text_5), Write(text_6), Write(text_7), Write(text_8))
		self.wait(2)
		self.remove((text_3), (text_4), (text_5), (text_6), (text_7), (text_8))
		self.wait(1)
		
		from manim import WHITE
		config.background_color = WHITE
		config["background_color"] = WHITE



		text_9 = Text("2. Point Of Intersection:", font_size=36)
		text_9.next_to(transform_text_2, DOWN-3)
		self.play(Write(text_9))
		self.wait()

		text_10 = Text("Put (x = 0)", font_size=28)
		text_10.next_to(text_9, RIGHT+DOWN)
		text_11 =  MathTex(r"y= \frac{64}{(0)^2+32}", font_size=40)
		text_11.next_to(text_10, DOWN)
		text_12 =  MathTex(r"y= 2", font_size=50)
		text_12.next_to(text_11, DOWN)
		text_13 = Text("First point of intersection is (0, 2)", font_size=40, line_spacing=100)
		text_13.next_to(text_12, DOWN)
		
		self.play(Write(text_10), Write(text_11), Write(text_12), Write(text_13))
		self.wait(2)
		self.remove((text_10), (text_11), (text_12), (text_13))



		text_14 = Text("(0,2)", font_size=40)
		text_14.next_to(text_9)
		self.play(Write(text_14))
		self.wait(1)


		text_15 = Text("Put (y = 0)", font_size=28)
		text_15.next_to(text_9, RIGHT+DOWN)
		text_16 =  MathTex(r"0= \frac{64}{(x)^2+32}", font_size=40)
		text_16.next_to(text_15, DOWN)
		text_17 =  MathTex(r"0 * {((x)^2+32)} = 64", font_size=50)
		text_17.next_to(text_16, DOWN)
		text_18 =  MathTex(r"0  = 64", font_size=50)
		text_18.next_to(text_17, DOWN)
		text_19 = Text("Point of intersection at (y=0), Not Exist", font_size=40, line_spacing=100)
		text_19.next_to(text_18, DOWN)
		
		self.play(Write(text_15), Write(text_16), Write(text_17), Write(text_18), Write(text_19))
		self.wait(2)
		self.remove((text_15), (text_16), (text_17), (text_18), (text_19))


		text_14 = Text("(0,2)", font_size=40)
		text_14.next_to(text_9)
		self.play(Write(text_14))
		self.wait()
