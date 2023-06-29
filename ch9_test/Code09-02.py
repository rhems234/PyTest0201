import urllib.request
import bs4
import ssl

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE

nateUrl = "https://www.nate.com"
# htmlObject 형으로 보면 복잡함.
htmlObject = urllib.request.urlopen(nateUrl, context=ssl_context)
# bsObject -> BeautifulSoup html.parser형으로 보기 편함.
bsObject = bs4.BeautifulSoup(htmlObject, "html.parser")

print(bsObject)
