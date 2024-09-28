from manim import *

class SquareToCircle(Scene):
#     def construct(self):
#         circle = Circle()
#         circle.set_fill(BLUE, opacity=0.5)
#         circle.set_stroke(BLUE_E, width=4)
#         square = Square()

#         self.play(ShowCreation(square))
#         self.wait()
#         self.play(ReplacementTransform(square, circle))
#         self.wait()
#         # Try typing the following lines
#         # self.play(circle.animate.stretch(4, dim=0))
#         # self.play(Rotate(circle, TAU / 4))
#         # self.play(circle.animate.shift(2 * RIGHT), circle.animate.scale(0.25))
#         # circle.insert_n_curves(10)
#         # self.play(circle.animate.apply_complex_function(lambda z: z**2))

# class SquareToCircleEmbed(Scene):
#     def construct(self):
#         circle = Circle()
#         circle.set_fill(BLUE, opacity=0.5)
#         circle.set_stroke(BLUE_E, width=4)

#         self.add(circle)
#         self.wait()
#         self.play(circle.animate.stretch(4, dim=0))
#         self.wait(1.5)
#         self.play(Rotate(circle, TAU / 4))
#         self.wait(1.5)
#         self.play(circle.animate.shift(2 * RIGHT), circle.animate.scale(0.25))
#         self.wait(1.5)
#         circle.insert_n_curves(10)
#         self.play(circle.animate.apply_complex_function(lambda z: z**2))
#         self.wait(2)

    CONFIG = {
        "color":BLUE,
        "buff":0.3,
        "lateral":0.3,
        "invert":True,
        "dashed_segment_length":0.09,
        "dashed":True,
        "ang_arrows":30*DEGREES,
        "size_arrows":0.2,
        "stroke":2.4,
    }

    def construct(self):

        tex = Text("Integration", font_size=120, gradient=[RED, BLUE])
        self.play(Write(tex), time=3)
        self.wait(5)
        return super().construct()