import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import csv

"""
Simple script to scrape vgmdb pages and store the info into a csv file.
Last used 2021-07.
"""

# where to write csv file
csv_path_input = r'g:\temp\pso2.csv'

# vgmdb urls to use, should be {'album_name': url str}
url_dict_input = {
    'Vol 1': 'https://vgmdb.net/album/40535',
    'Vol 2': 'https://vgmdb.net/album/40536',
    'Vol 3': 'https://vgmdb.net/album/47532',
    'Vol 4': 'https://vgmdb.net/album/55599',
    'Vol 5': 'https://vgmdb.net/album/66655',
    'Vol 6': 'https://vgmdb.net/album/69058',
    'Vol 7': 'https://vgmdb.net/album/88672',
    'Vol 8': 'https://vgmdb.net/album/88673',
    'Vol 9': 'https://vgmdb.net/album/108952',
    'Vol 10': 'https://vgmdb.net/album/110185'
}


def main(urls: dict, csv_path: str) -> None:
    output_list = []
    Track = namedtuple('track', ('track_number', 'track_name', 'track_length'))
    csv_fieldnames = ['album', 'disc', 'track_number', 'track_name', 'track_length']

    for url in urls:
        page_text = requests.get(urls[url]).text
        soup = BeautifulSoup(page_text, 'html.parser')

        table = soup.find(id='tracklist')
        rows = table.find_all('tr')
        # iterate through the table rows
        data = [[td.findChildren(text=True) for td in tr.findAll('td')] for tr in rows]

        disc_number = 0
        tracks = {}
        for item in data:
            # item will look like: [['18'], ['\r\n\r\nRoad to Next Frontiers'], ['2:47', '\n']]
            track_number = item[0][0]
            track_name = item[1][0].strip()
            if not track_name:
                track_name = 'unknown'
            # if the length is missing, this will just be \n
            track_length = item[2][0].strip()
            if not track_length:
                track_length = 'unknown'
            # this is the assumption that track 1 is always a new disc
            if track_number == '01':
                disc_number = disc_number + 1
                tracks[disc_number] = []
            tracks[disc_number].append(Track(track_number=track_number,
                                             track_name=track_name,
                                             track_length=track_length))

        for disc in tracks:
            for track in tracks[disc]:
                output_list.append({
                    'album': url,
                    'disc': disc,
                    'track_number': track.track_number,
                    'track_name': track.track_name,
                    'track_length': track.track_length
                })

    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=csv_fieldnames)
        writer.writeheader()
        writer.writerows(output_list)


if __name__ == '__main__':
    assert url_dict_input, 'missing url_dict'
    assert csv_path_input, 'missing csv_path_input'
    main(url_dict_input, csv_path_input)
