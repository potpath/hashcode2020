from util import Answer


def cal(books, libs):
    def sort_by_signup_day(lib):
        return -lib.book_per_day, lib.signup_day

    sort_keys = [
        sort_by_signup_day,
    ]
    answers = []
    for key in sort_keys:
        sorted_libs = sorted(libs, key=key)
        for lib in sorted_libs:
            ans = Answer(lib.id, sorted(lib.books, key=lambda book: book.score))
            answers.append(ans)

    return answers
