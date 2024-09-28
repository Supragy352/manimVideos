from manim import *

class TypesParameters(Scene):

    config.pixel_height=1080
    config.pixel_width=1920
    config.frame_height=18
    config.frame_width=32

    def construct(self):    
        positions = [
            LEFT * 4 + UP * 2,       
            RIGHT * 4 + UP * 2,      
            LEFT * 4 + DOWN * 2,     
            RIGHT * 4 + DOWN * 2    
        ]

        for i, pos in enumerate(positions):

            dot = Dot(point=ORIGIN, color=WHITE)
                        
            screen = Rectangle(width=40, height=25, color=WHITE, stroke_width=5)
            screen.scale(0.1)
            screen.move_to(dot.get_center())

            self.play(Create(dot))            
            self.play(Transform(dot, screen))
            
            axes = Text("Anooj", font_size=150)
            
            graph_group = VGroup(axes).scale(0.2)  
            graph_group.move_to(screen.get_center())

            self.play(Create(graph_group))

            screen_struct = VGroup(graph_group,screen)
            
            self.play(screen_struct.animate.scale(1.0).move_to(pos),Uncreate(dot))

        self.wait(2)
