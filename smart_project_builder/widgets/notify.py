from kivymd.toast import  toast
from kivymd.uix.snackbar import Snackbar
from kivy.lang import Builder

Builder.load_string("""

<Message>

""")


def notify(message):
    toast(message)
