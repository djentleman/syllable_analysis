# Syllable Analysis
comparing syllable count between japanese and english
英語と日本語の文章の音節の数を比べるプロジェクト

## Idea

As a way of measuring information density in spoken language, I wanted to compare syllable counts between English and Japanese - I felt japanese sentences generally had more syllables in them compared to their English counterparts, but I wanted to quantify it. I used a machine translation dataset available from the [university of stanford](https://nlp.stanford.edu/projects/jesc/) - made up of English and Japanese subtitles.

英語と日本語の情報密度を比較するために、音節の数を数えて比べらかった。日本語は大体英語に比べて、音節の数は多い気がしたけど、具体的な証明がなかったので、このプロジェクトを行った。英語と日本語の字幕が入ってる[スタンフォード大学](https://nlp.stanford.edu/projects/jesc/)の機械翻訳向けのデータセットを用いた。

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

### Syllable Counts

![graph1](https://github.com/djentleman/syllable_analysis/blob/master/assets/syllables.png?raw=true)

The results of the analysis can be seen in the graph above - The x-axis is the syllable count of a sentence, and the y-axis is the frequency of that syllable count. It is clear that in general Japanese setences have a far higher syllable count than that of English sentences.

以上のグラフ結果が見える。横軸は音節の数を表し、縦軸は音節数の頻度を表してる。一般的に、日本語の文章は英語より音節が多いという結果ははっきり。

### Syllable Count Ratios

After this, I compred the ratio of syllable counts of each sentence and it's english translation. The mean ratio was 2.02, meaning that Japanese sentences on average had twice the syllables of their English counterparts. The distribution of these Ratios can be seen below.

その後、全ての文章の日本語と英語の音節数の比率を比べた。比率の平均値は2.02だった。つまり、一般的に日本語の文章は、英語の翻訳より、音節数は2倍くらいと言える。以下のグラフで比率の分布が見える

![graph2](https://github.com/djentleman/syllable_analysis/blob/master/assets/ratios.png?raw=true)


### Letter Counts

The information density of spoken langage is related to the syllable count, however when it comes to written language letter count becomes more important, So i also compared the letter count of Japanese and English

音節の数は話し言葉の情報密度に関係あるけど、書き言葉の場合、文字数の方が情報密度に関係があるから、英語と日本語の文字数も比べた。

![graph3](https://github.com/djentleman/syllable_analysis/blob/master/assets/wordcounts.png?raw=true)

Unlike the Comparison of syllable counts, the letter count comparison shows that the Japanese letter count is generally much lower than that of english. In other words the information density of written Japanese is much higher than that of English.

音節数の比較と違って、英語より日本語の文字数の方が少ない。つまり、書き言葉というと日本語の情報密度は英語より非常に高い。


### Conclusion

When it comes to syllable count, Japanese has a higher syllable count, or less information per syllable than English. However when comparing letter count, Japanese is generally much less than English, this is likely due to kanji.

音節数というと、日本語は大体英語より、音節が多くて情報が薄い。しかし文字数を比べたら、漢字のお陰で日本語は一般的に英語より少ない。
