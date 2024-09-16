#!/bin/sh

# Set the path to the Stanford NER directory
nerdir="./stanford-ner-2020-11-17"

# Run Stanford NER on the input file (first argument)
java -mx700m -cp "$nerdir/stanford-ner.jar:$nerdir/lib/*" edu.stanford.nlp.ie.crf.CRFClassifier \
    -loadClassifier "$nerdir/classifiers/english.all.3class.distsim.crf.ser.gz" -textFile $1 > ner-output.txt

# Compare the NER output with the gold standard (second argument)
python3 eval.py $2 ner-output.txt
