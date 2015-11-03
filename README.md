# iCorpus 臺華平行新聞語料庫漢字臺羅版
原本的[iCorpus 臺華平行新聞語料庫](https://github.com/sih4sing5hong5/icorpus)臺語只含教羅音標，本專案補充2008/11/06到2014/3/14文章漢字和臺羅音標。

## 授權
iCorpus 臺華平行新聞語料庫漢字臺羅版由薛丞宏製作，以[創用CC 姓名標示 4.0 國際 授權條款](http://creativecommons.org/licenses/by/4.0/)釋出。

## 語料介紹
本專案補充2008/11/06到2014/3/14文章，於取出文章後，在2014內正規化。

### 原始語料
* `原始華語` - 網路上華語新聞語句
* `斷詞華語` - `原始華語`經中研院[CKIP](http://ckipsvr.iis.sinica.edu.tw/)斷詞結果
* `原始教羅音標` - 由何澤政翻譯的臺語語句

### 正規化語料
* `自動標漢字` - 由程式自動化依辭典自`原始華語`和`原始教羅音標`挑出臺華共同詞
* `自動標音標` - 由程式自動化將`原始教羅音標`轉成臺羅
* `自動標人工改漢字` - 由人工正規化`自動標漢字`
* `自動標人工改音標` - 由人工正規化`自動標音標`

## 臺灣言語資料庫
### 產生yaml格式資料
```bash
sudo apt-get install -y python-virtualenv python3 python3-dev libyaml-dev
virtualenv --python=python3 venv
. venv/bin/activate
pip install pyyaml
python 產生臺灣言語資料庫格式.py
```

### 匯入資料
在`臺灣言語資料庫`專案目錄下
```bash
python manage.py 匯入資料 https://Taiwanese-Corpus.github.io/icorpus_ka1_han3-ji7/臺華平行新聞語料庫.yaml
```

