from svgelements import Curve
from typing_extensions import runtime
from manim import *
import numpy as np

class title(Scene):
    config.pixel_height=1080
    config.pixel_width=1920
    config.frame_height=18
    config.frame_width=32

    def construct(self):

        Title_1 = Text("INTEGRATION", gradient=[RED, BLUE], font_size=110)
        self.play(Write(Title_1), runtime=3)

        # Title_2 = Text("INTEGRATION", gradient=[RED, BLUE], font_size=110)
        self.wait(1)