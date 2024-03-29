from urllib.request import urlopen
from link_finder import LinkFinder
from methods import *
from datetime import datetime
from domain import *


class Spider:
    # Class variables
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('Initial Spider', base_url)

    @staticmethod
    def boot():
        create_project_directory(Spider.project_name)
        created_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_index(Spider.queue_file)
        Spider.crawled = file_to_index(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print("{} : {} crawling {}.".format(datetime.utcnow(), thread_name, page_url))
            print("Queue : {} || Crawled: {} .".format(str(len(Spider.queue)), str(len(Spider.crawled))))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print("{} : Can't crawl page.".format(datetime.utcnow()))
            print(str(e))
            return set()
        return finder.page_urls()


    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != get_main_domain(url):
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue_file, Spider.queue)
        set_to_file(Spider.crawled_file, Spider.crawled)
