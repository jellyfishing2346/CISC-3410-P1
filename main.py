from dictionary import Dictionary
from search import Search

def main():
    print("**************Dictionary usage example**************")
    file_name = "words.txt"
    dict_obj = Dictionary(file_name)
    
    if dict_obj.search_word("test"):
        print("The tested word is in our dictionary")

    print("**************Example to test search implementation **************")
    start_word = "glass"
    end_word = "clink"
    new_search = Search(start_word, end_word)

    # BFS
    bfs_result = new_search.bfs()
    if bfs_result is not None:
        bfs_path, bfs_nodes_expanded = bfs_result
        if bfs_path:
            print("BFS Word ladder found:")
            print(" -> ".join(bfs_path))
            print(f"BFS Nodes expanded: {bfs_nodes_expanded}")
        else:
            print("BFS: No word ladder found.")
    else:
        print("BFS: You are yet to implement the code, try after implementation")

    # DFS
    dfs_result = new_search.dfs()
    if dfs_result is not None:
        dfs_path, dfs_nodes_expanded = dfs_result
        if dfs_path:
            print("\nDFS Word ladder found:")
            print(" -> ".join(dfs_path))
            print(f"DFS Nodes expanded: {dfs_nodes_expanded}")
        else:
            print("DFS: No word ladder found.")
    else:
        print("DFS: You are yet to implement the code, try after implementation")

    # Compare results
    if bfs_result is not None and dfs_result is not None:
        print("\nComparison:")
        print(f"BFS path length: {len(bfs_path) - 1}, Nodes expanded: {bfs_nodes_expanded}")
        print(f"DFS path length: {len(dfs_path) - 1}, Nodes expanded: {dfs_nodes_expanded}")

if __name__ == "__main__":
    main()
