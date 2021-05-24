#!/bin/sh

source ./venv/bin/activate
cd scraper

rm data/zandparts.csv
cd scraper

scrapy runspider ./spiders/zandparts.py -o ../data/zandparts.csv

