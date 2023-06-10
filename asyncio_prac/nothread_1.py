import requests
import time


def scan1(sites):
    with requests.Session() as session:
        for url in sites:
            res = session.get(url)
            print(res)


def scan2(sites):
    for url in sites:
        res = requests.get(url)
        print(res)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 5
    start_time = time.time()
    scan1(sites)
    duration = time.time() - start_time

    print(f"Downloaded {len(sites)} in {duration} seconds")
