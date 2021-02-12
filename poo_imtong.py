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
                try:
                    tsua.pop('')
                except KeyError:
                    pass
                lui, ho = tsua['編號'].split('-')
                lui = int(lui)
                ho = int(ho)
                if tsua['客語標音']:
                    tsua['客語音檔'] = (
                        'https://wiki.hakka.gov.tw'
                        '/file/107/{2}/{3}/w/{4}-{0:02}-{1:03}.mp3'.format(
                            lui, ho, kip, gi, ma)
                    )
                else:
                    tsua['客語音檔'] = ''
                kesueleku(tsua)
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


main('siw.csv', '1', 'si')
main('si3-1.csv', '2', '1si')
main('si3-2.csv', '3', '2si')

main('haw.csv', '1', 'ha')
main('ha3-1.csv', '2', '1ha')
main('ha3-2.csv', '3', '2ha')

main('daw.csv', '1', 'da')
main('da3-1.csv', '2', '1da')
main('da3-2.csv', '3', '2da')
