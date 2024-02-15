import os

class Generator:
    def __init__(self) -> None:
        if not os.path.exists("export"):
            os.mkdir("export")
        if not os.path.exists("export/posts"):
            os.mkdir("export/posts")
        if not os.path.exists("export/assets"):
            os.mkdir("export/assets")

    def generate_contact_sec(self, icon, href, target, txt):
        return f"""
        <a class="link" href="{href}" target="{target}" rel="noopener noreferrer">
            <img src="{icon}"/>{txt}
        </a>
        """
    
    def generate_blog_sec(self, href, desc, title, date):
        return f"""
        <div class="blog_sec">
            <a href="{href}" target="_self">
                <h2>{title}</h2>
                {date}
                <p>{desc}</p>
            </a>
        </div>
        """
    
    def generate_blog_page(self, title, content):
        index = f"""
        <html>
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>{title[11:]}</title>
            </head>
            <body>
                <header>
                    <h1>{title[11:]}</h1>
                    {title[:10]}
                    <hr>
                </header>
                <p>{content}</p>
            </body>
            <style>
                * {{
                    margin: 0;
                }}
    
                p {{
                    margin-top: 3px;
                }}
            </style>
        </html>
        """
        
        with open(f"export/posts/{title}.html", "w") as file:
            file.write(index)
    
    def generate_index(self, header, content, footer):
        index = f"""
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Uthmn</title>
            <link rel="stylesheet" href="styles.css">
          </head>
          <body>
            <header>
              {header}
              <hr>
            </header>

            <!-- Content -->
            {content}

            <footer>
                <hr>
                {footer}
            </footer>
          </body>
        </html>
        """

        with open("export/index.html", "w") as file:
            file.write(index)
    
    def generate_css(self):
        global css
        css = """
        /* resetting default styles */
        * {
            min-width: 0;
            padding: 0;
            margin: 1;
        }
        /* Links for hover/idle */
        .link:hover {
            color:blue;
        }
        
        .link {
            color:blueviolet;
            display: block;
            margin-top: 3px;
            margin-bottom: 3px;
        }
        
        /* Smaller icons for links */
        .link img {
            width: 25px;
        }
        
        .blog_sec a {
            color: black;
            text-decoration: none;
        }
        .blog_sec:hover a {
            color: black;
            margin: 1 !important;
            text-decoration: none;
        }
        """
    
        with open("export/styles.css", "w") as file:
            file.write(css)