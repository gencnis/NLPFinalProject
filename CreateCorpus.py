import os
import requests
import urllib.request as urlRequest
from bs4 import BeautifulSoup
import ssl

import re

def extractText(url):
    '''
    Extracts a page from a wiki-styled web page.

    @param url - the URL of the webpage

    @return content.text - the text on the wiki page
    @return pageExtensions - a list of all of the relative links on the web page
    '''

    page = requests.get(url)
    content = BeautifulSoup(page.content, "html.parser")

    html = str(page.content)

    pageExtensions = re.findall(r"href=\"/\w+\"", html)

    return content.text, pageExtensions


def main():


    # Create the SSL environment to bypass security certificates
    ssl._create_default_https_context = ssl._create_unverified_context

    corpusFolder = os.path.join(os.path.dirname(__file__), "Corpus2")


    # Create a list of visited and unvisited webpage extensions
    extensionsVisited = []
    extensionsToVisit = ["/Stardew_Valley_Wiki"]
    rootSite = "https://stardewvalleywiki.com"

    while len(extensionsToVisit) > 0:
        extension = extensionsToVisit[0]

        url = rootSite + extension


        extensionsToVisit.remove(extension)
        extensionsVisited.append(extension)


        with open(os.path.join(corpusFolder, extension[1:] + ".txt"), mode = 'w', encoding = "utf-8") as output:
            outText, newExtensions = extractText(url)
            output.write(outText)

            # Add new extensions
            for entry in newExtensions:

                possiblePage = entry[6:-1]

                if (possiblePage not in extensionsVisited) and (possiblePage not in extensionsToVisit):
                    extensionsToVisit.append(possiblePage)
            


if __name__ == "__main__":
    main()