from util import Answer


def cal(books, libs):
    def sort_by_signup_day(lib):
        return sum(book.score for book in lib.books), -len(lib.books), -lib.book_per_day, lib.signup_day

    answers = []
    sorted_libs = sorted(libs, key=sort_by_signup_day)
    for lib in sorted_libs:
        ans = Answer(lib.id, sorted(lib.books, key=lambda book: book.score))
        answers.append(ans)

    return answers
