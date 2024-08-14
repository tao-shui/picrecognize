#导入需要使用的模块
from PIL import ImageChops, ImageStat,Image  
import os
from tkinter import filedialog
from tqdm import tqdm

print("程序加载中...")
print("1.启动（回车默认选择项）")
print("2.退出")
input1 = input("\n按回车键启动，输入2回车退出：")
select = 0
while input1!= "2":
    pic1 = filedialog.askopenfilename()
    if not os.path.exists(pic1):
        print("图片不存在！")
        input1 = input("回车键继续，输入2回车退出：")
        continue
    if not pic1.endswith(".png") and not pic1.endswith(".jpg") and not pic1.endswith(".jpeg"):
        print("图片格式不正确！")
        input1 = input("回车键继续，输入2回车退出：")
        continue
    filename = os.path.basename(pic1)
    select += 1
    print("第"+str(select)+"张图片")
    print("已选择图片"+" "+filename)
    dicrectory = filedialog.askdirectory()
    if not os.path.exists(dicrectory):
        print("目录不存在！")
        input1 = input("回车键继续，输入2回车退出：")
        continue
    filenum = len(os.listdir(dicrectory))
    if filenum == 0:
        print("目录下没有图片！")
        input1 = input("回车键继续，输入2回车退出：")
        continue
    files = os.listdir(dicrectory)
    print("文件夹路径"+" "+dicrectory)

    filenum = 0
    for file in os.listdir(dicrectory):
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            filenum += 1
    print("共"+str(filenum)+"张图片")
    filenum1 = 0
    print("\n图片寻找中...")
    foundup = 0
    
    #打开需要对比的图片
    pic1=Image.open(pic1)
    pbar = tqdm(total=filenum)
    for file in files:
        pbar.update()

        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            pic3=file
            #print("文件名为："+pic3)
            pic2=Image.open(dicrectory+"\\"+file)
            if pic1.mode!=pic2.mode:
                pic1=pic1.convert(pic2.mode)
                #print("转换颜色模式中...")
            if pic1.size!=pic2.size:
                pic1=pic1.resize(pic2.size)
                #print("调整图片大小中...")
    #将图片转换为灰度图像(彩色转黑白)，该步可以跳过，直接对比获取的差异平均值要比转化后的高
    #pic1_gray =pic1.convert('L')
    #pic2_gray =pic2.convert('L')
    #显示图片
    #pic1_gray.show()
    #计算两张图片的差异，返回每个像素的差异
    #diff = ImageChops.difference(pic1_gray,pic2_gray)
            diff = ImageChops.difference(pic1,pic2)
    #统计差异的统计信息，计算整个图像或图像的部分区域的统计数据
            stat = ImageStat.Stat(diff)
            filenum1 += 1
            
            #print("正在对比第"+str(filenum1)+"张图片...（共"+str(filenum)+"张）")
    #输出差异的平均值，值越大差异越大
            if stat.mean[0]<30:
                print("\n"+pic3+"\n近似度"+str((stat.mean[0]-100)*-1)+"%"+" ")
                print("找到啦！在这！\n"+dicrectory+"/"+file)
                foundup += 1
                input2 = input("\n按回车键继续找，输入1回车返回：")
                if input2 == "1":
                    break
    pbar.close()

    if filenum1 == filenum and foundup >= 1:
        print("\n抱歉没找到其他图片了，呜呜呜...\n")
    if filenum1 == filenum and foundup < 1:
        print("\n没找到，呜呜呜...૮₍ɵ̷﹏ɵ̷̥̥᷅₎ა\n")
            #pic2.show()
    #print(stat.mean[0])
    print("1.启动（回车默认选择项）")
    print("2.退出")
    input1 = input("\n按回车键启动，输入2回车退出：")
    continue
exit()