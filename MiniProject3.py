from suffix_tree_v1 import SuffixTree as st_v1
from suffix_tree_v2 import SuffixTree as st_v2
from time import time


def read_file(path):
    with open(path, encoding="utf-8-sig") as f:
        return f.read()


def time_create_suffix_tree(string):
    start = time()
    st = st_v2(string)
    end = time()
    time_elapsed = end - start
    print(time_elapsed)
    return st


if __name__ == '__main__':
    text = read_file('king-james-bible.txt')
    # print(text)
    bible_st = time_create_suffix_tree(text)
