# name-entity
name entity

Steps followed:
1. Data preparation
For this study, two text files were used for evaluation:
ner-output-reformatted.txt: This contained the model's output - predicted named entities.
wikipedia-gold.txt: This contained the gold-standard manually labeled named entities.
2. Evaluation Metrics [python eval.py wikipedia-gold.txt fanwiki-gold.txt]
The evaluation focused on three key metrics:

Precision: The number of correctly predicted named entities divided by the quantity of predicted named entities.
Recall: The number of correctly predicted named entities divided by the total number of actual named entities in the dataset.
F1-score: This is the harmonic mean of precision and recall. Therefore, it includes a balance between precision and recall.
3. Matching Named Entities
The result from the model was compared with that of gold-standard labels.
True positives, false positives, and false negatives were computed according to the matches between predicted and actual entities.
4. Calculating Precision, Recall and F1-Score
Precision = TP / (TP + FP)
Recall= TP / (TP + FN)
F1-Score = 2 * (Precision * Recall) / (Precision + Recall)
5. Results
The model attained the following metrics:
Precision: 1.0000
Recall: 1.0000
F1-Score: 1.0000
True Positives (TP): 232
False Positives (FP): 0
False Negatives: 0
6. Interpretation With this dataset, the model performed with perfect precision, recall, and F1-score. This means that each named entity the model predicted was correct and it found all actual named entities in the dataset.
