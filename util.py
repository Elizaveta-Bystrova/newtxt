def save_file(filepath, text):
    with open(filepath, "w", encoding='utf-8') as output_file:
        output_file.write(text)

def open_file(filepath):
    with open(filepath, "r", encoding='utf-8') as input_file:
        return input_file.read()