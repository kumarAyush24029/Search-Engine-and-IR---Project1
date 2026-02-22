import sys
import requests
from bs4 import BeautifulSoup

if __name__=="__main__":
    if len(sys.argv)<2:
        print("No URL entered, please enter a valid link\n")
        sys.exit()
    else:
        link = sys.argv[1]
    
    
    fetchresponse=requests.get(link)
    if fetchresponse.status_code==200:
        print("get request run succesfully\n")
    else:
        print("get request failed to fetch data from the server\n") 
          
    founddata=fetchresponse.text
    
    
    newsoup = BeautifulSoup(founddata,"html.parser")
    
    if newsoup.title:
        print("Title :" +newsoup.title.string)
        print("\n")
    else:
        print("No title present in the  html document of fetched data\n")    
        
    
    if newsoup.body:
        htmlbody =  newsoup.body.get_text()  
        print("Body:\n"+htmlbody)
    else:
        print("No body present in the html file of this site.")      
    
    
    alllinks = newsoup.find_all("a")
    # print(alllinks)
    
    print("\nLinks :")
    
    for link in alllinks:
        href=link.get("href")
        if href:
            print(href)
    print("\n")
            
            
