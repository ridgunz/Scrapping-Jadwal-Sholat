# SCRAP KOORDINAT FROM API MYQURAN.COM


import datetime
import requests
import pymysql
import json


# connect to MySQL
con = pymysql.connect(host='host', user='user',
                      passwd='password', db='db_name')
cursor = con.cursor()


cursor.execute("SELECT id FROM lokasi order by id")


result = [res[0] for res in cursor.fetchall()]

# Looping id city from table lokasi
for x in result:
    for y in range(12):
        url = f'https://api.myquran.com/v1/sholat/jadwal/{x}/2022/{y}'

        # print(url)

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        data = response.json()

        print(json.dumps(data['status']))

        if json.dumps(data['status']) == "true":
            print("Insert Sucessfuly")

            for i in range(31):
                id = json.loads(json.dumps(int(data['data']['id'])))
                try:
                    jadwal = json.loads(json.dumps(data['data']['jadwal'][i]))
                    tanggal = json.loads(json.dumps(
                        data['data']['jadwal'][i]['tanggal']))
                    imsak = json.loads(json.dumps(
                        data['data']['jadwal'][i]['imsak']))
                    subuh = json.loads(json.dumps(
                        data['data']['jadwal'][i]['subuh']))
                    terbit = json.loads(json.dumps(
                        data['data']['jadwal'][i]['terbit']))
                    dhuha = json.loads(json.dumps(
                        data['data']['jadwal'][i]['dhuha']))
                    dzuhur = json.loads(json.dumps(
                        data['data']['jadwal'][i]['dzuhur']))
                    ashar = json.loads(json.dumps(
                        data['data']['jadwal'][i]['ashar']))
                    maghrib = json.loads(json.dumps(
                        data['data']['jadwal'][i]['maghrib']))
                    isya = json.loads(json.dumps(
                        data['data']['jadwal'][i]['isya']))
                    date = json.loads(json.dumps(
                        data['data']['jadwal'][i]['date']))

                    print(id, tanggal, imsak, subuh, dhuha,
                          dzuhur, ashar, maghrib, isya, date)
                    # do validation and checks before insert
                    # def validate_string(val):
                    #     if val != None:
                    #         if type(val) is int:
                    #             # for x in val:
                    #             #   print(x)
                    #             return str(val).encode('utf-8')
                    #         else:
                    #             return val

                    # # parse json data to SQL insert
                    # for i, item in enumerate(data_2):
                    #     id = validate_string(item.get("id", None))
                    #     lat = validate_string(item.get("lat", None))
                    #     lon = validate_string(item.get("lon", None))
                    #     lintang = validate_string(item.get("lintang", None))
                    #     bujur = validate_string(item.get("bujur", None))

                    cursor.execute(
                        "INSERT INTO jadwal (id_kota,tanggal,imsak,subuh,terbit,dhuha,dzuhur,ashar,maghrib,isya,date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (id, tanggal, imsak, subuh, terbit, dhuha, dzuhur, ashar, maghrib, isya, date))
                    con.commit()
                except IndexError:
                    print('Index Null')
                   # con.close()
        else:
            print("Insert Failed")
