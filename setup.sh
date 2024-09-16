sudo apt install openjdk-11-jdk
wget https://nlp.stanford.edu/software/stanford-ner-4.2.0.zip
sudo apt install unzip
unzip stanford-ner-4.2.0.zip
cd stanford-ner-2020-11-17
./ner.sh sample.txt
