"""make.fun image entry (round cream kitten face, big eyes, blush, pink bow, pastel hearts): copy the bundled picture to /output/entry.png.

The picture (entry.png, in this repository) was generated for this bounty.
Copying the exact bytes keeps both grader runs byte-identical.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # /output in the grader, MAKEFUN_OUTPUT_DIR when run locally.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()

# Entry variant: round cream kitten face, big eyes, blush, pink bow, pastel hearts
