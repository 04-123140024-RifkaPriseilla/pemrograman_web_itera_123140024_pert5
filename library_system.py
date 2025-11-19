from abc import ABC, abstractmethod

class LibraryItem(ABC):  # abstract class
    def __init__(self, item_id, title):
        self._item_id = item_id      # protected
        self._title = title          # protected

    @property
    def title(self):  # property
        return self._title

    @abstractmethod
    def display_info(self):  # wajib override
        pass


class Book(LibraryItem):  # subclass
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.__author = author       # private

    def display_info(self):  # polymorphism
        print(f"[BOOK] ID: {self._item_id}, Judul: {self._title}, Penulis: {self.__author}")


class Magazine(LibraryItem):  # subclass
    def __init__(self, item_id, title, issue):
        super().__init__(item_id, title)
        self.__issue = issue

    def display_info(self):  # polymorphism
        print(f"[MAGAZINE] ID: {self._item_id}, Judul: {self._title}, Edisi: {self.__issue}")


class Library:  # manajemen perpustakaan
    def __init__(self):
        self.__items = []  # private list

    def add_item(self, item):
        self.__items.append(item)
        print(f"Item '{item.title}' ditambahkan.")

    def show_items(self):
        if not self.__items:
            print("Tidak ada item.")
            return
        for item in self.__items:
            item.display_info()  # polymorphism

    def search_item(self, key):
        found = False
        for item in self.__items:
            if key.lower() in item.title.lower() or key == item._item_id:
                item.display_info()
                found = True
        if not found:
            print("Item tidak ditemukan.")


if __name__ == "__main__":  # simulasi
    lib = Library()
    lib.add_item(Book("B01", "Python Dasar", "Rifka"))
    lib.add_item(Book("B02", "Algoritma", "Priseilla"))
    lib.add_item(Magazine("M01", "Tech News", "Silitonga"))

    lib.show_items()
    lib.search_item("python")
