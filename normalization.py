import pandas as pd
import re
from clean_gadget import clean_gadget
import os


def normalization(source):
    nor_code = []
    for fun in source["code"]:
        lines = fun.split("\n")
        # print(lines)
        code = ""
        for line in lines:
            line = line.strip()
            line = re.sub("//.*", "", line)
            code += line + " "
        # code = re.sub('(?<!:)\\/\\/.*|\\/\\*(\\s|.)*?\\*\\/', "", code)
        code = re.sub("/\\*.*?\\*/", "", code)
        code = clean_gadget([code])
        nor_code.append(code[0])
        # print(code[0])
    return nor_code


def mutrvd():
    train = pd.read_pickle("./dataset/trvd_train.pkl")[
        0
    ]  # Assuming the first element of the tuple is the DataFrame
    test = pd.read_pickle("./dataset/trvd_test.pkl")[0]
    val = pd.read_pickle("./dataset/trvd_val.pkl")[0]

    train["code"] = normalization(train)
    if not os.path.exists("./dataset/mutrvd"):
        os.makedirs("./dataset/mutrvd")
    train.to_pickle("./dataset/mutrvd/train.pkl")

    test["code"] = normalization(test)
    test.to_pickle("./dataset/mutrvd/test.pkl")

    val["code"] = normalization(val)
    val.to_pickle("./dataset/mutrvd/val.pkl")


if __name__ == "__main__":
    mutrvd()
