import random
import subprocess
import os
from PIL import Image

desktop_path = os.path.join(os.path.expanduser('~'), 'Documents/!WALLPAPERS')

def files_in_folder(folder_path, image_extensions=['.jpg', '.jpeg', '.png'], min_width=1920):
    try: 
        valid_images = []
        # getting an array of images in the wallpaper folder which have .jpg, .png and .jpeg extensions
        for f in os.listdir(folder_path):
            file_path = os.path.join(folder_path, f)
            if os.path.isfile(file_path) and os.path.splitext(f)[1].lower() in image_extensions:
                try: 
                    with Image.open(file_path) as img:
                        width, height = img.size
                        if(width >= min_width): 
                            valid_images.append(file_path)
                except Exception as e: 
                    print(f"Error is {e}")
        return valid_images
    except Exception as e: 
        print(f"Error is: {e}")
        return []
    
items = os.path.join(desktop_path, files_in_folder(desktop_path)[random.randint(0, 15)])

def change_wallpaper(image_path):
    try: 
        # setting the background image of my ubuntu desktop to the image
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri-dark", f"file://{image_path}"])
        print(f"Your wallpaper has been changed to {image_path}")
    except Exception as e:
        print(f"Error is {e}")

change_wallpaper(items)