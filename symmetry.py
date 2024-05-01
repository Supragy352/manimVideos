# from manim import *

# class LineSymmetry(Scene):
# 	def construct(self):
# 		start = np.array((0,-7,0))
# 		end = np.array((0,7,0))
# 		line = Line(start, end, color=BLUE)

# 		self.play(Create(line), color = BLUE)
# 		self.wait(2)

from manim import *

class PlotLine(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": range(-4, 5)},
            y_axis_config={"numbers_to_include": range(-4, 5)}
        )
        
        line = Line(start=[0, -3, 0], end=[0, 3, 0], color=GREEN)

        self.play(Create(axes), Create(line))
        self.wait(1)

# To render this scene, you can use the following command:
# manim filename.py PlotLine -pql
