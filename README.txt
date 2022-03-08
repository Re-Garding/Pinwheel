Instructions:

run 'pip3 install -r requirements.txt'
this will install Flask, Beautiful Soup, and Requests for your use.

1. Navigate to the main file and run 'python3 server.py' to run Flask and host your page onto http://localhost:5000/

2. Opening http://localhost:5000/ within your preferred browser will open a basic search page, where you can enter
search criteria, form names and a range of years. You can indicate whether you would like the pdf's to be 
downloaded to your files. (if you enter no range of years, nothing will be downloaded)



NOTES:

I used python3.8.9, Beautiful Soup, Flask, and Requests for this task

Given More Time:

I would add the following features:
- additional function testing
- additional error exceptions
- js frontened to help filter/ensure user entries are in the correct format

Struggles:

Flask has a built in 'Jsonify' function to change items into the json type. There is an unfortunate bug in this where it 
defaults to sorting key values. So, though it then displayed as desired, the max_year was moved above the min_year, 
which is not the desired output. I had to refactor how the data was transitioned to Json. It transitioned well using the
json.dumps method, and though it displays as desired when printed to the terminal, it is not so pretty in the browser


Less obvious items to note:

I included in the initial data scrape from a search a section which pulls the total number of results, and incorporated that into 
following data pulls to curtail the number of times it scrapes the web to the minimum number necessary to retreive all data. 
This allows each scrape to be unique and as fast or as long as it needs to be depending on the search parameters. 