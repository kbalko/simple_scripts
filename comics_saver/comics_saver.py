#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, os, bs4

xkcd = 'https://xkcd.com/'

url = xkcd
os.makedirs('comics', exist_ok=True)

while not url.endswith('1'):
    print('Pobieranie strony %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Nie udało się odnaleźć pliku')
    else:
        comic_url = 'http:' + comic_elem[0].get('src')
        print('Pobieranie obrazu %s...' % (comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

    image_file = open(os.path.join('comics', os.path.basename(comic_url)), 'wb')
    for elem in res.iter_content(100000):
        image_file.write(elem)
    image_file.close()
    prev_link = soup.select('a[rel="prev"]')[0]
    url = xkcd + prev_link.get('href')

print('Gotowe')
