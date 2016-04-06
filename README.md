## Post-Assemblytics analysis buffet

This repository contains a collection of scripts for doing additional analysis beyond calling variants in Assemblytics. 
These are not executable but rather just notes and code where you can substitute your own files. There is no input validation here, so make sure what each step is doing makes sense on your own files. 

First use Assemblytics at qb.cshl.edu/assemblytics to call variants, download the zip file with all results, and use the .bed file of variants for these analyses.

Analyses available so far:
* Basic intersection with genes (needs gff annotation file) using bedtools
* Homopolymer analysis of insertions (needs the query fasta file, the one used in nucmer alignment)
    * this could be adapted to extract deletions as well, or any other features
    * the count_homopolymers.py script looks for homopolymers in a file containing the inserted sequence as well as the flanking sequences. 
* Alu element analysis using RepeatMasker for intersecting deletions, and then extracting insertions from the query fasta file so we can BLAST them. This extraction from the query/assembly can also be done using bedtools, which may be faster as used in the homopolymer analysis. 
