from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio import SeqIO

for record in SeqIO.parse("fat.fasta", "fasta"):
  # Convert sequence to string for analysis
  analyzed_seq = ProteinAnalysis(str(record.seq))

  print(f"ID: {record.id}")
  print(f"Molecular Weight: {analyzed_seq.molecular_weight():.2f} Da")
  print(f"Aromaticity: {analyzed_seq.aromaticity():.4f}")
  print(f"Estimated Isoelectric Point (pI): {analyzed_seq.isoelectric_point():.2f}\n")