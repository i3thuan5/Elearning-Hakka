from csv import DictReader, DictWriter
from os.path import join


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
                lui, ho = tsua['編號'].split('-')
                lui = int(lui)
                ho = int(ho)
                tsua['客語音檔'] = (
                    'https://wiki.hakka.gov.tw'
                    '/file/107/{2}/{3}/w/{4}-{0:02}-{1:03}.mp3'.format(
                        lui, ho, kip, gi, ma)
                )
                tsua['例句音檔'] = (
                    'https://wiki.hakka.gov.tw'
                    '/file/107/{2}/{3}/s/{4}-{0:02}-{1:03}s.mp3'.format(
                        lui, ho, kip, gi, ma)
                )
                tong.writerow(tsua)


def tiongkuan(tongmia, kip, ma):
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
                lui, ho = tsua['編號'].split('-')
                lui = int(lui)
                ho = int(ho)
                tsua['客語音檔'] = (
                    'https://wiki.hakka.gov.tw'
                    '/file/107/{2}/{3}/w/{4}-{0:02}-{1:03}.mp3'.format(
                        lui, ho, kip, gi, ma)
                )
                liantsohue = tsua.pop('華語詞義/例句')
                try:
                    華語詞義, 例句 = liantsohue.split('例如：')
                    tsua['華語詞義'] = 華語詞義.strip()
                    tsua['例句'] = 例句.strip()
                    tsua['例句音檔'] = (
                        'https://wiki.hakka.gov.tw'
                        '/file/107/{2}/{3}/s/{4}-{0:02}-{1:03}s.mp3'.format(
                            lui, ho, kip, gi, ma)
                    )
                except ValueError:
                    tsua['華語詞義'] = liantsohue.strip()
                    tsua['例句'] = ''
                    tsua['例句音檔'] = ''
                tong.writerow(tsua)


main('siw.csv', '1', 'si')
main('si3-1.csv', '2', '1si')
tiongkuan('si3-2.csv', '3', '2si')

main('haw.csv', '1', 'ha')
