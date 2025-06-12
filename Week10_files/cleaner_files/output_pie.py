import os
from Bio import SeqIO
import matplotlib.pyplot as plt

#inout variables
species_of_interest = "A_Schu"
input_dir = "/home/quinnz/novus/BB485/Aeromonas-Project/Week10_files/cleaner_files/OrthoFinder/Results_Jun07/Single_Copy_Orthologue_Sequences"


#using counters 
with_species = 0 
without_species = 0 

#processing files
for filename in os.listdir(input_dir):
    if filename.endswith(".fa") or filename.endswith(".fasta"):
        path = os.path.join(input_dir, filename)
        found = False

        for record in SeqIO.parse(path, "fasta"):
            if species_of_interest in record.id:
                found = True
                break

        if found:
            with_species += 1
        else:
            without_species += 1

# === PIE CHART ===
labels = ['Contains ' + species_of_interest, 'Does Not Contain']
sizes = [with_species, without_species]
colors = ['#66c2a5', '#fc8d62']
explode = (0.1, 0)

plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title(f'Presence of {species_of_interest} in Single-Copy Orthogroups')
plt.axis('equal')
plt.tight_layout()
plt.savefig(f"{species_of_interest}_orthogroup_piechart.png")
plt.show()
