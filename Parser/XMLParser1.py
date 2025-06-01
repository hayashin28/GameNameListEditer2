import xml.etree.ElementTree as xml
#         sg.Frame('フレーム1', frame1, key='FRAME1'),
#         sg.Frame('フレーム2', frame2, key='FRAME2')
#     ],
#     [ # sg.Button('実行', key='EXECUTE') ]
#     [ sg.Button('終了', key='EXIT') ] # sg.Button('実行', key='EXECUTE') ]
"""
# XMLParser1.py
# XMLファイルを解析して、ゲームタイトルとCRC32を辞書型で返すクラス
"""
# XMLParser1.py
# -*- coding: utf-8 -*-


class XMLParser:
    def __init__(self):   # インスタンス生成時に自動的に呼ばれるメソッド
        pass

    # xmlの解析
    def XMLParser1(self, xmlPath:str) -> dict[str, str]:
        tree = xml.parse(xmlPath)
        root = tree.getroot()

        xmlDic = {}
        for child in root:
            atrb:str = child.get('name')             # type: ignore
            for gran in child:
                for great in gran:
                    if great.tag != 'file':
                        continue
                    crc32:str = great.get('crc32')    # type: ignore
                    xmlDic[crc32.upper()] = atrb
                        
        return xmlDic
