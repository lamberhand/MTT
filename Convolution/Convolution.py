from manimlib import *
from sympy import Le, isolate



class VerticalMultiplication(Scene):
    def construct(self):
        

        axes = Axes(
            x_range=(-3,3),
            y_range=(-2.5, 2.5),
            width=5,
            height=6
        )

        # put everything into place
        factor1 = VGroup(*[
            Tex(digit)
            for digit in ["2", "2", "3", "1", "6"]
        ])
        x = -1
        for digit in factor1:
            digit.move_to(axes.c2p(x, 2.5))
            x += 1

        times = Tex("\\times")
        times.move_to(axes.c2p(-3, 1.5))

        factor2 = VGroup(*[
            Tex(digit)
            for digit in ["4", "2", "1"]
        ])
        x = 1
        for digit in factor2:
            digit.move_to(axes.c2p(x, 1.5))
            x += 1
        
        h_line1 = Line()
        h_line1.set_width(5.5)
        h_line1.move_to(axes.c2p(0, 1))

        interm1 = VGroup(*[
            Tex(digit)
            for digit in ["2", "2", "3", "1", "6"]
        ])
        x = -1
        for digit in interm1:
            digit.move_to(axes.c2p(x, 0.5))
            x += 1

        interm2 = VGroup(*[
            Tex(digit)
            for digit in ["4", "4", "6", "3", "2"]
        ])
        x = -2
        for digit in interm2:
            digit.move_to(axes.c2p(x, -0.5))
            x += 1
        
        interm3 = VGroup(*[
            Tex(digit)
            for digit in ["8", "9", "2", "6", "4"]
        ])
        x = -3
        for digit in interm3:
            digit.move_to(axes.c2p(x, -1.5))
            x += 1

        h_line2 = Line()
        h_line2.set_length(5.5)
        h_line2.move_to(axes.c2p(0, -2))

        result = VGroup(*[
            Tex(digit)
            for digit in ["9", "3", "9", "5", "0", "3", "6"]
        ])
        x = -3
        for digit in result:
            digit.move_to(axes.c2p(x, -2.5))
            x += 1

        vertical_m = VGroup(*[factor1, times, factor2, h_line1, interm1, interm2, interm3, h_line2, result])


        # write animation
        self.play(Write(factor1, run_time=1))
        self.play(Write(times, run_time=0.4), Write(factor2, run_time = 0.6))
        self.wait(0.5)
        self.play(Write(h_line1, run_time=0.6))

        # multiply animation
        self.play(factor2[2].animate.set_color(YELLOW_D))
        self.play(*[
            ReplacementTransform(factor1[i].copy(), interm1[i], run_time=1)
            for i in [0, 1, 2, 3, 4]
        ])
        self.play(factor2[2].animate.set_color(WHITE), factor2[1].animate.set_color(YELLOW_D))
        self.play(*[
            ReplacementTransform(factor1[i].copy(), interm2[i], run_time=1)
            for i in [0, 1, 2, 3, 4]
        ])
        self.play(factor2[1].animate.set_color(WHITE), factor2[0].animate.set_color(YELLOW_D))
        self.play(*[
            ReplacementTransform(factor1[i].copy(), interm3[i], run_time=1)
            for i in [0, 1, 2, 3, 4]
        ])
        self.play(factor2[0].animate.set_color(WHITE), Write(h_line2, run_time=0.6))

        self.play(
            *[
                ReplacementTransform(interm1[i].copy(), result[2+i], run_time=2, lag_ratio=0)
                for i in [0, 1, 2, 3, 4]
            ], 
            *[
                ReplacementTransform(interm2[i].copy(), result[1+i], run_time=2, lag_ratio=1/4)
                for i in [0, 1, 2, 3, 4]
            ],
            *[
                ReplacementTransform(interm3[i].copy(), result[i], run_time=2, lag_ratio=4/5)
                for i in [0, 1, 2, 3, 4]
            ]
        )
        self.wait()
       

        # put in another way

        self.play(FadeOut(VGroup(interm1, interm2, interm3, h_line2, result)))
        













