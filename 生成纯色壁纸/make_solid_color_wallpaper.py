import argparse
# import re
import random
from PIL import Image

colors = [
    {"name": "black", "rgb": (0, 0, 0)},
    {"name": "white", "rgb": (255, 255, 255)},
    {"name": "red", "rgb": (255, 0, 0)},
    {"name": "green", "rgb": (0, 255, 0)},
    {"name": "blue", "rgb": (0, 0, 255)},
    {"name": "yellow", "rgb": (255, 255, 0)},
    {"name": "orange", "rgb": (255, 165, 0)},
    {"name": "purple", "rgb": (128, 0, 128)},
    {"name": "pink", "rgb": (255, 192, 203)},
    {"name": "gray", "rgb": (128, 128, 128)},
    {"name": "brown", "rgb": (165, 42, 42)},
    {"name": "cyan", "rgb": (0, 255, 255)},
    {"name": "magenta", "rgb": (255, 0, 255)},
    {"name": "teal", "rgb": (0, 128, 128)},
    {"name": "navy", "rgb": (0, 0, 128)},
    {"name": "gold", "rgb": (255, 215, 0)},
    {"name": "silver", "rgb": (192, 192, 192)},
    {"name": "maroon", "rgb": (128, 0, 0)},
    {"name": "olive", "rgb": (128, 128, 0)},
    {"name": "lime", "rgb": (0, 128, 0)},
    {'name': '石榴', 'rgb': (242, 12, 0)},
    {'name': '炎色', 'rgb': (255, 51, 0)},
    {'name': '大红', 'rgb': (255, 33, 33)},
    {'name': '朱红', 'rgb': (255, 76, 0)},
    {'name': '朱砂', 'rgb': (255, 70, 31)},
    {'name': '丹砂', 'rgb': (255, 78, 32)},
    {'name': '品红', 'rgb': (240, 0, 86)},
    {'name': '橘红', 'rgb': (255, 117, 0)},
    {'name': '火红', 'rgb': (255, 45, 81)},
    {'name': '洋红', 'rgb': (255, 0, 151)},
    {'name': '酡红', 'rgb': (220, 48, 35)},
    {'name': '彤红', 'rgb': (243, 83, 54)},
    {'name': '橙黄', 'rgb': (255, 164, 0)},
    {'name': '妃红', 'rgb': (237, 87, 54)},
    {'name': '殷红', 'rgb': (190, 0, 47)},
    {'name': '朱膘', 'rgb': (243, 104, 56)},
    {'name': '杏红', 'rgb': (255, 140, 49)},
    {'name': '洋红', 'rgb': (255, 71, 119)},
    {'name': '橘黄', 'rgb': (255, 137, 54)},
    {'name': '赫赤', 'rgb': (201, 31, 55)},
    {'name': '银红', 'rgb': (240, 86, 84)},
    {'name': '赤色', 'rgb': (195, 39, 43)},
    {'name': '橙色', 'rgb': (250, 140, 53)},
    {'name': '绯红', 'rgb': (200, 60, 35)},
    {'name': '银朱', 'rgb': (191, 36, 42)},
    {'name': '枣红', 'rgb': (195, 33, 54)},
    {'name': '藤黄', 'rgb': (255, 182, 30)},
    {'name': '杏黄', 'rgb': (255, 166, 49)},
    {'name': '琥珀', 'rgb': (202, 105, 36)},
    {'name': '茜色', 'rgb': (203, 58, 86)},
    {'name': '樱桃', 'rgb': (201, 55, 86)},
    {'name': '雄黄', 'rgb': (233, 187, 29)},
    {'name': '酡颜', 'rgb': (249, 144, 111)},
    {'name': '棕红', 'rgb': (155, 68, 0)},
    {'name': '海棠', 'rgb': (219, 90, 107)},
    {'name': '雌黄', 'rgb': (255, 198, 75)},
    {'name': '棕黄', 'rgb': (174, 112, 0)},
    {'name': '桃红', 'rgb': (244, 121, 131)},
    {'name': '秋香', 'rgb': (217, 182, 17)},
    {'name': '缃色', 'rgb': (240, 194, 57)},
    {'name': '黄栌', 'rgb': (226, 156, 69)},
    {'name': '嫣红', 'rgb': (239, 122, 130)},
    {'name': '棕色', 'rgb': (178, 93, 37)},
    {'name': '赤金', 'rgb': (242, 190, 69)},
    {'name': '胭脂', 'rgb': (157, 41, 51)},
    {'name': '鹅黄', 'rgb': (255, 241, 67)},
    {'name': '茶色', 'rgb': (179, 92, 68)},
    {'name': '姜黄', 'rgb': (255, 199, 115)},
    {'name': '昏黄', 'rgb': (200, 155, 64)},
    {'name': '赭色', 'rgb': (156, 83, 51)},
    {'name': '棕黑', 'rgb': (124, 75, 0)},
    {'name': '粉红', 'rgb': (255, 179, 167)},
    {'name': '赭色', 'rgb': (149, 85, 57)},
    {'name': '檀色', 'rgb': (179, 109, 97)},
    {'name': '柳黄', 'rgb': (201, 221, 34)},
    {'name': '棕绿', 'rgb': (130, 113, 0)},
    {'name': '金色', 'rgb': (234, 205, 118)},
    {'name': '鸭黄', 'rgb': (250, 255, 114)},
    {'name': '樱草', 'rgb': (234, 255, 86)},
    {'name': '绛紫', 'rgb': (140, 67, 86)},
    {'name': '玄色', 'rgb': (98, 42, 29)},
    {'name': '嫩绿', 'rgb': (189, 221, 34)},
    {'name': '赭石', 'rgb': (132, 90, 51)},
    {'name': '栗色', 'rgb': (96, 40, 30)},
    {'name': '枯黄', 'rgb': (211, 177, 125)},
    {'name': '葱黄', 'rgb': (163, 217, 0)},
    {'name': '褐色', 'rgb': (110, 81, 30)},
    {'name': '秋色', 'rgb': (137, 108, 57)},
    {'name': '驼色', 'rgb': (168, 132, 98)},
    {'name': '葱绿', 'rgb': (158, 217, 0)},
    {'name': '柳绿', 'rgb': (175, 221, 34)},
    {'name': '紫棠', 'rgb': (86, 0, 79)},
    {'name': '绾色', 'rgb': (169, 129, 117)},
    {'name': '紫檀', 'rgb': (76, 34, 27)},
    {'name': '牙色', 'rgb': (238, 222, 176)},
    {'name': '紫酱', 'rgb': (129, 84, 99)},
    {'name': '酱紫', 'rgb': (129, 84, 118)},
    {'name': '黎色', 'rgb': (117, 102, 77)},
    {'name': '青莲', 'rgb': (128, 29, 174)},
    {'name': '荷色', 'rgb': (228, 198, 208)},
    {'name': '藕色', 'rgb': (237, 209, 216)},
    {'name': '缁色', 'rgb': (73, 49, 49)},
    {'name': '黧色', 'rgb': (93, 81, 60)},
    {'name': '白粉', 'rgb': (255, 242, 223)},
    {'name': '豆绿', 'rgb': (158, 208, 72)},
    {'name': '鱼白', 'rgb': (252, 239, 232)},
    {'name': '松花', 'rgb': (188, 230, 114)},
    {'name': '黝黑', 'rgb': (102, 87, 87)},
    {'name': '煤黑', 'rgb': (49, 37, 32)},
    {'name': '缟白', 'rgb': (242, 236, 222)},
    {'name': '紫色', 'rgb': (141, 75, 187)},
    {'name': '象牙', 'rgb': (255, 251, 240)},
    {'name': '丁香', 'rgb': (204, 164, 227)},
    {'name': '豆青', 'rgb': (150, 206, 84)},
    {'name': '黛紫', 'rgb': (87, 66, 102)},
    {'name': '乌色', 'rgb': (114, 94, 130)},
    {'name': '乌黑', 'rgb': (57, 47, 65)},
    {'name': '黑色', 'rgb': (0, 0, 0)},
    {'name': '白色', 'rgb': (255, 255, 255)},
    {'name': '灰色', 'rgb': (128, 128, 128)},
    {'name': '竹青', 'rgb': (120, 146, 98)},
    {'name': '荼白', 'rgb': (243, 249, 241)},
    {'name': '铅白', 'rgb': (240, 240, 244)},
    {'name': '银白', 'rgb': (233, 231, 239)},
    {'name': '漆黑', 'rgb': (22, 24, 35)},
    {'name': '玄青', 'rgb': (61, 59, 79)},
    {'name': '黝色', 'rgb': (107, 104, 130)},
    {'name': '黛螺', 'rgb': (74, 66, 102)},
    {'name': '霜色', 'rgb': (233, 241, 246)},
    {'name': '鸭卵', 'rgb': (224, 238, 232)},
    {'name': '鸦青', 'rgb': (66, 76, 80)},
    {'name': '花白', 'rgb': (194, 204, 208)},
    {'name': '素白', 'rgb': (224, 240, 233)},
    {'name': '雪白', 'rgb': (240, 252, 255)},
    {'name': '蟹青', 'rgb': (187, 205, 197)},
    {'name': '苍色', 'rgb': (117, 135, 138)},
    {'name': '雪青', 'rgb': (176, 164, 227)},
    {'name': '墨色', 'rgb': (80, 97, 109)},
    {'name': '月白', 'rgb': (214, 236, 240)},
    {'name': '莹白', 'rgb': (227, 249, 253)},
    {'name': '黯色', 'rgb': (65, 85, 93)},
    {'name': '黛蓝', 'rgb': (66, 80, 102)},
    {'name': '蓝灰', 'rgb': (161, 175, 201)},
    {'name': '藏蓝', 'rgb': (59, 46, 126)},
    {'name': '墨灰', 'rgb': (117, 138, 153)},
    {'name': '青白', 'rgb': (192, 235, 215)},
    {'name': '水色', 'rgb': (136, 173, 166)},
    {'name': '黛绿', 'rgb': (66, 102, 102)},
    {'name': '艾绿', 'rgb': (164, 226, 198)},
    {'name': '藏青', 'rgb': (46, 78, 126)},
    {'name': '铜绿', 'rgb': (84, 150, 136)},
    {'name': '石青', 'rgb': (123, 207, 166)},
    {'name': '绿沈', 'rgb': (12, 137, 24)},
    {'name': '宝蓝', 'rgb': (75, 92, 196)},
    {'name': '缥色', 'rgb': (127, 236, 173)},
    {'name': '群青', 'rgb': (76, 141, 174)},
    {'name': '绀紫', 'rgb': (0, 51, 113)},
    {'name': '花青', 'rgb': (0, 52, 114)},
    {'name': '松绿', 'rgb': (5, 119, 72)},
    {'name': '草绿', 'rgb': (64, 222, 90)},
    {'name': '靛蓝', 'rgb': (6, 82, 121)},
    {'name': '油绿', 'rgb': (0, 188, 18)},
    {'name': '石绿', 'rgb': (22, 169, 81)},
    {'name': '青葱', 'rgb': (10, 163, 68)},
    {'name': '青碧', 'rgb': (72, 192, 163)},
    {'name': '葱青', 'rgb': (14, 184, 58)},
    {'name': '柏绿', 'rgb': (33, 166, 117)},
    {'name': '绿色', 'rgb': (0, 229, 0)},
    {'name': '靛青', 'rgb': (23, 124, 176)},
    {'name': '石青', 'rgb': (22, 133, 169)},
    {'name': '蔚蓝', 'rgb': (112, 243, 255)},
    {'name': '翡翠', 'rgb': (61, 225, 173)},
    {'name': '碧绿', 'rgb': (42, 221, 156)},
    {'name': '玉色', 'rgb': (46, 223, 163)},
    {'name': '蓝色', 'rgb': (68, 206, 246)},
    {'name': '碧色', 'rgb': (27, 209, 165)},
    {'name': '碧蓝', 'rgb': (62, 237, 231)},
    {'name': '青翠', 'rgb': (0, 224, 121)},
    {'name': '青色', 'rgb': (0, 224, 158)}
    # 添加更多颜色及其RGB值... 
]


