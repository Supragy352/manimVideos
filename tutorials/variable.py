from typing_extensions import runtime
from click import clear
from manim import *
from manim.mobject import graph
from manim.utils.color.X11 import LIGHTBLUE
from manim.utils.color.XKCD import DARKBLUE, FLUORESCENTGREEN
from numpy import array

class WriteText(Scene):
    def construct(self):
        text18 = Text(
            "For any value of y , ",
            font_size=25,
            font="Arial",
            color= WHITE,
            )
        text18.shift(DOWN * 1.57,LEFT * 5.5)
        self.play(Write(text18))

        formula16 = MathTex(
            r"x^{2}=\frac{a^{2} + (a^{2}b^{2})}{(y^{2}-b^{2})}",
            font_size = 35,
            color= WHITE
            )
        formula16.shift(DOWN * 1.57 , LEFT * 2.2) 
        self.play(Write(formula16))
        

        text19 = Text(
            "Curve does not exist for -a < x < a ",
            font_size=30,
            font="Arial",
            color= FLUORESCENTGREEN,
            )
        text19.shift(DOWN * 2.6 ,LEFT * 3.9)
        self.play(Write(text19))