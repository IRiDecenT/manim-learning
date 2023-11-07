from manim import *
import os

class NameOfAnimation(Scene):
    def construct(self):
        box = Rectangle(stroke_color = GREEN_C, stroke_opacity=0.7,
                        fill_color = RED_B, fill_opacity = 0.5, height=1, width=1)
        self.add(box)
        self.play(box.animate.shift(RIGHT*2), run_time = 2)
        self.play(box.animate.shift(UP*3), run_time = 2)
        self.play(box.animate.shift(DOWN*5 + LEFT*5), run_time = 2)
        self.play(box.animate.shift(UP*1.5 + RIGHT*1), run_time = 2)

class FittingObjects(Scene):
    def construct(self):
        axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], x_length=6, y_length=6)
        axes.to_edge(LEFT, buff=1)

        circle = Circle(stroke_width = 6, stroke_color = YELLOW, fill_color = RED_C, fill_opacity = 0.8)
        circle.set_with(2).to_edge(DR, buff=0)
        triangle = Triangle(stroke_width = 10, stroke_color = GREY, fill_color = RED_C).set_height(2).shift(DOWN*2+RIGHT*3)

        self.play(Write(axes))
        self.play(DrawBorderThenFill(circle))
        self.play(circle.animate.set_width(1))
        self.play(Transform(circle, triangle), run_time=3)

SCENE = "FittingObjects"
FLAGS =  f"-pqm"

if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    print(script_name)
    os.system(f"manim {script_name} {SCENE} {FLAGS}")