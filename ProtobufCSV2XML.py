import csv
import xml.etree.ElementTree as ET

target_user = "cbeb07c9"  # 要提取的目标用户midHash

def convert_appear_time(ms):
    return f"{float(ms)/1000:.5f}"

def hex_to_decimal(hex_str):
    try:
        return str(int(hex_str.strip('#'), 16))
    except:
        return "16777215"

def csv_to_xml(csv_path, xml_path, target_user):
    root = ET.Element("i")

    with open(csv_path, "r", encoding="utf-8-sig") as csv_file:
        lines = csv_file.readlines()
        header_line = None
        for i, line in enumerate(lines):
            if "弹幕ID" in line and "出现时间(毫秒)" in line:
                header_line = i
                break

        reader = csv.DictReader(lines[header_line:], delimiter=',')

        for row in reader:
            # 检查用户midHash是否匹配
            if row.get('用户MID哈希', '').strip() != target_user:
                continue  # 跳过非目标用户

            # 仅处理目标用户的弹幕
            p_params = [
                convert_appear_time(row['出现时间(毫秒)']),
                row['模式'],
                row['字体大小'],
                hex_to_decimal(row['颜色']),
                "ctime",
                row['弹幕池'],
                "midHash",
                "dmid",
                "weight"
            ]
            danmaku = ET.Element("d")
            danmaku.set("p", ",".join(p_params))
            danmaku.text = row['内容']
            root.append(danmaku)

    # 生成XML（若未找到用户则生成空文件）
    xml_str = ET.tostring(root, encoding='utf-8').decode()
    final_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
{xml_str}'''

    with open(xml_path, 'w', encoding='utf-8') as f:
        f.write(final_xml)

csv_to_xml("input.csv", f"user_{target_user}.xml", target_user)
