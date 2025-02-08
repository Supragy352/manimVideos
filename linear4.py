from manim import *

class SecondOrderDiffEqApplications(Scene):
    def construct(self):
        # Mechanical Vibrations (Spring-Mass-Damper System)
        self.mechanical_vibrations_animation()

        # RLC Circuit Animation
        self.rlc_circuit_animation()

    def mechanical_vibrations_animation(self):
        # Title for Mechanical Vibrations
        title1 = Text("Application: Mechanical Vibrations").to_edge(UP)
        self.play(Write(title1))
        
        # Mass-Spring-Damper Equation
        equation1 = MathTex("m \\frac{d^2x}{dt^2} + c \\frac{dx}{dt} + kx = 0").scale(0.8).to_edge(UP, buff=1.5)
        self.play(Write(equation1))
        
        # Spring and Block setup
        ceiling = Line(LEFT, RIGHT).scale(1.5).shift(UP * 0.2)
        spring = Line(UP, DOWN, color=WHITE).set_height(1.5)  # Adjust spring length based on block position
        block = Square(color=BLUE, fill_opacity=1).next_to(spring, DOWN, buff=0.1)
        spring_block = VGroup(spring, block).move_to(DOWN * 1.5)  # Position spring and block

        self.play(Create(ceiling), Create(spring), Create(block))

        # Simulate Oscillatory Motion with Damping
        amplitude = 0.5
        for i in range(5):
            self.play(
                block.animate.shift(UP * amplitude),
                spring.animate.stretch(1 - amplitude / 5, 1, about_edge=UP),  # Only stretch the spring, but keep its top fixed
                run_time=0.5
            )
            self.play(
                block.animate.shift(DOWN * amplitude),
                spring.animate.stretch(1 + amplitude / 5, 1, about_edge=UP),  # Restore the spring length
                run_time=0.5
            )
            amplitude *= 0.7  # Reduce amplitude to simulate damping

        # Add Damping Text
        damping_text = Text("Damping affects the motion").next_to(block, DOWN * 0.5)
        self.play(Write(damping_text))
        self.wait(2)

        # Clear the scene for the next animation
        self.play(FadeOut(title1), FadeOut(equation1), FadeOut(spring), FadeOut(block), FadeOut(damping_text), FadeOut(ceiling))

    def rlc_circuit_animation(self):
        # Title for RLC Circuit
        title2 = Text("Application: RLC Circuit").to_edge(UP)
        self.play(Write(title2))
        
        # RLC Circuit Equation
        equation2 = MathTex("L \\frac{d^2q}{dt^2} + R \\frac{dq}{dt} + \\frac{q}{C} = E(t)").scale(0.8).to_edge(UP, buff=1.5)
        self.play(Write(equation2))
        
        # Realistic Circuit components
        resistor = Rectangle(height=0.5, width=1, color=RED)
        inductor = VGroup(*[Line(UP, DOWN, color=GREEN) for _ in range(4)]).arrange(RIGHT, buff=0.1)  # Coil-like structure for inductor
        capacitor = VGroup(Line(UP, DOWN, color=YELLOW), Line(UP, DOWN, color=YELLOW).shift(RIGHT * 0.2))

        # Wires for the circuit
        wire1 = Line(LEFT, RIGHT, color=WHITE).scale(2)
        wire2 = Line(LEFT, RIGHT, color=WHITE).scale(2).shift(DOWN * 1)
        
        # Position components in a loop
        circuit = VGroup(wire1, resistor, inductor, capacitor, wire2).arrange(RIGHT, buff=0.5)
        self.play(Create(circuit))

        # Simulate Current Flow with color changes
        current = Dot(color=BLUE).move_to(wire1.get_start())
        self.play(MoveAlongPath(current, wire1), run_time=2)
        self.play(MoveAlongPath(current, wire2), run_time=2)

        # Add Voltage Animation - changing colors to represent varying voltage
        self.play(circuit.animate.set_color_by_gradient(BLUE, RED), run_time=2)

        # Add Voltage Label with changing graph
        voltage_text = Text("Voltage changes over time").next_to(equation2, DOWN)
        voltage_graph = Axes(
            x_range=[0, 5, 1],
            y_range=[-1, 1, 0.5],
            axis_config={"color": WHITE},
            y_axis_config={"include_numbers": True}
        ).next_to(voltage_text, DOWN)

        voltage_wave = voltage_graph.plot(lambda x: 0.8 * np.sin(x), color=YELLOW)
        self.play(Write(voltage_text), Create(voltage_graph), Create(voltage_wave))

        self.wait(2)

        # Clear the scene after the second animation
        self.play(FadeOut(title2), FadeOut(equation2), FadeOut(circuit), FadeOut(voltage_text), FadeOut(voltage_graph), FadeOut(voltage_wave))
