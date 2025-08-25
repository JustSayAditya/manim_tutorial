from manim import *


class axes_with_graph_and_labels(Scene):
    def construct(self):

        # ---------------------------
        # Create axes with labels
        # ---------------------------
        # Axes(...) constructs a pair of coordinate axes (x and y) that you can
        # draw to the screen. Many arguments below are lists: [start, stop, step].
        # - x_range: [x_min, x_max, x_tick_step]
        # - y_range: [y_min, y_max, y_tick_step]
        #
        # Important: the x_range/y_range define the *mathematical* coordinate
        # ranges the Axes object represents. Separately, x_length/y_length control
        # how many screen units (in manim's coordinate space) are used to
        # visually draw the axes. So a larger length stretches the same
        # numerical interval farther on screen.
        #
        # axis_config is a dictionary of visual options for axis labels/numbers
        # and general axis styling. Not all manim versions support identical
        # keys; common ones are shown here.
        axes = Axes(
            x_range=[
                -2,
                2,
                1,
            ],  # x-axis mathematical range: from -2 to 2 with ticks every 1 unit
            y_range=[
                -1,
                3,
                1,
            ],  # y-axis mathematical range: from -1 to 3 with ticks every 1 unit
            # axis_config controls per-axis visual settings:
            axis_config={
                "color": WHITE,  # color of axis lines and ticks
                "include_numbers": False,  # whether numeric tick labels are shown
                "tip_shape": StealthTip,  # arrow head shape used for the ends of axes
                "font_size": 50,  # font size for numeric labels / axis text (if enabled)
                "stroke_width": 10,  # thickness used for axis lines when drawn via axis_config
            },  # Color of the axes
            # The following control how long the axes are on screen (visual length).
            # These are independent of the numeric x_range/y_range.
            x_length=7,  # length of the x-axis in manim scene units
            y_length=7,  # length of the y-axis in manim scene units
            # stroke_width (at this top level) also influences drawn line width.
            # In some manim versions the top-level stroke_width parameter sets the
            # default stroke width for the whole Axes mobject; axis_config["stroke_width"]
            # may be used for per-axis specifics. If values disagree, the exact
            # visual result depends on manim version/implementation.
            stroke_width=10,
        )

        # ---------------------------
        # Create axis labels
        # ---------------------------
        # axes.get_axis_labels returns a VGroup containing LaTeX-rendered labels
        # positioned near the ends of the axes. You can pass LaTeX strings;
        # r"\boldsymbol{x}" renders a bold italic/serif x depending on your TeX.
        labels = axes.get_axis_labels(
            x_label=r"\boldsymbol{x}",  # LaTeX string for the x-axis label
            y_label=r"\boldsymbol{f(x)}",  # LaTeX string for the y-axis label
        )

        # ---------------------------
        # Plot the function
        # ---------------------------
        # axes.plot expects a callable f(x) and an x_range in the form
        # [x_start, x_end, step_for_sampling]. Manim will sample the function
        # at points separated by `step_for_sampling` and approximate the curve
        # by connecting those sampled points.
        #
        # NOTE about the original code's ranges: the Axes object above is set
        # to show x from -2 to 2, but here we plot the parabola over -3..3.
        # That means parts of the plotted curve (x in (-3,-2) and (2,3)) will be
        # outside the visible axes area — they will still be drawn by manim, but
        # visually they extend beyond the axis ticks. If you want the graph to be
        # clipped to the axes' numeric window, make the plotting range match the
        # Axes x_range (or increase the Axes x_range).
        #
        # stroke_width here controls the thickness of the plotted curve itself.
        # A smaller sampling step (e.g. 0.001) yields a smoother curve but creates
        # many more vertices and may increase render time.
        graph = axes.plot(
            lambda x: x**2,  # function to plot: y = x^2
            x_range=[
                -3,
                3,
                0.01,
            ],  # sample x from -3 to 3 with 0.01 step (dense sampling)
            color=GOLD,  # color of the curve
            stroke_width=10,  # visual thickness of the plotted line
        )

        # ---------------------------
        # Add objects to the scene
        # ---------------------------
        # self.add places the provided mobjects into the scene immediately.
        # The order matters for layering: objects added later are drawn on top
        # of objects added earlier (so here the 'graph' will appear above axes
        # if it overlaps).
        #
        # If you prefer an animated entrance, use self.play(Create(mobject)) or
        # other animation primitives instead of self.add.
        self.add(axes, labels, graph)
