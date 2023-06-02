import os

def find_largest_common_substring():
    files = [file for file in os.listdir(".") if file.endswith((".mkv", ".mp4", ".avi", ".mov", ".wmv"))]
    substrings = []

    for file in files:
        filename, file_extension = os.path.splitext(file)
        substrings.append(filename)

    if substrings:
        largest_substring = min(substrings, key=len)
        while largest_substring:
            if all(substring.startswith(largest_substring) for substring in substrings):
                return largest_substring
            largest_substring = largest_substring[:-1]
    return None


def main():
    directory = os.getcwd()
    substring_cut = find_largest_common_substring()
    for filename in os.listdir("."):
        if filename.endswith((".mkv", ".mp4", ".avi", ".mov", ".wmv")):
            if substring_cut in filename:
                new_name = filename.replace(substring_cut, "")
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
                


if __name__ == "__main__":
    main()