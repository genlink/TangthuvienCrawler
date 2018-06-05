import re
import os
import requests
from bs4 import BeautifulSoup
import argparse



def parsing_main_page(mainpageURL,min,max,directory):

    lower = int(min)
    upper = int(max)
    for num in range(lower,upper + 1):
        mainURL = mainpageURL+'/chuong-'+str(num)
        response = requests.get(mainURL)
        parsed_html = BeautifulSoup(response.text,"html.parser")
    #    print(parsed_html)
        aaa = parsed_html.select('div[class*="box-chap box-chap-"]')
        
        line = re.sub(r'\[<div class=\"(.*)\">',"", str(aaa))
        line = re.sub(r'</div>\]',"", str(line))
        
        f = open(directory+'/demo.txt','w',encoding="utf-8")
        f.write(str(line))
        f.close()
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(directory+"/demo.txt","r",encoding="utf-8") as f, open(directory+'/'+str(num).zfill(5)+".txt","w",encoding="utf-8") as outfile:
            for i in f.readlines():
               if not i.strip():
                   continue
               if i:
                   outfile.write(i)
        os.remove(directory+'/demo.txt')
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