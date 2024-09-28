from typing_extensions import runtime
from manim import *
from moderngl_window.meta import scene

class Caculus(Scene):

    config.pixel_height=1080
    config.pixel_width=1920
    config.frame_height=18
    config.frame_width=32

    def construct(self):

        Title_1 = Text("CALCULUS", font_size=100, gradient=[RED, BLUE]).scale(2)
        self.play(GrowFromCenter(Title_1), run_time=3)
        self.play(ApplyWave(Title_1, rate_func=linear,ripples=4))
        self.play(ApplyWave(Title_1, direction=RIGHT, time_width=0.5, amplitude=0.5))
        self.wait(1)

        Title_2 = Text("CALCULUS", font_size=102, gradient=[RED, BLUE]).to_edge(UP)
        self.play(ReplacementTransform(Title_1, Title_2), run_time=3)
        self.wait(0.5)

        Def_1 = Text("Calculus, in its mathematical essence, is the study of how quantities change in relation to one another. Scientifically, it is a fundamental tool for analyzing and understanding change and motion, whether it be the motion of physical objects, the variation of quantities, or even more abstract concepts.", font_size=140).next_to(Title_2, DOWN)
        Def_1.set_width(config.frame_width - 1)
        # self.play(Create(Def_1), runtime=6)
        self.wait(1)

        for line in Def_1:
            underline = Line(
                start=line.get_left() + DOWN * 0.1,
                end=line.get_right() + DOWN * 0.1,
                color=WHITE
            )

        # highlight = SurroundingRectangle(Def_1, color=YELLOW, fill_opacity=0.1, buff=0.1)
        self.play(Create(Def_1), Create(underline), run_time=6)
        self.wait(10)
        return super().construct()  