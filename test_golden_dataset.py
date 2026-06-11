from rag.evaluation.golden_dataset import GOLDEN_DATASET

my_golden = GOLDEN_DATASET
types = []
for i in my_golden:
    for key, val in i.items():
        if key == "type":
            types.append(val)


print(len(GOLDEN_DATASET))



exact_match_no = types.count('A')
variation_no = types.count('B')
out_of_scope_no = types.count('C')

print(f"{exact_match_no}, {variation_no}, {out_of_scope_no}")
