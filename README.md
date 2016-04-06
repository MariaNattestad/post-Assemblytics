## Post-Assemblytics analysis buffet

This repository contains a collection of scripts for doing additional analysis beyond calling variants in Assemblytics. 

First use Assemblytics at qb.cshl.edu/assemblytics to call variants, download the zip file with all results, and use the .bed file of variants for these analyses.

Analyses available so far:
1. Basic intersection with genes (needs gff annotation file) using bedtools
2. Homopolymer analysis of insertions (needs the query fasta file, the one used in nucmer alignment)
	- this could be adapted to extract deletions as well, or any other features
	- the count_homopolymers.py script looks for homopolymers in a file containing the inserted sequence as well as the flanking sequences. 


