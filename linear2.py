from manim import *

class LinearDiffEqSolution(Scene):
    def construct(self):
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

        # Step 1: Find Integrating Factor
        step_1_text = Text("Step 1: Find Integrating Factor (IF):").scale(0.5).to_edge(LEFT)
        self.play(Write(step_1_text))
        self.wait(1)

        # IF Calculation
        if_text = MathTex(r"IF = e^{\int 2 \, dx} = e^{2x}").scale(0.7).next_to(step_1_text, DOWN, aligned_edge=LEFT)
        self.play(Write(if_text))
        self.wait(1.5)

        # Step 2: Multiply both sides by IF
        step_2_text = Text("Step 2: Multiply both sides by IF:").scale(0.5).next_to(if_text, DOWN, aligned_edge=LEFT)
        self.play(Write(step_2_text))
        self.wait(1)

        # Multiplying both sides by IF
        multiply_if_text = MathTex(r"e^{2x} \frac{dy}{dx} + 2 e^{2x} y = e^{3x}").scale(0.7).next_to(step_2_text, DOWN, aligned_edge=LEFT)
        self.play(Write(multiply_if_text))
        self.wait(1.5)

        # Step 3: Recognize left-hand side as a product derivative
        step_3_text = Text("Step 3: Recognize product derivative:").scale(0.5).next_to(multiply_if_text, DOWN, aligned_edge=LEFT)
        self.play(Write(step_3_text))
        self.wait(1)

        # Product derivative
        product_derivative_text = MathTex(r"\frac{d}{dx} \left( e^{2x} y \right) = e^{3x}").scale(0.7).next_to(step_3_text, DOWN, aligned_edge=LEFT)
        self.play(Write(product_derivative_text))
        self.wait(1.5)

        # Step 4: Integrate both sides
        step_4_text = Text("Step 4: Integrate both sides:").scale(0.5).next_to(product_derivative_text, DOWN, aligned_edge=LEFT)
        self.play(Write(step_4_text))
        self.wait(1)

        # Integration result
        integrate_text = MathTex(r"e^{2x} y = \int e^{3x} dx = \frac{1}{3} e^{3x} + C").scale(0.7).next_to(step_4_text, DOWN, aligned_edge=LEFT)
        self.play(Write(integrate_text))
        self.wait(1.5)

        # Step 5: Solve for y(x)
        step_5_text = Text("Step 5: Solve for y(x):").scale(0.5).next_to(integrate_text, DOWN, aligned_edge=LEFT)
        self.play(Write(step_5_text))
        self.wait(1)

        # Final solution
        final_solution_text = MathTex(r"y(x) = \frac{1}{e^{2x}} \left( \frac{1}{3} e^{3x} + C \right)").scale(0.7).next_to(step_5_text, DOWN, aligned_edge=LEFT)
        self.play(Write(final_solution_text))
        self.wait(2)

        # Clean up the scene
        self.play(Unwrite(question_text))
        self.play(Unwrite(equation_text))
        self.play(Unwrite(step_1_text))
        self.play(Unwrite(if_text))
        self.play(Unwrite(step_2_text))
        self.play(Unwrite(multiply_if_text))
        self.play(Unwrite(step_3_text))
        self.play(Unwrite(product_derivative_text))
        self.play(Unwrite(step_4_text))
        self.play(Unwrite(integrate_text))
        self.play(Unwrite(step_5_text))
        self.play(Unwrite(final_solution_text))
