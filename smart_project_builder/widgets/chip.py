from kivymd.uix.chip import MDChip
from kivy.lang import Builder

Builder.load_string("""
<MyChip>
    icon_right: "close-circle-outline"
    md_bg_color: app.colors.secondary
    icon_right_color: app.colors.white
    icon_left_color: app.colors.white
""")


class MyChip(MDChip):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
