Grading, submission, and late policy:
● You may work individually or in a group of up to two members.
● Please refer to the syllabus for the late submission policy.
● You must submit your assignment via Blackboard.
Project Overview
In this project, you will implement and solve the Word Ladder problem. The goal is to
transform one word into another by changing one letter at a time, with the constraint
that each intermediate word must be a valid English word. A word is considered valid
if it appears in the given dictionary file.
A Word Ladder is a sequence of words where each word differs from the previous
word by exactly one letter, and all intermediate words must be valid English words
from the dictionary. For example, to transform the word "GLASS" into "CLINK," a valid
ladder might be:
GLASS → GLANS → CLANS → CLANK → CLINK
Base Code:
The base code in Python and C++ consists of the following classes:
● Dictionary class - used to load and search the dictionary.
● Node class - used to represent nodes in the search tree.
● Search class - with placeholders for BFS and DFS methods.
Dictionary Class:
- Loads a dictionary of valid English words from a file (words.txt).
- Provides methods to search for words and retrieve words of a specific length.
- You are not required to modify this.
Node Class:
- Represents a node in the search tree, storing the current word and a pointer to its
parent node.
- You are not required to modify this.
Search Class:
- Contains the startWord and endWord as member variables.
- Includes a placeholder for the bfs() method that you will implement.
- Includes a placeholder for the dfs() method that you will implement.
main.cpp:
- Demonstrates using the Dictionary class to search for words
- Demonstrates using the Search class to find a word ladder using DFS.
Implementation:
Implement the dfs() and bfs() methods in the search.cpp/search.py file. You should
implement the graph search version of this. Use the Node class to create and track nodes.
Remember the order in which you expand nodes will vary between BFS and DFS. As we
consider only valid words, you will add to the frontier-only nodes with words in our dictionary.
