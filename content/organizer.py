import os
import frontmatter

files = os.listdir("./")

for f in files:
    if (not os.path.isdir(f) ):
        if ( os.path.splitext(f)[-1] == ".md"):
            print(f)
            post = frontmatter.load(f)
            breakpoint()
            print(post["tags"])

