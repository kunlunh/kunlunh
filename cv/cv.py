from bs4 import BeautifulSoup
indexFilepath = '/home/runner/work/hklcv/hklcv/public/index.html'

# 读取 HTML 文件
with open(indexFilepath, 'r', encoding='utf-8') as file:
    html_content = file.read()

# 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 找到 class 为 footer 的 div
footer_div = soup.find('div', class_='footer')

# 创建新的链接
new_links = [
    '<a href="https://beian.miit.gov.cn/">粤ICP备13053581号-5</a>.',
    '<a href="http://www.beian.gov.cn/portal/recordQuery">粤公网安备 44070302000613号</a>'
]

# 将新链接添加到 footer 中
for link in new_links:
    footer_div.append(BeautifulSoup(link, 'html.parser'))

# 将修改后的 HTML 写回文件
with open(indexFilepath, 'w', encoding='utf-8') as file:
    file.write(str(soup))
