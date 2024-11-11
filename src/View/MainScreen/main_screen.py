from View.base_screen import BaseScreenView
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton


class MainScreenView(BaseScreenView):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        book_items = [
            {
                "text": f"{book}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x =f"{book}": self.controller.book_selection_callback(x, self.ids.book_label, self.book_menu)} for book in self.model.all_books
        ]
        
        self.book_menu = MDDropdownMenu(
            caller = self.ids.book,
            items=book_items,
            width_mult=4,
            max_height=150
        ) 
        
    
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        
        if(self.model.book != None):
            self.ids.chapter.disabled = False
            chapter_items = [
                {
                    "text": f"{chapter}",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x =f"{chapter}": self.controller.chapter_selection_callback(x, self.ids.chapter_label, self.chapter_menu)
                    } for chapter in self.model.selectable_chapters
            ]
            
            self.chapter_menu = MDDropdownMenu(
                caller = self.ids.chapter,
                items=chapter_items,
                width_mult=3,
                max_height=150
            ) 
            
        if(self.model.chapter != None):
            self.ids.verse.disabled = False
            verse_items = [
                {
                    "text": f"{verse}",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x =f"{verse}": self.controller.verse_selection_callback(x, self.ids.verse_label, self.verse_menu)
                    } for verse in self.model.selectable_verses
            ]
            
            self.verse_menu = MDDropdownMenu(
                caller = self.ids.verse,
                items=verse_items,
                width_mult=3,
                max_height=150
            ) 
        
