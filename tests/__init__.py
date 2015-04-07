import os


def asset_path(filename, asset_dir='assets'):
    return os.path.join(os.path.dirname(__file__),
                        asset_dir,
                        filename)
