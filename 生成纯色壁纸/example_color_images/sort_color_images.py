import os

# 获取当前目录下的所有文件
files = os.listdir('.')

# 筛选出图片文件
image_extensions = ['.jpg', '.png', '.gif', '.bmp']
image_files = [f for f in files if any(f.endswith(ext) for ext in image_extensions)]

# 生成Markdown语句
for image_file in image_files:
    # 获取不带扩展名的文件名
    image_name = os.path.splitext(image_file)[0]
    print(f'## {image_name}\n')
    print(f'![{image_file}](./{image_file})\n')