import requests
import json
from typing import List


def getUsernames(threshold: int) -> List[str]:
    # set variables
    usernames = []
    page = 1
    total_pages = 1

    while page <= total_pages:

        # make request for each page
        r = requests.get(
            f"https://jsonmock.hackerrank.com/api/article_users?page{str(page)}")
        data = r.json()['data']
        # set total_pages
        if page == 1:
            total_pages = r.json()["total_pages"]

        # get data for each user
        for d in data:
            if d["submission_count"] > threshold:
                usernames.append(d['username'])
        page += 1

    return usernames


def main() -> None:
    names = getUsernames(10)
    print(names)


if __name__ == "__main__":
    main()
