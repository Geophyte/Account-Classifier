import pandas as pd
import json


def load_jsonl(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    records = [json.loads(line.strip()) for line in data]

    df = pd.DataFrame(records)

    return df


def load_jsonl_tuples(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    records = []
    for line in data:
        record = json.loads(line.strip())
        for key, value in record.items():
            if isinstance(value, list):
                record[key] = tuple(value)
        records.append(record)

    df = pd.DataFrame(records)

    return df
