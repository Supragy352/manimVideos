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
        equation_text = MathTex(r"\frac{dy}{dx} + P(x) y = Q(x)").scale(0.8).next_to(question_text, DOWN)
        self.play(Write(equation_text))
        self.wait(1.5)

        # Describing the method of solving - Integrating Factor
        method_text = Text("Integrating Factor Method:").scale(0.5).to_edge(LEFT)
        self.play(Write(method_text))
        self.wait(1)

        # Step 1: Find Integrating Factor
        step_1_text = Text("1. Find Integrating Factor (IF):", t2c={"IF": YELLOW}).scale(0.5).next_to(method_text, DOWN, aligned_edge=LEFT)
        self.play(Write(step_1_text))
        self.wait(0.5)

        if_formula = MathTex(r"IF = e^{\int P(x) dx}").scale(0.6).next_to(step_1_text, DOWN, aligned_edge=LEFT)
        self.play(Write(if_formula))
        self.wait(1)

        # Step 2: Multiply both sides by IF
        step_2_text = Text("2. Multiply both sides by IF", t2c={"IF": YELLOW}).scale(0.5).next_to(if_formula, DOWN, aligned_edge=LEFT)
        self.play(Write(step_2_text))
        self.wait(1)

        # Step 3: Solve the equation
        step_3_text = Text("3. Solve the equation", t2c={"equation": GREEN}).scale(0.5).next_to(step_2_text, DOWN, aligned_edge=LEFT)
        self.play(Write(step_3_text))
        self.wait(1.5)

        # General Solution
        general_solution_text = Text("General Solution:").scale(0.5).next_to(step_3_text, DOWN, aligned_edge=LEFT)
        self.play(Write(general_solution_text))

        solution_text = MathTex(r"y(x) = \frac{1}{IF} \left( \int IF \cdot Q(x) dx + C \right)").scale(0.6).next_to(general_solution_text, DOWN, aligned_edge=LEFT)
        self.play(Write(solution_text))
        self.wait(2)

        # Clean up the scene
        self.play(*[Unwrite(mob) for mob in [question_text, equation_text, method_text, step_1_text, if_formula, step_2_text, step_3_text, general_solution_text, solution_text]])

        # Now onto the actual equation example
        # Introduction Text for the Linear Differential Equation Problem
        question_text = Text("Solve the Linear Differential Equation:").scale(0.6)
        question_text.move_to(ORIGIN)
        self.play(Write(question_text))
        self.play(question_text.animate.shift(UP * 3))
        self.wait(1)

        # Displaying the equation
        equation_text = MathTex(r"\frac{dy}{dx} + 2y = e^x").scale(0.8).next_to(question_text, DOWN)
        self.play(Write(equation_text))
        self.wait(1.5)

        # Step 1: Find Integrating Factor (IF)
        step_1_text = Text("Step 1: Find Integrating Factor (IF):").scale(0.5).to_edge(LEFT)
        self.play(Write(step_1_text))
        self.wait(1)

        if_text = MathTex(r"IF = e^{\int 2 \, dx} = e^{2x}").scale(0.7).next_to(step_1_text, DOWN, aligned_edge=LEFT)
        self.play(Write(if_text))
        self.wait(1.5)

        # Step 2: Multiply both sides by IF
        step_2_text = Text("Step 2: Multiply both sides by IF:").scale(0.5).next_to(if_text, DOWN, aligned_edge=LEFT)
        self.play(Write(step_2_text))
        self.wait(1)

        multiply_if_text = MathTex(r"e^{2x} \frac{dy}{dx} + 2 e^{2x} y = e^{3x}").scale(0.7).next_to(step_2_text, DOWN, aligned_edge=LEFT)
        self.play(Write(multiply_if_text))
        self.wait(1.5)

        # Step 3: Recognize product derivative
        step_3_text = Text("Step 3: Recognize product derivative:").scale(0.5).next_to(multiply_if_text, DOWN, aligned_edge=LEFT)
        self.play(Write(step_3_text))
        self.wait(1)

        product_derivative_text = MathTex(r"\frac{d}{dx} \left( e^{2x} y \right) = e^{3x}").scale(0.7).next_to(step_3_text, DOWN, aligned_edge=LEFT)
        self.play(Write(product_derivative_text))
        self.wait(1.5)

        # Step 4: Integrate both sides
        step_4_text = Text("Step 4: Integrate both sides:").scale(0.5).next_to(product_derivative_text, DOWN, aligned_edge=LEFT)
        self.play(Write(step_4_text))
        self.wait(1)

        integrate_text = MathTex(r"e^{2x} y = \int e^{3x} dx = \frac{1}{3} e^{3x} + C").scale(0.7).next_to(step_4_text, DOWN, aligned_edge=LEFT)
        self.play(Write(integrate_text))
        self.wait(1.5)

        # Step 5: Solve for y(x)
        step_5_text = Text("Step 5: Solve for y(x):").scale(0.5).next_to(integrate_text, DOWN, aligned_edge=LEFT)
        self.play(Write(step_5_text))
        self.wait(1)

        final_solution_text = MathTex(r"y(x) = \frac{1}{e^{2x}} \left( \frac{1}{3} e^{3x} + C \right)").scale(0.7).next_to(step_5_text, DOWN, aligned_edge=LEFT)
        self.play(Write(final_solution_text))
        self.wait(2)

        # Clean up the scene
        self.play(*[Unwrite(mob) for mob in [question_text, equation_text, step_1_text, if_text, step_2_text, multiply_if_text, step_3_text, product_derivative_text, step_4_text, integrate_text, step_5_text, final_solution_text]])
