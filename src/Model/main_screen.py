from Model.base_model import BaseScreenModel


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """
    
    def __init__(self,book,chapter,verse,text,all_books,selectable_chapters,selectable_verses):
        #Initialize private properties
        self._book = None	
        self._chapter = None	
        self._verse = None	
        self._text = None
        self._all_books = None
        self._selectable_chapters = None
        self._selectable_verses = None
        
        #Call on value to set
        self.book = book
        self.chapter = chapter	
        self.verse = verse	
        self.text = text
        self.all_books = all_books
        self.selectable_chapters = selectable_chapters
        self.selectable_verses = selectable_verses
        
    #Declare properties
    @property
    def book(self):
        return self._book
    
    @property
    def chapter(self):
        return self._chapter
    
    @property
    def verse(self):
        return self._verse
    
    @property
    def text(self):
        return self._text
    
    @property
    def all_books(self):
        return self._all_books
    
    @property
    def selectable_chapters(self):
        return self._selectable_chapters
    
    @property
    def selectable_verses(self):
        return self._selectable_verses
    
    #Set Properties
    @book.setter
    def book(self, value):
        self._book = value
        
    @chapter.setter
    def chapter(self, value):
        self._chapter = value
        
    @verse.setter
    def verse(self, value):
        self._verse = value
        
    @text.setter
    def text(self, value):
        self._text = value
        
    @all_books.setter
    def all_books(self, value):
        self._all_books = value
    
    @selectable_chapters.setter
    def selectable_chapters(self, value):
        self._selectable_chapters = value
        
    @selectable_verses.setter
    def selectable_verses(self, value):
        self._selectable_verses = value