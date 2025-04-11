#!/usr/bin/env python3
import re
import base64
import os

# 创建图片目录
os.makedirs('docs/images', exist_ok=True)

# 读取index.md文件
try:
    with open('docs/index.md', 'r', encoding='utf-8') as file:
        content = file.read()
except Exception as e:
    print(f"Error reading file: {e}")
    exit(1)

# 提取和替换base64图片
def extract_and_replace_images(content):
    # 查找所有base64编码的图片
    pattern = r'!\[(.*?)\]\(data:image/(.*?);base64,(.*?)\)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    count = 0
    for alt_text, img_type, base64_data in matches:
        count += 1
        # 创建图片文件名
        filename = f"image_{count}.{img_type}"
        filepath = f"docs/images/{filename}"
        
        try:
            # 解码并保存图片
            img_data = base64.b64decode(base64_data)
            with open(filepath, 'wb') as img_file:
                img_file.write(img_data)
            
            # 替换Markdown中的图片引用，使用相对路径
            old_img_tag = f'![{alt_text}](data:image/{img_type};base64,{base64_data})'
            new_img_tag = f'![{alt_text}](images/{filename})'
            content = content.replace(old_img_tag, new_img_tag)
            
            print(f"Extracted image {count} to {filepath}")
        except Exception as e:
            print(f"Error processing image {count}: {e}")
    
    return content

# 将文本链接转换为Markdown链接
def convert_text_links_to_clickable(content):
    # 查找形如https://...这样的链接文本
    pattern = r'(?<!\[)(?<!\()(https?://[^\s()<>]+)(?!\))(?!\])'
    
    # 替换为可点击的Markdown链接
    content = re.sub(pattern, r'[\1](\1)', content)
    
    return content

# 处理图片和链接
new_content = extract_and_replace_images(content)
new_content = convert_text_links_to_clickable(new_content)

# 修复已经存在的绝对路径引用
new_content = new_content.replace('](/images/', '](images/')

# 写入修改后的内容
try:
    with open('docs/index.md', 'w', encoding='utf-8') as file:
        file.write(new_content)
    print("Successfully updated index.md")
except Exception as e:
    print(f"Error writing to file: {e}")
    exit(1) 