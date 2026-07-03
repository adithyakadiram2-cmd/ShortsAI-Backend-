import os

def generate_images(prompts):
    os.makedirs("images", exist_ok=True)

    image_paths = []

    for i, prompt in enumerate(prompts, start=1):
        filename = f"images/scene_{i}.jpg"

        # Placeholder until AI image generation is connected
        with open(filename, "w") as f:
            f.write(prompt)

        image_paths.append(filename)

    return image_paths
0

