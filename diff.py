from manim import *

class ChainRuleScene(ThreeDScene):
    def construct(self):
        title = Text("Chain Rule in Partial Differentiation").scale(0.75).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduce the functions and variables
        eq1 = MathTex(r"u = f(x, y)").shift(UP * 2)
        eq2 = MathTex(r"v = g(y, z)").shift(UP)
        self.play(Write(eq1), Write(eq2))
        self.wait(2)

        # Draw arrows showing dependency
        arrow1 = Arrow(start=LEFT, end=RIGHT).shift(UP * 2 + LEFT * 2)
        arrow2 = Arrow(start=LEFT, end=RIGHT).shift(UP + LEFT * 2)
        self.play(Create(arrow1), Create(arrow2))
        self.wait(1)

        # Show partial derivatives
        chain_rule = MathTex(r"\frac{\partial u}{\partial x} = \frac{\partial u}{\partial y} \cdot \frac{\partial y}{\partial x}").shift(DOWN)
        self.play(Write(chain_rule))
        self.wait(2)

        # Visualize a 3D surface
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        axes = ThreeDAxes()
        surface = Surface(
            lambda u, v: np.array([u, v, u**2 + v**2]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.75
        )
        self.add(axes, surface)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(10 )
        self.stop_ambient_camera_rotation()

        summary = Text("This is how the chain rule links partial derivatives!").shift(DOWN * 3)
        self.play(Write(summary))
        self.wait(2)
