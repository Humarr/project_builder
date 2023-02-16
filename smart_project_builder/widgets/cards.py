from kivymd.uix.behaviors import HoverBehavior,  RectangularElevationBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.scrollview import  MDScrollView
from kivymd.uix.card import MDCard
Builder.load_string("""
#: import Text widgets.label.Text
<ActionButton>
    size_hint: None, None
    size: [Window.width * .4, Window.height * .2]
    elevation: 20
    # padding: 1
    canvas.before:
        Color:
            rgba: app.colors.white
        RoundedRectangle:
            size: self.size[0], self.size[1]
            pos: self.pos
            radius: [self.height * .1]
    BoxLayout:
        orientation: 'vertical'
        # padding: 8
        canvas.before:
            Color:
                rgba: app.colors.white if root.state == "normal" else app.colors.secondary
            RoundedRectangle:
                size: self.size[0], self.size[1]
                pos: self.pos
                radius: [self.height * .1]
        # Text:
        #     text: root.title
        #     size_hint_y: None
        #     height: dp(18)
        #     halign: "center"
""")


class ActionButton(MDBoxLayout):
# class ActionButton(HoverBehavior,ButtonBehavior, MDBoxLayout):
    title = StringProperty("")
    icon = StringProperty("")
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
