from rag.evaluation.golden_dataset import GOLDEN_DATASET

my_golden = GOLDEN_DATASET
types = []
for i in my_golden:
    for key, val in i.items():
        if key == "type":
            types.append(val)


print(f"Συνολο ερωτήσεων:{len(GOLDEN_DATASET)}")



exact_match_no = types.count('A')
variation_no = types.count('B')
out_of_scope_no = types.count('C')

print(f"Exact match:{exact_match_no}, Variation:{variation_no}, Out of scope:{out_of_scope_no}")
