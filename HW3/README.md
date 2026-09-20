Week 3: DNA Pattern Matching

Pattern matching helps find known sequences and related regions in DNA databases. A seed-and-extend search starts with a short exact match, then checks the surrounding sequence. Longer seeds can reduce the search work but may miss related sequences. Expected match counts help distinguish common patterns from matches that are unlikely to occur by chance.

This assignment explores expected matches, search speed and sensitivity and searching multiple DNA patterns with a trie. A trie is a data structure resembling a directed graph that stores shared beginnings of patterns together. The solution files are described in the order of the assignment, with main.py at the end.

Assignment and provided files

- A3.pdf: The assignment sheet provided for the course.
- DNA.txt: The DNA search database, containing a region of human chromosome 12 in FASTA format.
- queries.txt: A dictionary of four DNA patterns to search for.
- queries2.txt: A larger dictionary containing 605 DNA patterns.

computing.py: Calculates estimated speed-up and sensitivity for seed lengths from 5 to 40. It uses 100-base queries and an assumed mismatch rate of 15% to compare the search settings.

trie.py: Stores query patterns in a trie without failure links, following the assignment's search approach. It follows matching letters through the tree to identify a pattern in a DNA substring.

eVals.py: Estimates how many times a query would occur by chance in DNA.txt. It uses the database's base frequencies, the query's letters and the number of possible match positions.

newDNA.txt: I manually created this test file from the first 4000 bases of DNA.txt and added the first query, AATAGCTAACA, at the beginning. This let me check the search on a smaller dataset with a known match before using the full database.

main.py: Search script combining trie.py and eVals.py to compare expected and observed matches. It reads DNA.txt, searches for patterns from queries2.txt at each position and prints both counts for each query.
