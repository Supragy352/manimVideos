from manim import *

class DerivativeIntroduction(Scene):
    config.pixel_height = 1080 
    config.pixel_width = 1920
    config.frame_height = 18
    config.frame_width = 32
    def construct(self):
        title = Text("Introduction to Derivatives").scale(1.5)
        title.to_edge(UP)
        self.play(Write(title))
        
        intro_text = Text("""
        In calculus, a derivative represents the rate at which a function is changing at any given point.
        """)
        intro_text.next_to(title, DOWN, buff=1)
        self.play(FadeIn(intro_text))d
        
        self.wait(2)
        
        func = MathTex("f(x) = x^2")
        func.next_to(intro_text, DOWN, buff=1.5)
        self.play(Write(func))
        
        tangent_line = MathTex("f'(x) = 2x")
        tangent_line.next_to(func, DOWN, buff=1.5)
        self.play(Write(tangent_line))
        
        self.wait(2)

        self.play(FadeOut(func), FadeOut(tangent_line), FadeOut(intro_text))
        
        graph = Axes(
            x_range=[-3, 3],
            y_range=[-1, 9],
            axis_config={"color": BLUE}
        )
        
        graph_labels = graph.get_axis_labels(x_label="x", y_label="f(x)")
        parabola = graph.plot(lambda x: x**2, color=YELLOW)
        parabola_label = graph.get_graph_label(parabola, label="x^2")
        
        self.play(Create(graph), Write(graph_labels))
        self.play(Create(parabola), Write(parabola_label))
        
        dot = Dot().move_to(graph.coords_to_point(1,1))
        dot_2 = Dot().move_to(graph.coords_to_point(2,4))
        dot_label = MathTex("A(1,1)").next_to(dot, RIGHT)
        self.play(FadeIn(dot, dot_2, scale=0.5), Write(dot_label))
        
        tangent = graph.plot(lambda x: 2*x - 1, x_range=[-3, 3], color=RED)
        tangent_label = graph.get_graph_label(tangent, label="Tangent Line", x_val=-7.1, direction=DOWN)
        self.play(Create(tangent), Write(tangent_label))
        
        self.wait(3)
