from manim import *

# class FittingObjects(Scene):  # Inherit from Scene class
#      def construct(self):
#          axes = Axes(x_range=[-10, 10, 1], y_range=[-10, 10, 1], x_length=10, y_length=10)

#          circle = Circle(stroke_color=WHITE, fill_color=RED, fill_opacity=0.5, radius=0.3)
        


#          self.play(Write(axes))
#          self.play(DrawBorderThenFill(circle))
#          self.play(circle.animate.shift(RIGHT * 2), run_time=2)
#          self.play(circle.animate.shift(DL * 2), run_time=2)
#          self.play(circle.animate.shift(UL * 2), run_time=2)
#          self.play(circle.animate.shift(UR * 2), run_time=2)
#          self.play(circle.animate.shift(DOWN * 2), run_time=2)
       
        

# To render the animation, you need to run this script using the manim command-line tool.
# For example: manim your_script_name.py FittingObjects -p 

# class update(Scene):
#     def construct(self):
#         r = ValueTracker(0.5)
#         circle = always_redraw(lambda : 
#         Circle(radius = r.get_value(), stroke_color=WHITE, stroke_width=3))
#         line_radius = always_redraw(lambda : 
#         Line(start = circle.get_center(), end = circle.get_bottom(), stroke_color=RED_B, stroke_width = 6))
#         line_circumference = always_redraw(lambda : 
#         Line(stroke_color=YELLOW, stroke_width=6). set_length(2 * r.get_value() * PI).next_to(circle, DOWN, buff=0.2))

#         triangle = always_redraw(lambda : 
#         Polygon(circle.get_top(), circle.get_left(), circle.get_right(), fill_color=GREEN_D))

#         self.play(LaggedStart(
#         Create(circle), DrawBorderThenFill(line_radius), DrawBorderThenFill(triangle), run_time=4, lag_ratio=0.75)) 
#         self.play(ReplacementTransform(circle.copy(), line_circumference), run_time=2)
#         self.play(r.animate.set_value(2), run_time=5)
        

class Graph_movement(Scene):
        def construct(self):
             axes = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=5, y_length=3,
             axis_config = {"include_tip":True, "numbers_to_exclude":[0]}).add_coordinates()
             axes.to_edge(UR) 
             axis_labels = axes.get_x_axis_labels(x_label = "x", y_label = "f(x)")
             graph = axes.get_graph(lambda x : x ** 0.5, x_range=[0,4], color = YELLOW)
             graphing_stuff = VGroup(axes, graph, axis_labels)

             self.play(DrawBorderThenFill(axes), Write(axis_labels))
             self.play(Create(graph))
             self.play(graphing_stuff.animate.shift(DOWN * 4))
             self.play(axes.animate.shift(LEFT * 3), run_time = 3)

# from manim import *

# class HelloWorld(Scene):
#     def construct(self):
#         text = Text("Hello world", font_size=144)
#         self.add(text)
          