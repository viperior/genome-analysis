import pandas as pd

genome_data_file_path = './input/ManuSporny-genome.txt'
df = pd.read_csv(filepath_or_buffer = genome_data_file_path, delimiter = '\t', header=14)
genotypes = {}

for index, row in df.iterrows():
    current_genotype = row['genotype']
    
    if current_genotype in genotypes.keys():
        genotypes[current_genotype] += 1
    else:
        genotypes[current_genotype] = 1
    
print(genotypes)
