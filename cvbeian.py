# For generated CV Html Profile
with open('public/resume/index.html', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Add the link
new_links = [
    '<a href="https://beian.miit.gov.cn/">粤ICP备13053581号-5</a>',
    '<a href="http://www.beian.gov.cn/portal/recordQuery">粤公网安备 44070302000613号</a>'
]

# before last line
for i in range(len(lines)):
    if '<div class="footer">' in lines[i]:
        # in footer end
        for j in range(i, len(lines)):
            if '</div>' in lines[j]:
                # before footer
                lines.insert(j, '\n'.join(new_links) + '\n')
                break
        break

# write changes to index.html
with open('public/resume/index.html', 'w', encoding='utf-8') as file:
    file.writelines(lines)
