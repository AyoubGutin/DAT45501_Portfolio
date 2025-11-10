from pathlib import Path


def find_root():
    current_dir = Path(__file__).parent
    # (current_dir.parents is a list like [/.../src/data_analysis, /.../src, /.../, /])
    PROJECT_ROOT = None
    for parent in current_dir.parents:
        # if requirements, we know its the project root
        if (
            parent / "requirements.txt"
        ).exists():  # requirements is always at the root, so if this file exists at parent / requirements, it exists
            PROJECT_ROOT = parent
            return PROJECT_ROOT
    if PROJECT_ROOT is None:
        raise FileNotFoundError("Could not find project root")
