import requests
try:
    text=open("C:/Users/oshra/Desktop/dests.txt", encoding='utf8')
    matrix=dict()


    for line in text:
        destination=line
        tlv='תל אביב'
        key="AIzaSyDOdvZBJSuaEu8WylgeOD6uhHlbJVtVa_Y"
        #matrix API
        url_mat='https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=%s&destinations=%s&key=%s' %(tlv,destination,key)
        result1=requests.get(url_mat).json()
        distance=result1['rows'][0]['elements'][0]['distance']['text']
        duration=result1['rows'][0]['elements'][0]['duration']['text']
        #gecode API
        url_geo='https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' %(destination,key)
        result2=requests.get(url_geo).json()
        location=result2['results'][0]['geometry']['location']
        lat=location['lat']
        lng=location['lng']
    
        informaion_city=(distance,duration,lat,lng)
        matrix[destination]=informaion_city

    import json
    print_matrix=json.dumps(matrix,ensure_ascii=False, indent=6).encode('utf8')
    print(print_matrix.decode())

    far_from_tlv=sorted(matrix, key=matrix.get, reverse=True)[0:3]
    print('The cantries are:',far_from_tlv)
    
except:
    print("חלה שגיאה")