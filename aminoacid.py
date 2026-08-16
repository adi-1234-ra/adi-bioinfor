from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio import SeqIO

for record in SeqIO.parse("fat.fasta", "fasta"):
  analyzed_seq = ProteinAnalysis(str(record.seq))

  # Get dictionary of amino acid counts
  aa_counts = analyzed_seq.count_amino_acids()
  print("Amino Acid Counts (Top 3):")
  # Sort by most frequent
  sorted_aa = sorted(aa_counts.items(), key=lambda x: x[1], reverse=True)
  for aa, count in sorted_aa[:3]:
    print(f"  {aa}: {count}")