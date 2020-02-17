import concurrent.futures
import importlib
import sys


def cal_all(input_file):
    print(f'Running {input_file}')
    with open(input_file) as fin:
        M, N = map(int, next(fin).split())
        Ss = list(map(int, next(fin).split()))
    ans = cal(M, N, Ss)
    if input_file.endswith('.in'):
        input_file = input_file[:-3]
    output_file = algo_name + '_' + input_file + '.out'
    with open(output_file, 'w') as fout:
        print(len(ans), file=fout)
        print(' '.join(map(str, ans)), file=fout)
    print(f'Done {input_file}')


algo_name, *input_files = sys.argv[1:]
if algo_name.endswith('.py'):
    algo_name = algo_name[:-3]
cal = importlib.import_module(algo_name).cal

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(cal_all, input_files, chunksize=1)
