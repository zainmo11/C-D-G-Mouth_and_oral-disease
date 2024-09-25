import os


def delete_matching_txt(image_folder, txt_folder,original_folder):
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

        # iterate over the original folder if there is any images not in image_name
        # move it to "detected folder"

        for original_file in os.listdir(original_folder):
            original_name, ext = os.path.splitext(original_file)
            if ext.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
                if original_name not in image_name:
                    os.rename(original_file, f"detected/{original_file}")
                    print(f"Moved: {original_file} to detected folder")
                else:
                    os.rename(original_file, f"not_detected/{original_file}")
                    print(f"Moved: {original_file} to not_detected folder")



# Define the paths to the image and txt folders
image_folder = 'path/to/your/image/folder'   # deleted images (not detected)
txt_folder = 'path/to/your/txt/folder'
original_folder = 'path/to/your/original/folder' #original images

delete_matching_txt(image_folder, txt_folder, original_folder)
