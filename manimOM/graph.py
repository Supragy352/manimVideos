from manim import *
import numpy as np

class ArcsinExample(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-1, 1, 0.1],  # Ensure x values fall within [-1, 1]
            y_range=[-np.pi/2, np.pi/2, 0.1],  # Range for arcsin
            axis_config={"color": BLUE},
        )

         # Define the function for arcsin curve
        def arcsin_function(x):
             return np.arcsin(x)

         # Plot arcsin curve
        arcsin_curve = axes.plot(lambda x: arcsin_function(x))

         # Add labels
        arcsin_label = axes.get_graph_label(arcsin_curve, label="arcsin(x)", x_val=0.5, direction=DOWN)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

         # Show everything
        self.play(Create(VGroup(axes, axes_labels, arcsin_label)),run_time=5)
        self.play(Create(arcsin_curve),run_time=6)

        self.wait()
# from manim import *

# class PangoRender(Scene):
#     def construct(self):
#         morning = Text("Jai Shree Ram", font="sans-serif")
#         self.play(Write(morning))
#         self.wait(2)