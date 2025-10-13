from abc import ABC, abstractmethod

class Medium(ABC):
    def __init__(self,title):
        self.__title = title
        self.__available = True

    @abstractmethod
    def info(self):
        pass

    @property
    def title(self):
        return self.__title

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, value: bool):
        self.__available = value


class Book(Medium):
    def __init__(self,title,author,genre):
        super().__init__(title)
        self.__author = author
        self.__genre = genre

    def info(self):
        return(f"Buch '{self.title}' von {self.__author}, Genre: {self.__genre}, verfügbar: {self.available}")

    @property
    def author(self):
        return self.__author

    @property
    def genre(self):
        return self.__genre


class Dvd(Medium):
    def __init__(self,title,director,runtime):
        super().__init__(title)
        self.__director = director
        self.__runtime = runtime

    def info(self):
        return(f"DVD '{self.title}', Director: {self.__director}, Runtime: {self.__runtime} Min, verfügbar: {self.available}")

    @property
    def director(self):
        return self.__director

    @property
    def runtime(self):
        return self.__runtime


class LibraryManager:
    def __init__(self):
        self.__library = []

    @property
    def media(self):
        Media = self.show_all_media_info()
        for x in Media:
            print(x)

    def add_medium(self, medium: Medium):
        self.__library.append(medium)

    def show_all_media_info(self):
        media_list = []
        for x in self.__library:
            media_list.append(x.info())
        return media_list

    def borrow(self,title:str):
        for x in self.__library:
            if x.title == title:
                x.available = False

    def return_item(self,title:str):
        for x in self.__library:
            if x.title == title:
                x.available = True


# Beispiel
lm = LibraryManager()
b = Book("Der Herr der Ringe", "J.R.R. Tolkien", "Fantasy")
d = Dvd("Inception", "Christopher Nolan", 148)

print("[OPERATION] Zwei Medien werden zur Bibliothek hinzugefügt...")
lm.add_medium(b)
lm.add_medium(d)
lm.media

print("[OPERATION] Zwei Medien werden ausgeliehen...")
lm.borrow("Der Herr der Ringe")
lm.borrow("Inception")
lm.media

print("[OPERATION] Ein Buch wird zurückgegeben...")
lm.return_item("Der Herr der Ringe")
lm.media
