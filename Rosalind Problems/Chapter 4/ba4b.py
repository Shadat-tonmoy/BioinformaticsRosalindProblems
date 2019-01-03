map = {'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'}

def reverseComplement(dna):
    rev = dna[::-1]
    rev_com = ''
    n_com = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    for n in rev:
        rev_com += n_com[n]
    return rev_com


def generateTextEncodingPeptide(dnaString, peptide):
    textEncodingPeptideList = []

    rnaString1 = dnaString.replace('T', 'U')
    rnaString2 = reverseComplement(dnaString).replace('T', 'U')
    l = len(peptide) * 3

    index = 0

    while index < len(dnaString) - l:
        i = index
        s = ''
        for p in peptide:
            rna = rnaString1[i:i + 3]
            if map[rna] == p:
                s += rna.replace('U', 'T')
                i = i + 3
            else:
                s = ''
                break;
        if (s != ''):
            textEncodingPeptideList.append(s)

        i = index
        s = ''
        for p in peptide:
            rna = rnaString2[i:i + 3]
            if map[rna] == p:
                dna = rna.replace('U', 'T')
                s += dna
                i = i + 3
            else:
                s = ''
                break;
        if (s != ''):
            s = reverseComplement(s)
            textEncodingPeptideList.append(s)
        index += 1

    return textEncodingPeptideList


text = input()
peptide = input()

textList = generateTextEncodingPeptide(text, peptide)
for i in textList:
    print(i)