Week 1: Fasta File Processing

FASTA is widely used in bioinformatics to store and share DNA, RNA and protein sequences across databases and analysis tools. Each entry has a header starting with > that identifies the sequence, followed by the sequence letters. A multi-FASTA file holds several entries.

This assignment uses Python to read FASTA files, count sequence lengths, filter by species and look up sequences. The solution files are described in the order of the assignment.

Assignment and provided files

- a1.pdf: The assignment sheet provided for the course.
- datafile.txt: A multi-FASTA dataset containing 16 protein sequences and their headers.
- data.seq: The protein sequences joined with @ separators and no headers.
- data.in: An index of sequence identifiers and positions used for lookup.

cat.py: Reads datafile.txt and prints each sequence's header and length, skipping blank lines.

filter.py: Selects mouse and rat sequences from datafile.txt by checking their headers. It prints the selected entries in FASTA format with up to 60 sequence letters per line.

seq.py: Builds the sequence format used in data.seq. It reads datafile.txt, removes headers and line breaks and joins the sequences with @ separators.

in.py: The indexing task pairs each sequence's GI identifier with its starting position. My solution reads headers from datafile.txt and counts sequence letters to write these pairs. file.txt contains the same index entries as data.in.

getSeq.py: Searches data.seq for a short sequence and uses data.in to find its identifier. The assigned example query is MHIQITDFGTAKVLSPDS.
