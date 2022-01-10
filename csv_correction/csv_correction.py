import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        print(full_filename)

search("C:/Users/css04/OneDrive/바탕 화면/sample/sample_data/sample_data/")
