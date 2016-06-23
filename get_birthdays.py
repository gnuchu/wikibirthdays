# import sys
# print(sys.stdout.encoding)

from bs4 import BeautifulSoup
import urllib.request
from datetime import date
from datetime import timedelta
import sys

base_url = 'https://en.wikipedia.org'
f = open("birthdays.html", "w", encoding="utf-8")

header = '''
<!doctype html>
<html> <!--<![endif]-->
  <head>
    <meta charset="utf-8">
    <title>Birthdays - Last week and this.</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/js/bootstrap.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/css/bootstrap.css">
  </head>
  <body>
    <div class='container'>
      <table class="table table-bordered table-condensed">
        <thead>
          <tr>
            <th>Name</th>
            <th>Picture</th>
          </tr>
        </thead>
        <tbody>
'''
footer = '''
        </tbody>
      </table>
    </div>
  </body>
  </html>
'''

f.write(header+"\n")

start_date = date.today() + timedelta(days=-4)
end_date = date.today() + timedelta(days=5)

tr_s = '<tr>'
tr_e = '</tr>'
td_s = '<td>'
td_e = '</td>'


while start_date < end_date:
  month = start_date.strftime('%B')
  day   = start_date.strftime('%d').lstrip('0') #remove zero padding
  page  = month + '_' + day
  start_date = start_date + timedelta(days=1)

  url = "https://en.wikipedia.org/wiki/" + page
  doc = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(doc, "html.parser")
  a = soup.find(id='Births')
  ul = a.find_next('ul')
  lis = ul.find_all('li')

  row = tr_s + '<td colspan="2" style="text-align: center; background-color: #F7F7F7;">' + month + ' ' + day + td_e + tr_e
  f.write(row + "\n")
  page_title = ""

  for li in lis:
    row = ""
    row = str(li).replace('<li>','<td>')
    row = row.replace('</li>','</td>')
    row = row.replace('/wiki/', 'https://en.wikipedia.org/wiki/')

    for a in li.find_all('a'):
      page_title = a['href']
      try:
        int(page_title)
        pass
      except:
        page_title = page_title.replace('https://en.wikipedia.org/wiki/',"")

    page_title = page_title.replace('/wiki/',"")
    f.write('<tr>')
    f.write(row+"\n")
    f.write('<td>' + page_title + '</td>')
    f.write('</tr>')

f.write(footer+"\n")
f.close()

def get_image_url(page_title):
  placeholder = "https://placeholdit.imgix.net/~text?txtsize=33&txt=ImageN/A&w=200&h=200"
  url = base_url + '/wiki/' + page_title
  


