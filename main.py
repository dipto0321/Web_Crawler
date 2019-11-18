import threading
from queue import Queue
from spyder import Spider
from domain import *
from methods import *

project_name = input("Give your crawler project a name: ")
homepage = input("Enter home page url which you want to crawl: ")
domain_name = get_main_domain(homepage)
queued_file = project_name + '/queue.txt'
crawled_file = project_name + '/crawled.txt'

number_of_threads = int(input("Enter thread number based on your CPU capability: "))

# Create an object of thread queue

queue = Queue()
Spider(project_name,homepage,domain_name)


def create_threads():
    for _ in range(number_of_threads):
        t = threading.Thread(target=_thread)
        t.daemon = True
        t.start()


def _thread():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


def create_job():
    for link in file_to_index(queued_file):
        queue.put(link)
    queue.join()
    crawl()


def crawl():
    queued_links = file_to_index(queued_file)
    if len(queued_file) > 0:
        print("{} links in the queue".format(str(len(queued_links))))
        create_job()


create_threads()
crawl()
