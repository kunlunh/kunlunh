#!/bin/bash

indexFilepath="/home/runner/work/hklcv/hklcv/public/index.html"

# 创建临时文件
temp_file=$(mktemp)

# 读取文件并处理
while IFS= read -r line || [[ -n "$line" ]]; do
    echo "$line" >> "$temp_file"
    if [[ "$line" == *"<div class=\"footer\">"* ]]; then
        in_footer=true
        footer_content=""
        while IFS= read -r footer_line || [[ -n "$footer_line" ]]; do
            if [[ "$footer_line" == *"</div>"* ]]; then
                echo '<a href="https://beian.miit.gov.cn/">粤ICP备13053581号-5</a>' >> "$temp_file"
                echo '<a href="http://www.beian.gov.cn/portal/recordQuery">粤公网安备 44070302000613号</a>' >> "$temp_file"
                echo "$footer_line" >> "$temp_file"
                break
            fi
            echo "$footer_line" >> "$temp_file"
        done
    fi
done < "$indexFilepath"

# 将临时文件移回原文件
mv "$temp_file" "$indexFilepath"
