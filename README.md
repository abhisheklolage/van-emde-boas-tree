This is an implementation of van Emde Boas Tree, an integer data structure.

Elements are in the range [0, 1, ..., u - 1]
	- u is the universe size
	- duplicates are not allowed

It has special operations like predecessor(x) and successors(x) which gives the previous and the next element present in the universe.

Following operations are implemented
	- Insertion    O(lg lg u)
	- Deletion     O(lg lg u)
	- Minimum      O(1)
	- Maximum      O(1)
	- Predecessor  O(lg lg u)
	- Successor    O(lg lg u)

TODO: Resolve side effects of Delete operation
Note: For achieving O(lg lg n) bound where n is the number of integers actually present in the tree, see y-fast trees.
