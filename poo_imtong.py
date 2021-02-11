from csv import DictReader, DictWriter
from os.path import join


def main(tongmia, kip, ma):
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
                    '/file/107/{2}/si/w/{3}-{0:02}-{1:03}.mp3'.format(
                        lui, ho, kip, ma)
                )
                tsua['例句音檔'] = (
                    'https://wiki.hakka.gov.tw'
                    '/file/107/{2}/si/s/{3}-{0:02}-{1:03}s.mp3'.format(
                        lui, ho, kip, ma)
                )
                tong.writerow(tsua)


main('siw.csv', '1', 'si')
main('si3-1.csv', '2', '1si')
