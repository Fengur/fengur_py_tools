# 纯色壁纸生成器

## 项目描述

为一些喜欢纯色壁纸的同学提供（因本人比较需要）的一个python3脚本，它可以生成指定尺寸和颜色的纯色壁纸。你可以通过命令行参数来指定壁纸的设备标签、尺寸和颜色。

## 使用方法

1. 首先，确保你的系统中已经安装了python3和PIL库。如果没有，你可以使用以下命令来安装：

```
pip3 install pillow
```
2.运行脚本，你可以使用以下命令来生成一个壁纸：
```
python3 generate_wallpaper.py --label iPhone12 --color red
```
这将会生成一个尺寸为iPhone12的红色壁纸。
你也可以使用--size参数来指定壁纸的尺寸，例如：
```
python3 generate_wallpaper.py --size 1920x1080 --color green
```
这将会生成一个尺寸为1920x1080的绿色壁纸。

--color参数可以接受颜色名称或RGBA值，例如：
```
python3 generate_wallpaper.py --label iPhone13 --color 255,0,0
```
这将会生成一个尺寸为iPhone13的红色壁纸。

3.如果你需要查看所有的命令行参数以及它们的帮助信息，你可以使用--help选项：
```
python3 generate_wallpaper.py --help
```
## 注意事项
- 如果你没有指定--label或--size参数，脚本将会使用默认的尺寸（4k）。
- 如果你没有指定--color参数，或者提供了无效的颜色值，脚本将会从预定义的颜色列表中随机选择一个颜色。
## 更多信息
- 一些生成好的[纯色图片示例](./example_color_images/readme.md)
- examples中的图片对应RGB已经预置在脚本文件内的list中，按需自取即可
## 项目维护者
fengur@qq.com
