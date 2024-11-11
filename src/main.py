"""
$ kivymd.create_project \
>     MVC \
>     "/c/Users/mxnyers/Documents/Python Test Programs/KivyTestBApp" \
>     KivyTestBApp \
>     python3
"""

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from View.screens import screens

import pythonbible as bible

class KivyTestBApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = MDScreenManager()
        
    def build(self) -> MDScreenManager:
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self) -> None:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """

        for i, name_screen in enumerate(screens.keys()):
            books = [e.value for e in bible.books.Book]
            book_titles = []
            for j in books:
                book_titles.append(bible.get_book_titles(bible.Book(int(j))).short_title)
            model = screens[name_screen]["model"](None,None,None,None,book_titles,None,None)
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)


KivyTestBApp().run()
