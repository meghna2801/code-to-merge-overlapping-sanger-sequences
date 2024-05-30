# code-to-merge-overlapping-sanger-sequences
PROJECT BRIEF

OVERWIEW- I designed this project as a part of my summer internship at MS Swaminathan Research Foundation, where i worked with the intersection of microbiology with computational biology which helped me hone both my wet lab skills and computing knowledge. This project aims to merge DNA sequences from a file by identifying and combining overlapping segments. it involves reading sequences, identifying overlaps and then merging them into a single, contiguous space. 

Algorithm Details:
Overlap Detection: Sequences are compared to find overlaps of the specified length. If a match is found, the sequences are merged.
Sequence Comparison: The program uses helper functions to compare sequences and verify overlaps.
Sequence Merging: Overlapping sequences are combined to form a longer sequence.

Error Handling:
The program checks for file reading errors and prompts the user if the file cannot be opened.

Benefits
Automates the process of reconstructing a longer DNA sequence from smaller fragments.
Ensures that overlapping sequences are correctly identified and merged.
Provides clear output files for both the merged sequence and any leftover sequences.

This project is particularly useful in bioinformatics for tasks such as genome assembly, where small fragments of DNA need to be accurately combined into a complete sequence.
