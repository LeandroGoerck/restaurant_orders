class FileWriter():
    @staticmethod
    def save_data(arquivo, content):
        with open(arquivo, 'w') as file:
            for line in content:
                file.write(str(line))
                file.write('\n')
