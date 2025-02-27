from itertools import product
from gradio_demo import BGSource

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

GENERATION_PROMPT = {
    "scene": [
        "professional product photography studio",
        "outdoor park bench with natural surroundings",
        "coffee shop table with cafe interior",
        "office desk with computer and papers",
        "home kitchen counter with appliances",
        "library reading table with books",
        "cozy reading room with armchair and lamp",
        "busy street sidewalk with urban background",
        "car cup holder with dashboard view",
        "picnic blanket on grass",
    ],
    "bg_source": [
        BGSource.NONE,
        BGSource.LEFT,
        BGSource.RIGHT,
        BGSource.TOP,
        BGSource.BOTTOM,
    ],
    "seed": [
        4242,
        1234,
        5678,
        9012,
        2468,
    ],
}

# main
if __name__ == "__main__":
    # print out all the combinations of the prompt
    for combination in product(*DESCRIPTION_PROMPT.values()):
        # print out combination as a single string
        print(", ".join(combination))
