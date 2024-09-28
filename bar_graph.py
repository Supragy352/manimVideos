# from pathlib import Path
# import pandas as pd
# from manim import *
# file_path = Path("C:\\GEN1_AI\\Dataset\\Machine_Learning\\medical-charges.csv" )

# csv_df = pd.read_csv(file_path).set_index('age')
# csv_df.head(7)



# class BarGraphAnimation(Scene):
#     def construct(self):
#         self.camera.background_color = WHITE

#         bar_names = csv_df.columns
#         initial_values = list(csv_df.iloc[0])

#         chart = BarChart(
#         	values=initial_values,
#             bar_names='bar_names',
#             y_range=[10,40,5],
#             y_length=6.5,
#             x_length=10,
#             x_axis_config={
#                 "font_size":20,
#                 "label_direction":DOWN
#             },
#             axis_config = {
#                 'color':BLACK,
#                 'tip_shape': StealthTip
#             }
#         )

#         for tick in chart.get_x_axis():
#             tick.set_color(BLACK)

#         for tick in chart.get_y_axis():
#             tick.set_color(BLACK)
            

#         labels = chart.get_axis_labels(
#             Tex("dogs", color=BLACK).scale(0.7),
#             Tex("weight", color=BLACK).scale(0.8)
#         )

#         self.add(chart, labels)

#         date_text = Tex(csv_df.index[0], color=BLUE_E)
#         date_text.move_to(UP*2 + RIGHT*3)
#         self.play(Create(date_text))

#         for i, row in enumerate (csv_df.itertuples()):
#             date_str = row[0]
#             new_date = Tex(date_str, color=BLUE_E)
#             weights = list(row[1:])

#             if i == 0:
#                 continue
#             elif i > 10:
#                 break


#             self.play(
#                 Create(chart),
#                 rate_fun=linear,
#                 run_time=0.2
#             )




# from typing_extensions import runtime
from manim import *
 
# class BarChartExample(Scene):
#     def construct(self):
#         chart = BarChart(
#             values=[-5, 40, -10, 20, -3],
#             bar_names=["one", "two", "three", "four", "five"],
#             y_range=[-20, 50, 10],
#             y_length=6,
#             x_length=10,
#             x_axis_config={"font_size": 36}
#         )
 
#         c_bar_lbls = chart.get_bar_labels(font_size=48)
 
#         self.play(Create(chart), Create(c_bar_lbls))



class ChangeBarValuesExample(Scene):
    def construct(self):
        values=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        final_values = [33.1, 36, 29.25, 33.58, 4, 4.5, 5, 4.3, 7.2, 5.5]
 
        chart = BarChart(
            values,
            y_range=[0, 40, 5],
            y_length=6.5,
            x_length=10,
            y_axis_config={"font_size": 24},
        )
        self.play(Create(chart))
        self.wait(2)
 
        self.play(chart.animate.change_bar_values(final_values), run_time=3)
        self.play(Create(chart.get_bar_labels(font_size=36))) 
 
        self.wait(3)