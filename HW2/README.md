Week 2: Sequence Alignment Implementation and Comparison

Sequence alignment is central to bioinformatics, helping identify related genes, align shorter dna sequences to a genome and understand evolutionary relationships. It places two DNA sequences alongside each other to compare their bases. A match occurs when the aligned bases are the same and a mismatch occurs when they differ. An indel is an insertion or deletion, represented by a gap in one of the aligned sequences. Local alignment finds the regions with the highest alignment score rather than requiring both sequences to align from beginning to end. Matches increase the score while mismatch and gap penalties reduce it. A linear gap penalty charges the same amount for each base in a gap.

This assignment covers local DNA sequence alignment with linear gap penalties, random DNA generation, the effect of scoring parameters on alignment length and memory-conscious alignment of longer sequences. The solution files are described in the order of the assignment.

Assignment and provided files

- A2.pdf: The assignment sheet provided for the course.
- p1seqs.txt: The course-provided DNA sequence pair for the local alignment task.
- p4pairs.txt: The course-provided longer DNA sequence pair for the memory-use task.

locAL.py: Local alignment task using dynamic programming in main.py to align the sequences from p1seqs.txt with user-selected scores. It reports the score and length and optionally prints the alignment.

randomDNA.py: Generates a chosen number of DNA sequences of a chosen length, giving each base an equal chance of appearing. It prints the sequences and their observed nucleotide frequencies.

graph.py: Scoring comparison aligning 500 random pairs of 1000-base sequences using the dynamic programming functions in main.py. It plots histograms showing how alignment lengths differ between two scoring settings.

graph3.py: Explores whether alignment lengths change abruptly as mismatch and indel penalties change. It uses the dynamic programming functions in main.py to calculate and plot average alignment lengths across different settings.

locAlLong.py: Longer-sequence task using the pair from p4pairs.txt. It keeps two rows of dynamic programming scores to locate the alignment region, then reconstructs the alignment within that smaller region. q4.txt saves a length of 140 and score of 56.0; answers.txt saves the same alignment as q1.txt with the length before the score.

main.py: Shared functions providing dynamic programming for the alignment tasks and random-sequence experiments. A traceback matrix records the steps used to build an alignment so they can be followed backward to recover the aligned sequences. This file also generates random DNA, calculates average alignment lengths and provides the two-row scoring method used by locAlLong.py.
