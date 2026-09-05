import os
import glob
import shutil
import frontmatter

files = os.listdir("./")

def move_all_to_dir(fname, dirname):
    for fpath in glob.glob(fname + "*"):
        if (os.path.isfile(fpath)):
            print(fpath, " -> ", dirname)
            shutil.move(fpath, dirname)


for f in files:
    if ( os.path.isfile(f) ):
        fnames = os.path.splitext(f)
        if ( fnames[-1] == ".md"):
            post = frontmatter.load(f)
            if ( "tags" in post.keys() and post["tags"] != None ):
                tags = post["tags"]
                if ("blockchain" in tags):
                    move_all_to_dir(fnames[0], "./Blockchain//")
                elif ("os" in tags):
                    move_all_to_dir(fnames[0], "./OS/")
                elif ("programming" in tags):
                    move_all_to_dir(fnames[0], "./Programming/")
                elif ("compilers" in tags):
                    move_all_to_dir(fnames[0], "./Programming/")
                elif ("algorithm" in tags):
                    move_all_to_dir(fnames[0], "./Programming/")
                elif ("security" in tags):
                    move_all_to_dir(fnames[0], "./Security/")
                elif ("cryptography" in tags):
                    move_all_to_dir(fnames[0], "./Security/")
                elif ("verification" in tags):
                    move_all_to_dir(fnames[0], "./Security/")
                elif ("privacy" in tags):
                    move_all_to_dir(fnames[0], "./Security/")
                elif ("windows" in tags):
                    move_all_to_dir(fnames[0], "./Windows/")
                elif ("math" in tags):
                    move_all_to_dir(fnames[0], "./Math/")
                elif ("statistics" in tags):
                    move_all_to_dir(fnames[0], "./Math/")
                elif ("proofs" in tags):
                    move_all_to_dir(fnames[0], "./Math/")
                elif ("web" in tags):
                    move_all_to_dir(fnames[0], "./Web/")
                elif ("hardware" in tags):
                    move_all_to_dir(fnames[0], "./Hardware/")
                elif ("robotics" in tags):
                    move_all_to_dir(fnames[0], "./Hardware/")
                elif ("business" in tags):
                    move_all_to_dir(fnames[0], "./Economics/")
                elif ("economy" in tags):
                    move_all_to_dir(fnames[0], "./Economics/")
                elif ("linux" in tags):
                    move_all_to_dir(fnames[0], "./Linux/")
                elif ("networking" in tags):
                    move_all_to_dir(fnames[0], "./Network/")
                elif ("IT" in tags):
                    move_all_to_dir(fnames[0], "./IT/")
                elif ("3d" in tags):
                    move_all_to_dir(fnames[0], "./Art/")
                elif ("game_dev" in tags):
                    move_all_to_dir(fnames[0], "./Programming/")
                elif ("philosophy" in tags):
                    move_all_to_dir(fnames[0], "./Philosophy/")
                elif ("religion" in tags):
                    move_all_to_dir(fnames[0], "./Philosophy/")
                elif ("law" in tags):
                    move_all_to_dir(fnames[0], "./Philosophy/")
                elif ("politics" in tags):
                    move_all_to_dir(fnames[0], "./Philosophy/")
                elif ("linguistics" in tags):
                    move_all_to_dir(fnames[0], "./Philosophy/")
                elif ("internet_culture" in tags):
                    move_all_to_dir(fnames[0], "./Philosophy/")
                elif ("scifi" in tags):
                    move_all_to_dir(fnames[0], "./Philosophy/")
                elif ("biology" in tags):
                    move_all_to_dir(fnames[0], "./Biology/")
                elif ("academia" in tags):
                    move_all_to_dir(fnames[0], "./Misc/")
                elif ("job" in tags):
                    move_all_to_dir(fnames[0], "./Misc/")
                elif ("ctf" in tags):
                    move_all_to_dir(fnames[0], "./CTFs/")
                elif ("machine_learning" in tags):
                    move_all_to_dir(fnames[0], "./Machine Learning/")
                elif ("ai_safety" in tags):
                    move_all_to_dir(fnames[0], "./Machine Learning/")
                elif ("occult" in tags):
                    move_all_to_dir(fnames[0], "./Magic/")
                elif ("health" in tags):
                    move_all_to_dir(fnames[0], "./Biology/")
                elif ("psychology" in tags):
                    move_all_to_dir(fnames[0], "./Biology/")
