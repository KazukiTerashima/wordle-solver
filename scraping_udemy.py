import pprint

with open("input", "r") as fp:
    input = list(map(lambda x: x.rstrip("\n"), fp.readlines()))

word_info = {}
cor = {}
pre = {}
abo = set()
target = set()

for i in range(len(input)):
    cor_flg = True
    pre_flg = True
    tep = ""
    word, correct, present = input[i].split()
    if correct != "-1" and present != "-1":
        target = target.union(set(correct + present))
    elif correct == "-1" and present == "-1":
        cor_flg = False
        pre_flg = False
    elif correct == "-1":
        cor_flg = False
        target = target.union(set(present))
    elif present == "-1":
        pre_flg = False
        target = target.union(set(correct))
    word_info["target"] = target

    abo = abo.union(set(word) - set(correct) - set(present))
    word_info["abort"] = abo

    if cor_flg:
        correct = list(correct)
        while correct:
            char = correct.pop()
            idx = list(word).index(char)
            if word_info.get("correct"):
                if char in word_info.get("correct").keys():
                    continue
                else:
                    cor[char] = idx
            else:
                cor[char] = idx
            word_info["correct"] = cor

    if pre_flg:
        present = list(present)
        while present:
            char = present.pop()
            idx = list(word).index(char)
            pre_set = {idx}
            if pre.get(char):
                update_tmp = pre[char].union(pre_set)
                pre[char] = update_tmp
            else:
                pre[char] = pre_set
        word_info["present"] = pre



with open("txt", "r") as fp:
    wordles = list(map(lambda x: x.rstrip("\n"), fp.readlines()))
    wordles = list(map(lambda x: (x, set(x)), wordles))


def match_pattern(target, info):
    word_set = target[1]
    predict_word = target[0]
    if not info["target"] <= word_set:
        return
    if info.get("correct"):
        for c, idx in info["correct"].items():
            if list(predict_word).index(c) != idx:
                return

    if info.get("present"):
        for p, idx in info["present"].items():
            if p in predict_word and not set(str(list(predict_word).index(p))).isdisjoint(idx):
                return
                
    if not set(predict_word).isdisjoint(info["abort"]):
        return
    print(predict_word)


            


if __name__ == "__main__":
    for wordle in wordles:
        match_pattern(wordle, word_info)
    

    pprint.pprint(word_info)
