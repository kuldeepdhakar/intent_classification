import requests
import json

headers = {'content-type': 'application/json'}


def test_match_intent():
    method = '/api/ml/get_intent'

    query_list = ["What's the booking status for reservation ID XYZ789?", 'book a ticket', "cancel my reservation"]
    for query in query_list:
        print(query)
        payload = {'utterance': query}


        url_local = 'http://0.0.0.0:8000'
        print(url_local + method)
        res = requests.post(url_local + method, data=json.dumps(payload),
                            headers=headers)

        print(res.status_code)
        print(res.json())


def test_add_intent():
    method = '/api/ml/add_intent'


    payload = {
  "name": "check-booking-status",
  "examples": [
    "What's the booking status for reservation ID XYZ789?",
    "Can you provide me with the current seat assignment for my booking?",
    "I'd like to know if my booking for flight ABC123 is confirmed.",
    "What's the departure gate for my reservation with confirmation number LMN456?",
    "Has there been any cabin upgrade for my reservation on flight DEF789?",
    "Can you check the booking status for the email address jane.doe@email.com?",
    "I want to inquire about the gate information for my flight with booking reference QRS123.",
    "Please tell me the current status of my booking for flight WXY456.",
    "Has there been any change in the meal preference for my booking on flight TUV123?",
    "What's the booking status for my ticket on the flight with reference code STU456?"
  ]
}



    url_local = 'http://0.0.0.0:8000'
    res = requests.post(url_local + method, data=json.dumps(payload),
                        headers=headers)

    print(res.status_code)
    print(res.json())




def test_delete_intent():
    method = '/api/ml/delete_intent'
    payload = {'machine_name': "check-booking-status"}


    url_local = 'http://0.0.0.0:8000'
    res = requests.post(url_local + method, data=json.dumps(payload),
                        headers=headers)

    print(res.status_code)
    print(res.json())


if __name__ == '__main__':

    # test_add_intent()

    test_match_intent()

    # test_delete_intent()

