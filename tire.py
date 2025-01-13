from manim import *

from manim._config.utils import ManimConfig

ManimConfig.background_color = "#ece6e2"
radius = 2
ground_len = 5
FONT = "product sans"
BLACK = "#343434"
WHITE = "#ece6e2"
SPEED = 25


def time_adj(k):
    return 1 + 1 / k


def speed_adj(k):
    return (k - 1) / (k + 1)


def get_slow_mo(k):  # |k| > 1
    return lambda t: (t / k) * (k + 1 - t)


class Test(MovingCameraScene):
    def construct(self):
        wheel = SVGMobject(r"C:\Users\Anooj Dilip Archana\Downloads\wheel.svg").scale(1.25).shift(1.22 * DOWN)
        wheel.speed = SPEED

        ground = VGroup(
            # Dashed lines
            DashedLine(
                start=ground_len * LEFT,
                end=(ground_len + 12) * RIGHT,
                dashed_ratio=0.4,
                dash_length=0.2,
                color=BLACK,
            ).shift(2.5 * DOWN)
        )
        [i.rotate(PI / 4) for i in ground[0].submobjects]
        ground.add(
            # Add simple line for ground
            Line(ground_len * LEFT, ground_len * RIGHT, color=BLACK).align_to(
                ground, UP
            ),
            # Mask for left side
            Rectangle(
                fill_opacity=1,
                color=WHITE,
                height=0.2,
                width=config.frame_x_radius - ground_len,
            )
            .move_to(ground, aligned_edge=UP)
            .to_edge(LEFT, 0),
            # Mask for right side
            Rectangle(
                fill_opacity=1,
                color=WHITE,
                height=0.2,
                width=config.frame_x_radius - ground_len,
            )
            .move_to(ground, aligned_edge=UP)
            .to_edge(RIGHT, 0),
        )
        head = VGroup(
            Text(
                "Translational",
                font=FONT,
                color=BLACK,
            ),
            Text(
                "Motion",
                font=FONT,
                color=BLACK,
            ),
        )
        head1 = VGroup(
            Text(
                "Rotational",
                font=FONT,
                color=BLACK,
            ),
            Text(
                "Motion",
                font=FONT,
                color=BLACK,
            ),
        )
        head2 = VGroup(
            Text(
                "Rolling",
                font=FONT,
                color=BLACK,
            ),
            Text(
                "Motion",
                font=FONT,
                color=BLACK,
            ),
        )
        [i.arrange().scale(1.2).shift(3 * UP) for i in [head, head1, head2]]
        head2[0].shift(0.1 * DOWN)

        self.play(
            AnimationGroup(FadeIn(ground), Write(wheel), run_time=2, lag_ratio=0.5)
        )
        self.wait(0.5)
        self.play(AnimationGroup(Write(head),  lag_ratio=0.5))
        self.play(
            wheel.animate.shift(4 * LEFT),
            ground[0].animate.shift(4 * LEFT),
        )

        # Start slow-mo
        d = 3
        k = 1.01
        self.play(
            wheel.animate.shift(d * RIGHT),
            self.camera.frame.animate.scale(0.8).shift(DOWN),
            rate_func=get_slow_mo(k),
            run_time=d * time_adj(k) / wheel.speed,
        )
        wheel.speed *= speed_adj(k)
        # End slow-mo

        v = VGroup(
            Vector(RIGHT / 2),
            Vector(RIGHT / 2).shift(DR * 0.7),
            Vector(RIGHT / 2).shift(DL * 0.75),
            Vector(RIGHT / 2).shift(UL * 0.75),
            Vector(RIGHT / 2).shift(UR * 0.75),
            Vector(RIGHT / 2).shift(LEFT),
            Vector(RIGHT / 2).shift(RIGHT),
            Vector(RIGHT / 2).shift(DOWN * 1.1),
            Vector(RIGHT / 2).shift(UP * 1.1),
        ).set_color(RED)
        v[0].set_color(BLUE_D)
        v.add_updater(
            lambda v: v.move_to(wheel.get_center()).shift(
                v.get_center() - v[0].get_start()
            )
        )
        Vcom = MathTex("V_{Center\ of\ mass}", color=BLACK).shift(0.4 * UP)
        wheel.add_updater(lambda m, dt: m.shift(RIGHT * m.speed * dt))
        self.play(Create(v))
        self.wait()
        self.play(
            Succession(
                Write(Vcom),
                Wait(),
                Transform(Vcom, MathTex("V_{c}", color=BLACK).move_to(Vcom)),
            ),
        )
        self.wait(3)
        wheel.clear_updaters()

        # Reverse start slow-mo
        d = 4
        k *= -1
        self.play(
            wheel.animate.shift(d * RIGHT),
            FadeOut(v),
            FadeOut(Vcom),
            self.camera.frame.animate.shift(UP).scale(1.25),
            rate_func=get_slow_mo(k),
            run_time=d * time_adj(k) / wheel.speed,
        )
        wheel.speed *= speed_adj(k)
        # Reverse end slow-mo

        self.wait()
        self.play(
            wheel.animate.shift(wheel.get_center()[0] * LEFT),
            ground[0].animate.shift(wheel.get_center()[0] * LEFT),
        )
        self.play(Transform(head, head1))
        self.play(Rotate(wheel, TAU - PI / 4))
        self.wait(0.5)

        wheel.speed = SPEED
        wheel.w = wheel.speed / 1.2

        # Start slow-mo
        d = PI / 1.7
        k = 1.05
        self.play(
            Rotate(wheel, -d),
            self.camera.frame.animate.scale(0.8).shift(DOWN),
            rate_func=get_slow_mo(k),
            run_time=d * time_adj(k) / wheel.w,
        )
        wheel.w *= speed_adj(k)
        # End slow-mo
        wheel.add_updater(lambda m, dt: m.rotate(-m.w * dt))

        v = VGroup(
            Dot(fill_opacity=0),
            *[
                Dot(color=WHITE)
                .shift(RIGHT / (i % 2 + 1) * 1.04)
                .rotate_about_origin(PI / 3 * i)
                for i in range(6)
            ],
            *[
                DashedLine(
                    ORIGIN,
                    RIGHT / (i % 2 + 1) * 1.04,
                    
                    color=WHITE,
                ).rotate_about_origin(PI / 3 * i)
                for i in range(6)
            ],
            *[
                Vector(RIGHT / (i % 2 + 1), color=RED)
                .shift(RIGHT / (i % 2 + 1) * 1.04)
                .rotate(-PI / 2, about_point=(RIGHT / (i % 2 + 1) * 1.04))
                .rotate_about_origin(PI / 3 * i)
                for i in range(6)
            ],
        ).move_to(wheel.get_center())
        v.shift(v.get_center() - v[0].get_center())
        v.add_updater(
            lambda m, dt: m.rotate(-wheel.w * dt, about_point=wheel.get_center())
        )
        omega = MathTex(r"\omega").shift(0.4 * UP)
        self.play(Create(v))
        self.play(Write(omega))

        self.wait(5)
        wheel.clear_updaters()