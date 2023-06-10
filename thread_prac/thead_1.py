from threading import Thread, Event, Lock, Semaphore
from time import sleep
import requests


class FindGoogle:
    def __init__(self):
        self.website = r"https://www.google.com"
        self.status = None

    def thread_receive(self):
        sleep(4)
        html = requests.get(self.website)
        if "Google" in html.text:
            self.status = True
        else:
            self.status = False

    def thread_status(self):
        while True:
            sleep(10)
            if not self.status == None:
                print(f"In statusThread - Status->> {self.status}")
                break

    def start_both_threads(self):
        Thread(target=self.thread_receive, name="receiver").start()
        Thread(target=self.thread_status, name="status_teller").start()


if __name__ == "__main__":
    finder = FindGoogle()
    finder.start_both_threads()
