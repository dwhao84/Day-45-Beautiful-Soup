from bs4 import BeautifulSoup

with open('website.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
    print(html_content)
    
print("================================")

# 如果html_parser，沒辦法使用的話，可以改用lxml做不同的解析。
soup = BeautifulSoup(html_content, 'html.parser')
print(soup.title)
print(soup.title.string) # 印出 title的string內容。

print(soup.prettify()) # 運用prettify把html印的比較好閱讀。
print(soup.a) # 用soup.a 印出<a><a/> tag。

print("================================")
# Section 2:
# 如果想要印出所有相關a tag(其他內容也是)，可以用find_all()
print(soup.find_all("a"))

all_the_tags = soup.find_all("a")

# 如何找到所有a tag裡面的內容?
for tag in all_the_tags:
    # 印出所有連結
    print(tag.get("href"))
    
    # 印出所有的文字
    print(tag.getText())
# 顯示：
# The App Brewery
# My Hobbies
# Contact Me

# 如果要找特定內容的話，可以用soup.find(name="元素", id="名稱")
heading = soup.find(name="h1", id="name")
print(f"Heading: {heading}")

# 如果要找到特定的section_heading(要注意，class的話，要用class_)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# 用CSS Selector找特定的內容
name = soup.select_one(selector="#name")
print(f"company_url: { name }")

# 用CSS Selector找同一屬性的內容
dot_heading = soup.select(".heading")
print(dot_heading)
