import time
from View.MainScreen.main_screen import MainScreenView
from Utility.pyttsx3_text_to_speech import TextToSpeech
from kivy.clock import Clock
import pythonbible as bible


class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = MainScreenView(controller=self, model=self.model)

    def get_view(self) -> MainScreenView:
        return self.view

    def book_selection_callback(self, text_item, dropdownBox, dropdown):
        dropdownBox.text = text_item
        selectedBook = self.convert_to_enum_name(text_item)
        if(self.model.book is not None and self.model.book != bible.Book[selectedBook]):
            self.model.book = bible.Book[selectedBook]
            self.model.chapter = None
            self.view.ids.chapter.disabled = True
            self.view.ids.chapter_label.text = ""
            self.model.verse = None
            self.view.ids.verse.disabled = True
            self.view.ids.verse_label.text = ""
        else: 
            self.model.book = bible.Book[selectedBook]
        numOfChapters = bible.get_number_of_chapters(self.model.book)
        self.model.selectable_chapters = [i+1 for i in range(numOfChapters)]
        dropdown.dismiss()
        self.view.model_is_changed()
        
    def convert_to_enum_name(self, book):
        output = book.upper()
        if not any(char.isdigit() for char in output):
                if any(char == " " for char in output):
                    output = output.replace(" ","_")                  
                #Issue Correction with short title not being the same name as the key
                if output == "SONG_OF_SOLOMON":
                    output = "SONG_OF_SONGS"               
        else:
            bookName = ""
            bookNumber = ""
            for char in output:
                if char.isdigit():
                    bookNumber += char
                else:
                    if char != " ":
                        bookName += char     
                    
            output = bookName + "_" + bookNumber
        return output
    
    def chapter_selection_callback(self, text_item, dropdownBox, dropdown):
        dropdownBox.text = text_item
        if(self.model.chapter is not None and self.model.chapter != int(text_item)): 
            self.model.verse = None
            self.view.ids.verse.disabled = True
            self.view.ids.verse_label.text = ""
        self.model.chapter = int(text_item)
        numOfVerses = bible.get_number_of_verses(self.model.book, self.model.chapter)
        self.model.selectable_verses = [i+1 for i in range(numOfVerses)]
        dropdown.dismiss()
        self.view.model_is_changed()
        
    def verse_selection_callback(self, text_item, dropdownBox, dropdown):
        dropdownBox.text = text_item
        self.model.verse = int(text_item)
        dropdown.dismiss()
        self.view.model_is_changed()
        
    def on_submit(self):
        self.read_selected_verse()
        
    def read_selected_verse(self):
        selectedVerse = bible.get_verse_id(self.model.book, self.model.chapter, self.model.verse)
        outputText = bible.get_verse_text(selectedVerse)
        TextToSpeech.text_to_speech(outputText)
        