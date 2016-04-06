#! /usr/bin/env python

# Author: Maria Nattestad
# Email: mnattest@cshl.edu

#########  Count homopolymers given a file like this (with header, whitespace delimited) ##############
######### name                      left            insertion       right
######### Assemblytics_w_1        ACCCTAAACC      TAAAC         CTAAACCCTG
######### Assemblytics_w_2        AACCCTAAAC      CCTGAACC        CTAAACCCTA
######### Assemblytics_w_3        ACCCTAAACC      TAAAC         CTAAACCCTA
######### Assemblytics_w_6        ACCCTAAACC      CTAAACC       TAAACCCTAA

import argparse
def run(args):

    f = open(args.file)
    fout = open(args.out,'w')

    fout.write(f.readline().strip() + "\t" + "homopolymer" + "\n") # header

    homopolymers_by_nucleotide = {}
    linecounter = 0
    for line in f:
        fields = line.strip().split()
        left = fields[1].upper()
        insertion = fields[2].upper()
        right = fields[3].upper()
        report = "none"

        is_homopolymer = True
        for nucleotide in insertion[1:]:
            if nucleotide != insertion[0]:
                is_homopolymer = False
        
        if is_homopolymer:
            homopolymer_nucleotide = insertion[0]
            if homopolymer_nucleotide*6 in left or homopolymer_nucleotide*6 in right:
                report = "poly-" + homopolymer_nucleotide
                homopolymers_by_nucleotide[homopolymer_nucleotide] = homopolymers_by_nucleotide.get(homopolymer_nucleotide,0) + 1
                # left_matches = True
                # for nucleotide in left:
                #     if nucleotide != homopolymer_nucleotide:
                #         left_matches = False
                # right_matches = True
                # for nucleotide in right:
                #     if nucleotide != homopolymer_nucleotide:
                #         right_matches = False

                # if right_matches or left_matches:
                #     homopolymers_by_nucleotide[homopolymer_nucleotide] = homopolymers_by_nucleotide.get(homopolymer_nucleotide,0) + 1
                #     report = "poly-" + homopolymer_nucleotide
        else:
            dinucleotides = ["TA","TC","TG","AC","AG","CG"]
            for dinuc in dinucleotides:
                if insertion in dinuc*20 and (dinuc*3 in left or dinuc*3 in right):
                    homopolymers_by_nucleotide[dinuc] = homopolymers_by_nucleotide.get(dinuc,0) + 1
                    # print line
                    report = "poly-" + homopolymer_nucleotide
        fout.write(line.strip() + "\t" + report + "\n")
        linecounter += 1

    f.close()
    fout.close()
    print "Total insertions:", linecounter
    for nucleotide in homopolymers_by_nucleotide:
        print "poly-"+nucleotide+":",homopolymers_by_nucleotide[nucleotide]
    

def main():
    parser=argparse.ArgumentParser(description="Counts and labels homopolymers")
    parser.add_argument("-file",help="delta file" ,dest="file", type=str, required=True)
    parser.add_argument("-out",help="output file" ,dest="out", type=str, required=True)
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__=="__main__":
    main()


