# Automated import from: https://github.com/ndleah/python-mini-project.git
# Original Author: ndleah

from trie import Trie

trie = Trie()
trie.insert("apple")
trie.search("apple")    # return True
trie.search("app")      # return False
trie.starts_with("app")  # return True
trie.insert("app")
trie.search("app")      # return True
