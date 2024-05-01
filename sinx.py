from manim import *

class MyScene(Scene):
    def construct(self):
        text_obj = Text("Some text")
        self.play(Write(text_obj))  # Display the text
        self.wait(1)
        self.remove(text_obj)  # Remove the text from the scene
        self.wait(1)
