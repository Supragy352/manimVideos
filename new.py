from manim import *

class Hyperbola(Scene):
    def construct(self):
        # Step 1: Symmetry about x-axis
        sym_text = Text("Symmetry about x-axis", font_size=30, color=RED).to_edge(UP)
        self.play(Write(sym_text))
        self.wait()

        # Step 2: Points of Intersection
        points_text = Text("Points of Intersection:", font_size=30, color=RED).to_edge(UP)
        point_1 = MathTex("(0, 0),").next_to(points_text, DOWN).align_to(points_text, LEFT)
        point_2 = MathTex("(a, 0),").next_to(point_1, DOWN).align_to(point_1, LEFT)
        point_3 = MathTex("(2a, 0)").next_to(point_2, DOWN).align_to(point_2, LEFT)
        self.play(Transform(sym_text, points_text), Write(point_1), Write(point_2), Write(point_3))
        self.wait()

        # Step 3: Tangents
        tangent_text = Text("Tangents:", font_size=30, color=RED).to_edge(UP)
        tangent_1 = Text("At (a, 0) parallel to Y-axis", font_size=25).next_to(tangent_text, DOWN).align_to(tangent_text, LEFT)
        tangent_2 = Text("At (2a, 0) parallel to Y-axis", font_size=25).next_to(tangent_1, DOWN).align_to(tangent_1, LEFT)
        self.play(Transform(sym_text, tangent_text), Write(tangent_1), Write(tangent_2))
        self.wait()

        # Step 4: Asymptotes
        asymptote_text = Text("Asymptotes:", font_size=30, color=RED).to_edge(UP)
        self.play(Transform(sym_text, asymptote_text))
        self.wait()

        # Step 5: Region of Absence
        roa_text = Text("Region of Absence:", font_size=30, color=RED).to_edge(UP)
        roa_part1 = Text("x < a", font_size=25).next_to(roa_text, DOWN).align_to(roa_text, LEFT)
        roa_part2 = Text("2a < x", font_size=25).next_to(roa_part1, DOWN).align_to(roa_part1, LEFT)
        self.play(Transform(sym_text, roa_text), Write(roa_part1), Write(roa_part2))
        self.wait()

        # Step 6: Final Curve
        final_text = Text("Final Curve", font_size=30, color=RED).to_edge(UP)
        self.play(Transform(sym_text, final_text))
        self.wait()

        # Drawing the curve
        self.play(FadeOut(sym_text))
        a = 2
        graph = ImplicitFunction(
            lambda x, y: (a ** 2) * (y ** 2) - (x ** 2) * (2 * a - x) * (x - a),
            color=YELLOW
        )
        self.play(Create(graph))
        self.wait()
#manim new rock.py TraceCurve -p -ql
