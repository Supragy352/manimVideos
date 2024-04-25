from math import sin
from manim import *

class RoseCurve(Scene):
    def construct(self):
        
        def rose_curve(t):
            n = 4  
            x = np.cos(n * t) * np.cos(t)
            y = np.cos(n * t) * np.sin(t)
            return np.array([x, y, 0])

        rose = ParametricFunction(rose_curve, t_range=[0, 2*PI], color=WHITE)
        
        axes = Axes(
            x_range=[-1.5, 1.5, 0.4],  
            y_range=[-1.5, 1.5, 0.4],  
            x_length=8,  
            y_length=8,  
            axis_config={"color": BLUE},
            tips=True
        )

        self.add(axes)
   
        self.play(Create(rose),run_time=4)

        self.wait(2)
