# SCRAP KOORDINAT FROM API MYQURAN.COM


import requests
import pymysql
import json


# connect to MySQL
con = pymysql.connect(host='host', user='user',
                      passwd='password', db='db_name')
cursor = con.cursor()


cursor.execute("SELECT id FROM lokasi where id > 1002 order by id")


result = [res[0] for res in cursor.fetchall()]

for x in result:
    url = f'https://api.myquran.com/v1/sholat/jadwal/{x}/2022/01'

    # print(url)

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()

    print(json.dumps(data['status']))

    if json.dumps(data['status']) == "true":
        print("Insert Sucessfuly")
        id = json.dumps(int(data['data']['id']))
        lat = json.dumps(data['data']['koordinat']['lat'])
        lon = json.dumps(data['data']['koordinat']['lon'])
        lintang = json.dumps(data['data']['koordinat']['lintang'])
        bujur = json.dumps(data['data']['koordinat']['bujur'])

        print(id, lat, lon, lintang, bujur)

        # do validation and checks before insert
        def validate_string(val):
            if val != None:
                if type(val) is int:
                    # for x in val:
                    #   print(x)
                    return str(val).encode('utf-8')
                else:
                    return val

        # # parse json data to SQL insert
        # for i, item in enumerate(data_2):
        #     id = validate_string(item.get("id", None))
        #     lat = validate_string(item.get("lat", None))
        #     lon = validate_string(item.get("lon", None))
        #     lintang = validate_string(item.get("lintang", None))
        #     bujur = validate_string(item.get("bujur", None))

        cursor.execute(
            "INSERT INTO kordinat (id,lat,lon,lintang,bujur) VALUES (%s,%s,%s,%s,%s)", (id, lat, lon, lintang, bujur))
        con.commit()
        # con.close()
    else:
        print("Insert Failed")
