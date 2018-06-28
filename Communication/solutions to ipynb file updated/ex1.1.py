import os

from urllib import urlopen, urlretrieve
from bs4 import BeautifulSoup
from datetime import datetime as dt

def get(url):
    u = urlopen(url)
    html = u.read()
    code = u.getcode()

    if code >= 400:
        raise ValueError("HTTP Request error %d" % code)
        
    return html, u

def check_dir(path):
    directory = os.path.abspath(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

def divider():
    print "." * 50 + "\n"
        
def download(links, basedir):
    files = []
    check_dir(basedir + '/')

    total = len(links)
    count = 0
    print "%d files to download." % total
    divider()
    
    for filename, link in links.iteritems():
        count += 1
        path = os.path.abspath(basedir + '/%s' % filename)
        files.append(path)

        print "Start download file %s %d/%d - %2.f%%" % (path, count, total, float(count - 1) * 100 / total)
        urlretrieve(link, path)
        print "Finished download file %s %d/%d - %2.f%%" % (path, count, total, float(count) * 100 / total)
        divider()

    print "%d files download has finished successfully." % total
    divider()
    
    return files
    
def get_turnstile_links(year, month=None):
    try:
        html, u = get("http://web.mta.info/developers/turnstile.html")
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find("div", class_="last").find_all("a")

        datalinks = {}

        for link in links:
            try:
                date = dt.strptime(link.get_text(), "%A, %B %d, %Y")

                if (date.year == year and (not month or date.month == month)):
                    href = link.get("href")
                    filename = href.rsplit("/", 1)[-1]
                    datalinks[filename] = "http://web.mta.info/developers/" + href
            except ValueError as e:
                print "Invalid link %s: Reason %s" % (link.get("href"), str(e))

        return datalinks
    except Exception as e:
        raise RuntimeError("Reason %s" % str(e))

input_datadir = "data"
year = 2017
month = 6
links = get_turnstile_links(year, month)
datapath = download(links, input_datadir)