import urllib2
from bs4 import BeautifulSoup
import csv



quote_page='https://github.com/christine-hu/summer-2019-internships/blob/master/README.md'
page=urllib2.urlopen(quote_page)
soup=BeautifulSoup(page,'html.parser')
table_rows=[]
table_bodies=soup.find_all('tbody')
for t in table_bodies:
    table_rows+=t.find_all('tr')
d=table_rows[1].find_all('td')[0].select('a')[0].text
csv_data=[]
count=0
for row in table_rows:
    csv_row=[]
    cols=row.find_all('td')
    a=cols[0].select('a')
    href=''
    firm=''
    notes=''
    if a!=[]:
        href=a[0].get('href').encode('utf-8')
        firm=a[0].text.encode('utf-8')
    else:
        firm=cols[0].text.encode('utf-8')
    location=cols[1].text.encode('utf-8')
    if len(cols)==3:
        notes=cols[2].text.encode('utf-8')
    else:
        notes=cols[3].text.encode('utf-8')
    csv_row+=[href,firm,location,notes]
    csv_data+=[csv_row]
    count+=1

csv_data=sorted(csv_data, key=lambda x: x[1])


with open('tech_internships.csv','ab') as tech_internships:
    writer=csv.writer(tech_internships)
    writer.writerow(["Company","Location","Notes"])
    for row in csv_data:
        first=''
        if row[0]=="":
            first=row[1]
        else:
            first='=HYPERLINK(\"'+row[0]+'\",\"'+row[1]+"\")"
        writer.writerow([first,row[2],row[3]])