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