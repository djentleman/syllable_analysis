# Syllable Analysis
comparing syllable count between japanese and english
英語と日本語の文章の音節の数を比べるプロジェクト

## Idea

I wanted to compare syllable counts between English and Japanese - I felt japanese sentences generally had more syllables in them compared to their English counterparts, but I wanted to quantify it. I used a machine translation dataset available from the [university of stanford](https://nlp.stanford.edu/projects/jesc/) - made up of English and Japanese subtitles.

英語と日本語の音節の数を比べたかった。日本語は大体英語に比べて、音節の数は多い気がしたけど、具体的な証明がなかったので、このプロジェクトを行った。英語と日本語の字幕が入ってる[スタンフォード大学](https://nlp.stanford.edu/projects/jesc/)の機械翻訳向けのデータセットを用いた。

## Setup

### NLTK

run this on the command line:
コマンドラインで以下のコードを実行して

```
python -c 'import nltk; nltk.download("cmudict")'
```

### Dataset

run this code in the root directory of the project:
リポジトリのルートディレクトリーで以下のコードを実行して


```
mkdir -p data
wget https://nlp.stanford.edu/projects/jesc/data/raw.tar.gz
tar xvf raw.tar.gz
mv raw/raw data/raw
rm -rf raw*
```

## Result

![graph](https://github.com/djentleman/syllable_analysis/blob/master/assets/output.png?raw=true)

The results of the analysis can be seen in the graph above - The x-axis is the syllable count of a sentence, and the y-axis is the frequency of that syllable count. It is clear that in general Japanese setences have a far higher syllable count than that of English sentences.

以上のグラフ結果が見える。横軸は音節の数を表し、縦軸は音節数の頻度を表してる。一般的に、日本の文章は英語より音節が多いという結果ははっきり。
