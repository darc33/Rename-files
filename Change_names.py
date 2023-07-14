from dotenv import load_dotenv
import os
 
load_dotenv()

os.chdir(os.environ["folder_loc"])
print(os.getcwd())
def_name="Image"#File, Video, Song

for count, f in enumerate(os.listdir()):
    print(count)
    f_name, f_ext = os.path.splitext(f)
    f_name = def_name + str(count)
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)