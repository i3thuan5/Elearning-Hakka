# Elearning-Hakka
客語能力認證詞彙及音檔

## xlsx
- [初級](https://elearning.hakka.gov.tw/ver2015/kaga/Kaga_QD.aspx?type=primary)
- [中級](https://elearning.hakka.gov.tw/ver2015/kaga/Kaga_QD.aspx?type=middle)
- [客語能力認證詞彙](https://wiki.hakka.gov.tw/ver2018/list.aspx)

## xlsx to csv
```
find . -type f -name '*xlsx' -exec soffice --headless --convert-to csv:'Text - txt - csv (StarCalc):44,34,76' --outdir csv/ {} \;
```

## csv補音檔
```
python3 poo_imtong.py
```

## 掠mp3音檔
```
python3 tshiau_imtong.py
wget --input-file imtongpio.txt --directory-prefix mp3/ \
  --wait 10 --random-wait
```
