import requests
import time
import random

url_1 = "https://bloodlore-chronicles.com/api/Game/hunt"
payload_1={}
headers_1 = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9',
  'ApiKey': '3DB373CF32AC02834ED4A388F512980EF3D8ED3FEF92640F6DC3B2C20DEB2935',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2Njg3MTY1ZmMzNDliYjkyODBjM2NmNjQiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJ1c2VyIiwibmJmIjoxNzIwNTA5NDM2LCJleHAiOjE3MjA1OTU4MzYsImlzcyI6IlNwb29reSBIdW50ZXJzIiwiYXVkIjoiU3Bvb2t5IEh1bnRlcnMifQ.d90eGd2vKYoBZGNFph3kTYMx-Ha4T3JtzSzi4XqkGMs',
  'Connection': 'keep-alive',
  'Cookie': '_ga=GA1.1.199610205.1720025946; gtc_cookie=true; _ga_WT859GPG6Q=GS1.1.1720025946.1.1.1720025958.0.0.0; isPlaying=false; volume=0.2',
  'Referer': 'https://bloodlore-chronicles.com/hunt',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

url_2 = "https://bloodlore-chronicles.com/api/Game/quickhunt"

payload_2={}
headers_2 = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9',
  'ApiKey': '3DB373CF32AC02834ED4A388F512980EF3D8ED3FEF92640F6DC3B2C20DEB2935',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2Njg3MTY1ZmMzNDliYjkyODBjM2NmNjQiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJ1c2VyIiwibmJmIjoxNzIwNTA5NDM2LCJleHAiOjE3MjA1OTU4MzYsImlzcyI6IlNwb29reSBIdW50ZXJzIiwiYXVkIjoiU3Bvb2t5IEh1bnRlcnMifQ.d90eGd2vKYoBZGNFph3kTYMx-Ha4T3JtzSzi4XqkGMs',
  'Connection': 'keep-alive',
  'Cookie': '_ga=GA1.1.199610205.1720025946; gtc_cookie=true; _ga_WT859GPG6Q=GS1.1.1720025946.1.1.1720025958.0.0.0; isPlaying=false; volume=0.2',
  'Referer': 'https://bloodlore-chronicles.com/hunt',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

url_3 = "https://bloodlore-chronicles.com/api/clientshop/GetWeaponMaster"

payload_3={}
headers_3 = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9',
  'ApiKey': '3DB373CF32AC02834ED4A388F512980EF3D8ED3FEF92640F6DC3B2C20DEB2935',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2Njg3MTY1ZmMzNDliYjkyODBjM2NmNjQiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJ1c2VyIiwibmJmIjoxNzIwNTA5NDM2LCJleHAiOjE3MjA1OTU4MzYsImlzcyI6IlNwb29reSBIdW50ZXJzIiwiYXVkIjoiU3Bvb2t5IEh1bnRlcnMifQ.d90eGd2vKYoBZGNFph3kTYMx-Ha4T3JtzSzi4XqkGMs',
  'Connection': 'keep-alive',
  'Cookie': '_ga=GA1.1.199610205.1720025946; gtc_cookie=true; isPlaying=false; volume=0.2; _ga_WT859GPG6Q=GS1.1.1720025946.1.1.1720027011.0.0.0',
  'Referer': 'https://bloodlore-chronicles.com/weaponmaster',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

headers_4 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "ApiKey": "3DB373CF32AC02834ED4A388F512980EF3D8ED3FEF92640F6DC3B2C20DEB2935",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2Njg3MTY1ZmMzNDliYjkyODBjM2NmNjQiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJ1c2VyIiwibmJmIjoxNzIwNTA5NDM2LCJleHAiOjE3MjA1OTU4MzYsImlzcyI6IlNwb29reSBIdW50ZXJzIiwiYXVkIjoiU3Bvb2t5IEh1bnRlcnMifQ.d90eGd2vKYoBZGNFph3kTYMx-Ha4T3JtzSzi4XqkGMs",
    "Origin": "https://bloodlore-chronicles.com",
    "Referer": "https://bloodlore-chronicles.com/jewel",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Version": "0.1.0",
    "sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryoNbB6DKnrZDDtTV7"
}

cookies_4 = {
    "_ga": "GA1.1.199610205.1720025946",
    "gtc_cookie": "true",
    "isPlaying": "false",
    "volume": "0.2",
    "_ga_WT859GPG6Q": "GS1.1.1720025946.1.1.1720029256.0.0.0"
}

# Define the body content
body_4 = (
    "------WebKitFormBoundaryoNbB6DKnrZDDtTV7\r\n"
    "Content-Disposition: form-data; name=\"itemId\"\r\n\r\n"
    "64ecd734a77efbd2ce8cca15\r\n"
    "------WebKitFormBoundaryoNbB6DKnrZDDtTV7\r\n"
    "Content-Disposition: form-data; name=\"amount\"\r\n\r\n"
    "10\r\n"
    "------WebKitFormBoundaryoNbB6DKnrZDDtTV7--\r\n"
)

# pearl: 64ecd734a77efbd2ce8cca15
# jasper: 660eb31b5273f51a9e2eebb4

buy_counter = 5

while True:
    buy_counter += 1
    hunt_response = requests.request("GET", url_1, headers=headers_1, data=payload_1)
    print("Hunt status code: {}".format(hunt_response.status_code))
    time.sleep(random.randint(4, 8))
    hunt_response = requests.request("GET", url_2, headers=headers_2, data=payload_2)
    print("Quick hunt status code: {}".format(hunt_response.status_code))
    if buy_counter == 10:
        # Send the POST request
        buy_response = requests.post(
            "https://bloodlore-chronicles.com/api/game/buysell",
            headers=headers_4,
            cookies=cookies_4,
            data=body_4
        )
        print("Buy response status code: {}".format(buy_response.status_code))
        buy_counter = 0
    time.sleep(random.randint(620, 660))
