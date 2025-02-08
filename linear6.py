from manim import *

class DifferentialEquations(Scene):
    def construct(self):
        self.introduction_with_theory()
        self.clear_scene()
        self.mechanical_vibrations_animation()
        self.clear_scene()
        self.rlc_circuit_animation()
        self.clear_scene()
        self.population_dynamics_animation()

    def introduction_with_theory(self):
        # Introduction Title
        title = Text("Second Order Differential Equations", font_size=40)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))

        # Small Theory Introduction
        theory_text = Text(
            "Second-order differential equations are widely used in real-world applications.", 
            font_size=24
        ).next_to(title, DOWN)
        self.play(Write(theory_text))
        self.wait(2)

        # Display General Form
        general_form = MathTex(r"m\frac{d^2x}{dt^2} + c\frac{dx}{dt} + kx = F(t)").scale(0.8).next_to(theory_text, DOWN)
        self.play(Write(general_form))
        self.wait(2)

        # Transition to Mechanical Vibrations Application
        self.clear_scene()

    def mechanical_vibrations_animation(self):
        # Mechanical Vibrations
        app_title_1 = Text("Application 1: Mechanical Vibrations", font_size=32).to_edge(UP)
        self.play(Write(app_title_1))

        # Brief explanation
        mech_vib_text = Text(
            "The motion of a spring-mass system is modeled by the equation:", font_size=24
        ).next_to(app_title_1, DOWN)
        self.play(Write(mech_vib_text))

        # Mechanical Vibrations Equation
        mech_vib_eq = MathTex(r"m\frac{d^2x}{dt^2} + kx = 0").scale(0.8).next_to(mech_vib_text, DOWN)
        self.play(Write(mech_vib_eq))
        self.wait(2)

        # Transition to RLC Circuit Application
        self.clear_scene()

    def rlc_circuit_animation(self):
        # RLC Circuit
        app_title_2 = Text("Application 2: RLC Circuit", font_size=32).to_edge(UP)
        self.play(Write(app_title_2))

        # Explanation
        rlc_text = Text(
            "RLC circuit's voltage and current dynamics are modeled by the equation:", font_size=24
        ).next_to(app_title_2, DOWN)
        self.play(Write(rlc_text))

        # RLC Equation
        rlc_eq = MathTex(
            r"L\frac{d^2q}{dt^2} + R\frac{dq}{dt} + \frac{q}{C} = V(t)"
        ).scale(0.8).next_to(rlc_text, DOWN)
        self.play(Write(rlc_eq))

        # Placeholder for Circuit Components
        resistor = Square(color=RED).scale(0.8).shift(LEFT)
        inductor = Square(color=GREEN).scale(0.8)
        capacitor = Square(color=YELLOW).scale(0.8).shift(RIGHT)

        components = VGroup(resistor, inductor, capacitor).arrange(RIGHT, buff=1).next_to(rlc_eq, DOWN)
        self.play(FadeIn(components))

        self.wait(2)

        # Transition to Population Dynamics
        self.clear_scene()

    def population_dynamics_animation(self):
        # Population Dynamics
        app_title_3 = Text("Application 3: Population Dynamics", font_size=32).to_edge(UP)
        self.play(Write(app_title_3))

        # Brief Explanation
        pop_dyn_text = Text(
            "Population growth in ecology and biology can be modeled using differential equations.", font_size=24
        ).next_to(app_title_3, DOWN)
        self.play(Write(pop_dyn_text))

        # Population Dynamics Equation
        pop_dyn_eq = MathTex(
            r"\frac{d^2P}{dt^2} + r \frac{dP}{dt} - P \left(1 - \frac{P}{K}\right) = H(t)"
        ).scale(0.8).next_to(pop_dyn_text, DOWN)
        self.play(Write(pop_dyn_eq))
        self.wait(2)
        
        # Clear the scene
        self.clear_scene()

    def clear_scene(self):
        # Properly fade out all mobjects in the scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
