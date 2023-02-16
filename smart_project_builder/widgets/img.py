from kivymd.uix.fitimage import FitImage
from kivymd.uix.behaviors import HoverBehavior,  RoundedRectangularElevationBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder

Builder.load_string("""
<RoundImage>
    size_hint: None, None
    # size: "40dp", "40dp"
    radius: self.width / 2
    # elevation: 3
<Image>
    size_hint: None, None
    allow_stretch: False
    
    # # size: "40dp", "40dp"
    # radius: self.width / 2
    # elevation: 3
""")

class RoundImage(FitImage):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Image(FitImage):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    