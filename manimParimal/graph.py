from manim import *

class Graph_movement(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=10,
            y_length=10,
        ).add_coordinates()
        axes.to_edge(UR)
        
        x_label = Tex("x").next_to(axes.x_axis, UR)
        y_label = Tex("f(x)").next_to(axes.y_axis, UR)
        
        graph = ParametricFunction(lambda t: np.sin(t), color=YELLOW)
        graphing_stuff = VGroup(axes, graph, x_label, y_label)

        self.play(DrawBorderThenFill(axes), Write(x_label), Write(y_label))
        self.play(Create(graph))
        self.wait(3)
