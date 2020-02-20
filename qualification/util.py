from collections import defaultdict


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
    def __init__(self, lib, book_to_scan):
        self.lib = lib
        self.book_to_scan = book_to_scan


def unique(answers, n_day):
    book_done = set()
    lib_done = set()
    nth_book = defaultdict(int)
    new_ans = [Answer(ans.lib, []) for ans in answers]
    last_registered_day = 0
    for day in range(n_day):
        if len(lib_done) < len(answers):
            lib_to_be_registered = answers[len(lib_done)].lib
            if day == last_registered_day + lib_to_be_registered.signup_day:
                lib_done.add(lib_to_be_registered)
                last_registered_day = day
        for i_ans, ans in enumerate(answers):
            lib = ans.lib
            if lib not in lib_done:
                continue
            ok_count = 0
            for book in ans.book_to_scan[nth_book[lib]:]:
                if book not in book_done:
                    book_done.add(book)
                    new_ans[i_ans].book_to_scan.append(book)
                    ok_count += 1
                    if ok_count == lib.book_per_day:
                        break
            nth_book[lib] += 1

    return new_ans
