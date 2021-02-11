# Elearning-Hakka
客語能力認證詞彙及音檔

## xlsx to csv
```
find . -type f -name '*xlsx' -exec soffice --headless --convert-to csv:'Text - txt - csv (StarCalc):44,34,76' --outdir csv/ {} \;
```

## csv補音檔
```
python3 poo_imtong.py
```

