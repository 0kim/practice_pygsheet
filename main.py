# coding=utf-8

import gspread
from oauth2client.service_account import ServiceAccountCredentials

APPLICATION_NAME = 'Google Spreadsheet API sample'
SCOPES = ['https://spreadsheets.google.com/feeds']

spreadsheetsId = '## copy a spreadsheet ID and paste here ##'
keyfile = 'cred.json'

new_row = ['hello', 123, 'new test', u'utf8//한글']

credentials = ServiceAccountCredentials.from_json_keyfile_name(keyfile, scopes=SCOPES)

gc = gspread.authorize(credentials)
spreadsheet = gc.open_by_key(spreadsheetsId)
worksheets = spreadsheet.worksheets()

worksheets[0].append_row(new_row)

print('Done')
