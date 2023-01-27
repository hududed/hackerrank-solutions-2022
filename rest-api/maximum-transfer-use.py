
from time import sleep
from typing import Any, Dict, Optional

import requests

MAX_RETRIES = 5
TIMEOUT = 5


def get_request(url: str) -> Optional[Dict[str, Any]]:
    tries = 0
    while tries < MAX_RETRIES:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            print(err)
            tries += 1
            sleep(TIMEOUT)
    return None


def get_transactions(page: int = 1) -> Optional[Dict[str, Any]]:
    return get_request(
        url=f"https://jsonmock.hackerrank.com/api/transactions?page={page}"
    )


def maximumTransfer(name: str, city: str) -> tuple[str]:
    response = get_transactions()
    # print(response)
    total_pages = response["total_pages"]
    total_credit, total_debit = 0, 0
    for page in range(1, total_pages+1):
        print(f"{page}/{total_pages+1}")
        page_response = get_transactions(page)
        data_list = page_response["data"]

        for i, user in enumerate(data_list):
            user_name = user["userName"]
            user_city = user["location"]["city"]
            print(i+1, "/", len(data_list), user_name,
                  user_city, total_credit, total_debit)
            if user["userName"] == name and user_city == city:
                if user["txnType"] == "credit":
                    amount = user["amount"].replace(",", "").replace("$", "")
                    total_credit += float(amount)
                elif user["txnType"] == "debit":
                    amount = user["amount"].replace(",", "").replace("$", "")
                    total_debit += float(amount)

    return f"${total_credit:.2f}", f"${total_debit:.2f}"


def main():
    name, city = "John Oliver", "Bourg"
    total_credit, total_debit = maximumTransfer(name, city)
    print(total_credit, total_debit)


if __name__ == "__main__":
    main()
