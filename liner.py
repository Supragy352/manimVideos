from manim import *

class LinearDiffEq(Scene):
    def construct(self):
        # Introduction Text for the Linear Differential Equation Problem
        question_text = Text("Solve the Linear Differential Equation:").scale(0.6)
        question_text.move_to(ORIGIN)
        self.play(Write(question_text))
        self.play(question_text.animate.shift(UP * 3))
        self.wait(1.5)
        
        # Using MathTex for mathematical expressions
        equation_text = MathTex(r"\frac{dy}{dx} + P(x) y = Q(x)").scale(0.6).next_to(question_text, DOWN)
        self.play(Write(equation_text))
        self.wait(1)

        # Describing the method of solving - Integrating Factor
        method_text = Text("Integrating Factor Method:").scale(0.5).to_edge(LEFT)
        self.play(Write(method_text))
        self.wait(0.5)

        step_1_text = Text("1. Find Integrating Factor (IF): e^(∫P(x) dx)").scale(0.5).next_to(method_text, DOWN, aligned_edge=LEFT)
        self.play(Write(step_1_text))
        self.wait(0.5)

        step_2_text = Text("2. Multiply both sides by IF").scale(0.5).next_to(step_1_text, DOWN, aligned_edge=LEFT)
        self.play(Write(step_2_text))
        self.wait(0.5)

        step_3_text = Text("3. Solve the equation").scale(0.5).next_to(step_2_text, DOWN, aligned_edge=LEFT)
        self.play(Write(step_3_text))
        self.wait(1)

        # Displaying the general solution
        solved_eq_text = Text("General Solution:").scale(0.5).next_to(step_3_text, DOWN, aligned_edge=LEFT)
        self.play(Write(solved_eq_text))

        solution_text = MathTex(r"y(x) = \frac{1}{IF} \left( \int IF \cdot Q(x) \, dx + C \right)").scale(0.6).next_to(solved_eq_text, DOWN, aligned_edge=LEFT)
        self.play(Write(solution_text))
        self.wait(2)

        # Clean up the scene
        self.play(Unwrite(question_text))
        self.play(Unwrite(equation_text))
        self.play(Unwrite(method_text))
        self.play(Unwrite(step_1_text))
        self.play(Unwrite(step_2_text))
        self.play(Unwrite(step_3_text))
        self.play(Unwrite(solved_eq_text))
        self.play(Unwrite(solution_text))

