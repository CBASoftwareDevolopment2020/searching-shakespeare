from collections import deque
from time import time


def count_match(string: str, int_start: int, int_end: int, other_start: int) -> int:
    length = int_end - int_start
    for i in range(length):
        if string[int_start + i] != string[other_start + i]: return i
    return length


class Node:
    def __init__(self):
        self._children = deque()

    def add(self, string: str, start: int, end: int, val: int):
        node = next((child for child in self._children if string[child.start] == string[start]), None)
        if not node:
            self._children.append(KeyNode(start, end, val))
        elif type(node) is LinkedNode:
            node.add(string, start, end, val)
        else:
            # print(type(node), 'should be KeyNode')
            self._split_key_node(string, node, start, end, val)

    def _split_key_node(self, string: str, node, start: int, end: int, val: int):
        count = count_match(string, start, end, node.start)
        new_linked_node = LinkedNode(node.start, node.start + count)
        new_key_node1 = KeyNode(node.start + count, node.end, node.val)
        new_key_node2 = KeyNode(start + count, end, val)
        new_linked_node.children.append(new_key_node1)
        new_linked_node.children.append(new_key_node2)
        self._children.remove(node)
        self._children.appendleft(new_linked_node)

    def locate(self, string: str, substring: str):
        node = next(child for child in self._children if string[child.start] == substring[0])
        return node.locate(string, substring) if node else node

    def find_res_vals(self, idxs: list, max_res: int):
        for child in self._children:
            child.find_res_vals(idxs, max_res)
            if len(idxs) > max_res: break


class KeyNode(Node):
    def __init__(self, start: int, end: int, val: int):
        self.start = start
        self.end = end
        self.val = val

    def locate(self, string: str, substring: str) -> Node:
        node_length = self.end - self.start
        n = len(substring)
        return self if n <= node_length and string[self.start:self.start + n] == substring else None

    def find_res_vals(self, idxs: list, max_res: int):
        idxs.append(self.val)


class LinkedNode(Node):
    def __init__(self, start: int, end: int):
        self.start = start
        self._end = end
        self.children = deque()

    def add(self, string: str, start: int, end: int, val: int):
        if end - start < self._end - self.start:
            count = count_match(string, start, end, self.start)
            self.split_linked_node(start, end, val, count)
        else:
            count = count_match(string, self.start, end, start)
            if self.start + count < self._end:
                self.split_linked_node(start, end, val, count)
            else:
                start += count
                if start == end:
                    self.children.append(KeyNode(start, end, val))
                else:
                    node = next((child for child in self.children if string[child.start] == string[start]), None)
                    if not node:
                        self.children.append(KeyNode(start, end, val))
                    elif type(node) is LinkedNode:
                        node.add(string, start, end, val)
                    else:
                        # print(type(node), 'should be KeyNode')
                        self._split_key_node(string, node, start, end, val)

    def split_linked_node(self, start: int, end: int, val: int, count: int):
        new_linked_node = LinkedNode(self.start + count, self._end)
        new_linked_node.children = self.children
        new_key_node = KeyNode(start + count, end, val)
        self.children = deque([new_linked_node, new_key_node])
        self._end = self.start + count

    def _split_key_node(self, string: str, node: KeyNode, start: int, end: int, val: int):
        count = count_match(string, start, end, node.start)
        new_linked_node = LinkedNode(node.start, node.start + count)
        new_key_node1 = KeyNode(node.start + count, node.end, node.val)
        new_key_node2 = KeyNode(start + count, end, val)
        new_linked_node.children.append(new_key_node1)
        new_linked_node.children.append(new_key_node2)
        self.children.remove(node)
        self.children.appendleft(new_linked_node)

    def locate(self, string: str, substring: str) -> Node:
        node_length = self._end - self.start
        if len(substring) <= node_length:
            return self if string[self.start:self.start + len(substring)] == substring else None
        if substring.startswith(string[self.start:node_length]): return None

        node = next(child for child in self.children if string[child.start] == substring[node_length])

        return node.locate(string, substring[node_length:]) if node else node

    def find_res_vals(self, idxs: list, max_res: int):
        for child in self.children:
            if len(idxs) > max_res: break
            child.find_res_vals(idxs, max_res)


class SuffixTree:
    def __init__(self, string: str):
        self.string = string
        self.lower_string = self.string.lower()
        self._root = Node()
        self.length = len(self.lower_string)

        for i in range(self.length):
            self._root.add(self.lower_string, i, self.length, i)

    def search(self, string: str, max_res: int = 50, extra_chars: int = 100) -> list:
        res = []
        res_idxs = []
        string = string.lower()

        node = self._root.locate(self.lower_string, string)
        if not node: return res
        node.find_res_vals(res_idxs, max_res)
        res_idxs = sorted(res_idxs)

        for idx in res_idxs:
            res.append(f'Index: {idx}, {self.string[idx:idx + len(string) + extra_chars]}')
        return res


if __name__ == '__main__':
    start = time()
    st = SuffixTree('Hello World!')
    end = time()
    print(end - start)
