from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import random
from PIL import Image, ImageTk

# ウィンドウ
win = Tk()
win.title('☆ミニじゃんけんゲーム☆')
win.geometry('400x400')
# win.attributes('-topmost', True)
win.focus_set()
#フレーム
main_frame = Frame(
            win,
            bd = 3,
            relief="ridge", 
            )
main_frame.pack(pady = 30)
frame = Frame(main_frame)
frame.pack(padx = 25)
#テキストラベル
my_label = Label(frame, text = 'じゃんけんの手を選んでください')
my_label.pack(pady = 5)
# Image
janken_image = ImageTk.PhotoImage(file='janken_boys.png')
image_label = Label(main_frame, image = janken_image)
image_label.pack()

#OKがクリックされたときの挙動
def ok_click():
    hands = ['グー', 'チョキ', 'パー']
    hand_var = var.get()
    hand = hands[hand_var]
    computer_hand = random.randint(0, 2)
    c_hand = hands[computer_hand]
    #勝敗判定
    def judge(player, computer):
        if player == computer:
            return '引き分け'
        elif player == 0 and computer == 1:
            return '勝ち'
        elif player == 1 and computer == 2:
            return '勝ち'
        elif player == 2 and computer == 0:
            return '勝ち'
        else:
            return '負け'
    result = judge(hand_var, computer_hand)
    mb.showinfo('結果', f'あなたは{hand}を出しました。\n'
                f'何某くんは{c_hand}を出しました。\n'
                f'勝負の結果は{result}です')


# チェック判定用変数
var = IntVar()
# ラジオボタン初期選択
var.set(0)
# ラジオボタンの生成(frameに属する)
radio_1 = Radiobutton(frame, text='ぐー', value=0, variable=var).pack(side = LEFT)
radio_2 = Radiobutton(frame, text='ちょき', value=1, variable=var).pack(side = LEFT)
radio_3 = Radiobutton(frame, text='ぱー', value=2, variable=var).pack(side = LEFT)
#OKボタンを生成(main_frameに属する)
okButton = Button(main_frame, text = 'じゃーんけーんポンッ', command=ok_click)
okButton.pack(side = BOTTOM, pady = 5)
win.mainloop()
