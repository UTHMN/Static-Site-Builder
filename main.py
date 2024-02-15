from pygen import Generator
import os
import shutil

# post format dd-mm-yyyy-title

if not os.path.exists("posts"):
    os.mkdir("posts")

instance = Generator()
posts_data = {}
posts_listdir = os.listdir("posts")
posts_index_list = []
posts_index_string = ""

for i in range(len(posts_listdir)):
    with open(f"posts/{posts_listdir[i]}", "r") as file:
        posts_data[f"{posts_listdir[i]}"] = file.read()
        instance.generate_blog_page(posts_listdir[i],posts_data[posts_listdir[i]])

for i in range(len(posts_listdir)):
    posts_index_list.append(instance.generate_blog_sec(f"posts/{posts_listdir[i]}",posts_data[posts_listdir[i]][:512]+"...",posts_listdir[i][11:],posts_listdir[i][:10]))
instance.generate_css()

for i in range(len(posts_index_list)):
    posts_index_string += posts_index_list[i]

title = input("Title of website: ")
footer = ""

while True:
    contact = input("Contact style to add [website/email/exit] ")

    if contact.lower() == "exit":
        break
    elif contact.lower() == "email":
        email = input("email address: ")
        icon = input("path to icon: ")
        filename = os.path.basename(icon)
        shutil.copyfile(icon,f"export/assets/{filename}")
        footer += instance.generate_contact_sec(f"assets/{filename}", f"mailto:{email}", "_blank", "email")
    elif contact.lower() == "website":
        icon = input("path to icon: ")
        filename = os.path.basename(icon)
        shutil.copyfile(icon,f"export/assets/{filename}")
        footer += instance.generate_contact_sec(f"assets/{filename}", input("link to website: "), "_blank", input("name of site: "))

instance.generate_index(f"<h1>{title}</h1>",posts_index_string,footer)