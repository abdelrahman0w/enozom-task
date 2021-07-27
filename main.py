import os
import sys
import hashlib
import csv


class Parser:
    def __init__(
        self,
        file = os.path.join(sys.path[0], 'annual-enterprise-survey-2020-financial-year-provisional-csv.csv')
        # file = os.path.join(os.getcwd(), 'testcase.csv')
    ) -> None:
        self.file = file

    @property
    def __load_data(self) -> dict:
        data = {}
        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line_count, row in enumerate(csv_reader):
                if line_count == 0:
                    heads = row
                    for c_name in heads:
                        data[c_name] = []
                else:
                    for data_i in range(len(row)):
                        data[heads[data_i]].append(row[data_i])

        return data

    @property
    def concatenate(self) -> str:
        column_names = list(self.__load_data)
        return "".join(self.__load_data.get(column_names[2])[0::2])

    @property
    def hash_data(self) -> str:
        return hashlib.md5(self.concatenate.encode()).hexdigest().upper()


# Driver Code
parser = Parser()
# print(parser.concatenate)
print(parser.hash_data)