import os
from zipfile import ZipFile
from kaggle.api.kaggle_api_extended import KaggleApi


# Declare Kaggle Competition Name
comp = 'tabular-playground-series-jan-2021'


# Folders for Repos
if not os.path.isdir('./data'):
    os.mkdir('./data')
if not os.path.isdir('./figures'):
    os.mkdir('./figures')


# Connect to Kaggle
api = KaggleApi()
api.authenticate()
api.competition_download_files(comp, path = './data')


# Extract competition files
zf = ZipFile('./data/'+comp+'.zip', 'r')
zf.extractall('./data/')


# Remove ZIP file
os.remove('./data/'+comp+'.zip')
