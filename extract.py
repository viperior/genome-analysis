def copy_file_data(source_file_path, target_file_path, start_line_number=0, end_line_number=False):
    erase_file_contents(target_file_path)
    
    with open(source_file_path, 'r') as source_file:
        i = 0
        
        for line in source_file:
            if(i > start_line_number and ((end_line_number == False) or i <= end_line_number)):
                with open(target_file_path, 'a') as target_file:
                    target_file.write(line)
            i += 1

def erase_file_contents(file_path):
    open(file_path, 'w').close()

def extract_data():
    input_file_path = './input/ManuSporny-genome.txt'
    input_file_header_line_count = 14
    input_file_data_start_line_number = input_file_header_line_count + 1
    output_sample_data_file_path = './output/genome-sample.txt'
    output_data_file_path = './output/genome.txt'
    copy_file_data(input_file_path, output_sample_data_file_path, start_line_number=input_file_data_start_line_number, end_line_number=300)
    copy_file_data(input_file_path, output_data_file_path, start_line_number=input_file_data_start_line_number, end_line_number=3000)

extract_data()
