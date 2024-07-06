from manim import *

class MoveObjectAlongPath(Scene):
    def construct(self):
        # Create a circle path
        circle_path = Circle(radius=2, color=BLUE)
        
        # Create a dot
        dot = Dot(color=RED)
        
        # Animate the dot moving along the circle path
        self.play(MoveAlongPath(dot, circle_path), run_time=4)
        
        # Show the circle path
        # self.add(circle_path)

        # Pause for a moment to see the final position
        self.wait(2)

if __name__ == "__main__":
    scene = MoveObjectAlongPath()
    scene.render()
