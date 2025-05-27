import csv
import xml.etree.ElementTree as ET


def convert_appear_time(ms):
    """转换出现时间为秒（保留5位小数）"""
    return f"{float(ms) / 1000:.5f}"


def hex_to_decimal(hex_str):
    """将颜色十六进制转为十进制"""
    try:
        return str(int(hex_str.strip('#'), 16))
    except:
        return "16777215"  # 默认白色


def csv_to_xml(csv_path, xml_path):
    """将CSV转换为B站标准XML格式"""
    root = ET.Element("i")

    with open(csv_path, "r", encoding="utf-8-sig") as csv_file:
        lines = csv_file.readlines()
        # 自动定位标题行
        header_line = next(i for i, line in enumerate(lines) if "弹幕ID" in line and "出现时间(毫秒)" in line)
        reader = csv.DictReader(lines[header_line:], delimiter=',')

        for row in reader:
            # 构造p参数（无需过滤用户）
            p_params = [
                convert_appear_time(row['出现时间(毫秒)']),  # 出现时间（秒）
                row.get('模式', '1'),  # 弹幕类型
                row.get('字体大小', '25'),  # 字号
                hex_to_decimal(row.get('颜色', '#FFFFFF')),  # 颜色十进制
                "ctime",  # 保留字段（原数据可能没有）
                row.get('弹幕池', '0'),  # 弹幕池
                "midHash",  # 保留字段
                "dmid",  # 保留字段
                "weight" #row.get('权重', '0')  # 弹幕权重
            ]

            # 创建弹幕节点
            danmaku = ET.Element("d")
            danmaku.set("p", ",".join(p_params))
            danmaku.text = row['内容']  # 弹幕文本
            root.append(danmaku)

    # 生成XML结构
    xml_str = ET.tostring(root, encoding='utf-8').decode()
    final_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
{xml_str}'''

    with open(xml_path, 'w', encoding='utf-8') as f:
        f.write(final_xml)


# 使用示例（自动处理所有用户）
csv_to_xml("input-no.csv", "all_danmaku.xml")  # 输入输出路径可自定义
