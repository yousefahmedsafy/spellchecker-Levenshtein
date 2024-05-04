with open('alladwiaDatabase1.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
    # Iterate through each line in the input file
    for line in input_file:
        # Join white spaces with underscores and write the modified line to the output file
        modified_line = '_'.join(line.split())
        output_file.write(modified_line + '\n')