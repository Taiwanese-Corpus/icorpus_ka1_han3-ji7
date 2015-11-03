# -*- coding: utf-8 -*-
from os.path import dirname, abspath, join

import yaml


_專案目錄 = dirname(abspath(__file__))


def 讀語料(檔名):
    return open(join(_專案目錄, '語料', 檔名))

if __name__ == '__main__':
    資料內容 = {
        '來源': {
            '名': '何澤政', 'Name': 'Frank', '計劃主持人': '陳孟彰',
            '計劃': 'iCorpus 臺華平行新聞語料庫',
            '網址': 'http://icorpus.iis.sinica.edu.tw/'
        },
        '版權': '創用CC 姓名標示 4.0 國際',
        '種類': '語句',
        '語言腔口': '閩南語',
        '著作所在地': '臺灣',
        '著作年': '2014',
        '下層': [],
    }
    with 讀語料('原始華語.txt') as 原始華語檔案:
        with 讀語料('自動標音標.txt') as 自動標音標檔案:
            with 讀語料('自動標人工改漢字.txt') as 人工改漢字檔案:
                with 讀語料('自動標人工改音標.txt') as 人工改音標檔案:
                    for 原始華語, 自動標音標, 人工改漢字, 人工改音標 in zip(
                        原始華語檔案, 自動標音標檔案, 人工改漢字檔案, 人工改音標檔案
                    ):
                        資料內容['下層'].append({'相關資料組': [
                            {'外語資料': 原始華語.strip(), '外語語言': '華語'},
                            {'文本資料': 自動標音標.strip()},
                            {'文本資料': 人工改漢字.strip(), '屬性': {
                                '音標': 人工改音標.strip()
                            }},

                        ]})

    with open(join(_專案目錄, '臺華平行新聞語料庫.yaml'), 'w') as 檔案:
        yaml.dump(資料內容, 檔案, default_flow_style=False, allow_unicode=True)
