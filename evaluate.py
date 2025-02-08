import json

# 根据模型的最终输出评估F1值
def count_f1(file_path,column):
    total_true_entities = 0  # 所有真实实体的个数
    total_pred_entities = 0  # 所有预测实体的个数
    total_tp = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line.strip())

            # 解析真实标签和预测结果
            true_labels = data["labels"]
            pred_labels = data[column]

            mp = {}
            mp_cnt = {}

            # 统计真实实体的个数
            for label,entities in true_labels.items():
                for entity in entities:
                    mp[entity] = label
                    mp_cnt[entity] = mp_cnt.get(entity, 0) + 1
                total_true_entities += len(entities)

            # 统计预测实体的个数
            for label,entities in pred_labels.items():
                for entity in entities:
                    if entity in mp and mp[entity] == label:
                        total_tp += mp_cnt[entity]
                total_pred_entities += len(entities)
    print("Total true entities: {}".format(total_true_entities))
    print("Total pred entities: {}".format(total_pred_entities))
    print("Total TP entities: {}".format(total_tp))

    precision = total_tp / total_true_entities
    recall = total_tp / total_pred_entities
    f1 = 2 * precision * recall / (precision + recall)
    print("Precision: {}".format(precision))
    print("Recall: {}".format(recall))
    print("F1: {}".format(f1))
    return precision, recall, f1


def count_muti(file_path):
    for column in ["res_Qwen"]:
        pre,recall,f1 = count_f1(file_path,column)
        print("{}\t{}\t{}\t{}".format(column,pre,recall,f1))

if __name__ == '__main__':

    count_f1("result/Qwen.txt","res_Qwen")
