import requests
import csv
from os import path

def store(name,email):

  headers=['Names', 'E-mails']
  row=[name,email]    
  filename='data.csv'

  if path.exists(filename):
      with open('data.csv','a') as file:
          csv_write=csv.writer(file)
          csv_write.writerow(row)
  else:
      with open('data.csv','w') as file:
          csv_write=csv.writer(file)
          csv_write.writerow(headers)
          csv_write.writerow(row)

  with open('data.csv','rb') as file:
      upload = file.read()

  url='https://import.bit.io/willmiller155/demo_repo/chatbot_table'

  headers = {
      "Content-Disposition": "attachment;filename='data.csv'",
      "Authorization": "Bearer 3pJBE_U4RfVxDiRuPtF2apYPFN4Gm"
     }

  response = requests.request("POST", url, headers=headers, data=upload)

  return "Data has been stored"