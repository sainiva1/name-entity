def reformat_ner_output(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            tokens = line.strip().split()  # Split line by spaces
            for token in tokens:
                if '/' in token:
                    word, label = token.rsplit('/', 1)  # Split word and label
                    outfile.write(f"{word} {label}\n")
                else:
                    # Handle cases where there is no proper split
                    outfile.write(f"{token}\n")

# Reformat the ner-output.txt file
reformat_ner_output('ner-output.txt', 'ner-output-reformatted.txt')
reformat_ner_output('stanford-wikipedia.txt', 'stanford-wikipedia-reformatted.txt')
