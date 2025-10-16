import tkinter as tk
from tkinter import filedialog
import os

# --- Functions for menu commands ---

# 현재 열려있는 파일 경로를 저장하기 위한 변수
file_path = None

def new_file():
    """새 파일을 위해 텍스트 영역을 비웁니다."""
    global file_path
    text_area.delete(1.0, tk.END)
    window.title("제목 없음 - 메모장")
    file_path = None

def open_file():
    """파일을 열고 내용을 표시합니다."""
    global file_path
    path = filedialog.askopenfilename(
        filetypes=[("텍스트 문서", "*.txt"), ("모든 파일", "*.*")]
    )
    if not path:
        return
    
    with open(path, 'r', encoding='utf-8') as file:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, file.read())
    
    file_path = path
    window.title(f"{os.path.basename(path)} - 메모장")

def save_file():
    """현재 파일을 저장합니다. 새 파일이면 다른 이름으로 저장을 호출합니다."""
    global file_path
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text_area.get(1.0, tk.END))
        except Exception as e:
            print(f"Error saving file: {e}") # 오류 처리
    else:
        save_as_file()

def save_as_file():
    """새 이름으로 파일을 저장합니다."""
    global file_path
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("텍스트 문서", "*.txt"), ("모든 파일", "*.*")]
    )
    if not path:
        return

    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(text_area.get(1.0, tk.END))
        file_path = path
        window.title(f"{os.path.basename(path)} - 메모장")
    except Exception as e:
        print(f"Error saving file: {e}") # 오류 처리

# 1. 메인 윈도우(창) 생성
window = tk.Tk()

# 2. 창의 제목 설정
window.title("제목 없음 - 메모장")

# 3. 창의 초기 크기 설정 (가로x세로)
window.geometry("800x600")

# --- 메뉴 바 생성 ---
menu_bar = tk.Menu(window)

# 파일 메뉴 생성
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="새로 만들기", command=new_file)
file_menu.add_command(label="열기...", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_command(label="다른 이름으로 저장...", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="종료", command=window.quit)

# 메뉴 바에 파일 메뉴 추가
menu_bar.add_cascade(label="파일", menu=file_menu)

# 윈도우에 메뉴 바 설정
window.config(menu=menu_bar)
# --- 메뉴 바 생성 끝 ---

# 4. 여러 줄의 텍스트를 입력받을 수 있는 Text 위젯 생성
#    - window: 이 위젯이 속할 부모 창
#    - wrap='word': 단어 단위로 자동 줄 바꿈
text_area = tk.Text(window, wrap='word')

# 5. Text 위젯을 창에 배치하고, 창 크기가 변경될 때 함께 크기가 조절되도록 설정
#    - expand=True: 남는 공간을 모두 차지하도록 확장
#    - fill='both': 가로, 세로 방향으로 위젯을 꽉 채움
text_area.pack(expand=True, fill='both')

# 6. 창이 화면에 나타나고 사용자 입력을 받을 수 있도록 대기
window.mainloop()