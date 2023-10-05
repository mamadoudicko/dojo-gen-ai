def str_to_file(str, file_name):
    with open(file_name, "w") as file:
        file.write(str)
    return file
