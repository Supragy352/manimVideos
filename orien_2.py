from manim import *

class GraphLine(Scene):
    def construct(self):
        

        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-1.2, 1.2, 0.2],
            axis_config={"font_size": 42},
        ).add_coordinates()

        curve = ax.plot(lambda x: np.sin(x)  / np.e ** 2 * x)
        curve1 = ax.plot(lambda x: np.cos(x)  / np.e ** 2 * x)



        lines = ax.get_vertical_lines_to_graph(
            curve, x_range=[0, 9.2], num_lines=70, color=BLUE
        )

        lines1 = ax.get_vertical_lines_to_graph(
            curve1, x_range=[0, 9.2], num_lines=70, color=RED
        )


        self.play(Create(ax), run_time=3)
        self.play(Create(curve), Create(curve1), run_time=5)
        self.play(Create(lines), Create(lines1), run_time=5)
        self.wait(10)