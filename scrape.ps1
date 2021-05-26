conda activate
cd .\scraper\data
Get-ChildItem * -Include *.csv -Recurse | Remove-Item
cd ..\scraper
scrapy runspider .\spiders\zandparts.py -o ..\data\zandparts.csv
cd ..\..\adapter
python adapter.py