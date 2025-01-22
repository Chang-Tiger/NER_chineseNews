from bs4 import BeautifulSoup
#from opencc import OpenCC

import requests
from datetime import datetime

from write_excel import outputExcel
from tkwin import showWindow



def crawler_main(url):
    res = requests.get(url)
    res.encoding='utf-8'
    soup = BeautifulSoup(res.text,'lxml')
    content_div = soup.find('span', id='detailContent')
    meta_tag = soup.find('meta', attrs={'name': 'description'})
    short_content = meta_tag.get('content')
    if (content_div or main_content):
        main_content = content_div.get_text(separator='\n', strip=True)
        if(len(main_content) < 30):
            return short_content
        else:
            return main_content
    else:
        print("no content")
        return ""

def main():
    #text = "信息支援部隊"
    #cc = OpenCC('t2s')
    
    now_t = datetime.now().strftime("%Y-%m-%d_%H-%M")
    text = showWindow()
    #simplified_text = cc.convert(text) #convert to simplified ch

    # simplified_utf_encoded = simplified_text.encode('utf-8')
    # simplified_utf_hex = '%' + '%'.join(f'{b:02X}' for b in simplified_utf_encoded)

    utf_encoded = text.encode('utf-8')
    utf_hex = '%' + '%'.join(f'{b:02X}' for b in utf_encoded)
    print(utf_hex)
    
    #web2 = 'http://www.81.cn/ysym/ssjgy/index.html?keyword='+str(simplified_utf_hex)+'&searchfield=TITLE&indexsearch=2'
    XL_PATH = r"data" + "\\" + text + now_t + ".xlsx"

    info = []
    titles = []
    for page in range(1,11):
        web = 'https://so.news.cn/getNews?lang=cn&curPage='+str(page)+'+&searchFields=0&sortField=0&keyword='+str(utf_hex)
        response = requests.get(web)
        #print(response.text)
        if response.status_code == 200:
            print("ok")
            json_data = response.json()
            
            try:
                for data in json_data["content"]["results"]:
                    try:
                        time = datetime.strptime(data["pubtime"], "%Y-%m-%d %H:%M:%S")
                        #print(time)
                        title = data["title"]
                        titles.append(title)
                        url = data["url"]
                        print(url)
                        content = crawler_main(url)
                        
                        dic = {"Time":time,"Source":url,"Title":title, "Content":content}
                        info.append(dic)

                    
                    except Exception as e:
                        print(f"Error processing data: {e}")
            except Exception as e:
                print("No more pages.")
                break
         
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    if info :
        outputExcel(info,XL_PATH)  

if __name__ == '__main__':
    main()
