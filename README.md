# ProtobufCSV2XML CSV转XML弹幕工具
**注**：该项目已完成与[BiliDMProtobufDownloader](https://github.com/Mikuoso/BiliDMProtobufDownloader)的合并工作！本项目现已停止维护，请移步至[BiliDanmakuDownloader](https://github.com/Mikuoso/BiliDanmakuDownloader)！  

项目本身无使用意义，需搭配另外两个工具使用  
分别是[BiliDMProtobufDownloader](https://github.com/Mikuoso/BiliDMProtobufDownloader)与[BiliDanmakuDiff](https://github.com/Mikuoso/BiliDanmakuDiff)

## 功能描述
本脚本基于Python 3.10，对使用Protobuf方式获取的.csv格式的Bilibili弹幕文件，提取指定用户弹幕，并转换为标准 XML 格式。

## 🎯 功能特性
- **精准格式转换**：毫秒转秒/十六进制颜色转十进制
- **用户过滤**：支持按midHash筛选特定用户弹幕
- **兼容处理**：自动处理异常数据格式
## ⚙️ 配置说明
编辑脚本开头的用户配置区：
```python
INPUT_PATH = Path(r"C:\input.csv")    # 输入CSV路径
OUTPUT_PATH = Path(r"C:\output.xml")  # 输出XML路径
TARGET_USER_MIDHASH = "abcd1234"      # 指定用户midHash(留空则转换全部)
```

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

## 更新计划
本项目最初是为《【高清修复】东方幻想万华镜全集》补档工作而设计，现已与[BiliDMProtobufDownloader](https://github.com/Mikuoso/BiliDMProtobufDownloader)合并为[BiliDanmakuDownloader](https://github.com/Mikuoso/BiliDanmakuDownloader)，现决定停止维护。