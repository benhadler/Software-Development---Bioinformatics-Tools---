Week 4: CpG Islands and Evolutionary Trees

A dinucleotide is a pair of neighboring DNA bases on a nucleotide sequence. CpG islands are regions with more C-followed-by-G pairs than the surrounding DNA and are often found near gene promoters. A Markov model describes the chance of the next base based on the current base, helping distinguish these regions. A perfect phylogeny is an evolutionary tree that explains the observed variants with each mutation occurring once and no reversals.

This assignment compares DNA base-pair frequencies, predicts CpG islands and checks whether genetic variant data can form a perfect phylogeny. It also examines how the tree-checking program's running time changes with input size. The solution files are described in the order of the assignment, with main.py at the end.

Assignment and provided files

- A4.pdf: The assignment sheet provided for the course.
- chrA.fasta: The DNA sequence used for frequency analysis and CpG island prediction.
- chrA.islands: The course-provided labels listing known CpG island start and end positions in chrA.fasta.
- a1data1.txt: A genetic variant matrix with 10 individuals and 10 sites.
- a1data2.txt: A genetic variant matrix with 100 individuals and 100 sites.
- a1data3.txt: A genetic variant matrix with 1000 individuals and 1000 sites.
- a1data4.txt: Another genetic variant matrix with 1000 individuals and 1000 sites.
- a1data5.txt: The fifth genetic variant matrix, also with 1000 individuals and 1000 sites.

freqs.py: My solution reads chrA.fasta and compares observed frequencies of all 16 dinucleotides with frequencies expected from the individual bases. These calculations also support the CpG models in main.py.

sort.py: My solution checks the five a1data files for a perfect phylogeny. It sorts the matrix columns, checks pairs for conflicting variant patterns and prints the result and running time for each dataset.

graph.py: My solution plots saved running times against the number of matrix entries using Matplotlib. It shows all five measurements and a second plot with the first three.

main.py: My CpG prediction solution uses chrA.fasta and chrA.islands to learn separate Markov models for island and non-island DNA. It compares the models in 100-base windows and joins neighboring windows with positive CpG scores into predicted regions. I created predIslands.islands by saving my predicted CpG island start and end positions from this analysis.
