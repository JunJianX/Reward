import time
import threading
from PIL import Image
import tkinter as tk  # 导入 tk库 模块
import random  # 导入 随机库 模块
from socket import *
address ='106.13.93.74'
port =8080
buffsize =1024

chance = 0

root = tk.Tk()  # 初始化Tk() 建立一个窗口
root.title('抽奖')  # 设置标题
root.minsize(1024, 755)

photo = tk.PhotoImage(file="4.png")  # file：图片路径
imgLabel = tk.Label(root, image=photo)  # 把图片整合到标签类中
imgLabel.pack(side=tk.RIGHT)  # 右对齐

label1 = tk.Label(root, text='一起看综艺看到爽', bg='yellow', font=('Arial', 15))
label1.place(x=0, y=0, width=256, height=180)

label2 = tk.Label(root, text='追剧10集', bg='yellow', font=('Arial', 30))
label2.place(x=256, y=0, width=256, height=180)

label3 = tk.Label(root, text='一秒来道歉', bg='yellow', font=('Arial', 30))
label3.place(x=512, y=0, width=256, height=180)

label4 = tk.Label(root, text='做好吃的', bg='yellow', font=('Arial', 30))
label4.place(x=768, y=0, width=256, height=180)

label5 = tk.Label(root, text='罚款50元', bg='yellow', font=('Arial', 30))
label5.place(x=0, y=574, width=256, height=180)

label6 = tk.Label(root, text='偷偷买购物车里的一件东西', bg='yellow', font=('Arial', 15))
label6.place(x=256, y=574, width=256, height=180)

label7 = tk.Label(root, text='打扫卫生干净版', bg='yellow', font=('Arial', 15))
label7.place(x=512, y=574, width=256, height=180)

label8 = tk.Label(root, text='马上按摩', bg='yellow', font=('Arial', 30))
label8.place(x=768, y=574, width=256, height=180)

# label9 = tk.Label(root, text='51核心板', bg='yellow', font=('Arial', 50))
# label9.place(x=780, y=600, width=256, height=180)



# 将所有抽奖选项添加到列表
things = [label1, label2, label3, label4, label5, label6, label7, label8]
# 获取列表的最大索引值
maxvalue = len(things) - 1

# 设置起始值为随机整数
starts = random.randint(0, 6)
# 是否停止标志
notround = False

url = address + ':' + str(8080)
url_result = tk.StringVar(value=url)

cdk = tk.StringVar(value="请输入密码")
# 定义滚动函数
def round():
    global chance
    s = socket(AF_INET, SOCK_STREAM)
    print(address)
    print(port)
    s.connect((address, port))
    s.send(t2.get().encode())

    while True:
       revdata=s.recv(buffsize).decode('utf-8')
       if(len(revdata)==1):
           print(1)
           chance +=1
           break
    s.close()
    if(chance!=0):
        t = threading.Thread(target=startup)  # 启动start
        chance=chance-1
        t.start()
    else:
        print("没有机会啦~")


# 定义开始函数
def startup():
    global starts
    global notround
    while True:
        # 检测停止按钮是否被按下
        if notround == True:
            notround = False
            return starts
        # 程序延时
        time.sleep(0.017)

        # 在所有抽奖选项中循环滚动
        for i in things:
            i['bg'] = 'lightSkyBlue'  # 开始时 底色变成天蓝
        things[starts]['bg'] = 'red'  # 滚动框为 红色
        starts += 1
        if starts > maxvalue:
            starts = 0


# 定义停止函数
def stops():
    global notround  # notround 为全局变量
    global starts

    notround = True  # 停止标志位
    if starts == 1:  # 如果抽中“简易四轴”就跳转为“谢谢惠顾”【奸商^_^】
        starts = 2



# 设置启动按键      背景文本为“RUN”  底色为“天蓝”    字体“Arial” 字体大小“50”   回调函数command 为【滚动函数】
btn1 = tk.Button(root, text='RUN', bg='lightSkyBlue', font=('Arial', 30), command=round)
# 设置按键坐标
btn1.place(x=400, y=494, width=120, height=70)
# 设置停止按键      背景文本为“RUN”  底色为“红色”    字体“Arial” 字体大小“50”   回调函数command 为【停止函数】
btn2 = tk.Button(root, text='STOP', bg='red', font=('Arial', 30), command=stops)
# 设置按键坐标
btn2.place(x=656, y=494, width=120, height=70)


t1 = tk.Entry(root,textvariable =url_result)
t1.place(x = 270,y=220,width=450,height = 30)

t2 = tk.Entry(root,textvariable = cdk)
t2.place(x = 270,y=300,width=450,height = 30)
# 循环，时刻刷新窗口
root.mainloop()




