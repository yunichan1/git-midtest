import tkinter as tk

# 1. 메인 윈도우(창) 생성
window = tk.Tk()

# 2. 창의 제목 설정
window.title("제목 없음 - 메모장")

# 3. 창의 초기 크기 설정 (가로x세로)
window.geometry("800x600")

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