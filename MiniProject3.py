import tkinter as tk
from time import time

from suffix_tree_v1 import SuffixTree as st_v1
from suffix_tree_v2 import SuffixTree as st_v2


def read_file(path):
    with open(path, encoding="utf-8-sig") as f:
        return f.read()


def time_create_suffix_tree(string: str, out: str, case_insensitive=False):
    start = time()
    # st = st_v1(string)
    st = st_v2(string, case_insensitive=case_insensitive)
    end = time()
    time_elapsed = end - start
    print(out, time_elapsed)
    return st


def search_text():
    global text
    global bible_st
    global search
    global output
    substring = search.get()
    index_start = bible_st.find_substring(substring)
    index_end = index_start + 100
    msg = text[index_start:index_end] if index_start != -1 else 'Not found in text'
    output.configure(text=msg)


if __name__ == '__main__':
    file = 'king-james-bible.txt'
    text = read_file(file)
    bible_st = time_create_suffix_tree(text, file, True)

    main = tk.Tk()
    in_frame = tk.Frame(main)
    in_frame.pack()
    out_frame = tk.Frame(main)
    out_frame.pack()
    close_frame = tk.Frame(main)
    close_frame.pack()

    tk.Label(in_frame, text=f'Search {file[:-4]}').grid(row=0)
    search = tk.Entry(in_frame)
    search.grid(row=0, column=2)
    confirm = tk.Button(in_frame, text='Search', width=10, command=search_text)
    confirm.grid(row=0, column=3)

    output = tk.Message(out_frame, text=text[:1000], width=1920)
    output.grid()

    button = tk.Button(close_frame, text='Close', width=25, command=main.destroy)
    button.grid()

    main.mainloop()
