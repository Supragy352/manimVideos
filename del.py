# from manim import *
# import matplotlib.pyplot as plt

# class Example(Scene):
#     def construct(self):
#         self.camera.background_color= WHITE
#         fig = plt.figure(dpi=300)
#         ax = fig.add_subplot(projection='3d')
#         x=np.full((21,27,27),0)
#         x[10,10,10]=1
#         x[10,16,10]=1
#         ax.voxels(x, edgecolor='k')
#         fig.canvas.draw()
#         buf = fig.canvas.buffer_rgba()
#         img = ImageMobject(buf).scale(1)
#         plt.close(fig)
#         self.add(img)

# from manim import *
# from sklearn.datasets import make_blobs
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set()
# MAX_N=400
# X, y = make_blobs(
#     n_samples=MAX_N,
#     n_features=2,
#     centers=3,
#     cluster_std=0.8,
#     shuffle=True,
#     random_state=0,
# )
# def plot(param):
#     fig, ax = plt.subplots(figsize = (4,3) , dpi = 250)
#     param = int(param)
#     X_show = X[:param, :]
#     ax.set_xlim(-4,4)
#     ax.set_ylim(-1,6)

#     ax.scatter(X_show[:, 0], X_show[:, 1], s=50, c="lightgray", edgecolor="black")
#     fig.canvas.draw()
#     img = ImageMobject(fig.canvas.buffer_rgba())
#     plt.close(fig)
#     return img


# class ShowScreenResolution(Scene):
#     def construct(self):
#         pyFrame = config["pixel_height"]  # 1080 default
#         pxFrame = config["pixel_width"]  # 1920 #default
#         frame_width = config["frame_width"]
#         frame_height = config["frame_height"]
#         d1 = Line(frame_width * LEFT / 2, frame_width * RIGHT / 2).to_edge(DOWN)
#         self.add(d1)
#         self.add(Tex(str(pxFrame)).scale(0.5).next_to(d1, DOWN, buff=0))
#         d2 = Line(frame_height * UP / 2, frame_height * DOWN / 2).to_edge(LEFT)
#         self.add(d2)
#         self.add(
#             Tex(str(pyFrame)).scale(0.5).rotate(90 * DEGREES).next_to(d2, LEFT, buff=0)
#         )
#         img = plot(0)
#         self.add(Text("My animated plot").next_to(img,UP))
#         self.play(FadeIn(img))
#         tr_amplitude = ValueTracker(0)
#         def update_image(mob):
#             new_mob = plot(tr_amplitude.get_value())
#             mob.become(new_mob)

#         img.add_updater(update_image)
#         self.play(tr_amplitude.animate.set_value(MAX_N), run_time=3)



# class Example(Scene):
#     def construct(self):
#         x = np.linspace(0, 30, 400)
#         amplitude = 0.5
#         self.camera.background_color = "#ece6e2"
#         fig, ax = plt.subplots()
#         ax.plot(x, amplitude * np.sin(x))
#         ax.set_ylim(-1, 1)
#         plt.savefig("test.svg")
#         plt.close(fig)
#         img = SVGMobject("test.svg").scale(3)
#         self.add(img)
#         for i in img.submobjects[:-18]: # replace with img.submobjects
#             self.play(i.animate.set_color(ORANGE), run_time = 0.1)


from manim import *
 
# class BarChartExample(Scene):
#     def construct(self):
#         chart = BarChart(
#             values=[-5, 40, -10, 20, -3],
#             bar_names=["one", "two", "three", "four", "five"],
#             y_range=[-20, 50, 10],
#             y_length=6,
#             x_length=10,
#             x_axis_config={"font_size": 36},
#         )
 
#         c_bar_lbls = chart.get_bar_labels(font_size=48)
 
#         self.add(chart, c_bar_lbls)


class ChangeBarValuesExample(Scene):
    def construct(self):
        values=[28, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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