#! python

from bs4 import BeautifulSoup
import requests

target_urls = {
"01":"http://zhuanlan.zhihu.com/p/28277072",
"02":"http://zhuanlan.zhihu.com/p/28325166",
"03":"http://zhuanlan.zhihu.com/p/28434767",
"04":"http://zhuanlan.zhihu.com/p/28490221",
"05":"http://zhuanlan.zhihu.com/p/28863518",
"06":"http://zhuanlan.zhihu.com/p/29410442",
"07":"http://zhuanlan.zhihu.com/p/29585082",
"08":"http://zhuanlan.zhihu.com/p/29734799",
"09":"http://zhuanlan.zhihu.com/p/29903948",
"10":"http://zhuanlan.zhihu.com/p/29953781",
"11":"http://zhuanlan.zhihu.com/p/30133379",
"12":"http://zhuanlan.zhihu.com/p/30261154",
"13":"http://zhuanlan.zhihu.com/p/30494021",
"14":"http://zhuanlan.zhihu.com/p/30515094",
"15":"http://zhuanlan.zhihu.com/p/30515493",
"16":"http://zhuanlan.zhihu.com/p/30809762",
"17":"http://zhuanlan.zhihu.com/p/30954790",
"18,19":"http://zhuanlan.zhihu.com/p/32007844",
"20":"http://zhuanlan.zhihu.com/p/32035771",
"21":"http://zhuanlan.zhihu.com/p/33205535",
"22":"http://zhuanlan.zhihu.com/p/33295067",
"23":"http://zhuanlan.zhihu.com/p/33867542",
"24":"http://zhuanlan.zhihu.com/p/33952689",
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


for prefix, url in target_urls.items():
#     print(prefix)
    img_index = 1
    
    r = requests.get(url, headers = headers)
    content = r.text
    soup = BeautifulSoup(content, "html5lib")
    main_div = soup.find("div", class_="RichText Post-RichText")
    
    # print(main_div.prettify())
    # print("-"*20)
    # print("-"*20)
    # print("-"*20)

    file_string = ""
    for child in main_div.children:
        # print(child.name)
        if child.name == "h2":
            # print("##",child.get_text())
            file_string = file_string + "## " + child.get_text() + "\n\n"
        elif child.name != "figure":
            # print(child.get_text())
            file_string = file_string + child.get_text() + "\n\n"

        if child.name == "figure":
            img_url = child.find("img")["data-actualsrc"]
            img_name = f"lec{prefix}_fg{img_index:02}.jpg"
            img_index += 1
            img_path = f"images/{img_name}"
            # img_path = img_name
            img_md = f"![pass]({img_path})"
            # print("-"*20)
            # print(child.find("img"))
            # print("-"*20)
            # print(img_url)
            # print("-"*20)
            file_string = file_string + img_md + "\n\n"

            response = requests.get(img_url, headers = headers)

            with open(img_path, 'wb') as f:
                f.write(response.content)
            
            
            # print(img_md)
        
    print("-"*20)
    # print(file_string)

    md_file_name = prefix + ".md"
    with open(md_file_name, 'w',encoding='utf-8') as f:
        # print(file_string, file=f)
        f.write(file_string)

 
    