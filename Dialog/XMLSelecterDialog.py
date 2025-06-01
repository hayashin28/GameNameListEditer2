import PySimpleGUI as sg

class XMLSelecterDialog:
    
    def __init__(self):   # インスタンス生成時に自動的に呼ばれるメソッド
        pass
    
    def XMLSelecterDialog(self) -> str:
        path = str( sg.popup_get_file('ファイルを選択してください', file_types=(('XMLファイル', '.xml'),)) )
        return path