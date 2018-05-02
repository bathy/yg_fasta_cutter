import re
import time

def parse_fasta(file_name):
    protein_name=[]
    protein_dict={}
    with open(file_name,'r') as fasta_file:
        for line in fasta_file:
            if line.startswith('>'):
                if len(protein_name)>1:
                    protein_dict[protein_name[1]]=[protein_name[0],protein_name[2],sequence]
                protein_name=line[1:].rstrip().split('|')
                sequence=''
            elif len(protein_name)>1 and line[0].isalpha():
                sequence+=line.rstrip()
        protein_dict[protein_name[1]] = [protein_name[0], protein_name[2], sequence]
    return protein_dict

def cut_peptide_sequence(sequence,cut_list,nocut_list):
    cut_sequence=filter(None,re.split('([A-JL-QS-Z]+[K|R])',sequence))
    return cut_sequence

if __name__=="__main__":
    start_time=time.clock()
    file_name='uniprot_human_2018_04_27.fasta'
    parsed_fasta=parse_fasta(file_name)
    print parsed_fasta['C9JX34']
    peptide_set=set()
    for each in parsed_fasta:
        for each_peptide in cut_peptide_sequence(parsed_fasta[each][2],[],[]):
            if 5<len(each_peptide)<50:
                peptide_set.add(each_peptide)
    print len(list(peptide_set))
    print time.clock()-start_time
    #test