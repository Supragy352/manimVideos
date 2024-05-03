from manim import *

class Squaretocircle(Scene):
    def construct(self):
        text13 = Text(
            "Region of Absence : ",
            font_size=30,
            font="Arial",
            color= WHITE,
            )
        text13.shift(UP * 3  , LEFT * 5)
        self.play(Write(text13))
        self.wait(1)
        formula11 = MathTex(
            " x^{2} = a^{2} + (a^{2}b^{2})/(y^{2}-b^{2}) ",
            font_size = 40,
            color= WHITE
            )
        formula11.shift(UP * 2.3 , LEFT * 4.6) 
        self.play(Write(formula11))
        self.wait(1)

        
        formula12 = MathTex(
            " y < -b : x^{2} ",
            font_size = 40,
            color= WHITE
            )
        formula12.shift(UP * 2.4 ) 
        self.play(Write(formula12))
        text14 = Text(
            "is +ve => Curve exists ",
            font_size=30,
            font="Arial",
            color= WHITE,
            )
        text14.shift(UP * 2.4 , RIGHT * 3.3)
        self.play(Write(text14))
        self.wait(1)



        formula13 = MathTex(
            "-b < y < 0 : x^{2} ",
            font_size = 40,
            color= WHITE
            )
        formula13.shift(UP * 1.8 ) 
        self.play(Write(formula13))
        text15 = Text(
            "is -ve => Curve does not exist ",
            font_size=30,
            font="Arial",
            color= WHITE,
            )
        text15.shift(UP * 1.8 , RIGHT * 4.3)
        self.play(Write(text15))
        self.wait(1)


        formula14 = MathTex(
            "0 < y < b : x^{2} ",
            font_size = 40,
            color= WHITE
            )
        formula14.shift(UP * 1.2 ) 
        self.play(Write(formula14))
        text16 = Text(
            "is -ve => Curve does not exist ",
            font_size=30,
            font="Arial",
            color= WHITE,
            )
        text16.shift(UP * 1.2 , RIGHT * 4.2)
        self.play(Write(text16))
        self.wait(1)

        formula15 = MathTex(
            " y > b : x^{2} ",
            font_size = 40,
            color= WHITE
            )
        formula15.shift(UP * 0.6 ) 
        self.play(Write(formula15))
        text17 = Text(
            "is +ve => Curve exists ",
            font_size=30,
            font="Arial",
            color= WHITE,
            )
        text17.shift(UP * 0.6 , RIGHT * 3)
        self.play(Write(text17))
        self.wait(1)

        text18 = Text(
            "For any value of y , ",
            font_size=30,
            font="Arial",
            color= WHITE,
            )
        text18.shift(DOWN * 0.5,LEFT * 5)
        self.play(Write(text18))
        self.wait(1)

        formula16 = MathTex(
            " x^{2}= a^{2} + (a^{2}b^{2})/(y^{2}-b^{2}) ",
            font_size = 40,
            color= WHITE
            )
        formula16.shift(DOWN * 0.5 , LEFT * 0.6) 
        self.play(Write(formula16))
        self.wait(1)

        text19 = Text(
            "Curve does not exist for -a < x < a ",
            font_size=30,
            font="Arial",
            color= WHITE,
            )
        text19.shift(DOWN * 1.3,LEFT * 1)
        self.play(Write(text19))
        self.wait(1)

