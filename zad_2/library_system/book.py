from .library import Library


class Book:
    """
    Class containing info on books available in the libraries
    """
    def __init__(self, library: Library, publication_name: str,
                 author_name: str, author_surname: str,
                 number_of_pages: int) -> None:
        self.library = library
        self.publication_name = publication_name
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f'Book info. Library: {self.library}, \
                 publication name: {self.publication_name}, \
                 author {self.author_surname} {self.author_name} \
                 number of pages {self.number_of_pages}'
