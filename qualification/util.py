class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score


class Library:
    def __init__(self, id, signup_day, book_per_day, books):
        self.id = id
        self.signup_day = signup_day
        self.book_per_day = book_per_day
        self.books = books


class Answer:
    def __init__(self, lib_id, book_to_scan):
        self.lib_id = lib_id
        self.book_to_scan = book_to_scan
