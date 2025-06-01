# -*- coding: utf-8 -*-
# GameNameListEditer2/MainGui.py
# GameNameListEditer2/MainGui.py
# ゲームタイトルのXMLファイルを選択して、名寄せ処理を行うGUIアプリケーション    
import xml
import PySimpleGUI as sg
from Dialog.XMLSelecterDialog import XMLSelecterDialog
from Process.XmlOutput import XMLOutput
from Parser import XMLParser1, XMLParser2



"""
【要件定義】

英数字・空白は半角に変換
xmlのパーサ
名寄せ処理

"""



#テーマカラーをsg.themeで設定
sg.theme('NeutralBlue') # 'Dark Brown'

#sg.Frameでフレームを定義
#フレーム1(中はからっぽ、フレームサイズだけ指定)
frame1 = sg.Frame('',
    [] , size=(500, 700) #幅,高さ
)

"""
#フレーム2(中はからっぽ、フレームサイズだけ指定)
frame2 = sg.Frame('',
    [] , size=(500, 700) #幅,高さ
)

value = sg.popup('OK Cancel')
if value == 'OK':
    sg.popup('OKが押されました')    
"""


#全体レイアウト
"""
レイアウトの中に記述する[]が「1行」を表している
今回はframe1と2を横に並べるので、同じ[]の中に記述する
"""
frame1 = [
    #以下[]で1行の扱いになる。カンマ区切りで横に部品を並べられる
    [
        sg.Text('日本語のゲームタイトルのXMLファイルを選択', key='XMLTEXT')
    ],
    [
        sg.Input(key='XMLPATH1', readonly=True), sg.Button('ボタン', key='XMLBTN1')
    ],
]

frame2 = [
    #以下[]で1行の扱いになる。カンマ区切りで横に部品を並べられる
    [
        sg.Text('XMLファイルを選択', key='XMLTEXT')
    ],
    [
        sg.Input(key='XMLPATH2', readonly=True), sg.Button('ボタン', key='XMLBTN2')
    ],
]

layout = [
    [
        sg.Frame('',frame1),
    ],
    [
        sg.Frame('',frame2),
    ],
    [
        sg.Button('置換実行', disabled=False, key='REPBTN'),
    ],
]

#GUIタイトルと全体レイアウトをのせたWindowを定義する。画面サイズは省略OK
#resizableでWindowサイズをマウスで変更できるようになる
window = sg.Window('', layout, resizable=False)
window.finalize()

#GUI表示実行部分
while True:
    # ウィンドウ表示
    event, values = window.read()

    #クローズボタンの処理
    if event in (sg.WIN_CLOSED, event is None):
        break
    
    elif event == 'XMLBTN1':
        instance = XMLSelecterDialog()
        path = instance.XMLSelecterDialog()        
        window['XMLPATH1'].Update(path)  # テキスト追記 # type: ignore 

    elif event == 'XMLBTN2':
        instance = XMLSelecterDialog()
        path = instance.XMLSelecterDialog()
        window['XMLPATH2'].Update(path)  # テキスト追記 # type: ignore

    elif event == 'REPBTN':
        xmlPath1 = values['XMLPATH1']
        xmlPath2 = values['XMLPATH2']

        instance1 = XMLParser1.XMLParser()
        xmlDic1 = instance1.XMLParser1(xmlPath1)
        
        instance2 = XMLParser2.XMLParser()
        xmlDic2 = instance2.XMLParser2(xmlPath2)
        
        # インスタンス生成
        instance3 = XMLOutput()
        instance3.GameListsOutput(xmlPath1, xmlDic1, xmlDic2)  # XML出力処理
        sg.popup('名寄せ処理が完了しました。')
        # sg.popup_scrolled('名寄せ処理が完了しました。')  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True)  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20))  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12))  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue')  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue', background_color='lightgray')  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue', background_color='lightgray', button_color=('white', 'blue'))  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue', background_color='lightgray', button_color=('white', 'blue'), title='名寄せ処理完了')  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue', background_color='lightgray', button_color=('white', 'blue'), title='名寄せ処理完了', auto_close=True, auto_close_duration=3)  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue', background_color='lightgray', button_color=('white', 'blue'), title='名寄せ処理完了', auto_close=True, auto_close_duration=3, grab_anywhere=True)  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue', background_color='lightgray', button_color=('white', 'blue'), title='名寄せ処理完了', auto_close=True, auto_close_duration=3, grab_anywhere=True, no_titlebar=True)  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue', background_color='lightgray', button_color=('white', 'blue'), title='名寄せ処理完了', auto_close=True, auto_close_duration=3, grab_anywhere=True, no_titlebar=True, modal=True)  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue', background_color='lightgray', button_color=('white', 'blue'), title='名寄せ処理完了', auto_close=True, auto_close_duration=3, grab_anywhere=True, no_titlebar=True, modal=True, use_default_focus=True)  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue', background_color='lightgray', button_color=('white', 'blue'), title='名寄せ処理完了', auto_close=True, auto_close_duration=3, grab_anywhere=True, no_titlebar=True, modal=True, use_default_focus=True, keep_on_top=True)  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue', background_color='lightgray', button_color=('white', 'blue'), title='名寄せ処理完了', auto_close=True, auto_close_duration=3, grab_anywhere=True, no_titlebar=True, modal=True, use_default_focus=True, keep_on_top=True, finalize=True)  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue', background_color='lightgray', button_color=('white', 'blue'), title='名寄せ処理完了', auto_close=True, auto_close_duration=3, grab_anywhere=True, no_titlebar=True, modal=True, use_default_focus=True, keep_on_top=True, finalize=True, visible=True)  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue', background_color='lightgray', button_color=('white', 'blue'), title='名寄せ処理完了', auto_close=True, auto_close_duration=3, grab_anywhere=True, no_titlebar=True, modal=True, use_default_focus=True, keep_on_top=True, finalize=True, visible=True, alpha_channel=0.8)  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue', background_color='lightgray', button_color=('white', 'blue'), title='名寄せ処理完了', auto_close=True, auto_close_duration=3, grab_anywhere=True, no_titlebar=True, modal=True, use_default_focus=True, keep_on_top=True, finalize=True, visible=True, alpha_channel=0.8, border_width=2)  # スクロール可能なポップアップ
        # sg.popup_scrolled('名寄せ処理が完了しました。', keep_on_top=True, size=(50, 20), font=('Helvetica', 12), text_color='blue', background_color='lightgray', button_color=('white', 'blue'), title='名寄せ処理完了', auto_close=True, auto_close_duration=3, grab_anywhere=True, no_titlebar=True, modal=True, use_default_focus=True, keep_on_top=True, finalize=True, visible=True, alpha_channel=0.8, border_width=2, element_padding=(10, 10))  # スクロール可能なポップアップ          
        
    window.refresh()                   # 画面更新

window.close()