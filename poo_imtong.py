from csv import DictReader, DictWriter


def main():
    with open('csv/siw.csv') as thak:
        with open('csv_imtong/siw.csv', 'wt') as sia:
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
                    '/file/107/1/si/w/si-{:02}-{:03}.mp3'.format(lui, ho)
                )
                tsua['例句音檔'] = (
                    'https://wiki.hakka.gov.tw'
                    '/file/107/1/si/s/si-{:02}-{:03}s.mp3'.format(lui, ho)
                )
                tong.writerow(tsua)


main()
