from csv import DictReader
from os.path import join
from posix import listdir


def main(tongmia):
    with open(tongmia) as thak:
        for tsua in DictReader(thak):
            yield tsua['客語音檔']
            if tsua['例句音檔']:
                yield tsua['例句音檔']


def tshiau():
    for tong in sorted(listdir('csv_imtong')):
        yield from main(join('csv_imtong', tong))


with open('imtongpio.txt', 'wt') as sia:
    for pit in tshiau():
        print(pit, file=sia)
