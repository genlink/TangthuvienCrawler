import re
import os
import requests
from bs4 import BeautifulSoup
import argparse
from progress.bar import Bar

class FancyBar(Bar):
    message = 'Processing'
    fill = '#'
    suffix = '%(index)d/%(max)d - Elapsed %(elapsed)d  second - remaining %(eta)d second'

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


def parsing_main_page(mainpageURL,min,max,directory):
    createFolder(directory)
    lower = int(min)
    upper = int(max)
    bar = FancyBar(max=upper)
    for num in range(lower,upper + 1):
        mainURL = mainpageURL+'/chuong-'+str(num)
        response = requests.get(mainURL)
        parsed_html = BeautifulSoup(response.text,"html.parser")
#        print(parsed_html)
        chapterTitle = parsed_html.find_all(class_="more-chap btn hidden")
        chapterTitle = re.sub(r'\[<a class=\"more-chap btn hidden\" href=\"javascript:void\(0\);\" onclick=\"(.*)\">',"", str(chapterTitle))
        chapterTitle = re.sub(r'</a>]',"",str(chapterTitle))
#        print(chapterTitle)
        aaa = parsed_html.select('div[class*="box-chap box-chap-"]')
        line = re.sub(r'\[<div class=\"(.*)\">',chapterTitle+'\n', str(aaa))
        line = re.sub(r'</div>\]',"", str(line))
        
        f = open(directory+'/demo.txt','w',encoding="utf-8")
        f.write(str(line))
        f.close()

        with open(directory+"/demo.txt","r",encoding="utf-8") as f, open(directory+'/'+str(num).zfill(5)+".txt","w",encoding="utf-8") as outfile:
            for i in f.readlines():
               if not i.strip():
                   continue
               if i:
                   outfile.write(i)
        os.remove(directory+'/demo.txt')
        bar.next()
    bar.finish()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',dest='mainURL',default=[],help='Add novel URL')
    parser.add_argument('-l',dest='start',default=[],help='Add start chapter')
    parser.add_argument('-d',dest='stop',default=[],help='Add stop chapter')
    parser.add_argument('-f',dest='directory',default=[],help='Directory to save txt file')
    
    results = parser.parse_args()
    mainURL = results.mainURL
    min = results.start
    max = results.stop
    folder = results.directory
    parsing_main_page(mainURL,min,max,folder)
    print("Crawler completed with "+max+" chappters")
    
if __name__ == '__main__':
	main()
