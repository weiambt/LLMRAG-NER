import configparser


def load_multiple_objects_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    objects_config = {}

    # 遍历配置文件中的所有节
    for section in config.sections():
        # 为每个节创建一个字典来存储配置参数
        object_config = {}
        for key, value in config.items(section):
            object_config[key] = value
        # 将对象的配置字典添加到主字典中，键是对象名（节名）
        objects_config[section] = object_config

    return objects_config


# 使用示例
if __name__ == "__main__":
    config_file = '/Users/didi/Desktop/KYCode/RAG-NER/conf/dev/llm.ini'
    objects_config = load_multiple_objects_config(config_file)

    # 打印每个对象的配置
    for object_name, params in objects_config.items():
        print(f"Configuration for object '{object_name}':")
        for param, value in params.items():
            print(f"  {param} = {value}")
        print()  # 空行分隔不同对象的配置