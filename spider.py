import requests
import csv
from pyquery import PyQuery as pq
import time

# get the information of top 10 github projects
def spider():
    # url that selects the top projects while language=python&&date range=this month&&english
    url = "https://github.com/trending/python?since=monthly&spoken_language_code=en"
    r = requests.get(url)
    content = pq(r.content)
    # get the information of top projects
    articles = content('article')
    # the format of all information, any other info will be appended
    information = [['title','stars','folks','main contributors']]
    urls = []
    count = 0
    for article in articles:
        ar = pq(article)
        # title and url of the project
        title = ar('h1').text()
        url = "https://github.com" + ar('h1')('a').attr('href')
        urls.append(url)
        # intro = ar('p').text()  #introduction of projects

        # get the stats line of the project
        line2 = ar('.f6.text-gray.mt-2')

        # stars and folks of the project
        stars_and_folks = line2('.muted-link.d-inline-block.mr-3').text()
        stars_and_folks_list = stars_and_folks.split(' ')
        stars=stars_and_folks_list[0].replace(',','')
        folks=stars_and_folks_list[1].replace(',','')
        
        info = [title,stars,folks]
        # main contributors of the project
        contribs = line2('.d-inline-block.mr-3').items()
        for c in contribs:
            aes = c.find('a').items()
            for a in aes:
                info.append(a.attr('href').replace('/',''))        
        information.append(info)

        # break when collected 10 top projects
        count += 1
        if count == 10:
            break

    # write all information into a csv file 
    localtime = time.strftime("%Y%m%d", time.localtime())
    filename = localtime + '_top10_GitHub_projects.csv'
    with open(filename, 'w', newline='')as f:
        writer = csv.writer(f)
        writer.writerows(information)
        f.close()
        
    # return the urls for webdriver to do the next job(Watch these projects)
    return urls

# if __name__ == "__main__":
#     urls=spider()
