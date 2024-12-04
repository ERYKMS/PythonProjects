USERNAME="**********"
TOKEN="**********"
GRAPHID="**********"
import requests
pixela_params={"token":TOKEN,
               "username":USERNAME,
               "agreeTermsOfService":"yes",
               "notMinor":"yes"

}
pixela_endpoint="https://pixe.la/v1/users"

#response=requests.post(url=pixela_endpoint,json=pixela_params)
#print(response.text)


graph_config={
    "id":GRAPHID,
    "name":"eray",
    "unit":"calory",
    "type":"float",
    "color":"sora"
}

headers={
    "X-USER-TOKEN":TOKEN
}

from datetime import datetime
today=datetime.now().date().strftime('%Y%m%d')

requests_body={
    "date":today,
    "quantity":"5",
}

quantity={
    "quantity":"8"
}

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today}"

#response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
#print(response.text)

#response=requests.post(url=graph_endpoint,headers=headers,json=requests_body)
#print(response.text)
response=requests.put(url=graph_endpoint,headers=headers,json=quantity)

print(response.text)
