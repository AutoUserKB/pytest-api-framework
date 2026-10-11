import json


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f)


def load_json(path):
    with open(path) as f:
        file_data = json.load(f)
    return file_data


def test_save_and_load(tmp_path):
    file = tmp_path / "user.json"
    save_json(file ,{"name": "Kanchan", "role": "QA"} )
    assert load_json(file) == {"name": "Kanchan", "role": "QA"}
    
    # 1. call save_json with file and {"name": "Kanchan", "role": "QA"}
    # 2. assert load_json(file) == {"name": "Kanchan", "role": "QA"}