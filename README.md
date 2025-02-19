
# Web Scrapping Amazon Reviews using BeautifulSoup

The Python code presented in this Repo is simple and easy to understand. I made use of BeautifulSoup library of python to process the raw html obtained by web scrapping the Amazon website.


The project mainly can be divided into three sections: 1) Building the custom URL's based upon the user input of item. 2) Sending requests to these pages and web scrapping the reviews. 3) Storing them into Pandas DataFrames for further processing and exporting them to EXCEL.

### Python Libraries to be Installed:
1. Pandas:
```bash
 pip install pandas
```

2. BeautifulSoup:
```bash
  pip install beautifulsoup4
```

3. Requests:
```bash
  pip install requests
```

4. (Optional) time , random


### Clone the project

```bash
  git clone https://github.com/Siddhantraje6/Web-Scrapping-Amazon-Reviews-using-BeautifulSoup-Python
```


### Debugging:
- If the status code for the requests is 503, I suggest to try after an hour or half as the Amazon servers try to maintain the load.

- I was not able to get the code running over the Jupyter notebook due to error in find_all() function of the BeautifulSoup which just resolves by itself if I try to run the .py on VScode.

- Also the maximum reviews that can be web scrapped in a single go is 100.


### Support
For support, email siddhant.raje.5g@gmail.com 

Thank You


