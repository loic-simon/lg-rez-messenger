import gspread
from oauth2client.service_account import ServiceAccountCredentials

from config import DEFAULT_DOC_ID

def connect(key=DEFAULT_DOC_ID):
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('gsheets_infos.json', scope)
    client = gspread.authorize(creds)

    # Open the workbook
    workbook = client.open_by_key(key)

    return workbook
