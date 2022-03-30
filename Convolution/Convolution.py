from re import X
from manimlib import *
from sympy import Le, isolate, trigamma



class VerticalMultiplication(Scene):
    def construct(self):
        

        axes1 = Axes(
            x_range=(-3,3),
            y_range=(-2.5, 2.5),
            width=5,
            height=6
        )

        # put everything into place
        factor1 = VGroup(*[
            Tex(digit)
            for digit in ['2', '2', '3', '1', '6']
        ])
        x = -1
        for digit in factor1:
            digit.move_to(axes1.c2p(x, 2.5))
            x += 1

        times = Tex('\\times')
        times.move_to(axes1.c2p(-3, 1.5))

        factor2 = VGroup(*[
            Tex(digit)
            for digit in ['4', '2', '1']
        ])
        x = 1
        for digit in factor2:
            digit.move_to(axes1.c2p(x, 1.5))
            x += 1
        
        h_line1 = Line()
        h_line1.set_length(5.5)
        h_line1.move_to(axes1.c2p(0, 1))

        interm1 = VGroup(*[
            Tex(digit)
            for digit in ['2', '2', '3', '1', '6']
        ])
        x = -1
        for digit in interm1:
            digit.move_to(axes1.c2p(x, 0.5))
            x += 1

        interm2 = VGroup(*[
            Tex(digit)
            for digit in ['4', '4', '6', '3', '2']
        ])
        x = -2
        for digit in interm2:
            digit.move_to(axes1.c2p(x, -0.5))
            x += 1
        
        interm3 = VGroup(*[
            Tex(digit)
            for digit in ['8', '9', '2', '6', '4']
        ])
        x = -3
        for digit in interm3:
            digit.move_to(axes1.c2p(x, -1.5))
            x += 1

        h_line2 = Line()
        h_line2.set_length(5.5)
        h_line2.move_to(axes1.c2p(0, -2))

        result = VGroup(*[
            Tex(digit)
            for digit in ['9', '3', '9', '5', '0', '3', '6']
        ])
        x = -3
        for digit in result:
            digit.move_to(axes1.c2p(x, -2.5))
            x += 1

        vertical_m = VGroup(*[factor1, times, factor2, h_line1, interm1, interm2, interm3, h_line2, result])


        # write animation
        self.play(Write(factor1, run_time=1))
        self.play(Write(times, run_time=0.4), Write(factor2, run_time = 0.6))
        self.wait(0.5)
        self.play(Write(h_line1, run_time=0.6))

        # multiply animation
        self.play(factor2[0].animate.set_opacity(0.2), factor2[1].animate.set_opacity(0.2))
        self.play(*[
            ReplacementTransform(factor1[i].copy(), interm1[i], run_time=1)
            for i in range(5)
        ])
        self.play(factor2[1].animate.set_opacity(1), factor2[2].animate.set_opacity(0.2))
        self.play(*[
            ReplacementTransform(factor1[i].copy(), interm2[i], run_time=1)
            for i in range(5)
        ])
        self.play(factor2[0].animate.set_opacity(1), factor2[1].animate.set_opacity(0.2))
        self.play(*[
            ReplacementTransform(factor1[i].copy(), interm3[i], run_time=1)
            for i in range(5)
        ])
        self.play(factor2[1].animate.set_opacity(1), factor2[2].animate.set_opacity(1), Write(h_line2, run_time=0.6))

        self.play(
            *[
                ReplacementTransform(interm1[i].copy(), result[2+i], run_time=2, lag_ratio=0)
                for i in range(5)
            ], 
            *[
                ReplacementTransform(interm2[i].copy(), result[1+i], run_time=2, lag_ratio=1/4)
                for i in range(5)
            ],
            *[
                ReplacementTransform(interm3[i].copy(), result[i], run_time=2, lag_ratio=4/5)
                for i in range(5)
            ]
        )
        self.wait()
       

        # put in another way

        self.play(FadeOut(VGroup(interm1, interm2, interm3, h_line2, result)))
        
    

        # emphasize digit by opcaticy

        def compute_opacity(digit):
            dist = abs(digit.get_x() - factor2[2].get_x())
            if dist < 0.3:
                return 1
            else:
                if dist > 0.8:
                    return 0.2
                else:
                    return 1.48 - dist * 8 / 5

        def set_opacity(digits):
            for digit in digits:
                digit.set_opacity(compute_opacity(digit))

        self.play(
            *[
                factor1[i].animate.set_opacity(compute_opacity(factor1[i]))
                for i in range(5)
            ]
        )
        factor1.add_updater(set_opacity)


        # generate projective triangles
        
        # def edges_follow(edges, side=None):
        #     if side is None:
        #         return

        #     i = 0
        #     if side == 'left':
        #         for edge in edges:
        #             edge.set_points_by_ends(factor1[i].get_center(), factor2.get_left())
        #             i = i+1
        #         return
        #     if side == 'right':
        #         for edge in edges:
        #             edge.set_points_by_ends(factor1[i].get_center(), factor2.get_right())
        #             i = i+1
        #         return

        # # left edges
        # l_edges = VGroup(
        #     *[
        #         Line(stroke_opacity=0)
        #         for i in range(5)
        #     ]
        # )
        # self.add(l_edges)

        # l_edges.add_updater(lambda m: edges_follow(m, side='left'))
       
        # # right edges
        # r_edges = VGroup(
        #     *[
        #         Line(stroke_opacity=0)
        #         for i in range(5)
        #     ]
        # )
        # self.add(r_edges)

        # r_edges.add_updater(lambda m: edges_follow(m, side='right'))

        b_edge = h_line1.copy()
        b_edge.move_to(axes1.c2p(0, 0))
        # self.add(b_edge)


        tria0 = always_redraw(
            lambda: Polygon(*[factor1[0].get_center(), line_intersection([factor1[0].get_center(), factor2.get_left()], [b_edge.get_start(), b_edge.get_end()]), line_intersection([factor1[0].get_center(), factor2.get_right()], [b_edge.get_start(), b_edge.get_end()])], fill_color='#EEEEEE', fill_opacity=compute_opacity(factor1[0])-0.2, stroke_opacity=0)
        )

        tria1 = always_redraw(
            lambda: Polygon(*[factor1[1].get_center(), line_intersection([factor1[1].get_center(), factor2.get_left()], [b_edge.get_start(), b_edge.get_end()]), line_intersection([factor1[1].get_center(), factor2.get_right()], [b_edge.get_start(), b_edge.get_end()])], fill_color='#EEEEEE', fill_opacity=compute_opacity(factor1[1])-0.2, stroke_opacity=0)
        )

        tria2 = always_redraw(
            lambda: Polygon(*[factor1[2].get_center(), line_intersection([factor1[2].get_center(), factor2.get_left()], [b_edge.get_start(), b_edge.get_end()]), line_intersection([factor1[2].get_center(), factor2.get_right()], [b_edge.get_start(), b_edge.get_end()])], fill_color='#EEEEEE', fill_opacity=compute_opacity(factor1[2])-0.2, stroke_opacity=0)
        )

        tria3 = always_redraw(
            lambda: Polygon(*[factor1[3].get_center(), line_intersection([factor1[3].get_center(), factor2.get_left()], [b_edge.get_start(), b_edge.get_end()]), line_intersection([factor1[3].get_center(), factor2.get_right()], [b_edge.get_start(), b_edge.get_end()])], fill_color='#EEEEEE', fill_opacity=compute_opacity(factor1[3])-0.2, stroke_opacity=0)
        )

        tria4 = always_redraw(
            lambda: Polygon(*[factor1[4].get_center(), line_intersection([factor1[4].get_center(), factor2.get_left()], [b_edge.get_start(), b_edge.get_end()]), line_intersection([factor1[4].get_center(), factor2.get_right()], [b_edge.get_start(), b_edge.get_end()])], fill_color='#EEEEEE', fill_opacity=compute_opacity(factor1[4])-0.2, stroke_opacity=0)
        )
        
        trias = VGroup(*[tria0, tria1, tria2, tria3, tria4])
        self.play(GrowFromPoint(trias, factor1[4].get_center()))

        
        self.play(factor2.animate.shift(axes1.c2p(-4, 0, 0)), rate_func=there_and_back, run_time=4)


        # axes2 = Axes(
        #     x_range=(-3,3),
        #     y_range=(-3.5, 3.5),
        #     width=5,
        #     height=6
        # )
        
        # self.play(
        #     *[
        #         factor1[i].animate.move_to(axes2.c2p(i - 1, 3.5))
        #         for i in range(5)
        #     ],
        #     *[
        #         factor2[i].animate.move_to(axes2.c2p(i + 1, 2.5))
        #         for i in range(3)
        #     ],
        #     times.animate.move_to(axes2.c2p(-3, 2.5)),
        #     h_line1.animate.move_to(axes2.c2p(0, 2))
        # )


        

        # for i in [4, 3, 2, 1, 0]:
        #     digits = [4, 3, 2, 1, 0]
        #     digits.remove(i)
        #     self.play(
        #         factor1[i].animate.set_opacity(1),
        #         *[
        #             factor1[j].animate.set_opacity(0.2)
        #             for j in digits
        #         ],
        #         factor2.animate.shift(axes2.c2p(0 if i==4 else -1, 0, 0))
        #         )
        #     self.wait()

    
















