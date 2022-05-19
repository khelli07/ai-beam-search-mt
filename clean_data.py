f = open("data/raw_eng-ind.txt", "r", encoding="utf-8")
lines = f.read().encode().decode("utf-8").split("\n")
w = open("data/eng-ind.txt", "w", encoding="utf-8")
for line in lines:
    sep = line.split("\t")
    try:
        eng, ind = sep[1], sep[3]
        w.write(eng + "\t" + ind + "\n")
    except Exception:
        pass

f.close()
w.close()
