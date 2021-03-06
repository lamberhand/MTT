from ctypes import cast
from random import triangular
from re import L, X
from manimlib import *
from sympy import Le, isolate, trigamma



class VerticalMultiplication(Scene):
    def construct(self):
        
        greetings = Text("Vertical Multiplication")
        self.play(Write(greetings), run_time=2.5)
        self.wait()
        self.play(FadeOut(greetings))

        axes1 = Axes(
            x_range=(-3,3),
            y_range=(-2.5, 2.5),
            width=5,
            height=6
        )

        # put everything into place
        factor1_digits = [2, 2, 3, 1, 6]
        factor1 = VGroup(*[
            Tex(str(digit))
            for digit in factor1_digits
        ])
        x = -1
        for digit in factor1:
            digit.move_to(axes1.c2p(x, 2.5))
            x += 1

        times = Tex('\\times')
        times.move_to(axes1.c2p(-3, 1.5))

        factor2_digits = [4, 2, 1]
        factor2 = VGroup(*[
            Tex(str(digit))
            for digit in factor2_digits
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

        self.play(
            FadeOut(VGroup(interm1, interm2, interm3, h_line2, result)),
            factor1.animate.shift(axes1.c2p(0, -1)),
            factor2.animate.shift(axes1.c2p(0, -1)),
            times.animate.shift(axes1.c2p(0, -1)),
            h_line1.animate.shift(axes1.c2p(0, -1))
            )
        self.remove(interm1, interm2, interm3, h_line2, result)
        

        # emphasize digit by opacity

        def compute_opacity(digit):
            dist = abs(digit.get_x() - factor2[2].get_x())
            if dist < 0.3:
                return 1
            else:
                if dist > 0.8:
                    return 0.2
                else:
                    return 1.48 - dist * 8 / 5


        def set_digit_opacity(digits):
            for digit in digits:
                digit.set_opacity(compute_opacity(digit))

        self.play(
            *[
                factor1[i].animate.set_opacity(compute_opacity(factor1[i]))
                for i in range(5)
            ]
        )   

        # if animate.set_opacity called, set_opacity in updaters will not work
        # hence using duplicate
        factor1_old = factor1
        factor1 = factor1.copy()
        factor1.add_updater(set_digit_opacity) 
        self.add(factor1)
        self.remove(factor1_old)



        # generate projective triangles
        

        b_edge = h_line1.copy()
        b_edge.move_to(axes1.c2p(0, -1))
        # self.add(b_edge)


        tria0 = always_redraw(
            lambda: Polygon(*[factor1[0].get_center(), line_intersection([factor1[0].get_center(), factor2.get_left()], [b_edge.get_start(), b_edge.get_end()]), line_intersection([factor1[0].get_center(), factor2.get_right()], [b_edge.get_start(), b_edge.get_end()])], fill_color='#CCCCCC', fill_opacity=compute_opacity(factor1[0]) / 2 - 0.1, stroke_opacity=0)
        )

        tria1 = always_redraw(
            lambda: Polygon(*[factor1[1].get_center(), line_intersection([factor1[1].get_center(), factor2.get_left()], [b_edge.get_start(), b_edge.get_end()]), line_intersection([factor1[1].get_center(), factor2.get_right()], [b_edge.get_start(), b_edge.get_end()])], fill_color='#CCCCCC', fill_opacity=compute_opacity(factor1[1]) / 2 - 0.1, stroke_opacity=0)
        )

        tria2 = always_redraw(
            lambda: Polygon(*[factor1[2].get_center(), line_intersection([factor1[2].get_center(), factor2.get_left()], [b_edge.get_start(), b_edge.get_end()]), line_intersection([factor1[2].get_center(), factor2.get_right()], [b_edge.get_start(), b_edge.get_end()])], fill_color='#CCCCCC', fill_opacity=compute_opacity(factor1[2]) / 2 - 0.1, stroke_opacity=0)
        )

        tria3 = always_redraw(
            lambda: Polygon(*[factor1[3].get_center(), line_intersection([factor1[3].get_center(), factor2.get_left()], [b_edge.get_start(), b_edge.get_end()]), line_intersection([factor1[3].get_center(), factor2.get_right()], [b_edge.get_start(), b_edge.get_end()])], fill_color='#CCCCCC', fill_opacity=compute_opacity(factor1[3]) / 2 - 0.1, stroke_opacity=0)
        )

        tria4 = always_redraw(
            lambda: Polygon(*[factor1[4].get_center(), line_intersection([factor1[4].get_center(), factor2.get_left()], [b_edge.get_start(), b_edge.get_end()]), line_intersection([factor1[4].get_center(), factor2.get_right()], [b_edge.get_start(), b_edge.get_end()])], fill_color='#CCCCCC', fill_opacity=compute_opacity(factor1[4]) / 2 - 0.1, stroke_opacity=0)
        )
        
        trias = VGroup(*[tria0, tria1, tria2, tria3, tria4])

        

        class factorTex(Tex):
            def __init__(self, index1, index2, *tex_strings, **kwargs):
                self.index_of_factor1 = index1
                self.index_of_factor2 = index2
                self.string = tex_strings[0]
                super().__init__(*tex_strings, **kwargs)
            
            def get_index1(self):
                return self.index_of_factor1
            
            def get_index2(self):
                return self.index_of_factor2
            
            def get_number(self):
                return int(self.string)


        projection = VGroup(
            *[
                factorTex(i, j, str(factor1_digits[i] * factor2_digits[j]))
                for i in range(5)
                for j in range(3)
            ]
        )
        projection2 = projection.copy()

        projection_surface = h_line1.copy()
        projection_surface.move_to(axes1.c2p(0, -0.5))

        def projection_follow(projection):
            for digit in projection:
                index1 = digit.get_index1()
                index2 = digit.get_index2()
                alpha = compute_opacity(factor1[index1])
                projection_end = line_intersection([factor1[index1].get_center(), factor2[index2].get_center()], [projection_surface.get_start(), projection_surface.get_end()])
                digit.move_to(projection_end)
                digit.set_opacity(alpha / 0.8 - 0.25)

        
        # move these three first
        projection[-1].move_to(line_intersection([factor1[4].get_center(), factor2[2].get_center()], [projection_surface.get_start(), projection_surface.get_end()]))
        projection[-2].move_to(line_intersection([factor1[4].get_center(), factor2[1].get_center()], [projection_surface.get_start(), projection_surface.get_end()]))
        projection[-3].move_to(line_intersection([factor1[4].get_center(), factor2[0].get_center()], [projection_surface.get_start(), projection_surface.get_end()]))

        self.play(  # TODO causal relationship
            GrowFromPoint(trias, factor1[4].get_center()), 
            FadeInFromPoint(projection[-1], factor1[4].get_center(), lag_ratio=0),
            FadeInFromPoint(projection[-2], factor1[4].get_center(), lag_ratio=0),
            FadeInFromPoint(projection[-3], factor1[4].get_center(), lag_ratio=0),
            run_time=3
            )
        self.wait()

        projection.add_updater(projection_follow)
        self.add(projection)


        self.play(factor2.animate.shift(axes1.c2p(-4, 0)), times.animate.shift(axes1.c2p(0, 0.5)), rate_func=there_and_back, run_time=5)


        # start convolution

        axes2 = Axes(
            x_range=(-3,3),
            y_range=(-3.5, 3.5),
            width=5,
            height=6
        )

        self.play(FadeOut(VGroup(projection, trias)))
        self.remove(projection, trias)

        
        self.play(
            *[
                factor1[i].animate.move_to(axes2.c2p(i - 1, 3.5))
                for i in range(5)
            ],
            *[
                factor2[i].animate.move_to(axes2.c2p(i + 1, 2.5))
                for i in range(3)
            ],
            times.animate.move_to(axes2.c2p(-3, 2.5)),
            h_line1.animate.move_to(axes2.c2p(0, 2))
        )

        for digit in projection2:
            digit.move_to(axes2.c2p(-3 + digit.get_index1() + digit.get_index2(), -2.5 + digit.get_index1()))
        
        factor1_old = factor1
        factor1 = factor1.copy()
        factor1.add_updater(set_digit_opacity)
        self.add(factor1)
        self.remove(factor1_old)


        for i in range(-1, -6, -1):
            self.play(
                *[
                    ReplacementTransform(factor1[i].copy(), projection2[j + (i + 1) * 3])
                    for j in range(-1, -4, -1)
                ]
            )
            if i == -4:
                self.play(factor2.animate.shift(axes2.c2p(-1, 0)), times.animate.shift(axes2.c2p(0, 0.5)))
            elif i == -5:
                break
            else:
                self.play(factor2.animate.shift(axes2.c2p(-1, 0)))

        
        h_line2 = Line()
        h_line2.set_length(6)
        h_line2.move_to(axes2.c2p(0, -3))

        factor1.remove_updater(set_digit_opacity)
        self.play(
            Write(h_line2, run_time=0.6), 
            factor2.animate.shift(axes2.c2p(4, 0)), 
            times.animate.shift(axes2.c2p(0, -0.5)), 
            *[
                digit.animate.set_opacity(1)
                for digit in factor1
            ]
            )
        
        
        correspond = [[0], [1, 3], [2, 4, 6], [5, 7, 9], [8, 10, 12], [11, 13], [14]]
        final = VGroup()
        for l in correspond:
            sum = 0
            for i in l:
                sum += projection2[i].get_number()
            final.add(Tex(str(sum)))
        
        
        for i in range(7):
            final[i].move_to(axes2.c2p(i - 3, -3.5))


        def compute_lag(index):
            storey = int(index / 3)
            return 1 - 0.2 * storey

        trans_list = []
        for l in range(7):
            for i in correspond[l]:
                trans_list.append(ReplacementTransform(projection2[i].copy(), final[l], run_time=2, lag_ratio=compute_lag(i), rate_func=linear))

        self.play(*trans_list)

        # merging
        
        finale = [
            Tex("8"),
            Tex("1", "2"),
            Tex("1", "8"),
            Tex("1", "2"),
            Tex("2", "9"),
            Tex("1", "3"),
            Tex("6")
        ]

        for i in range(7):
            finale[i].move_to(axes2.c2p(i - 3, -3.5))
        
        for digit in finale:
            self.add(digit)
        self.remove(final)
        # self.play(TransformMatchingTex(finale[5].submobjects[0].copy(), finale[4], run_time=5))

        class positionedTex(Tex):
            def __init__(self, position=None, *tex_strings, **kwargs):
                super().__init__(*tex_strings, **kwargs)
                if position is not None:
                    self.move_to(position)

        self.wait(2)
        
        # TODO try Text
        temp = positionedTex(axes2.c2p(1, -3.5), "3", "0")
        self.play(
            FadeOut(finale[5].submobjects[0], axes2.c2p(-1, 0, 0), scale=0.5, path_arc=-90 * DEGREES), # tens merge to left
            finale[5].submobjects[1].animate.move_to(axes2.c2p(2, -3.5)), # units become king
            TransformMatchingTex(finale[4], temp) # left digit accept tens
            )
        finale[4] = temp
        
        temp = positionedTex(axes2.c2p(0, -3.5), "1", "5")
        self.play(
            FadeOut(finale[4].submobjects[0], axes2.c2p(-1, 0, 0), scale=0.5, path_arc=-90 * DEGREES),
            finale[4].submobjects[1].animate.move_to(axes2.c2p(1, -3.5)), 
            TransformMatchingTex(finale[3], temp)
        )
        finale[3] = temp

        temp = positionedTex(axes2.c2p(-1, -3.5), "1", "9")
        self.play(
            FadeOut(finale[3].submobjects[0], axes2.c2p(-1, 0, 0), scale=0.5, path_arc=-90 * DEGREES),
            finale[3].submobjects[1].animate.move_to(axes2.c2p(0, -3.5)), 
            TransformMatchingTex(finale[2], temp)
        )
        finale[2] = temp

        temp = positionedTex(axes2.c2p(-2, -3.5), "1", "3")
        self.play(
            FadeOut(finale[2].submobjects[0], axes2.c2p(-1, 0, 0), scale=0.5, path_arc=-90 * DEGREES),
            finale[2].submobjects[1].animate.move_to(axes2.c2p(-1, -3.5)), 
            TransformMatchingTex(finale[1], temp)
        )
        finale[1] = temp

        self.play(
            FadeOut(finale[1].submobjects[0], axes2.c2p(-1, 0, 0), scale=0.5, path_arc=-90 * DEGREES),
            finale[1].submobjects[1].animate.move_to(axes2.c2p(-2, -3.5)), 
            TransformMatchingTex(finale[0], positionedTex(axes2.c2p(-3, -3.5), "9"))
        )

        
        
class ConvolutionalSum(Scene):
    def construct(self):
        
        greetings = VGroup(Text("Convolutional"), Text(" Sum")).arrange(RIGHT)
        equation = Tex("\sum_{k=-\infty}^{\infty}", " x[k]y[n-k]")
        self.play(Write(greetings), run_time=2.5)
        self.wait()

        self.play(
            TransformMatchingShapes(greetings[0], equation[1]), 
            TransformMatchingShapes(greetings[1], equation[0]), 
            run_time=2.5
            )
        
        axes1 = Axes(
            x_range=(-1, 5),
            y_range=(0, 1.2),
            height=3,
            width=12,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
                "include_ticks": False
            },
        )
        axes1.get_y_axis().set_opacity(0)
        

        axes2 = Axes(
            x_range=(-1, 3),
            y_range=(0, 1.2),
            height=2,
            width=8,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
                "include_ticks": False
            },
        )
        axes2.get_y_axis().set_opacity(0)
        

        self.play(Write(axes1), Write(axes2))
        self.play(VGroup(equation, axes1, axes2).animate.arrange(DOWN))

        signal = [0.2, 0.2, 0.3, 0.1, 0.6]
        ir = [1.0, 0.5, 0.25]
        
        xn = [
            Line(axes1.c2p(i, 0), axes1.c2p(i , signal[i]))
            for i in range(5)
        ]
        x_marks = [
            Tex(str(signal[i]), font_size=28).move_to(axes1.c2p(i, signal[i] + 0.1))
            for i in range(5)
        ]
        yn = [
            Line(axes2.c2p(i, 0), axes2.c2p(i, ir[i]))
            for i in range(3)
        ]
        y_marks = [
            Tex(str(ir[i]), font_size=28).move_to(axes2.c2p(i, ir[i] + 0.1))
            for i in range(3)
        ]
        # TODO write value and label
        for x in xn:
            self.add(x)
            axes1.add(x)
        for x_mark in x_marks:
            self.add(x_mark)
            axes1.add(x_mark)
        for y in yn:
            self.add(y)
            axes2.add(y)
        for y_mark in y_marks:
            self.add(y_mark)
            axes2.add(y_mark)

        signal_label = Tex("x[n]").move_to(axes1.c2p(5, 0.5))
        axes1.add(signal_label)
        ir_label = Tex("y[n]").move_to(axes2.c2p(3, 0.5))
        axes2.add(ir_label)

        # start convolution





