### Directory Structure

```
manim/
├── manimlib/
│   ├── animation/
│   ├── ...
│   ├── default_config.yml
│   └── window.py
├── custom_config.yml
└── start.py
```



```python
from manimlib import *
```



```python
class SquareToCircle(Scene):
```

`Scene` is a base class, `SquareToCircle` inheriting.



```python
self.play(ShowCreation(square))
self.play(ReplacementTransform(square, circle))
```

Call `Scene`'s `.play` method



```python
self.wait()		# default 1s
```



### Animate methods

If an object can be operated using methods, add a `.animate` can animate this operation. e. g.

```python
grid.set_color(YELLOW)
```

can be animated with

```python
grid.animate.set_color(YELLOW)
```





```python
self.embed()	# enable interaction
```





### Keyboard

Type `touch()` in command line, and

z - zoom	s - pan	d - 3d view	r - reset camera position	q - stop interaction and quit to command input



### [CLI flags](https://3b1b.github.io/manim/getting_started/configuration.html)

`-w` to write the scene to a file.

`-o` to write the scene to a file and open the result.

`-s` to skip to the end and just show the final frame.

`-so` will save the final frame to an image and show it.

`-n <number>` to skip ahead to the `n`’th animation of a scene.

`-f` to make the playback window fullscreen.

`--file_name FILE_NAME` 

`--resolution RESOLUTION` Resolution, passed as “WxH”, e.g. “1920x1080”

$ ` manimgl start.py AnimatingMethods -w --file_name 2kVersion --resolution "2560x1440" --frame_rate 120`



### Text

````python
# Text
text = Text(
	"""
	asdfagsdg
	""",
  font="asd", font_size=123,
  t2f={"a": "YAHEI", "s": "SONGTI", "d":"SIMSUN"}	# text to font, specify font by string
  t2c={"a": RED, "s": GREEN, "d":BLUE}	# text to color, specify color by string
  t2s={"a": ITALIC, "s": BOLD} # text to slant, specify slant by string
)

VGroup(text1, text2).arrange(DOWN, buff=0.8) # specify text arrangement, direction and spacing



# Tex

tex1 = Tex("A^2", "+", "B^2", "=", "C^2") # comma divides sub-objects for later animation

to_isolate = ["B", "C", "=", "(", ")"]
tex2 = Tex("A^2 = (C + B)(C - B)", isolate=["A^2", *to_isolate]) # put together in TeX but later isolate something out

TransformMatchingTex(tex1, tex2) # animation based on TeX sub-objects

TransformMatchingTex(
                tex1, tex2,
                key_map={					# manually specify what sub-objects transforms to what sub-objects
                    "C^2": "C",
                    "B^2": "B",
                }
            )

TransformMatchingShapes(tex1, tex2) # automatic transform according to shapes



# TexText
complex_map_words = TexText(
            """
            Or thinking of the plane as $\\mathds{C}$,\\\\
            this is the map $z \\rightarrow z^2$
            """
        )

````







```python

```



### Updaters

```python
always_redraw(Constructor, *args, **kwargs) # returns a dynamic mobject constantly calling constructor

always(label.next_to, brace, UP)
f_always(number.set_value, square.get_width)    # f_always if arg itself changes

.add_updater() #sets an update function for the object. For example: 
mob1.add_updater(lambda m: m.next_to(mob2)) # means mob1.next_to(mob2) is executed every frame.

x_tracker = ValueTracker(2)		# a slide bar
f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )
 self.play(x_tracker.animate.set_value(4), run_time=3)

```



### Coordinate System

```python
axes = Axes(
            x_range=(-1, 10),
            y_range=(-2, 2, 0.5),
            height=6,
            width=10,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            y_axis_config={
                "include_tip": False,
            }
        )

# or
# axes = Axes((-1, 10), (-2, 2, 0.5))

axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )

dot = Dot(axes.c2p(0, 0), color=RED)
self.play(dot.animate.move_to(axes.c2p(5, 0.5)))

h_line = always_redraw(
            lambda: axes.get_h_line(dot.get_left())
        )
        v_line = always_redraw(
            lambda: axes.get_v_line(dot.get_bottom())
        )
  
 graph = axes.get_graph(
            lambda x: ...,
            color=BLUE,
 				)
```







### Animation Collection

```python
Write(text)
FadeIn(xxx, shift=UP)
FadeOut(xxx, shift=DOWN)

```

