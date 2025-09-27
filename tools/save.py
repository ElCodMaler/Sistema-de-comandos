import json

def trasnform_json_dict(value: str) -> dict[str,any]:
    """ Find the location of the database and assign it to a variable such as a dictionary """
    fileDB = value
    if not value:
        fileDB = "C"
    with open(f'db/{fileDB}.json', 'r', encoding='utf-8') as archivo:
        return json.load(archivo)
    raise ValueError("no se encontro tu archivo DB")