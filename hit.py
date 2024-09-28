from manim import *

class ThreeDCamera(Scene, Camera):
    def __init__(
        self,
        focal_distance=20.0,
        shading_factor=0.2,
        default_distance=5.0,
        light_source_start_point=9 * DOWN + 7 * LEFT + 10 * OUT,
        should_apply_shading=True,
        exponential_projection=False,
        phi=0,
        theta=-90 * DEGREES,
        gamma=0,
        zoom=1,
        **kwargs,
    ):
        """Initializes the ThreeDCamera

        Parameters
        ----------
        *kwargs
            Any keyword argument of Camera.
        """
        self._frame_center = Point(kwargs.get("frame_center", ORIGIN), stroke_width=0)
        super().__init__(**kwargs)
        self.focal_distance = focal_distance
        self.phi = phi
        self.theta = theta
        self.gamma = gamma
        self.zoom = zoom
        self.shading_factor = shading_factor
        self.default_distance = default_distance
        self.light_source_start_point = light_source_start_point
        self.light_source = Point(self.light_source_start_point)
        self.should_apply_shading = should_apply_shading
        self.exponential_projection = exponential_projection
        self.max_allowable_norm = 3 * config["frame_width"]
        self.phi_tracker = ValueTracker(self.phi)
        self.theta_tracker = ValueTracker(self.theta)
        self.focal_distance_tracker = ValueTracker(self.focal_distance)
        self.gamma_tracker = ValueTracker(self.gamma)
        self.zoom_tracker = ValueTracker(self.zoom)
        self.fixed_orientation_mobjects = {}
        self.fixed_in_frame_mobjects = set()
        

        x = Text("HELLO")
        self.play(Create(x))