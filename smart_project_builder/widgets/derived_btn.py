
from kivymd.uix.button import MDRaisedButton
# from kivy.uix.behaviors import ToggleButtonBehavior
# from kivymd.uix.button import BaseButton
from kivy.lang import Builder
from kivy.properties import BooleanProperty
# import kivymd_icon_viewer

Builder.load_string("""
<SelectionButton>
    group: 'gender'
    md_bg_color: app.colors.secondary
    size_hint: .3, .03
    markup: True
    radius: [20]
    theme_text_color: "Custom"
    text_color: app.colors.white
    font_name: app.fonts.body
    font_size: app.fonts.size.h5

""")


class SelectionButton(MDRaisedButton):
    # allow_no_selection = BooleanProperty(False)

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

