import requests, os
from bs4 import BeautifulSoup

def download_url(url, product, year):
    """create file path and download pdf"""


    current = os.getcwd()
    new_dir = os.path.join(current, product)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)



    if '.pdf' in url:
        data = requests.get(url)

        file_name = os.path.join(new_dir, f"{product} - {year}")

        pdf = open(f"{file_name}.pdf", 'wb')
        pdf.write(data.content)
        pdf.close()
    print(f"Downloaded {product} - {year}")

    





def list_year_range(years):
    """return list of years in rage requested by user"""

    year = years.split("-")
  
    if len(year) == 1 and len(year[0] == 4):
        return year
    if len(year) == 2 and len(year[0]) == 4 and len(year[1]) == 4:
        return list(range(int(year[0]), int(year[1])+1))
    else:
        return []