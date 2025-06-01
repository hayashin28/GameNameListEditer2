# -*- coding: utf-8 -*-
from xml.dom import minidom
import xml.etree.ElementTree as ET
import os




class XMLOutput:
    
    def __init__(self):   # インスタンス生成時に自動的に呼ばれるメソッド
        pass


    def GameListsOutput(self, XmlPath:str, xmlDic1:dict, xmlDic2:dict):
        # XMLデータをファイルに書き込み
        #with open(XmlPath + 'gamelists.xml', 'w', encoding='utf-8') as file:

        # XMLのルート要素を作成
        root = ET.Element('gamelist')
        
        for key in xmlDic2:
            
            # items['label']がxmlDic1のキーに存在する場合
            # ここでxmlDic1のキーとitems['label']を比較して、存在する場合の処理を行う
            # items['label']がxmlDic1のキーに存在
            # items['label']がxmlDic1のキーに存在する場合
            if key in xmlDic1:
                # 子要素を作成
                child = ET.SubElement(root,'game')            # 子要素に属性を追加
                # 孫要素を作成するか確認
                grand = ET.SubElement(child,'path')
                grand.text = './' + xmlDic1[key] + '.zip'  # 孫要素にテキストを追加
                grand = ET.SubElement(child,'name')
                grand.text = xmlDic2[key]
                grand = ET.SubElement(child,'playcount')
                grand.text = '1'
                grand = ET.SubElement(child,'lastplayed')
                grand.text = '20250524T200507'


        # インデントを付けて保存
        dir_path = os.path.dirname(XmlPath)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        doc = minidom.parseString(ET.tostring(root, 'utf-8'))
        output_path = os.path.join(dir_path, 'gamelist.xml') if dir_path else XmlPath
        with open(output_path, 'w', encoding='utf-8') as f:
            doc.writexml(f, encoding='utf-8', newl='\n', indent='', addindent='  ')
        # print('XMLファイルを出力しました。')