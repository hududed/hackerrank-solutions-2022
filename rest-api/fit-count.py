from time import sleep
from typing import Any, Dict, Optional

import requests

MAX_RETRIES, TIMEOUT = 2, 1


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


def get_medical_records(page: int = 1) -> Optional[Dict[str, Any]]:
    return get_request(
        url=f"https://jsonmock.hackerrank.com/api/medical_records?page={page}"
    )


def healthCheckup(lower: int, upper: int) -> Optional[Dict[str, Any]]:
    response = get_medical_records()
    total_pages = response["total_pages"]
    total_diastole = 0
    for page in range(1, total_pages+1):
        print(f"{page}/{total_pages+1} total_so_far: {total_diastole}")
        page_response = get_medical_records(page)
        data_list = page_response["data"]

        for i, patient in enumerate(data_list):
            bp_diastole = patient["vitals"]["bloodPressureDiastole"]
            print(
                f"{i+1}/{len(data_list)} {bp_diastole >= lower and bp_diastole <= upper}")
            if bp_diastole >= lower and bp_diastole <= upper:
                total_diastole += 1
    return total_diastole


def main():
    lower, upper = 120, 160
    count = healthCheckup(lower, upper)
    print(count)


if __name__ == "__main__":
    main()
