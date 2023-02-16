import os
import shutil

import plyer
# from kaki.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.text import DEFAULT_FONT
from kivy.core.window import Window
from kivy.event import EventDispatcher
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (AliasProperty, BooleanProperty, ColorProperty,
                             ListProperty, NumericProperty, ObjectProperty,
                             OptionProperty, StringProperty,
                             VariableListProperty)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (CommonElevationBehavior,
                                  RectangularRippleBehavior)
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.spinner import MDSpinner

"Riverdale"
_is_desktop = False
if Config:
    _is_desktop = Config.getboolean('kivy', 'desktop')
Window.size = (350, 650)


class WindowManager(ScreenManager):
    pass


class Item(OneLineAvatarListItem):
    divider = None


class MyButton(RectangularRippleBehavior, ButtonBehavior, MDFloatLayout):

    text = StringProperty()
    ripple_scale = NumericProperty(0.85)


class MyCheckButton(MDBoxLayout):

    text = StringProperty()
    checked = BooleanProperty(False)
    ripple_scale = NumericProperty(0.85)


class TextField(MDFloatLayout, CommonElevationBehavior, ThemableBehavior):
    hint = StringProperty()
    text = StringProperty()


class Home(Screen):
    def choose_project(self, *args):
        """
        The choose_project function is called when the user clicks on the &quot;Choose Project&quot; button. 
        It opens a file chooser dialog that allows them to choose a directory and saves it as their project path.


        :param self: Access the class attributes
        :param *args: Pass a variable number of arguments to a function
        :return: The path of the selected folder
        :doc-author: Trelent
        """

        plyer.filechooser.choose_dir(
            on_selection=self.save_path)

    def choose_project_scheduler(self):
        Clock.schedule_once(self.choose_project, 1)

    def save_path(self, *args):
        """
        The save_path function is called when the user clicks on the &quot;Create Project&quot; button.
        It takes in a list of arguments, which are passed to it by its parent class (ProjectCreator).
        The save_path function then checks if there is a path selected. If not, it calls the choose() function to prompt 
        the user to select one. If there is a path selected, then it proceeds with creating and saving all of the necessary files 
        and folders for our project.

        :param self: Access the class attributes and methods
        :param *args: Pass a variable number of arguments to a function
        :return: The path that the user has chosen
        :doc-author: Trelent
        """

        try:
            self.confirm_path = MDDialog(
                title="Continue?", text=f"You have chosen [color=#b90000]{args[0][0]}[/color] as the path to create your project\n\n Are you sure you want to continue with the chosen path?", buttons=[MDFlatButton(text="ofcourse, [b]let's do this![/b]", on_press=self.proceed), MDFlatButton(text="No, let's change it!", on_press=self.change)])

            path = args[0][0].replace("\\", "/")
            self.ids['path'].text = path
            with open("path.txt", 'w') as f:
                f.write(path)
            self.confirm_path.open()
        except IndexError as e:
            self.show(title="[color=#b90000]Error[/color]",
                      message="The folder selected cannot be written to. Please select a more probable folder.", method="dialog")
            # self.choose()
            # self.notice.dismiss()
            print(f'folder error: {e}')
            # self.choose()

    def proceed(self, *args):
        """
        The proceed function is called when the user clicks on the &quot;Proceed&quot; button.
        It takes a single argument, which is a list of strings that were passed in from
        the kivy file.

        :param self: Access the attributes and methods of the class in python
        :param *args: Pass a variable number of arguments to a function
        :return: The path that the user has selected
        :doc-author: Trelent
        """
        # self.ids['path'].text = path

        print(f'proceed_args:: {args}')
        self.confirm_path.dismiss()
        with open("path.txt", 'r') as f:
            ppath = f.read()
            print(ppath)
            # self.ids.path.text = ppath
            # print(self.ids)
        self.show(message="path set successfully!")

    def change(self, *args):
        """
        The change function is used to change the path of the file that will be opened.
        It takes no arguments and returns nothing.

        :param self: Access the attributes and methods of the class in python
        :param *args: Pass a variable number of arguments to a function
        :return: The value of the confirm_path attribute
        :doc-author: Trelent
        """

        self.choose_project()
        self.confirm_path.dismiss()

    def show(self, message, title="", method="snackbar"):
        if method == "snackbar":

            Snackbar(text=f"{message}").open()

        elif method == "dialog":
            self.show_dialog = MDDialog(
                title=f"{title}", text=f"{message}", buttons=[MDRaisedButton(text="[b]Got It![/b]", md_bg_color="purple", on_press=self.close), ])
            self.show_dialog.open()

    def close(self, obj):
        self.show_dialog.dismiss()

    def get_path(self):
        with open("path.txt", 'r') as f:
            ppath = f.read()
            ppath = ppath.replace("\\", "/")

            print(ppath)
        return ppath

    def project_path(self, project_name):
        path = self.get_path()

        path = f"{path}/{project_name}"
        return path

    def build_main(self, project_name, screen_name, *args):
        path = self.project_path(project_name)

        with open("paths/main.txt", "r") as f:
            main_content = f.read()

            main_content = main_content.replace(
                "app_name", project_name.title())

            main_content = main_content.replace(
                "name_screen", screen_name)

            with open(f"{path}/main.py", "w") as f:
                f.write(main_content)

    def build_main_hot_reload(self, project_name, screen_name, *args):
        path = self.project_path(project_name)

        with open("paths/main_hot.txt", "r") as f:
            main_content = f.read()

            main_content = main_content.replace(
                "app_name", project_name.title())

            main_content = main_content.replace(
                "name_screen", screen_name.title())

            main_content = main_content.replace(
                "kv_screen", screen_name)

            with open(f"{path}/main.py", "w") as f:
                f.write(main_content)


    def build_appp(self, project_name, *args):
        folder = "app"
        path = self.project_path(project_name)

        with open("paths/app.txt", "r") as f:
            app_content = f.read()

            with open(f"{path}/{folder}/app.py", "a") as f:
                f.write(app_content)

    def build_controllers(self, project_name, screen_name, *args):
        folder = "controllers"
        path = self.project_path(project_name)

        with open("paths/controllers.txt", "r") as f:
            controllers_content = f.read()

            controllers_content = controllers_content.replace(
                "name_of_screen", screen_name.title())

            controllers_content = controllers_content.replace(
                "screen_kv", screen_name+".kv")

            with open(f"{path}/{folder}/{screen_name}.py", "a") as f:
                f.write(controllers_content)

    def database_dialog(self, *args):
        self.db_dialog = MDDialog(
            title="Database",
            type="simple",
            items=[
                Item(text="sqlite3", on_press=self.pick_db),
                Item(text="Firebase", on_press=self.pick_db),
            ],
        )

        self.db_dialog.open()
        print(args)

    def pick_db(self, inst):
        choice: str = inst.text
        print(inst)

        with open("db.txt", "w") as f:
            f.write(choice)

        self.db_dialog.dismiss()
        self.show(f"preparing {choice} database ...")

    def build_database(self, project_name):
        folder = "models"
        path = self.project_path(project_name)

        with open("db.txt", "r") as f:
            choice = f.read()

        with open(f"paths/{choice.lower()}.txt", "r") as f:
            db_content = f.read()

            with open(f"{path}/{folder}/{choice.lower()}.py", "w") as f:
                f.write(db_content)

    def build_views(self, project_name, screen_name, *args):
        path = self.project_path(project_name)
        folder = "views"

        with open("paths/views.txt", "r") as f:
            views_content = f.read()

            views_content = views_content.replace(
                "name_of_screen", screen_name.title())

            with open(f"{path}/{folder}/{screen_name}.kv", "w") as f:
                f.write(views_content)

    def build_imports_kv(self, project_name, *args):
        path = self.project_path(project_name)

        with open("paths/imports.txt", "r") as f:
            imports_content = f.read()

            with open(f"{path}", "w") as f:
                f.write(imports_content)

    def build_androidly(self, project_name, *args):
        path = self.project_path(project_name)
        folder = "models"

        with open("paths/androidly.txt", "r") as f:
            androidly_content = f.read()

            with open(f"{path}/{folder}/androidly.py", "w") as f:
                f.write(androidly_content)

    def build_screens(self, project_name, screen_name, end=False, * args):
        path = self.project_path(project_name)
        folder = "models"

        with open("paths/screens.txt", "r") as f:
            screens_content = f.read()

            screens_content = screens_content.replace(
                "name_of_screen", screen_name.title())

            screens_content = screens_content.replace(
                "screen_name", screen_name)

        with open(f"{path}/{folder}/screens.json", 'a') as f:
            f.write(screens_content)

        # if end == True:
    def add_braces_to_screens_json(self, project_name):
        path = self.project_path(project_name)
        folder = "models"

        with open(f"{path}/{folder}/screens.json", 'r') as f:
            add_braces = f.read()
            added_braces = '{' + add_braces + '}'

        with open(f"{path}/{folder}/screens.json", 'w') as f:
            f.write(added_braces)

    def build_widgets(self, project_name, *args):
        dir = "widgets"
        path = self.project_path(project_name=project_name)
        shutil.copytree(
            dir, f"{path}/widgets")

    def build_assets(self, project_name, *args):
        pass

    def build_project(self, *args):
        project_name: str = self.ids['project_name_field'].text
        screen_names: str = self.ids['screen_name_field'].text
        app_color: str = self.ids['color_field'].text
        database: bool = self.ids['database_'].checked
        hotreload: bool = self.ids['hotreload_'].checked
        if_simple: bool = self.ids['simple_'].checked

        path = self.get_path()
        path = f"{path}/{project_name}"

        print(f"project name: {project_name}")
        print(f"path: {path}")

        if project_name == "":
            self.loading_dialog.dismiss()
            self.show(message="Provide  your project name")

        elif not screen_names:
            self.loading_dialog.dismiss()
            self.show(message="Provide your screen names")

        elif "," not in screen_names and if_simple == False:
            self.loading_dialog.dismiss()
            self.show(
                message="screen names should be separated by ',' ")

        elif self.get_path() == "":
            self.loading_dialog.dismiss()
            self.show(
                message="Please choose a directory for your project")

        else:

            self.generate_paths(path=path)
            screen_names = screen_names.split(',')
            for screen_name in screen_names:

                self.build_controllers(
                    project_name=project_name, screen_name=screen_name)

                self.build_views(project_name=project_name,
                                 screen_name=screen_name)

                self.build_screens(project_name=project_name,
                                   screen_name=screen_name)

            self.build_appp(project_name=project_name)

            self.build_androidly(project_name=project_name)

            self.add_braces_to_screens_json(project_name=project_name)

            self.build_widgets(project_name=project_name)

            if hotreload == False:
                self.build_main(project_name=project_name,
                                screen_name=screen_names[0])
            elif hotreload == True:
                self.build_main_hot_reload(
                    project_name=project_name, screen_name=screen_names[0])

            if database == True:
                print(database)
                self.build_database(project_name=project_name)

            self.loading_dialog.dismiss()

    def generate_paths(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
            os.mkdir(f"{path}/app")
            os.mkdir(f"{path}/controllers")
            os.mkdir(f"{path}/models")
            os.mkdir(f"{path}/views")
            os.mkdir(f"{path}/assets")
            print("mkdir")
        else:
            self.show(message=f"{path} folder already exists")

    def loader(self):
        # content = MDSpinner(
        #     size= dp(46), dp(46),
        #     size_hint= (None, None),
        #     pos_hint= {'center_x': .5, 'center_y': .5},
        #     ),
        # view = ModalView(auto_dismiss=False)
        # view.add_widget(content)
        spinner = Factory.MDSpinner(line_width=dp(2.5), color="white")
        self.loading_dialog = ModalView(
            auto_dismiss=False,
            background="",
            background_color=[1, 1, 1, 0],  # same as 0,0,0,0
            size_hint=(None, None),
            size=(dp(50), dp(50)),
            on_pre_open=lambda x: setattr(spinner, "active", True),
            on_dismiss=lambda x: setattr(spinner, "active", False)
        )
        self.loading_dialog.add_widget(spinner)
        self.loading_dialog.open()

        Clock.schedule_once(self.build_project, 1)
# class ProjectBuilder(MDApp, App):


class ProjectBuilder(MDApp):
    DEBUG = 1  # To enable Hot Reload

    # *.kv files to watch
    KV_FILES = ["projectbuilder1.kv"]

    # Class to watch from *.py files
    # You need to register the *.py files in libs/uix/baseclass/*.py
    # CLASSES = {"Root": "libs.libpy.root", "Home": "libs.libpy.home"}

    # Auto Reloader Path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    AUTORELOADER_IGNORE_PATTERNS = [
        "*.pyc", "*__pycache__*", "*p4a_env_vars.txt*", "*sitecustomize.py*", "*/.kivy*"
    ]

    # def build_app(self):
    def build(self):

        # Create a list of all screen, loop through it and add it to the screenmanager
        # and return the screenmanager.
        self.wm = WindowManager()
        Builder.load_file("projectbuilder1.kv")

        screens = [
            Home(name="home"),
        ]

        for screen in screens:
            self.wm.add_widget(screen)

        return self.wm

    def on_start(self):
        with open("path.txt", 'w') as f:
            f.write('')

if __name__ == "__main__":
    ProjectBuilder().run()
