import requests # pip install requests
import json
from datetime import datetime, date #pip install datetime
from connect import connectBD
import pymysql #pip install pymysql #pip install mysql-connector-python-rf


url="https://metabase.munitienda.com/public/question/e8e1234f-6818-430f-a6c8-86585cd4ef09.json"
response = requests.get(url)
if  response.status_code == 200:
  content = response.json()
  for row in content:
    if row['EAN']:
        routeName= row['ROUTENAME']
        FUName=row['FUNAME']
        Service_Zone=row['SERVICE_ZONE']
        fk_order= row['FK_ORDER']
        packer=row['PACKER']
        FuOrder=row['FUORDER']
        ean=row['EAN']
        operationGroup=row['OPERATIONGROUP']
        productName=row['PRODUCTNAME']
        type=row['TYPE']
        deliveryDate=row['DELIVERYDATE']
        originalQuantity=int(row['ORIGINALQUANTITY'])
        Vendor=row['VENDOR']
        CLid=row['CLID']
        Stop=row['STOP']
        currentQuantity=int(row['CURRENTQUANTITY'])
        pendingQuantity=int(originalQuantity)-int(currentQuantity)
        if originalQuantity==currentQuantity:
          status= 'Finished'
        elif currentQuantity>0 and pendingQuantity> 0:
          status= 'In Process'
        else:
          status= 'Pending'
