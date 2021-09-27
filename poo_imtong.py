from csv import DictReader, DictWriter
from os.path import join
import unicodedata


def main(tongmia, kip, ma):
    gi = ma[-2:]
    with open(join('csv', tongmia)) as thak:
        with open(join('csv_imtong', tongmia), 'wt') as sia:
            tong = DictWriter(sia, fieldnames=[
                '編號',
                '客家語', '客語標音', '客語音檔',
                '華語詞義',
                '例句', '例句音檔', '翻譯',
                '備註',
                '詞性1', '詞性2',
                '分類'
            ])
            tong.writeheader()
            for tsua in DictReader(thak):
                tshiau_nuaui_mia(tsua)
                lui, ho = tsua['編號'].split('-')
                lui = int(lui)
                ho = int(ho)
                if not tsua['客語標音']:
                    continue
                tsua['客語音檔'] = (
                    'https://wiki.hakka.gov.tw'
                    '/file/107/{2}/{3}/w/{4}-{0:02}-{1:03}.mp3'.format(
                        lui, ho, kip, gi, ma)
                )
                kesueleku(tsua)
                tsua['例句'] = piann_tsoji(tsua['例句'])
                tsua['客家語'] = piann_tsoji(tsua['客家語'])
                tsua['華語詞義'] = piann_tsoji(tsua['華語詞義'])  # 例句拆無清氣ê問題，先按呢處理
                if tsua['例句']:
                    tsua['例句音檔'] = (
                        'https://wiki.hakka.gov.tw'
                        '/file/107/{2}/{3}/s/{4}-{0:02}-{1:03}s.mp3'.format(
                            lui, ho, kip, gi, ma)
                    )
                else:
                    tsua['例句音檔'] = ''
                try:
                    tong.writerow(tsua)
                except ValueError:
                    print('tsua', tsua)
                    raise


def kesueleku(tsua):
    try:
        liantsohue = tsua.pop('華語詞義/例句')
    except KeyError:
        return
    try:
        華語詞義, 例句 = liantsohue.split('例如：')
        tsua['華語詞義'] = 華語詞義.strip()
        tsua['例句'] = 例句.strip()
    except ValueError:
        tsua['華語詞義'] = liantsohue.strip()
        tsua['例句'] = ''


def tshiau_nuaui_mia(tsua):
    try:
        tsua.pop('')
    except KeyError:
        pass
    try:
        tsua['編號'] = tsua.pop('編碼')
    except KeyError:
        pass
    try:
        tsua['客語標音'] = tsua.pop('客語音標')
    except KeyError:
        pass


TSOJI = {
    # 認證詞彙例句內底ê造字
    '\ue004': '𧩣',  # U+27A63
    '\ue40f': '㘝',  # U+361D
    '\ue452': '䗁',  # U+45C1
    '\ue459': '䟘',  # U+47D8
    '\ue560': '𤊶',  # U+242B6
    '\ue5a4': '𪐞',  # U+2A41E
    '\ue08d': '𢯭',  # U+22BED
    '\ue548': '𢳆',  # U+22CC6

    '\ue0c7': '𫠛',  # U+2B81B
    '\ue700': '𫣆',  # U+2B8C6
    '\ue711': '𫝘',  # U+2B758
    '\ue725': '𬠖',  # U+2C816
    '\ue72c': '𫟧',  # U+2B7E7
    '\ue76f': '⿺皮卜',  # 無Unicode
    # 下底是近反義詞才有出現--ê，對應豆腐烏外字表ê「客語教典PUA」欄
    '\uf354': '䞚',  # U+479A
    '\uf369': '𧊅',  # U+27285
    '\uf36e': '𧩣',  # U+27A63
    '\uf36f': '𩜰',  # U+29730
    '\uf374': '𢯭',  # U+22BED
    '\uf3b9': '𥉌',  # U+2524C
    '\uf545': '⿺皮卜',  # 無Unicode
}


def piann_tsoji(hanji):
    for k, v in TSOJI.items():
        hanji = hanji.replace(k, v)
    for ji in hanji:
        pianbe = hex(ord(ji))
        if unicodedata.category(ji) == 'Co':
            print(f'欄位「{hanji}」有造字字元，編碼{pianbe}')
    return hanji


for gi in ['si', 'ha', 'da', 'rh', 'zh', ]:
    main('{}w.csv'.format(gi), '1', '{}'.format(gi))
    main('{}3-1.csv'.format(gi), '2', '1{}'.format(gi))
    main('{}3-2.csv'.format(gi), '3', '2{}'.format(gi))
