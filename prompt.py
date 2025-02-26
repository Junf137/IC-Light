from itertools import product

# Define all possible categories and variations of description prompt
DESCRIPTION_PROMPT = {
    "angle": [
        "front view",
        "side view",
        "camera looking down at cup from 45-degree angle above",
        "camera looking up at cup from 45-degree angle below",
        "top-down view",
    ],
    "placement": [
        "held by hand",
        "not held by hand",
    ],
    "accessories_lid": [
        "with lid",
        "without lid",
    ],
    "accessories_sleeve": [
        "with sleeve",
        "without sleeve",
    ],
    "color": [
        "Tim Hortons red",
        "dark cyan",
    ],
    "logo": [
        "Tim Hortons maple leaf logo on the cup",
        "Tim Hortons text logo on the cup",
        "Tim Hortons maple leaf logo on the lid",
        "Tim Hortons maple leaf logo on the cup and Tim Hortons maple leaf logo on the lid",
        "Tim Hortons text logo on the cup and Tim Hortons maple leaf logo on the lid",
    ],
}

# TODO: Define all possible categories and variations of generation prompt
GENERATION_PROMPT = {
    "style": [
        "realistic photography",
        "cartoonish style",
        "line art sketch",
        "watercolor painting",
        "3D render",
    ],
}


# main
if __name__ == "__main__":
    # print out all the combinations of the prompt
    for combination in product(*DESCRIPTION_PROMPT.values()):
        # print out combination as a single string
        print(", ".join(combination))