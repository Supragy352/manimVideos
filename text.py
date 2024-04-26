from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello world", font_size=144)
        self.play(Create(text),run_time=3)