import requests
import time
import random

bearer = ""

def get_next_hunt_time():
    url = "https://bloodlore-chronicles.com/api/ClientUser/getme"

    header = {
        'ApiKey': '3DB373CF32AC02834ED4A388F512980EF3D8ED3FEF92640F6DC3B2C20DEB2935',
        'Authorization': 'Bearer {}'.format(bearer),
    }

    response = requests.request("GET", url, headers=headers)

    next_hunt_time = response.json()['nextAllowedHuntTimeStamp']

    return next_hunt_time

def get_new_bearer():
    url = "https://bloodlore-chronicles.com/api/user/login"

    payload={'username': 'Keurbz',
        'password': 'b5a5e93992d49895d87efa09f26e10eec80f2878f72eb7b4f0af542e4596181d'}

    headers = {
        'ApiKey': '3DB373CF32AC02834ED4A388F512980EF3D8ED3FEF92640F6DC3B2C20DEB2935',
        }

    response = requests.request("POST", url, headers=headers, data=payload)

    new_bearer = response.json()['access_token']

    return new_bearer

url_1 = "https://bloodlore-chronicles.com/api/Game/hunt"
url_2 = "https://bloodlore-chronicles.com/api/Game/quickhunt"
url_3 = "https://bloodlore-chronicles.com/api/game/buysell"

# Define the body content
# pearl: 64ecd734a77efbd2ce8cca15
# jasper: 660eb31b5273f51a9e2eebb4
buy_body = (
    "------WebKitFormBoundaryoNbB6DKnrZDDtTV7\r\n"
    "Content-Disposition: form-data; name=\"itemId\"\r\n\r\n"
    "64ecd734a77efbd2ce8cca15\r\n"
    "------WebKitFormBoundaryoNbB6DKnrZDDtTV7\r\n"
    "Content-Disposition: form-data; name=\"amount\"\r\n\r\n"
    "10\r\n"
    "------WebKitFormBoundaryoNbB6DKnrZDDtTV7--\r\n"
)

buy_counter = 0
bearer = get_new_bearer()

header = {
  'ApiKey': '3DB373CF32AC02834ED4A388F512980EF3D8ED3FEF92640F6DC3B2C20DEB2935',
  'Authorization': 'Bearer {}'.format(bearer),
}

while True:
    # buy_counter += 1
    hunt_response = requests.request("GET", url_1, headers=header)
    hunt_status_code = hunt_response.status_code
    print("Hunt status code: {}".format(hunt_status_code))
    if hunt_status_code != 200:
        bearer = get_new_bearer()
        header = {
            'ApiKey': '3DB373CF32AC02834ED4A388F512980EF3D8ED3FEF92640F6DC3B2C20DEB2935',
            'Authorization': 'Bearer {}'.format(bearer),
        }
    time.sleep(random.randint(4, 8))
    hunt_response = requests.request("GET", url_2, headers=header)
    print("Quick hunt status code: {}".format(hunt_response.status_code))

    # Set the time to sleep depending on whether blood craze procced or not
    # Figure out whether blood craze procced or not depending on the next hunt time
    next_hunt_time = get_next_hunt_time()
    time_delta = next_hunt_time - int(time.time())

    time.sleep(random.randint(time_delta + 15, time_delta + 45))

# if buy_counter == 10:
#     # Send the POST request
#     buy_response = requests.post(
#         url_3,
#         headers=header,
#         data=buy_body
#     )
#     print("Buy response status code: {}".format(buy_response.status_code))
#     buy_counter = 0
