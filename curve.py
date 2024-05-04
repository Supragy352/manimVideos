from manim import *

class GraphAnimationExample(Scene):
  def construct(self):
    a = 2  # You can change 'a' as per your requirement

    # Create axes
    axes = Axes(
        x_range=[-0.5*a, 3.5*a],
        y_range=[-1.2*a, 1.2*a],
        axis_config={"color": WHITE},
    )

    # Define the graph function (piecewise for absence regions)
    def curve_func(t):
      if t < a or t > 2*a:
        return [np.nan, np.nan, 0]  # Create absence regions (NaN)
      x = t
      y = np.sqrt((a**2 * (2*a - t) * (t - a)) / a**3)  # Corrected equation for y
      return [x, y, 0]

    def curve_func_negative(t):
      if t < a or t > 2*a:
        return [np.nan, np.nan, 0]  # Create absence regions (NaN)
      x = t
      y = -np.sqrt((a**2 * (2*a - t) * (t - a)) / a**3)  # Add negative branch for symmetry
      return [x, y, 0]

    # Create separate parametric functions for positive and negative branches
    curve_pos = ParametricFunction(curve_func, t_range=[a, 2*a], color=BLUE)
    curve_neg = ParametricFunction(curve_func_negative, t_range=[a, 2*a], color=BLUE)

    # Show axes
    self.play(Create(axes), run_time=2)

    # Animate the positive and negative branches of the graph
    self.play(Create(curve_pos), run_time=2)
    self.play(Create(curve_neg), run_time=2)

    # Emphasize points of intersection and tangent points (optional)
    dot1 = Dot(axes.c2p(0, 0), color=RED)  # Point (0, 0)
    # Shift dot2 (assuming it's the second pink dot) one unit to the left
    dot2 = Dot(axes.c2p(a - 1, 0), color=RED)  # Point (a - 1, 0)
    # Shift dot3 (assuming it's the third pink dot) two units to the left
    dot3 = Dot(axes.c2p(2*a - 2, 0), color=RED)  # Point (2a - 2, 0)
    self.play(FadeIn(dot1, dot2, dot3))

    self.wait(1)
