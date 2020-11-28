from tkinter import * 

# ウインドウを作成

win = Tk()

# 描画のためのキャンパスを作成

cv = Canvas(win, width = 400, height = 300)

cv.pack()

for i in range(19):
    y = i * 20
    cv.create_line(0, y, 380, y, fill="black", width=2)

    x = i * 20
    cv.create_line(x, 0, x, 380, fill="black", width=2)


win.mainloop()