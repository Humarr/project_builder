from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.app import MDApp
# from field import InputField

KV = '''
# : import InputField field.InputField
<ItemForCustomBottomSheet@OneLineIconListItem>
    on_press: app.custom_sheet.dismiss()
    icon: ""

    IconLeftWidget:
        icon: root.icon


<ContentCustomSheet@BoxLayout>:
    orientation: "vertical"
    size_hint_y: None
    height: "400dp"

    MDTopAppBar:
        title: 'Custom bottom sheet:'

    ScrollView:

        MDGridLayout:
            cols: 1
            adaptive_height: True
            MDTextField:
                hint_text: "Enter Transaction pin"

            # ItemForCustomBottomSheet:
            #     icon: "page-previous"
            #     text: "Preview"

            # ItemForCustomBottomSheet:
            #     icon: "exit-to-app"
            #     text: "Exit"


MDScreen:

    MDTopAppBar:
        title: 'Example BottomSheet'
        pos_hint: {"top": 1}
        elevation: 4

    MDRaisedButton:
        text: "Open custom bottom sheet"
        on_release: app.show_pin_bottomsheet()
        pos_hint: {"center_x": .5, "center_y": .5}
    

'''


class Example(MDApp):
    custom_sheet = None

    def build(self):
        return Builder.load_string(KV)

    def show_pin_bottomsheet(self):
        self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())
        self.custom_sheet.open()


Example().run()