import os
import shutil
import sys
import turtle

def copy_files(src, dest):
    try:
        for item in os.listdir(src):
            path = os.path.join(src, item)
            if os.path.isdir(path):
                copy_files(path, dest)
            else:
               
                file_extension = os.path.splitext(item)[1][1:]
                if file_extension:
                    extension_directory = os.path.join(dest, file_extension)
                    if not os.path.exists(extension_directory):
                        os.makedirs(extension_directory)
                    shutil.copy(path, os.path.join(extension_directory, item))
                else:
                    
                    no_extension_directory = os.path.join(dest, "no_extension")
                    if not os.path.exists(no_extension_directory):
                        os.makedirs(no_extension_directory)
                    shutil.copy(path, os.path.join(no_extension_directory, item))
    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до вихідної директорії.")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    copy_files(source_directory, destination_directory)

if __name__ == "__main__":
    main()



    