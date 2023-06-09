def write_from_file(data: dict, path: str) -> bool:
    file_name = str(data['f_name']).lower() + '.txt'
    string_for_file = "<{}>".format('><'.join(data.values()))
    with open(f'{path}/{file_name}', 'a+', encoding='utf-8') as file:
        file.write(string_for_file + '\n')
    return True

