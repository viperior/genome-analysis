input_file_path = './input/ManuSporny-genome.txt'
output_file_path = './output/genome.txt'

with open(input_file_path, 'r') as input_file:
    i = 0
    open(output_file_path, 'w').close()
    
    for line in input_file:
        i += 1
        
        if(i <= 100):
            print(line.strip())
            with open(output_file_path, 'a') as output_file:
                output_file.write(line)
