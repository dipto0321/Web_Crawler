from urllib.parse import urlparse


# Get main domain name

def get_main_domain(url):
    try:
        results = get_sub_domain(url).split('.')
        return "{}.{}".format(results[-2],results[-1])
    except:
        return ''


# Get main domain name
def get_sub_domain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

