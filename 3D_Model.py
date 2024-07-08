from manim import *
import pywavefront

class ThreeDModelScene(ThreeDScene):
    def construct(self):
        # Load the OBJ file using pywavefront
        obj = pyw avefront.Wavefront("C:\\Users\\Anooj Dilip Archana\\Downloads\\fdx54mtvuz28-FinalBaseMesh\\model.obj",)
        
        # Extract vertices and faces from the loaded object
        vertices = np.array(obj.vertices)
        faces = [face for name, mesh in obj.mesh_list.items() for face in mesh.faces]
        
        # Create the surface from vertices and faces
        surface = Surface(
            lambda u, v: vertices[v],
            u_min=0, u_max=1,
            v_min=0, v_max=len(vertices) - 1,
            resolution=(1, len(vertices))
        )

        # Scale and position the surface
        surface.scale(3)
        surface.rotate(PI / 2, axis=RIGHT)
        surface.set_color(WHITE)
        
        # Add the surface to the scene
        self.add(surface)
        
        # Set the camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # Play an animation rotating the model
        self.play(Rotate(surface, angle=PI, axis=UP, run_time=4))
        self.wait()

# To render the scene, use the command below in the terminal
# manim -pql 3D_Model.py ThreeDModelScene
