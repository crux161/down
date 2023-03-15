import markdownify
import sys
import hashlib

def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

# check that argc only contains 1 argument (the file name)
if len(sys.argv) != 2:
    print("Usage: down <file_name>")
    sys.exit(1)

# get file name from command line
file_name = sys.argv[1]

# open file
html = open(file_name, "r")

# convert html to markdown
markdown = markdownify.markdownify(html, heading_style="ATX")

# write the file to a file with the same name but .md extension
with open(file_name[:-5] + ".md", "w") as f:
    f.write(markdown)

# close the file
html.close()

# close the file
f.close()

output_sz = sizeof_fmt(len(markdown))
digest = hashlib.md5(markdown.encode()).hexdigest()
# report the conversion with the file size and md5 hash
print("[DOWN] Converted {} to {} with size {}.\n\tMD5 hash: {}".format(file_name, file_name[:-5] + ".md", output_sz, digest))

