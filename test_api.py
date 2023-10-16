import requests
import json

headers = {'content-type': 'application/json'}


def test_match_intent():
    method = '/match_intent'

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
    method = '/add_intent'


    payload = {
        "name": "book-a-ticket",
        "examples": [
            "I want to book a ticket from Hyderabad to Chennai",
            "I'd like to book a plane ticket for a flight on August 25th",
            "Can you help me reserve a seat on a flight from New York to Los Angeles?",
            "I'm interested in flying to Paris from London on the 10th of September.",
            "I want to travel to Tokyo and I need a ticket for a flight next week.",
            "Could you assist me in booking a flight from Chicago to Miami on the 15th of October?",
            "I'm looking for a round-trip ticket from San Francisco to Seattle for the weekend of November 5th.",
            "I need to get to Dubai from Mumbai, preferably on a direct flight.",
            "Can you check for available flights from Toronto to Vancouver for the 20th of December?",
            "I'm planning a trip to Rome, and I'd like to book a business class ticket with extra legroom.",
            "I want to fly to London, departing on the 8th of January and returning on the 20th."
        ]
    }



    url_local = 'http://0.0.0.0:8000'
    res = requests.post(url_local + method, data=json.dumps(payload),
                        headers=headers)

    print(res.status_code)
    print(res.json())




def test_delete_intent():
    method = '/delete_intent'
    payload = {'machine_name': "book-a-ticket"}


    url_local = 'http://0.0.0.0:8000'
    res = requests.post(url_local + method, data=json.dumps(payload),
                        headers=headers)

    print(res.status_code)
    print(res.json())


if __name__ == '__main__':

    test_delete_intent()
    test_match_intent()
    test_add_intent()
    test_match_intent()


