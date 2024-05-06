from manim import *

SUB_SIZE = 30
SS_SIZE = 26
class TraceCurve(Scene):
    def construct(self):
        
        ################################ Graph Code ########################################

        plane = Axes(x_range=[-5, 5], y_range=[-4, 4], x_length=10, y_length=8)

        point = Dot(color=BLUE,stroke_width=6).move_to(plane.coords_to_point(0, 0))

        curve = plane.plot(lambda x: x / (1 + x**2), color=RED)
        
        y_equals_x_line = DashedLine(
            plane.coords_to_point(-4, -4),
            plane.coords_to_point(4, 4),
            dash_length=0.15,
            stroke_width=2,  
        )

        origin = plane.coords_to_point(0, 0)
        
        shading1 = Rectangle(width=plane.x_length/2, height=plane.y_length/2, color=BLUE, fill_opacity=0.3, stroke_width=0)
        shading1.move_to(origin + RIGHT * plane.x_range[1]/2 + UP * plane.y_range[1]/2)
        
        shading2 = Rectangle(width=plane.x_length/2, height=plane.y_length/2, color=BLUE, fill_opacity=0.3, stroke_width=0)
        shading2.move_to(origin - RIGHT * plane.x_range[1]/2 + DOWN * plane.y_range[1]/2)

        shading3 = Rectangle(width=plane.x_length/2, height=plane.y_length/2, color=BLUE, fill_opacity=0.3, stroke_width=0)
        shading3.move_to(origin - RIGHT * plane.x_range[1]/2 + UP * plane.y_range[1]/2)
        
        shading4 = Rectangle(width=plane.x_length/2, height=plane.y_length/2, color=BLUE, fill_opacity=0.3, stroke_width=0)
        shading4.move_to(origin + RIGHT * plane.x_range[1]/2 + DOWN * plane.y_range[1]/2)


        x_axis = Line(plane.coords_to_point(plane.x_range[0], 0), plane.coords_to_point(plane.x_range[1], 0), color=GREEN)

        graph = VGroup(plane, curve, point, shading1, shading2,shading3, shading4, y_equals_x_line, x_axis).shift(RIGHT * 4.5 + DOWN * 1.5).scale(0.4)

        ###################################################################################

        
        trace = Text(text= "Trace the Following Curve",color=BLUE,font_size=35)
        
        given_eqn = MathTex( r" y = \frac{x}{1+{x^2}}",font_size = 50)
        
        self.wait(1)
        self.add(trace.shift(UP*1.5))
        self.play(Write(given_eqn),run_time=1)

        self.play(ApplyMethod(given_eqn.shift, UP * 2.6),FadeOut(trace), run_time=1)

        sym = Text(text = "a) Symmetry : ",font_size=SUB_SIZE )
        poi = Text(text = "b) Point of Intersection : ",font_size=SUB_SIZE )
        tang = Text(text = "c) Tangent : ",font_size=SUB_SIZE , line_spacing=1.5)
        asym = Text(text = "d) Asymptote : ",font_size=SUB_SIZE , line_spacing=1.5)
        roa = Text(text = "e) Region of Absence : ",font_size=SUB_SIZE , line_spacing=1.5)

        sub_sym = Text("If we replace x with -x and y with -y, no change occurs.\n\n ∴ Symmetric about opposite quadrant.", font_size=SS_SIZE)


        self.play(Write(sym.shift(UP*1.8 + LEFT*5.6 )))
        self.play(Write(sub_sym.shift(UP*0.8 + LEFT*1.5 ),run_time=3))


        self.play(Create(plane), Create(shading1,run_time=2),Create(shading2,run_time=2))
        self.play(FadeOut(shading2,shading1))
        self.play(Create(shading3,run_time=2),Create(shading4,run_time=2) )
        self.play(FadeOut(shading3,shading4))

        sub_poi = Text(f"If we put x = {0} then y becomes {0} \n\n ∴ Passing through origin", font_size=SS_SIZE)

        self.play(FadeOut(sym,sub_sym))
        self.wait()
        self.play(Write(poi.shift(UP*1.8 + LEFT*4.7 )))
        self.play(Write(sub_poi.shift(UP*0.8 + LEFT*3.3 ),run_time=3))

        
        self.play(Create(point))


        sub_tang = Text("At Origin : Equating lowest degree term to zero", font_size=SS_SIZE)
        msub_tang1 = MathTex(r" y{ ({1}+{x^2}}) = {x}")
        msub_tang2 = MathTex(r" y + y{x^2} - x = 0")
        msub_tang3 = MathTex(r" y - x = 0 ")
        msub_tang4 = MathTex(r" y = x")
        
        self.play(FadeOut(poi,sub_poi))
        self.wait()
        self.play(Write(tang.shift(UP*1.8 + LEFT*5.8 )))
        self.play(Write(sub_tang.shift(UP*1.1 + LEFT*2.2 ),run_time=3))
        self.play(Write(msub_tang1.shift(UP*0.3 + LEFT*2.2 )))
        self.play(Write(msub_tang2.shift(UP*-0.5 + LEFT*2.2 )))
        self.play(Write(msub_tang3.shift(UP*-1.3 + LEFT*2.2 )))
        self.play(Write(msub_tang4.shift(UP*-2.1 + LEFT*2.2 )))


        self.play(Create(y_equals_x_line))


        sub_asym1 = Text("||el to x axis : Equating Highest degree coefficient of x term to zero", font_size=SS_SIZE)
        msub_asymx1 = MathTex(r" y + y{x^2} - x = 0")
        msub_asymx2 = MathTex(r" y = 0")

        sub_asym2 = Text("||el to y axis : Equating Highest degree coefficient of y term to zero", font_size=SS_SIZE)
        msub_asymy1 = MathTex(r" y + y{x^2} - x = 0")
        msub_asymy2 = MathTex(r" 1 + {x^2} = 0")
        msub_asymy3 = MathTex(r" {x^2} = -1")
        msub_asymy4 = Text("Which is not possible ∴ No Asymptote ||el to y axis",font_size=SS_SIZE)
        

        self.play(FadeOut(tang,sub_tang,msub_tang1,msub_tang2,msub_tang3,msub_tang4))
        self.wait()
        self.play(Write(asym.shift(UP*1.8 + LEFT*5.6 )))
        self.play(Write(sub_asym1.shift(UP*1.1 + LEFT*0.6 ),run_time=3))
        self.play(Write(msub_asymx1.shift(UP*0.3 + LEFT*2.2 )))
        self.play(Write(msub_asymx2.shift(UP*-0.5 + LEFT*2.2 )))


        ###################################

        self.play(Create(x_axis))

        ##################################

        self.play(FadeOut(sub_asym1,msub_asymx1,msub_asymx2))
        self.play(Write(sub_asym2.shift(UP*1.1 + LEFT*0.6 ),run_time=3))
        self.play(Write(msub_asymy1.shift(UP*0.3 + LEFT*2.2 )))
        self.play(Write(msub_asymy2.shift(UP*-0.5 + LEFT*2.2 )))
        self.play(Write(msub_asymy3.shift(UP*-1.3 + LEFT*2.2 )))
        self.play(Write(msub_asymy4.shift(UP*-2.1 + LEFT*2.2 ),run_time=2))


        self.play(FadeOut(asym,sub_asym2,msub_asymy1,msub_asymy2,msub_asymy3,msub_asymy4))
                
        sub_roa = Text("When : ", font_size=SS_SIZE)
        msub_roa1 = MathTex(r" x > 0 \Rightarrow y > 0")
        msub_roa2 = MathTex(r" x < 0 \Rightarrow y < 0")
        msub_roa3 = Text("The curve will exist in I and III Quadrant",font_size=SS_SIZE)

        self.wait(1)

        self.play(Write(roa.shift(UP*1.8 + LEFT*4.8 )))
        self.play(Write(sub_roa.shift(UP*1.1 + LEFT*2.6 )))
        self.play(Write(msub_roa1.shift(UP*0.3 + LEFT*2.2 )))
        self.play(Write(msub_roa2.shift(UP*-0.5 + LEFT*2.2 )))
        self.play(Write(msub_roa3.shift(UP*-1.3 + LEFT*2.2 )))
        
        self.play(Create(shading1,run_time=3),Create(shading2,run_time=3) )


        self.play(FadeOut(roa,sub_roa,msub_roa1,msub_roa2,msub_roa3))
        self.play(FadeOut(curve,plane,point,y_equals_x_line,x_axis,given_eqn,shading1,shading2))

        plane = Axes(x_range=(-3,3),y_range=(-2,2),y_length=7.4,x_length=13.2)


        curve = plane.plot(lambda x: x / (1 + x**2), color=BLUE)
        

        self.play(Create(curve,run_time=4),Create(plane))

        self.wait(4)