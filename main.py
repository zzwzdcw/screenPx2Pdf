import tkinter
import keyboard
import os
import shutil
from PIL import ImageGrab, Image


distPath = "./img/"
print("按下D键进行全屏截图")
print("按下O键把截图组装成PDF")
if os.path.exists(distPath):
    print("img存在，清空img文件夹")
    shutil.rmtree("img")
    os.mkdir("img")
else:
    print("img文件夹不存在，创建文件夹")
    os.mkdir("img")
# 获取当前分辨率下的屏幕尺寸
win = tkinter.Tk()
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
total = 0


def print_screen():
    global total
    global distPath
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    # 保存截图i
    filename = distPath + str(total) + ".jpg"
    total += 1
    img.save(filename)
    print("截图文件保存到：" + filename)


def package_img():
    print("正在组装pdf")
    global distPath
    global total
    # 创建一个空列表，用来存放图片对象
    images = []
    # 循环total次，打开total个jpg图片
    for i in range(total):
        # 打开第i个图片，f字符串可以插入变量
        image = Image.open(f"./img/{i}.jpg")
        # 把图片转换为RGB模式，以便于合并
        image = image.convert("RGB")
        # 把图片对象添加到列表中
        images.append(image)
    # 指定输出的pdf文件路径
    pdf_path = "output.pdf"
    # 把列表中的图片对象合并输出为一个pdf文件
    images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
    print("组装完成，pdf位置" + pdf_path)


if __name__ == '__main__':
    keyboard.add_hotkey('d', print_screen)
    keyboard.add_hotkey('o', package_img)
    keyboard.wait()