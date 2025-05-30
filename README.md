# ProtobufCSV2XML CSV转XML弹幕工具
 
### 功能描述
本脚本基于Python 3.10，对使用Protobuf方式获取的.csv格式的Bilibili弹幕文件，提取指定用户弹幕，并转换为标准 XML 格式。

目前有两个版本:  
`ProtobufCSV2XML.py`通过 `midHash` 标识符指定目标用户弹幕并转化为标准 XML 格式。  
`ProtobufCSV2XML-no-target.py`不指定目标用户，直接将所有弹幕转化为标准 XML 格式。
