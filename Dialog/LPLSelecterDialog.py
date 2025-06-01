import PySimpleGUI as sg

class LPLSelecterDialog:
    
    def __init__(self):   # インスタンス生成時に自動的に呼ばれるメソッド
        pass
    
    def LPLSelecterDialog(self) -> str:
        path = str( sg.popup_get_file('ファイルを選択してください', file_types=(('LPLファイル', '.lpl'),)) )
        return path