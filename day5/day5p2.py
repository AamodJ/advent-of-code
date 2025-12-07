import numpy as np

with open("input.txt", "r") as fd:
    s = fd.readlines()

    blank_idx = s.index("\n")
    fresh_ranges = [r.strip().split("-") for r in s[:blank_idx]]
    for idx, r in enumerate(fresh_ranges):
        fresh_ranges[idx] = [int(r[0]), int(r[1])]
    ingredients = [r.strip() for r in s[blank_idx + 1 :]]

SWALLOW_RANGE = 0
OVERLAP_RANGE = 1
DISJOINT_RANGE = 2
SEARCH_RANGE = 3
OVERSHADOW_RANGE = 4
WTF_RANGE = 5


class WTF(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


def is_in_range(item: int, r: list) -> bool:
    if item in range(r[0], r[1] + 1):
        return True
    else:
        return False


def range_classification(base_idx: int, base_range: list, search_ranges: list):
    global SWALLOW_RANGE, OVERLAP_RANGE, DISJOINT_RANGE, SEARCH_RANGE, OVERSHADOW_RANGE
    overlap_tracker = []
    if base_idx == 3:
        debug_flag = False
    else:
        debug_flag = False

    for idx, s_range in enumerate(search_ranges):
        if idx == base_idx:
            overlap_tracker.append(SEARCH_RANGE)
            if debug_flag:
                print("Hit idx = base_idx")
            continue

        lower_is_in_range = is_in_range(base_range[0], s_range)
        upper_is_in_range = is_in_range(base_range[1], s_range)

        if lower_is_in_range and upper_is_in_range:
            if debug_flag:
                print("Hit swallow")
            return None
        elif (lower_is_in_range and not upper_is_in_range) or (
            not lower_is_in_range and upper_is_in_range
        ):
            if debug_flag:
                print("Hit overlap")
            overlap_tracker.append(OVERLAP_RANGE)
        elif (base_range[1] <= s_range[0]) or (base_range[0] >= s_range[1]):
            if debug_flag:
                print("Hit disjoint")
            overlap_tracker.append(DISJOINT_RANGE)
        elif base_range[0] <= s_range[0] and base_range[1] >= s_range[1]:
            if debug_flag:
                print("Hit overshadow")
            overlap_tracker.append(OVERSHADOW_RANGE)
        else:
            if debug_flag:
                print("Hit wtf")
            raise WTF(
                f"Reached WTF with {base_range} while searching with range {s_range}"
            )

    if OVERLAP_RANGE in overlap_tracker:
        overlap_indices = [
            idx for idx, r in enumerate(overlap_tracker) if r == OVERLAP_RANGE
        ]
        overlap_ranges = [search_ranges[idx] for idx in overlap_indices]
        overlap_ranges.append(base_range)
        lower_limit = min([r[0] for r in overlap_ranges])
        upper_limit = max([r[1] for r in overlap_ranges])
        return [lower_limit, upper_limit]
    else:
        return base_range


def normalize_range(to_normalize: list):
    deduped = []
    for r in to_normalize:
        if r not in deduped:
            deduped.append(r)

    to_normalize = deduped

    while True:
        new_ranges = []
        for search_idx, r in enumerate(to_normalize):
            classification = range_classification(search_idx, r, to_normalize)
            if classification is not None and classification not in new_ranges:
                new_ranges.append(classification)

        if new_ranges == to_normalize:
            break
        to_normalize = new_ranges

    return to_normalize


# fresh_ranges = [[1, 25], [5, 10], [12, 17], [1, 25]]
fresh_ranges = np.array(normalize_range(fresh_ranges))
# np.array(normalize_range(fresh_ranges))

print(f"Total valid ranges: {(fresh_ranges[:, 1] - fresh_ranges[:, 0] + 1).sum()}")
