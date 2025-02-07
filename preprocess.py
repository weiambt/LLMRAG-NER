import json

# 需要将bio数据处理成json数据,如下所示
# {"text": "中国有ABC公司", "label": {"ORG": ["中国", "ABC公司"], "PER": [], }}

def bio_to_json(bio_data):
    """
    将 BIO 格式的数据转换为 JSON 格式。

    参数:
    bio_data (str): 包含 BIO 标注的文本数据，每行格式为 '词语 标签'，句子之间用空行分隔。

    返回:
    list: 包含转换后 JSON 数据的列表，每个元素是一个字典，包含 'text' 和 'label'。
    """
    sentences = bio_data.strip().split('\n\n')
    result = []

    for sentence in sentences:
        # 为了处理最后一个实体，所以多加一个无意义字符
        sentence += "\n- O"
        words = []
        labels = []
        entities = {}

        last_entity = []
        last_entity_type = ""

        for line in sentence.split('\n'):
            word, label = line.split()
            words.append(word)

            labels.append(label)

            if label == 'O' or label.startswith('B-'):
                if len(last_entity) > 0:
                    entity_text = ''.join(last_entity)
                    if last_entity_type not in entities:
                        entities[last_entity_type] = []
                    entities[last_entity_type].append(entity_text)
                    last_entity = []

            if label != 'O':
                last_entity.append(word)
                last_entity_type = label.split('-')[1]

        # 去除无意义的最后一个字符
        text = ''.join(words)[:-1]
        label = {key: value for key, value in entities.items()}
        result.append(json.dumps({"text": text, "label": label}, ensure_ascii=False))
    res = "\n".join(result)
    print(res)
    return res

def solve_file(input_path,output_path):
    with open(input_path, "r") as f:
        with open(output_path, "w") as out:
            l = f.readlines()
            input = ''.join(l)
            # print(input)
            res = bio_to_json(input)
            out.write(res)

def test1():
    # 示例 BIO 数据
    bio_data = """
        中 B-ORG
        国 I-ORG
        有 O
        A B-ORG
        B I-ORG
        C I-ORG
        公 I-ORG
        司 I-ORG
        """

    # 转换为 JSON 格式
    json_data = bio_to_json(bio_data)

    # 输出结果
    print(json.dumps(json_data, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    # test1()
    solve_file("data/train.csv", "data/train.txt")


