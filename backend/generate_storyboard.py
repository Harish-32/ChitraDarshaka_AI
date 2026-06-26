from image_generator import generate_image

prompts =extract_scenes_from_story(story)


for i,prompt in enumerate(prompts):

    generate_image(
        prompt,
        f"scene{i+1}.png"
    )

print("Storyboard Generated")