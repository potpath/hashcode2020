from util import Answer

'''
'''
def cal(books, libs, n_day):
    def sort_by_signup_day(lib):
        scan_day = max(n_day - lib.signup_day, 0)
        sum_score = sum(book.score for book in sorted(lib.books, key=lambda book: book.score, reverse=True)[:scan_day])
        return sum_score

    answers = []
    sorted_libs = sorted(libs, key=sort_by_signup_day, reverse=True)
    for lib in sorted_libs:
        ans = Answer(lib, sorted(lib.books, key=lambda book: book.score, reverse=True))
        answers.append(ans)

    return answers


'''
def cal(books, libs, n_day):
    remain_day = n_day
    remain_libs_idx = list(range(len(libs)))
    sorted_libs = []

    def sort_by_score(lib):
        if lib.signup_day>=remain_day:
            return 10000000000000000, 10000000000000000

        max_book_can_scan = max((remain_day-lib.signup_day)*lib.book_per_day,0)
        sum_score = sum(book.score for book in lib.books[:max_book_can_scan])
        # jo_score = sum_score*lib.book_per_day*(n_day-lib.signup_day)
        jo_score = sum_score*lib.book_per_day
        return lib.signup_day, -jo_score
        # return -jo_score

    def get_next_lib(books, remain_libs, remain_day):
        sorted(remain_libs, key=sort_by_score)
        return remain_libs[0]

    while remain_day>0 and len(remain_libs_idx)>0:
        remain_libs = [libs[k] for k in remain_libs_idx]

        next_lib = get_next_lib(books, remain_libs, remain_day)
        sorted_libs.append(next_lib)
        remain_libs_idx.remove(next_lib.id)
        remain_day -= next_lib.signup_day

    answers = []
    for lib in sorted_libs:
        ans = Answer(lib.id, sorted(lib.books, key=lambda book: book.score, reverse=True))
        answers.append(ans)

    return answers
'''