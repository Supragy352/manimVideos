from manim import *

class Surface(ThreeDScene):

    config.pixel_height=1080
    config.pixel_width=1920
    config.frame_height=18
    config.frame_width=32

    def construct(self):

        resolution_fa = 32
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(0.35)
        axes = ThreeDAxes(x_range=(-16, 16, 1), y_range=(-16, 16, 1), z_range=(-16, 16, 1))

        def param_trig(u, v):
            x = u
            y = v
            z = 3 * np.sin(x) + 2 * np.cos(y)
            return z

        trig_plane = axes.plot_surface(
            param_trig,
            resolution=(resolution_fa, resolution_fa),
            u_range = (-15, 15),
            v_range = (-15, 15),
            colorscale = [BLUE, GREEN, YELLOW, ORANGE, RED],
            
            )
        self.play(Create(axes), run_time=2)
        self.play(Create(trig_plane), run_time=5)
        self.wait(10)

        self.set_camera_orientation(phi=15 * DEGREES, theta=-20 * DEGREES)

        self.play(Create(axes), run_time=2)
        self.play(Create(trig_plane), run_time=5)
        self.wait(10)