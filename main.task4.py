import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(csvFilename, delimiter = ',', new_line = '\n') -> list[dict]:
    jsonArray = []
    with open(csvFilename, 'r', encoding="utf-8") as f:
        fullString = f.readlines()
        headers = fullString[0].replace(new_line, "").split(delimiter)

        for indexString in range(1, len(fullString)):
            dict = {}
            for indexHeader in range(0, len(headers)):
                dict[headers[indexHeader]] = fullString[indexString].replace(new_line, "").split(delimiter)[indexHeader]
            jsonArray.append(dict)
        f.close()
    return jsonArray


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
