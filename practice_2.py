from manim import *

class Load3DModel(ThreeDScene):
    def construct(self):
        # Set up the 3D camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Load the .obj model
        model = OpenGLSurface(
            File("C:\\Users\\Anooj Dilip Archana\\Desktop\\INSIDE BEARING v2.obj"),
            fill_color=BLUE,  # You can customize the color
            fill_opacity=1.0
        )

        # Add the model to the scene
        self.add(model)

        # Add some animation (optional)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(10)

