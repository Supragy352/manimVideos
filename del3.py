from typing_extensions import runtime
from manim import *
from manim.utils.color.XKCD import RED, BLUE, GREEN

class IntegralCalculusAnimation(Scene):
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_height = 18.0
    config.frame_width = 32.0
    def construct(self):
        # Title Animation
        integral_text = "Integral"
        calculus_text = "Calculus"

        integral_letters = VGroup(*[Text(letter, font_size=110) for letter in integral_text])
        calculus_letters = VGroup(*[Text(letter, font_size=110) for letter in calculus_text])

        for letter in integral_letters:
            letter.shift(np.random.uniform(-10, 10) * RIGHT + np.random.uniform(-6, 6) * UP)
            letter.set_color_by_gradient(BLUE, RED, GREEN)
        
        for letter in calculus_letters:
            letter.shift(np.random.uniform(-10, 10) * RIGHT + np.random.uniform(-6, 6) * UP)
            letter.set_color_by_gradient(GREEN, BLUE)
       
        self.play(Create(integral_letters), Create(calculus_letters))
        

        integral_complete = Text("Integral", font_size=96).scale(2.3).set_color_by_gradient(BLUE, RED)
        calculus_complete = Text("Calculus", font_size=96).scale(2.3).set_color_by_gradient(GREEN, BLUE)
        
        combined_words = VGroup(integral_complete, calculus_complete).arrange(RIGHT, buff=0.5).move_to(ORIGIN)

        self.play(
            *[
                letter.animate.move_to(integral_complete[i].get_center())
                for i, letter in enumerate(integral_letters)
            ],
            *[
                letter.animate.move_to(calculus_complete[i].get_center())
                for i, letter in enumerate(calculus_letters)
            ],
            run_time=3,
            lag_ratio=10
        )

        self.remove(integral_letters, calculus_letters)
        self.add(integral_complete, calculus_complete)

        self.play(
            integral_complete.animate.set_color_by_gradient(BLUE, RED),
            calculus_complete.animate.set_color_by_gradient(BLUE, GREEN),
            run_time=3,
            lag_ratio=10
        )

        self.play(combined_words.animate.to_edge(UP * 3).scale(1.1), lag_ratio=0.05)
        self.wait(5)