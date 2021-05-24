conda activate
cd .\scraper
Remove-Item –path .\data\zandparts.csv –recurse
cd .\scraper
scrapy runspider .\spiders\zandparts.py -o ..\data\zandparts.csv