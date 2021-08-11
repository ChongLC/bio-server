import sys
from Bio import SeqIO
import string
import random

fastafile = sys.argv[1]
#fastafile = "structural_conserved_peptides.fasta"
outputfile = "randomSeq.fasta"
seq_list = ""
percent_dict = []
counter = 0

for sequence in SeqIO.parse(fastafile, "fasta"):
  seq_list += str(sequence.seq)
  
aa_list = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'J', 'O', 'U', 'Z', 'X']
def CalculateFrequency(seq_list):
    Length = len(seq_list)
    ProteinDict = {}
    for aa in aa_list:
         ProteinDict[aa] = seq_list.count(aa)
    return(ProteinDict)
  
def CalculatePercent(seq_list,ProteinDict):
  PercentDict = {}
  Length = len(seq_list)
  for aa in ProteinDict:
     PercentDict[aa] = round((ProteinDict[aa] / float(len(seq_list)))*100,2)
  return(PercentDict)

def PrintOutput(Dict):
  for aa in Dict:
    print(aa,":",round(Dict[aa],2))

def PrintOutput2(Dict):
  for aa in Dict:
    percent_dict.append(round(Dict[aa],2))

def Main():
  ProteinDict = CalculateFrequency(seq_list)
  PercentDict = CalculatePercent(seq_list,ProteinDict)
  PrintOutput(PercentDict)
  PrintOutput2(PercentDict)
if __name__=='__main__':
  Main()

with open(outputfile, 'w') as f:
  for sequence in SeqIO.parse(fastafile, "fasta"):
    seq = sequence.seq
    counter += 1
    randomSeqList = ''.join(random.choices(aa_list, weights = percent_dict, k=len(seq)))
    f.write(f">Sequence {counter} | {len(seq)}aa" + '\n' + randomSeqList + '\n')