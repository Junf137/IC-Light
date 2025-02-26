import os
import numpy as np
from PIL import Image
from typing import List

from gradio_demo import process_relight, BGSource


# Process images
def process_batch(input_paths: List[str], prompts: List[str], output_dir: str, **process_kwargs) -> None:
    """
    Batch process images with multiple prompts
    :param input_paths: List of input image paths
    :param prompts: List of prompts (one per image)
    :param output_dir: Root directory to save results
    :param process_kwargs: Additional arguments for process_relight
    """
    os.makedirs(output_dir, exist_ok=True)

    for img_path, prompt in zip(input_paths, prompts):
        # Load image
        pil_img = Image.open(img_path).convert("RGB")
        np_img = np.array(pil_img)

        # Process image
        preprocessed, outputs = process_relight(input_fg=np_img, prompt=prompt, **process_kwargs)

        # Create output structure
        base_name = os.path.splitext(os.path.basename(img_path))[0]
        prompt_dir = os.path.join(output_dir, base_name, "prompt_" + prompt[:64].replace(" ", "_"))
        os.makedirs(prompt_dir, exist_ok=True)

        # Save results
        Image.fromarray(preprocessed).save(os.path.join(prompt_dir, "preprocessed.png"))
        for i, output in enumerate(outputs):
            Image.fromarray(output).save(os.path.join(prompt_dir, f"output_{i}.png"))


if __name__ == "__main__":
    # Configuration
    config = {
        "image_width": 512,  # Output width (multiple of 64)
        "image_height": 640,  # Output height (multiple of 64)
        "num_samples": 3,  # Number of outputs per image
        "seed": 4242,  # Random seed
        "steps": 25,  # Diffusion steps
        "a_prompt": "best quality, high resolution, good cup shape",  # Automatic positive prompt addition
        "n_prompt": "low resolution, cropped, worst quality, deformed cup",  # Negative prompt
        "cfg": 2.0,  # Classifier-free guidance scale
        "highres_scale": 1.5,  # High-res upscale factor
        "highres_denoise": 0.5,  # High-res denoise strength
        "lowres_denoise": 0.9,  # Low-res denoise strength
        "bg_source": BGSource.LEFT,  # Background source
    }

    # Input setup
    input_images = [""]

    prompts = ["red Tim Hortons cup with white lid, Tim Hortons logo, high resolution, natural light, grass ground"]

    # Run processing
    process_batch(input_paths=input_images, prompts=prompts, output_dir="./batch_outputs", **config)
