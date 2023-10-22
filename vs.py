import argparse
import requests
import pandas as pd
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('--username', help='VirusShare username')
parser.add_argument('--password', help='VirusShare password')
parser.add_argument('--family', help='MOTIF family')
parser.add_argument('--output_folder', help='Output folder')

args = parser.parse_args()

headers = {'Accept': '*/*', 'X-User-IP': '1.1.1.1'}

def check_file_hash_exist_in_vs(soup: BeautifulSoup):
    for c in soup.find_all("center"):
        if "No results." in c.text:
            return False
    return True

def login_vs(username, password):
    url = 'https://virusshare.com/processlogin'
    data = {'username': username, 'password': password}
    session = requests.Session()
    r = session.post(url, data=data, headers=headers)
    
    return session

if __name__ == '__main__':
    available_files = pd.read_csv('motif_reports.csv', encoding='ISO-8859-1')
    session = login_vs(args.username, args.password)
    df = available_files[available_files["Reported family"] == args.family]

    for file in df["File hash"]:
        r = session.post("https://virusshare.com/search", data={'search': file}, headers=headers)
        file_exist = check_file_hash_exist_in_vs(BeautifulSoup(r.text, 'html.parser'))
        if file_exist:
            d = session.get(f"https://virusshare.com/download?{file}", headers=headers)
            with open(f"{args.output_folder}/{args.family}_{file}.zip", 'wb') as f:
                f.write(d.content)