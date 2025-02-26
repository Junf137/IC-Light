import os


def create_txt_files_from_png(folder_path):
    """
    For each PNG file in the given folder, create a corresponding TXT file with the same name.

    Parameters:
        folder_path (str): Path to the folder containing PNG files.
    """
    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist.")
        return

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".png") or filename.lower().endswith(".jpeg"):
            txt_filename = os.path.splitext(filename)[0] + ".txt"  # Change extension to .txt
            txt_filepath = os.path.join(folder_path, txt_filename)

            # create empty file txt_filepath
            with open(txt_filepath, "w") as f:
                f.write("")

            print(f"Created: {txt_filepath}")


if __name__ == "__main__":
    folder_path = "./imgs/TimHortonsPaperCup/genAI/part_1"  # Change this to your target folder
    create_txt_files_from_png(folder_path)
