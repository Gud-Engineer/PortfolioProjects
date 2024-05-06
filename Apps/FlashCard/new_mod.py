import  os
# TODO : List files in directory and update language list.
def language_parser():
    original_path = os.getcwd()
    language_list = []
    # 1. Get Files List
    os.chdir('./Data')
    target_dir = os.getcwd()
    # print(target_dir)
    files_list = []
    for file_path in os.listdir(target_dir):
        if os.path.isfile(os.path.join(target_dir, file_path)):
            files_list.append(file_path)
    # print(files_list)
    # 2. Filter out only .csv files
    files_list = [file for file in files_list if os.path.splitext(file)[1] == '.csv']
    # print(files_list)

    for file in files_list:
        language_list.append(os.path.splitext(file)[0].split('_')[0].title())

    # Returning file path
    os.chdir(original_path)
    return language_list


