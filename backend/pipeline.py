import os

from trailer_script_generator import generate_trailer_script
from narration import generate_narration
from image_generator import generate_image
from scene_prompt_generator import generate_scene_prompts


def generate_trailer_from_story(story, language):

    os.makedirs("outputs", exist_ok=True)

    print("🎬 Creating Trailer From Story")

    # Trailer Script
    trailer_script = generate_trailer_script(
        story,
        language
    )

    print("Trailer Length:", len(trailer_script))
    print("✅ Trailer Script Generated")

    # Narration
    generate_narration(
        trailer_script,
        language,
        "outputs/trailer_voice.mp3"
    )

    print("✅ Narration Generated")

    # Dynamic Scene Prompts
    scene_prompts = generate_scene_prompts(story)

    print("\n===== GENERATED SCENES =====")

    for i, scene in enumerate(scene_prompts):
        print(f"Scene {i+1}: {scene}")

    # Generate Images
    for i, prompt_text in enumerate(scene_prompts[:5]):

        generate_image(
            prompt_text,
            f"outputs/scene{i+1}.png"
        )

        print(f"✅ Scene {i+1} Generated")
    # Create Trailer Video
    os.system(
        "python trailer_creator.py"
    )

    print("✅ Trailer Video Created")

    return {
    "trailer_script": trailer_script,
    "video_path": "outputs/trailer.mp4"
}