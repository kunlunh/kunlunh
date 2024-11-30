indexFilepath = '/home/runner/work/hklcv/hklcv/public/index.html'
# For generated CV Html Profile
with open(indexFilepath, 'r', encoding='utf-8') as file:
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
                print("Inserting".join(new_links)+'\n')
                lines.insert(j, '\n'.join(new_links) + '\n')
                break
        break

# write changes to index.html
with open(indexFilepath, 'w', encoding='utf-8') as file:
    print("Saving")
    file.writelines(lines)
