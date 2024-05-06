from os import write
from manim.opengl import scale_matrix
from manim.utils import tex
from typing_extensions import runtime
import numpy as np
from manim import *


        

class Curvetracing(Scene):
    def construct(self):

        text = Text("Curve tracing using Manim").scale(1.2)
        self.play(Create(text))
        self.wait(2)
        self.play(FadeOut(text))

        ax = Axes(
            x_range = [-6,6], y_range=[-6,6],)
        ax.set_color(WHITE)
        ax_labels= ax.get_axis_labels(x_label='x-axis',y_label='y-axis')
        self.add(ax,ax_labels)
        point1= Dot(point=np.array([0,0,0]),color=RED)
        point1_label=Tex("(0,0)").next_to(point1,LEFT+DOWN)
        point2= Dot(point=np.array([0,1,0]),color=RED)
        point2_label=Tex("(0,2a)").next_to(point2,RIGHT+UP)
        curve1 = ax.plot_parametric_curve (lambda t: np.array([np.sqrt(2*t**3 - t**4) if(2*t**3-t**4) >= 0 else 0, t,0]),
            color=BLUE, t_range=[0, 2])
        tangent1= Line(start=np.array([-2,1,0]),end=np.array([2,1,0]),color=GREEN)
        tangent2=Line(start=np.array([0,2,0]),end=np.array([0,-2,0]),color=GREEN)
        curve2 = ax.plot_parametric_curve (lambda t: np.array([- np.sqrt(2*t**3 - t**4) if(2*t**3-t**4) >= 0 else 0, t,0]),
            color=BLUE, t_range=[0, 2])
        region_of_absence=Polygon(ax.c2p(-6,2),ax.c2p(6,2),ax.c2p(6,0),ax.c2p(-6,0),fill_color=GREEN,fill_opacity=0.3)
        graph = VGroup(ax,curve1,curve2,tangent1,tangent2, point1,point2,point1_label,point2_label,region_of_absence,ax_labels).shift(UP*1+RIGHT*3).scale(0.6)
        


        text = Text("Tracing the curve:", font_size=30)
        equation=MathTex("a^2x^2=y^3(2a-y)",font_size=30)
        text.shift(UP*3 +LEFT*3.5)
        equation.next_to(text,RIGHT)
        self.play(Create(text))
        self.play(Create(equation))
        self.wait(1)
        self.play(Uncreate(text))
        solution1=Text("Symmetry: About y axis.\n").shift(LEFT*3).scale(0.6)
        self.play(Write(solution1))
        self.wait(1)
        self.play(FadeOut(solution1))
        solution2=Text("Point of Intersection: \nx_intercept and y_intercept\n").shift(LEFT*3).scale(0.6)
        x_intercept=MathTex(": y=0\n \Longrightarrow x=0").shift(LEFT*3+DOWN*1).scale(0.6)
        y_intercept=MathTex(":x=0\n \Longrightarrow y=0  and  y=2a").shift(LEFT*3+DOWN*1.5).scale(0.6)
        text1=MathTex(r" \rightarrow (0,0)  and  (0,2a)").shift(LEFT*3+DOWN*2).scale(0.6)
        self.play(Write(solution2))
        self.wait(1)
        self.play(Write(x_intercept),Write(y_intercept))
        self.wait(1)
        self.play(Write(text1))
        self.play(Create(point1),Create(point2),Create(point1_label),Create(point2_label))
        self.play(FadeOut(solution2))
        self.play(FadeOut(x_intercept),FadeOut(y_intercept))
        self.play(FadeOut(text1))
        self.wait(1)
        solution3=Text("AT (0,0): \n").shift(LEFT*3).scale(0.6)
        text2=MathTex("dy/dx="r"\infty").shift(LEFT*3+DOWN*1)
        solution6=Text("At (0,2a): \n").shift(LEFT*3).scale(0.6)
        text3=MathTex("dy/dx=0").shift(LEFT*3+DOWN*1)
        self.play(Write(solution3))
        self.play(Write(text2))
        self.wait()
        self.play(Create(tangent2))
        self.wait(1)
        self.play(FadeOut(solution3),FadeOut(text2))
        self.wait(1)
        self.play(Write(solution6))
        self.play(Write(text3))
        self.wait()
        self.play(Create(tangent1))
        self.wait(1)
        self.play(FadeOut(solution6),FadeOut(text3))
        self.wait(1)
        solution4=Text("Asymptotes: No Assymptote parallel to x and y-axis.\n").shift(LEFT*2).scale(0.6)
        self.play(Write(solution4))
        self.wait(1)
        self.play(FadeOut(solution4))
        solution5=Text("Region of Absence:\n").shift(LEFT*3).scale(0.6)
        self.play(Write(solution5))
        self.wait(1)
        self.play(FadeOut(solution5))
        roI=Text("y<0 : Absent \n0<y<2a : Present \ny<0 : Absent").shift(LEFT*3).scale(0.6)
        self.play(FadeIn(roI))
        self.play(Create(region_of_absence))
        self.wait(1)
        self.play(Uncreate(region_of_absence))
        self.wait(1)
        self.play(Create(curve1),Create(curve2))
        self.wait(2)
        self.clear()
        