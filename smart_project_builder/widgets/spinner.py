from kivymd.uix.spinner import MDSpinner
from kivy.lang import Builder

Builder.load_string("""
<Spin>
    # size_hint: None, None
    # size: dp(46), dp(46)
    # pos_hint: {'center_x': .5, 'center_y': .5}
    # determinate: True
    # active: True
    line_width: "5dp"
    # determinate_time: 12
    # palette: [app.colors.yellow, app.colors.white, app.colors.orange, app.colors.warning]



""")

class Spin(MDSpinner):
    def __init__(self,**kwargs):
        super().__init__(self, **kwargs)