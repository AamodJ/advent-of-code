import numpy as np

with open("input.txt", "r") as fd:
    s = fd.readlines()

    blank_idx = s.index("\n")
    fresh_ranges = np.array([r.strip().split("-") for r in s[:blank_idx]]).astype(int)
    ingredients = np.array([r.strip() for r in s[blank_idx + 1 :]]).astype(int)


num_fresh_ing = 0
for ingredient in ingredients:
    if ((ingredient >= fresh_ranges[:, 0]) & (ingredient <= fresh_ranges[:, 1])).any():
        num_fresh_ing += 1
        # print(f"Ingredient {ingredient} is fresh")


print(f"Total number of fresh ingredients: {num_fresh_ing}")
