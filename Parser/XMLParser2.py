from types import coroutine
import xml.etree.ElementTree as xml
#         sg.Frame('フレーム1', frame1, key='FRAME1'),
#         sg.Frame('フレーム2', frame2, key='FRAME2')
#     ],    
#     [ # sg.Button('実行', key='EXECUTE') ]
#     [ sg.Button('終了', key='EXIT') ] # sg.Button('実行', key='EXECUTE') ]
"""
# XMLParser2.py
# XMLファイルを解析して、ゲームタイトルとCRC32を辞書型で返すクラス
"""
# XMLParser2.py
# -*- coding: utf-8 -*-



class XMLParser:
    def __init__(self):   # インスタンス生成時に自動的に呼ばれるメソッド
        pass

    # xmlの解析
    def XMLParser2(self, xmlPath: str) -> dict[str, str]:
        # XMLファイルを明示的にutf-8で開いて内容を読み込む
        with open(xmlPath, encoding="utf-8") as f:
            xml_content = f.read()
        root = xml.fromstring(xml_content)
        xmlDic = {}
        for child in root:
            if child.tag != 'games':
                continue
            for gran in child:
                if gran.tag != 'game':
                    continue
                for great in gran:
                    if great.tag == 'title':
                        atrb = great.text
                    for yashago in great:
                        if yashago.tag == 'romCRC':
                            romCrc:str = str(yashago.text)
                            # xmlDicにゲームタイトルとCRC32を格納して返す
                            xmlDic[romCrc.lower()] = atrb

        # 解析した結果を辞書型で返す
        return xmlDic
