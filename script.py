import os


def delete_matching_txt(image_folder, txt_folder):
    # Get list of image files in the image folder
    for image_file in os.listdir(image_folder):
        # Extract the name without the extension
        image_name, ext = os.path.splitext(image_file)

        # Proceed only if it's an image file (you can add more extensions if needed)
        if ext.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            # Build the path to the corresponding .txt file in the txt folder
            txt_file = os.path.join(txt_folder, f"{image_name}.txt")

            # Check if the txt file exists, then delete it
            if os.path.exists(txt_file):
                os.remove(txt_file)
                print(f"Deleted: {txt_file}")
            else:
                print(f"No matching .txt file found for: {image_name}")


# Example usage
image_folder = 'path/to/your/image/folder'
txt_folder = 'path/to/your/txt/folder'

delete_matching_txt(image_folder, txt_folder)
