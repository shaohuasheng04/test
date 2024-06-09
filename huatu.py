import re

# 提取文件中的 IoU、Recall、Precision、F1-score、Inference Time
def extract_metrics_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # 使用正则表达式提取 IoU、Recall、Precision、F1-score、Inference Time
    iou_values = re.findall(r'Avg.\s+IoU\s+=\s+([\d.]+)', content)
    recall_values = re.findall(r'Avg.\s+Recall\s+=\s+([\d.]+)', content)
    precision_values = re.findall(r'Avg.\s+Precision\s+=\s+([\d.]+)', content)
    f1_score_values = re.findall(r'Avg.\s+F1-score\s+=\s+([\d.]+)', content)
    inference_time_value = re.findall(r'Inference\s+Time\s+=\s+([\d.]+)', content)

    return iou_values, recall_values, precision_values, f1_score_values, inference_time_value

# 保存指标到文件
def save_metrics_to_file(metrics_values, output_file):
    with open(output_file, 'w') as file:
        for metric in metrics_values:
            file.write(f"{metric}\n")

# 处理文件
def process_file(input_file_path, output_file):
    # 从输入文件中提取指标
    iou_values, recall_values, precision_values, f1_score_values, inference_time_value = extract_metrics_from_file(input_file_path)

    # 将指标保存到输出文件中
    output_file = output_file + ".txt"  # 添加文件扩展名
    save_metrics_to_file(iou_values, output_file.replace('.txt', '.IoU.txt'))
    save_metrics_to_file(recall_values, output_file.replace('.txt', '.Recall.txt'))
    save_metrics_to_file(precision_values, output_file.replace('.txt', '.Precision.txt'))
    save_metrics_to_file(f1_score_values, output_file.replace('.txt', '.F1-score.txt'))
    save_metrics_to_file(inference_time_value, output_file.replace('.txt', '.Inference Time.txt'))

if __name__ == "__main__":
    input_file_path = "dsfd.txt"  # 输入文件的路径
    output_file = "dsfd" # 输出文件的路径

    process_file(input_file_path, output_file)