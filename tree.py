from manim import *
import numpy as np

class CalculusIntroduction(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Calculus", font_size=72)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Introductory Text
        intro_text = Text("""
        Calculus is a branch of mathematics focused on limits, functions,
        derivatives, integrals, and infinite series. It has widespread
        applications in science, engineering, and economics.
        """, font_size=36).scale(0.5)
        self.play(Write(intro_text))
        self.wait(4)
        self.play(FadeOut(intro_text))

class Limits(Scene):
    def construct(self):
        # Title
        title = Text("Limits", font_size=72)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Limit Definition
        limit_text = Text("""
        The limit of a function is the value that the function approaches
        as the input approaches some value.
        """, font_size=36).scale(0.5)
        self.play(Write(limit_text))
        self.wait(4)
        self.play(FadeOut(limit_text))