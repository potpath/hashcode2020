import concurrent.futures
import importlib
import sys
from util import Book, Library


def cal_all(input_file):
    print(f'Running {input_file}')
    with open(input_file) as fin:
        n_book, n_lib, n_day = map(int, next(fin).split())
        books = [Book(book_id, score) for book_id, score in enumerate(map(int, next(fin).split()))]
        libs = []
        for lib_id in range(n_lib):
            _, signup_day, book_per_day = map(int, next(fin).split())
            books_in_lib = [books[book_id] for book_id in map(int, next(fin).split())]
            if signup_day >= n_day:
                continue
            lib = Library(lib_id, signup_day, book_per_day, books_in_lib)
            libs.append(lib)

    answers = cal(books, libs, n_day)

    if input_file.endswith('.txt'):
        input_file = input_file[:-4]
    output_file = algo_name + '_' + input_file + '.out'
    with open(output_file, 'w') as fout:
        print(len(answers), file=fout)
        for ans in answers:
            if not ans.book_to_scan:
                continue
            print(ans.lib.id, len(ans.book_to_scan), file=fout)
            print(' '.join(str(book.id) for book in ans.book_to_scan), file=fout)
    print(f'Done {input_file}')


algo_name, *input_files = sys.argv[1:]
if algo_name.endswith('.py'):
    algo_name = algo_name[:-3]
cal = importlib.import_module(algo_name).cal

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(cal_all, input_files, chunksize=1)

# for input_file in input_files:
#     cal_all(input_file)
