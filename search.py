from collections import deque
import string
from node import Node
from dictionary import Dictionary

class Search:
    def __init__(self, start_word, end_word):
        self.start_word = start_word
        self.end_word = end_word
        self.dictionary = Dictionary("words.txt")

    def bfs(self):
        queue = deque([(Node(self.start_word))])
        visited = set([self.start_word])
        nodes_expanded = 0

        while queue:
            current_node = queue.popleft()
            nodes_expanded += 1

            if current_node.value == self.end_word:
                return self.construct_path(current_node), nodes_expanded

            for i in range(len(current_node.value)):
                for c in string.ascii_lowercase:
                    new_word = current_node.value[:i] + c + current_node.value[i+1:]
                    if self.dictionary.search_word(new_word) and new_word not in visited:
                        new_node = Node(new_word)
                        new_node.set_parent(current_node)
                        queue.append(new_node)
                        visited.add(new_word)

        return None, nodes_expanded

    def dfs(self):
        stack = [Node(self.start_word)]
        visited = set()
        nodes_expanded = 0

        while stack:
            current_node = stack.pop()
            nodes_expanded += 1

            if current_node.value == self.end_word:
                return self.construct_path(current_node), nodes_expanded

            if current_node.value not in visited:
                visited.add(current_node.value)

                for i in range(len(current_node.value)-1, -1, -1):
                    for c in string.ascii_lowercase:
                        new_word = current_node.value[:i] + c + current_node.value[i+1:]
                        if self.dictionary.search_word(new_word) and new_word not in visited:
                            new_node = Node(new_word)
                            new_node.set_parent(current_node)
                            stack.append(new_node)

        return None, nodes_expanded

    def construct_path(self, node):
        path = []
        while node:
            path.append(node.value)
            node = node.get_parent()
        return path[::-1]
