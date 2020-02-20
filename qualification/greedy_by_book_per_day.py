from util import Answer, unique


def cal(books, libs, n_day):
    def sort_by_signup_day(lib):
        return -lib.book_per_day, lib.signup_day

    sorted_libs = sorted(libs, key=sort_by_signup_day)
    answers = []
    for lib in sorted_libs:
        ans = Answer(lib, sorted(lib.books, key=lambda book: -book.score))
        answers.append(ans)

    answers = unique(answers, n_day)
    return answers
