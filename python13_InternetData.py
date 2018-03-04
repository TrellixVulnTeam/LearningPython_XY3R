# File for retrieveing data from the internet

import urllib.request

def main():
    webUrl = urllib.request.urlopen("https://google.com/")
    print("Result code: " + str(webUrl.getcode()))
    data = webUrl.read()
    # Read html
    print(str(data))

main()