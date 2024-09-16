import sys
from collections import defaultdict

def read_ner_file(filename):
    entities = []
    with open(filename, 'r') as f:
        current_entity = []
        current_label = None

        for line in f:
            if line.strip():
                parts = line.strip().split()
                if len(parts) != 2:
                    print(f"Error in line: {line}")
                word, label = parts
                if label == "O":  # Not an entity
                    if current_entity:
                        entities.append((current_label, " ".join(current_entity)))
                        current_entity = []
                        current_label = None
                else:
                    entity_type = label.split("-")[-1]
                    if current_entity and entity_type != current_label:
                        entities.append((current_label, " ".join(current_entity)))
                        current_entity = []
                    current_entity.append(word)
                    current_label = entity_type
        if current_entity:
            entities.append((current_label, " ".join(current_entity)))
    return set(entities)



def evaluate(gold_standard, ner_output):
    true_positive = 0
    false_positive = 0
    false_negative = 0

    gold_entities = read_ner_file(gold_standard)
    ner_entities = read_ner_file(ner_output)

    for entity in ner_entities:
        if entity in gold_entities:
            true_positive += 1
        else:
            false_positive += 1

    for entity in gold_entities:
        if entity not in ner_entities:
            false_negative += 1

    precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
    recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0
    f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    return precision, recall, f1_score, true_positive, false_positive, false_negative


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 eval.py <gold_standard.txt> <ner_output.txt>")
        sys.exit(1)

    gold_standard = sys.argv[1]
    ner_output = sys.argv[2]

    precision, recall, f1_score, tp, fp, fn = evaluate(gold_standard, ner_output)

    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1_score:.4f}")
    print(f"True Positives (TP): {tp}")
    print(f"False Positives (FP): {fp}")
    print(f"False Negatives (FN): {fn}")


if __name__ == "__main__":
    main()
