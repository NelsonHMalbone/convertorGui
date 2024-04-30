import zipfile
import pathlib

def archive(filepaths, dest_dir):
    dist_path = pathlib.Path(dest_dir, 'compressed_folder.zip')
    with zipfile.ZipFile(dist_path, 'w') as archived_folder:  # create a file to represent file path name
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archived_folder.write(filepath, arcname=filepath.name)  # exacting filepath name



