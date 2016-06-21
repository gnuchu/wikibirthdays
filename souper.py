html = '''
<html>
  <head><title>Page title</title>
  </head>
  <body>
    <h1 id="first-heading">First Heading</h1>
    <ul>
      <li>1</li>
      <li>2</li>
      <li>3</li>
    </ul>
    <h1 id="second-heading">Second Heading</h1>
    <ul>
      <li>
       <a href="/wiki/1999" title="1999">
        1999
       </a>
       –
       <a href="/wiki/Chandler_Riggs" title="Chandler Riggs">
        Chandler Riggs
       </a>
       , American actor
      </li>
    </ul>
  <body>
</html>
'''

from bs4 import BeautifulSoup
import sys

soup = BeautifulSoup(html, "html.parser")
a = soup.find(id="second-heading")
ul = a.find_next('ul')
all_lis = ul.find_all('li')
base_url = 'https://en.wikipedia.org'

for li in all_lis:
  all_as = li.find_all('a', href=True)
  print(li)
  # for a in all_as:
  #   print(a)