import re

def extract_ner(file_path, output_file):
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Find all the named entities
    entities = re.findall(r'(\b[A-Z][a-zA-Z]+\b(?:\s[A-Z][a-zA-Z]+)*)/\b(?:PERSON|ORGANIZATION|LOCATION)\b', text)

    # Remove duplicates and write to output file
    entities = list(set(entities))
    with open(output_file, 'w') as out_file:
        for entity in sorted(entities):
            out_file.write(entity + "\n")

# Process both Wikipedia and Fanwiki texts
extract_ner('stanford-wikipedia.txt', 'ner-list-wikipedia.txt')
extract_ner('stanford-fanwiki.txt', 'ner-list-fanwiki.txt')
