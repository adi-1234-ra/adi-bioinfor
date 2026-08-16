from Bio import SeqIO

# Replace 'your_file.fasta' with your actual file name
fasta_file = "fat.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):
  print(f"ID: {record.id}")
  print(f"Length: {len(record.seq)}")
  print(f"Sequence: {record.seq[:30]}...\n")  # Prints first 30 bases/amino acids