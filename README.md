# syllable\_analysis
comparing syllable count between japanese and english


## setup

### NLTK

run this:

```
python -c 'import nltk; nltk.download("cmudict")'
```

### dataset

run this:

```
mkdir -p data
wget https://nlp.stanford.edu/projects/jesc/data/raw.tar.gz
tar xvf raw.tar.gz
mv raw/raw data/raw
rm -rf raw*
```

