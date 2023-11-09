from manim import *
FRAME_HEIGHT=config['frame_height']
FRAME_WIDTH=FRAME_HEIGHT*19/6
FRAME_X_RADIUS=FRAME_WIDTH/2
FRAME_Y_RADIUS=FRAME_HEIGHT/2

class MyPorpose(ThreeDScene):
    my_dict={
        'x_min':-5,
        'x_max':5,
        'y_min':-5,
        'y_max':5,
        'surface_resolution':32
    }
    @staticmethod
    def first_curve(x,y):
        return np.array([
            x,y,np.sin(x)+np.cos(y)
        ])
    def construct(self):
        first_scene=self.first_scene()
        second_scene=self.second_scene()
        third_scene=self.third_scene()
        my_vgroup=VGroup(first_scene[0],second_scene[0],third_scene[0])
        my_vgroup.set_width(FRAME_WIDTH/4)
        my_vgroup.move_to(3*UP).arrange(RIGHT,buff=0.4)
        self.play(*first_scene[1])
        self.wait()
        self.play(*second_scene[1])
        self.wait()
        self.play(*third_scene[1])
        self.wait()
        self.play(third_scene[0][0].set_fill,WHITE)
        self.wait()
    def first_scene(self):
        axes=ThreeDAxes()
        self.set_camera_orientation(phi=60*DEGREES,theta=140)
        config_1={
            'u_min':-5,
            'u_max':5,
            'v_min':-5,
            'v_max':5,
            'resolution':18,
            'fill_opacity':0
        }
        surface=ParametricSurface(lambda x,y: self.first_curve(x,y),**config_1)
        return VGroup(axes,surface),[ShowCreation(axes),ShowCreation(surface)]
    def second_scene(self):
        axes=ThreeDAxes()
        self.set_camera_orientation(phi=60*DEGREES,theta=140)
        self.begin_ambient_camera_rotation()
        config_1={
            'u_min':-5,
            'u_max':5,
            'v_min':-5,
            'v_max':5,
            'resolution':18,
            'fill_opacity':0
        }
        surface=ParametricSurface(lambda x,y: self.first_curve(x,y),**config_1)
        return VGroup(axes,surface),[ShowCreation(axes),ShowCreation(surface)]
    def third_scene(self):
        axes=ThreeDAxes()
        self.set_camera_orientation(phi=60*DEGREES,theta=140)
        self.begin_ambient_camera_rotation()
        config_1={
            'u_min':-5,
            'u_max':5,
            'v_min':-5,
            'v_max':5,
            'resolution':18,
            'fill_opacity':0
        }
        surface=ParametricSurface(lambda x,y: self.first_curve(x,y),**config_1)
        return VGroup(axes,surface),[ShowCreation(axes),ShowCreation(surface)]