import os




EXTENSION = ['.json', '.yaml']


def get_files(path_to_file):
    worked_files = [os.path.split(path_to_file)[-1]]
    path_to_file = ''
    for root, _, files in os.walk(os.getcwd()):
        for document in files:
            if document in worked_files:
                path_to_file = os.path.join(root, document)
    print(path_to_file)
    return path_to_file


def main():
    get_files('gendiff/tests/fixtures/before.json')


if __name__ == "__main__":
    main()