devices = [
    {"name": "iPhone12", "size": (1125, 2436)},
    {"name": "iPhone13", "size": (1170, 2532)},
    {"name": "iPhone13promax", "size": (1284, 2778)},
    {"name": "1080p", "size": (1920, 1080)},
    {"name": "2k", "size": (2560, 1440)},
    {"name": "4k", "size": (3840, 2160)},
    {"name": "5k", "size": (5120, 2880)},
    # 添加更多设备及其尺寸...
]

def get_device_size(device_name): 
    for device in devices:
        if device["name"] == device_name:
            return device["size"]
    
    return None  # 如果找不到对应设备的尺寸，返回None或其他适当的值

def get_color_rgba(color_name):
    for color in colors:
        if color["name"] == color_name:
            return color["rgb"] + (255,)  # 默认透明度为 255

    # 尝试解析 RGBA 值
    try:
        rgba = tuple(map(int, color_name.split(",")))
        if len(rgba) == 3:
            rgba += (255,)  # 默认透明度为 255
        return rgba
        rgba[3] = round(rgba[3] * 255)  # 将透明度转换为整数
    except ValueError:
        return None  # 无效的颜色值
    
def generate_wallpaper(label=None, size=None, color=None):
    if label:
        # 根据标签获取尺寸
        size = get_device_size(label)
    elif size is None:
        # 设置默认尺寸
        label = "4k"
        size = get_device_size(label)

    if color is None:
        print("无效的颜色值，从颜色列表中随机选择一个颜色作为默认颜色")
        color = get_color_rgba(random.choice(colors)["name"])
    else:
        # 根据颜色名称获取 RGBA 值
        color_rgba = get_color_rgba(color)
        if color_rgba:
            color = color_rgba
        else:
            print("无效的颜色值，从颜色列表中随机选择一个颜色作为默认颜色")
            color = get_color_rgba(random.choice(colors)["name"])
    

    # 创建纯色壁纸
    image = Image.new("RGBA", size, color)
    
    # 获取颜色的RGB值
    rgb = color[:3]
    # 获取颜色的透明度值
    alpha = color[3]
    # 将透明度转换为整数
    alpha_int = int(alpha)
    # 移除透明度为0的情况
    if alpha_int == 0:
        rgb_str = f"R_{rgb[0]}_G_{rgb[1]}_B_{rgb[2]}"
    else:
        rgb_str = f"R_{rgb[0]}_G_{rgb[1]}_B_{rgb[2]}_A_{alpha_int}"
    
    if label is None:
        label = ""

   # 获取颜色的名称
    color_name = ""
    for c in colors:
        if c["rgb"] == rgb:
            color_name = c["name"]
            break
    
    # 拼接文件名
    filename = f"wallpaper_{label}_{color_name}_{rgb_str}_{size[0]}x{size[1]}.png"
    # 保存图像文件
    image.save(filename)
    
    print(f"壁纸已生成并保存为 {filename}")
    

# 解析命令行参数
parser = argparse.ArgumentParser()
parser.add_argument("--label", help="设备标签")
parser.add_argument("--size", help="尺寸，格式为宽度x高度")
parser.add_argument("--color", help="颜色名称或RGBA值，格式为R,G,B,A")
args = parser.parse_args()


# 提取参数值
label = args.label
size = tuple(map(int, args.size.split("x"))) if args.size else None
color = args.color



# 生成壁纸
# generate_wallpaper(label=label, size=size, color=color)
size = (200, 163)
for color in colors:
    color_name = color["name"]
    generate_wallpaper(color=color_name,size=size)