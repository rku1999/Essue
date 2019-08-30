import requests
import json
from bs4 import BeautifulSoup
from datetime import date
from emailtest import sendEmail

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'category=business&'
       'apiKey=fcc95fc7b66e4126a5cdd6cb8108f06a')

response = requests.get(url).json()
r_json = json.dumps(response, indent = 4, ensure_ascii=False).encode('utf8')

with open('output.json', 'w') as f:
       f.write(r_json)

with open('output.json', 'r') as w:
       data = json.load(w)

del(data["status"])
article_numb = data["totalResults"]
del(data["totalResults"])

html_template = """<tr>
                <td>
                    <img src = """
html_template2 = """ alt = "News image" height = "125" width = "225">
                    </br>"""
html_template3 = """      </td>
                <td>"""
html_template4 = """                </td>
                <td>"""
html_template5 = """          <a href=""" 
html_template6 = """                >[read more]
                    </a>
                </td>
                <td>"""
html_template7 =     """</td>
                   </tr>
                       """
html_template8 = """</table>
                     </body>
                     </html>"""

html_header = """<!DOCTYPE html>
<html>
    <style>
        table, th, td{
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td{
            padding: 5px;
            text-align: left;    
        }
        table#t01 tr:nth-child(even), table#t02 tr:nth-child(even) {
            background-color: #eee;
        }
        table#t01 tr:nth-child(odd), table#t02 tr:nth-child(odd) {
            background-color: #fff;
        }
        table#t01 th {
            background-color: rgb(248, 176, 21);
            color: white;
        }
        table#t02 th {
            background-color: rgb(252, 41, 4);
            color: white;
        }
    </style>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <p>Hi,<br>
            This message is sent from Python.<br>
        </p>
        <table style="width:100%" id="t01">"""

html_footer = """ </table>
              </body>
              </html>"""

today = date.today().strftime("%d-%b-%Y")

g = open(today + ".html", 'a')
g.write(html_header)

for news in data["articles"]:
    if news["content"] is None:
        del news
        continue
    # print("Title: " + news["title"])
    # print("URL: " + news["url"])
    if news["urlToImage"] is None and news["description"] is None:
            # print("Image: No Image")
            html = html_template + "No Image" + html_template2 + news["title"] + html_template3 + "No description" + html_template4 + news["content"] + html_template5 + news["url"] + html_template6 + news["source"]["name"] + html_template7
    elif news["description"] is None:
            html = html_template + news["urlToImage"] + html_template2 + news["title"] + html_template3 + "No description" + html_template4 + news["content"] + html_template5 + news["url"] + html_template6 + news["source"]["name"] + html_template7
    elif news["urlToImage"] is None:
            html = html_template + "No Image" + html_template2 + news["title"] + html_template3 + news["description"] + html_template4 + news["content"] + html_template5 + news["url"] + html_template6 + news["source"]["name"] + html_template7
    else:
            # print("Image: " + news["urlToImage"])
            html = html_template + news["urlToImage"] + html_template2 + news["title"] + html_template3 + news["description"] + html_template4 + news["content"] + html_template5 + news["url"] + html_template6 + news["source"]["name"] + html_template7
    g.write(html.encode('utf-8'))
       
g.write(html_footer)
g.close()

sendEmail(today + ".html")