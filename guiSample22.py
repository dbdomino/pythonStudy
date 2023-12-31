from tkinter import *

root = Tk() # root를 통해 Tk()를 선언해준다.
root.title("GUI test Title") # 제목을 선언
root.geometry("440x350+200+200") # "가로 x 세로 + x좌표 + y좌표"

root.resizable(True, False) #True 허용, 참 False 비허용, 거짓

#-------------------------------------
# 체크박스, 여러 선택지를 원하는만큼 선택가능
# variable을 넣어서 체크 박스 선택 유무 값을 저장해 줘야 함.
checkbox01value = IntVar()
checkbox02value = IntVar()
checkbox01 = Checkbutton(root, text="오늘 하루 그만 보기", variable=checkbox01value)
checkbox01.pack()

checkbox02 = Checkbutton(root, text="1주일 동안 그만 보기")
checkbox02.deselect()
#checkbox02.select()
checkbox02.pack()

def value_checkbox():
    #print("체스박스선택 = ",checkbox01value) # PY_VAR0
    print("오늘 하루 그만 보기 = ", checkbox01value.get()) # 0 비선택, 1 선택

button01 = Button(root, text="checkbox01value", command=value_checkbox) #값 삭제
button01.pack()

# 라디오 버튼, 여러 선택지 중 하나만 선택가능 
radio_var = IntVar() # 여기에 라디오버튼 값 저장
button_burger01 = Radiobutton(root, text="데리버거", value=1, variable=radio_var)
button_burger02 = Radiobutton(root, text="치킨버거", value=2, variable=radio_var)
button_burger03 = Radiobutton(root, text="새우버거", value=3, variable=radio_var)
button_burger04 = Radiobutton(root, text="불고기버거", value=5, variable=radio_var)
button_burger05 = Radiobutton(root, text="라이스버거", value=7, variable=radio_var)
button_burger01.pack()
button_burger02.pack()
button_burger03.pack()
button_burger04.pack()
button_burger05.pack()

def print_radio():
    #print("라디오 버튼 선택 = ",radio_var) # PY_VAR0
    print("주문한 값 = ", radio_var.get()) # 0 비선택, 1 선택
button02 = Button(root, text="주문하기", command=print_radio) #값 삭제
button02.pack()

root.mainloop() # 루트에 메인 루프 선언, 루프가 작동되면서 Tk()로 선언된 gui 화면이 동작시작
