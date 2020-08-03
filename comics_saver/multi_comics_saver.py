#! python3
# -*- coding: utf-8 -*-

import requests, os, bs4, threading


os.makedirs('comics', exist_ok=True)

def comicsdownload(start_comic, end_comic):
    for url_number in range (start_comic, end_comic):
        print('Pobieranie strony http://xkcd.com/%s...' % (url_number))
        res = requests.get('http://xkcd.com/%s' % (url_number))
        res.raise_for_status()

        soup =  bs4.BeautifulSoup(res.text, 'lxml')

        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('Nie odnaleziono pliku')
        else:
            comic_url = 'http:' + comic_elem[0].get('src')
            print('Pobieranie obrazu %s...' % (comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()

            image_file = open(os.path.join('comics', os.path.basename(comic_url)), 'wb')
            for elem in res.iter_content(100000):
                image_file.write(elem)
            image_file.close()

#  multi thread
download_threads = []
for i  in range(0, 1400, 100):  #  14 wątków
    download_thread = threading.Thread(target=comicsdownload, args=(i, i + 99))
    download_threads.append(download_thread)
    download_thread.start()

for download_thread in download_threads:
    download_thread.join()
print('Gotowe')
