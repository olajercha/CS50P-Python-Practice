"""In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""


def get_media_type(file_name):
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }

    file_extension = file_name.strip().lower().rsplit(".", 1)[-1] if "." in file_name else None

    return media_types.get(f'.{file_extension}', "application/octet-stream")


def main():
    file_name = input("File name: ")

    media_type = get_media_type(file_name)

    print(media_type)


main()
