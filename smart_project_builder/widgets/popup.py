from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.properties import StringProperty



class Pop(MDDialog):
    title = StringProperty()
    text = StringProperty()
    def __init__(self, *args, **kwargs):
        # pass
        super().__init__(*args, **kwargs)
    