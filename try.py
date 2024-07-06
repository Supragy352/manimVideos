from manim import *

class ZoomInOutTitle(Scene):
    def construct(self):
        # Create the first letter with a larger font size
        first_letter = Text("C", font_size=164, color=WHITE)

        self.play(first_letter.animate.scale(1.2).shift(UP*0.5), run_time=0.7)
        self.play(first_letter.animate.scale(0.8).shift(DOWN*0.5), run_time=0.5)
        self.play(first_letter.animate.scale(1).set_color(WHITE).move_to(ORIGIN), run_time=1)
        
        # Create the rest of the title with a smaller font size
        rest_of_title = Text("alculus", font_size=72, color=WHITE)
        
        # Position the rest of the title relative to the first letter
        rest_of_title.next_to(first_letter, RIGHT, buff=0.1)
        
        # Group the two parts together
        title_group = VGroup(first_letter, rest_of_title).move_to(ORIGIN)
        
        # Zoom in the title group
        self.play(title_group.animate.scale(1.5).set_color(RED).move_to(ORIGIN), run_time=2)
        
        # Rotate and change color
        self.play(title_group.animate.rotate(PI/4).set_color(GREEN), run_time=1)
        
        # Zoom out the title group
        self.play(title_group.animate.scale(0.7).set_color(BLUE), run_time=2)
        
        # Rotate back and move down
        self.play(title_group.animate.rotate(-PI/4).move_to(DOWN), run_time=1)
        
        # Final bounce effect
        self.play(title_group.animate.scale(1.2).shift(UP*0.5), run_time=0.5)
        self.play(title_group.animate.scale(0.8).shift(DOWN*0.5), run_time=0.5)
        self.play(title_group.animate.scale(1).set_color(YELLOW).move_to(ORIGIN), run_time=1)
        
        # Pause to display the final title
        self.wait(2)

if __name__ == "__main__":
    scene = ZoomInOutTitle()
    scene.render()
