from kivy.lang import Builder
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivymd.app import MDApp

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True




<Navigator>

    MDScreenManager:

        MDScreen:
            IconButton:
                icon: "menu"
                icon_size: app.fonts.size.h1 + dp(10)
                theme_icon_color: "Custom"
                icon_color: app.colors.white
                on_press: nav_drawer.set_state("open")
                pos_hint: {"top": .99}

    MDNavigationDrawer:
        id: nav_drawer
        radius: (0, 16, 16, 0)

        MDNavigationDrawerMenu:

            MDNavigationDrawerHeader:
                title: "Header title"
                title_color: "#4a4939"
                text: "Header text"
                spacing: "4dp"
                padding: "12dp", 0, 0, "56dp"

            MDNavigationDrawerLabel:
                text: "Mail"

            DrawerClickableItem:
                icon: "gmail"
                right_text: "+99"
                text_right_color: "#4a4939"
                text: "Inbox"

            DrawerClickableItem:
                icon: "send"
                text: "Outbox"

            MDNavigationDrawerDivider:

            MDNavigationDrawerLabel:
                text: "Labels"

            DrawerLabelItem:
                icon: "information-outline"
                text: "Label"

            DrawerLabelItem:
                icon: "information-outline"
                text: "Label"
'''


class Navigator(MDNavigationLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
