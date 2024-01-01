import click
import requests
import os
import pandas as pd

pkg_dir = os.path.dirname(__file__)

def download_motif():
    if not os.path.exists(f"{pkg_dir}/motif_reports.csv"):
        print("Downloading motif_reports.csv")
        r = requests.get("https://raw.githubusercontent.com/boozallen/MOTIF/master/dataset/motif_reports.csv")
        with open(f"{pkg_dir}/motif_reports.csv", 'wb') as f:
            f.write(r.content)
        

@click.group()
def cli():
    pass

@cli.command(name="download", help="Download samples from VirusShare")
@click.option('--username', help='VirusShare username')
@click.option('--password', help='VirusShare password')
@click.option('--family', help='MOTIF family')
@click.option('--output_folder', help='Output folder')
def download(username, password, family, output_folder):
    # -- download motif_reports.csv if not exist --
    download_motif()

    # -- read motif_reports.csv --
    df = pd.read_csv(f"{pkg_dir}/motif_reports.csv", encoding='ISO-8859-1')
    
    # -- filter by family --
    df = df[df["Reported family"] == family]

    

if __name__ == '__main__':
    cli()