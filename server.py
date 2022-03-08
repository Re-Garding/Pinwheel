from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import json
from methods import download_url, list_year_range

app = Flask(__name__)

base_url = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html?sortColumn=sortOrder&resultsPerPage=200&isDescending=false"
first_row = "&indexOfFirstRow="



@app.route("/")
def homepage():
    """display homepage"""
    return render_template("homepage.html")
    


@app.route("/results", methods=['POST'])
def results():
    """display results of search and download requested pdfs"""
    form = request.form.get("form")
    form_one = form.split(" ")
    search = "+".join(form_one)
    download = request.form.get("download")
    year = request.form.get("years")
    year_range = list_year_range(year)
    count = 0
    products = []
    search_num = 21000

    final = {}

    #create set with total number of years attributed to search result
    years_total = set()


    while True:
        if count > search_num:
            break

        URL = f"https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow={count}&criteria=formNumber&value={search}&isDescending=false"

        data = requests.get(URL)
        soup = BeautifulSoup(data.content, "html.parser")

        #pull total number of results from search page and set to an integer value
        #will only work at very first count. This will avoid errors if it navigates beyond results
        if count == 0:
            search_total = int(soup.find(class_="ShowByColumn").text.split(" ")[-4].replace(",", ""))
            #with 200 results per page (maxxed out) it will determine the number of times it 
            # needs to pull data dependent on search results
            search_num = ((search_total // 200) + 1) * 200
            

        #each unique result will be pulled as a Beautiful Soup item, and placed into a list

        products.extend(soup.find_all('tr', class_="odd"))
        products.extend(soup.find_all('tr', class_="even"))

        #we increase the results count, so we can ensure we aren't pulling the same data
        #multiple times - 200 is the max results per page for display

        count += 200




    for item in products:

        #we'll iterate through the list and pull out the form number, title, and year
        #for each form and place it into a tuple for further analysis

        product = str(item.find('td', class_="LeftCellSpacer").text.strip())
        title = str(item.find('td', class_="MiddleCellSpacer").text.strip())
        year = str(item.find('td', class_="EndCellSpacer").text.strip())
        pdf_url = (item.find('a').get('href'))


        if product.title() == form.title():
            years_total.add(year)
            if download != None and int(year) in year_range:
                download_url(pdf_url, product, year)
            if product not in final:
                final["form_number"] = product.title()
                final["form_title"] = title.title()
    final["min_year"] = min(years_total)
    final["max_year"] = max(years_total)
    
    final_list = []
    final_list.append(final)
    
    return json.dumps(final_list, sort_keys=False)




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    use_reloaded=True,
    use_debugger=True

