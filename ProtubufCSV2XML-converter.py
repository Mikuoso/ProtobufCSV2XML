import csv
import xml.etree.ElementTree as ET
from pathlib import Path


# ——————————用户配置区——————————
INPUT_PATH = Path(r"C:\path\to\the\input_file.csv")    #输入路径（含输入文件名）
OUTPUT_PATH = Path(r"C:\path\to\the\output.xml")    #输出路径（含输出文件名）
TARGET_USER_MIDHASH = "abcd1234"    #指定用户midHash，留空则转换全部
# ————————————————————————————


def convert_appear_time(ms: str) -> str:
    """转换出现时间为秒（保留5位小数）"""
    return f"{float(ms) / 1000:.5f}"


def hex_to_decimal(hex_str: str) -> str:
    """颜色：十六进制转为十进制"""
    try:
        return str(int(hex_str.strip('#'), 16))
    except:
        return "16777215"   # B站默认弹幕颜色：白色


def progress_row(row, filter_target):
    """用户过滤逻辑：按midHash筛选，为空时不筛选"""
    if filter_target:
        current_midHash = row.get("用户MID哈希", "").strip()
        if current_midHash != filter_target:
            return False
    return True


def csv_to_xml(input_path: Path, output_path: Path, filter_target: str = None):
    """核心转换函数：CSV转换XML"""
    root = ET.Element("i")
    processed = 0   # 初始化处理弹幕数量

    with open(input_path, "r", encoding="utf-8-sig") as csvfile:
        lines = csvfile.readlines()

        # 定位标题行（如果存在说明行的情况下）
        try:
            header_line = next(i for i, line in enumerate(lines)
                               if "弹幕ID" in line and "出现时间(毫秒)" in line)
        except StopIteration:
            raise ValueError("CSV格式错误，未找到有效标题行")

        reader = csv.DictReader(lines[header_line:], delimiter=",")

        for row in reader:
            if not progress_row(row, filter_target):
                continue

            # 构建XML属性参数列表
            p_params = [
                convert_appear_time(row['出现时间(毫秒)']), # 出现时间（秒）
                row.get('模式', '1'), # 弹幕类型
                row.get('字体大小', '25'), # 字号
                hex_to_decimal(row.get('颜色', '#FFFFFF')), # 颜色十进制
                "ctime", # 保留字段
                row.get('弹幕池', '0'), # 弹幕池
                "midHash", # 保留字段
                "dmid", # 保留字段
                "weight" # row.get('权重', '0')  # 弹幕权重
            ]

            # 创建弹幕节点
            danmaku = ET.Element("d")
            danmaku.set("p", ",".join(p_params))
            danmaku.text = row['内容']  # 弹幕文本
            root.append(danmaku)
            processed += 1

    # 生成标准XML格式
    xml_str = ET.tostring(root, encoding='utf-8').decode()
    final_xml = f'<?xml version="1.0" encoding="UTF-8"?>\n{xml_str}'

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_xml)

    print(f"转化完成\n输入文件：{INPUT_PATH}\n输出文件：{OUTPUT_PATH}\n成功处理{processed}条弹幕")


if __name__ == "__main__":
    user_target = TARGET_USER_MIDHASH.strip() or None
    csv_to_xml(INPUT_PATH, OUTPUT_PATH, user_target)