# ProtobufCSV2XML CSV转XML弹幕工具
项目本身无使用意义，需搭配另外两个工具使用（尚未完善）
## 更新计划
《幻想万华镜》补档工作现已结束，本项目将继续作为练手作继续练习开发、维护。

## 功能描述
本脚本基于Python 3.10，对使用Protobuf方式获取的.csv格式的Bilibili弹幕文件，提取指定用户弹幕，并转换为标准 XML 格式。

## 版本选择
### 合并后的新版本
`ProtobufCSV2XML-converter.py`：  
通过 `midHash` 标识符指定目标用户  
当变量`TARGET_USER_MIDHASH`留空时，默认转化全部弹幕为标准 XML 格式。
### 现已计划停止维护的两个版本:  
`ProtobufCSV2XML.py`：  
通过 `midHash` 标识符指定目标用户弹幕并转化为标准 XML 格式。  

`ProtobufCSV2XML-no-target.py`：  
不指定目标用户，直接将所有弹幕转化为标准 XML 格式。
