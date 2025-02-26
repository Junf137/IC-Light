from pathlib import Path
import json
import numpy as np
from PIL import Image
from itertools import product

from prompt import GENERATION_PROMPT
from gradio_demo import process_relight


def process_dataset(input_dir: Path, output_root: Path, **process_kwargs: dict):
    """Process images with base prompts and generate variations"""
    # Create all possible generation combinations
    combinations = list(product(GENERATION_PROMPT["scene"], GENERATION_PROMPT["bg_source"], GENERATION_PROMPT["seed"]))

    for img_path in input_dir.glob("*.*"):
        if img_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
            continue

        # Get base prompt from text file
        txt_path = img_path.with_suffix(".txt")
        if not txt_path.exists():
            continue

        with open(txt_path, "r") as f:
            base_prompt = f.read().strip()

        # Load image
        img = np.array(Image.open(img_path).convert("RGB"))

        # Process all combinations
        for scene, bg_source, seed in combinations:
            # Construct full prompt
            full_prompt = f"{base_prompt}, {scene}"

            # Create output directory structure
            output_dir = output_root
            output_dir.mkdir(parents=True, exist_ok=True)

            # Generate images
            preprocessed, outputs = process_relight(
                input_fg=img,
                prompt=full_prompt,
                **process_kwargs,
                seed=seed,
                bg_source=bg_source.value,
            )

            # save preprocessed image
            fname_preprocessed = f"{img_path.stem}-{scene[:4]}-{bg_source.value[:2]}-{seed}-preprocessed.png"
            Image.fromarray(preprocessed).save(output_dir / fname_preprocessed)

            # Save with metadata
            for idx, output in enumerate(outputs):
                fname = f"{img_path.stem}-{scene[:3]}-{bg_source.value[:2]}-{seed}-{idx}.png"
                meta = {
                    "full_prompt": full_prompt,
                    "base_prompt": base_prompt,
                    "scene": scene,
                    "bg_source": bg_source.value,
                    "seed": seed,
                    "source_image": img_path.name,
                }

                Image.fromarray(output).save(output_dir / fname)
                with open(output_dir / f"{fname}.json", "w") as f:
                    json.dump(meta, f, indent=2)


if __name__ == "__main__":
    input_folder = Path("./imgs/TimHortonsPaperCup")
    output_folder = Path("./output/")

    config = {
        "image_width": 512,
        "image_height": 640,
        "num_samples": 1,
        "steps": 25,
        "a_prompt": "best quality, sharp focus",
        "n_prompt": "lowres, blurry, distorted, deformed, incorrect logo, cropped, worst quality",
        "cfg": 2,
        "highres_scale": 1.5,
        "highres_denoise": 0.5,
        "lowres_denoise": 0.9,
    }
    process_dataset(input_folder, output_folder, **config)
