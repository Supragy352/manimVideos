from manim import *

from manim import *

class GraphAnimationExample(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-2, 2],
            axis_config={"color": WHITE},
        )

        # Create a graph
        graph1 = axes.plot(lambda x: np.cos(x), color=BLUE)
        graph = axes.plot(lambda x: np.sin(x), color=PINK)
        graph2 = axes.plot(lambda x: np.sin(x)+(x), color=RED)
        graph3 = axes.plot(lambda x: np.tan(x), color=GREEN)
       
        # Show the axes
        self.play(Create(axes),run_time=4)

        # Animate the graph
        self.play(Create(graph1),run_time=5)
        self.play(Create(graph),run_time=5)
        self.play(Create(graph2),run_time=5)
        self.play(Create(graph3),run_time=5)
        self.wait(1)



