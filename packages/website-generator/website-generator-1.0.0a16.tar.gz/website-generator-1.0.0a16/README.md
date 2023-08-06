# Website Generator

A minimalistic static website generator

Features:
* **Ease of use**
* **Markdown support** - Markdown can be used as an alternative to html
* **Blogging**
  * Tags
  * RSS
* **Small code base** - Easy to get an overview of what the program does (all code is contained in the `./main.py` file)
* **Themes** - customize one of the included ones or create your own from scratch
  * **Easy to create your own themes**

Target groups:
* Non-tech-savvy people or small groups that want a simple and secure website or blog
  * If you want to create custom themes, html knowledge is needed, but for the content markdown can be used
  * Basic knowledge of using a terminal window (command line) is required
* More tech-savvy people who want full control over the application (and perhaps want to customize the Python code)

Why a static website instead of something like WordPress?
* Less underlying software to maintain
* Easy access to the code
* Faster
* Safer

Why this static website generator instead of pure html?
* You can have multiple pages and get the same look for all without having to copy and paste each time a change is made for the look
* Very easy to change the theme of the website (and keep the content)
* Markdown supports enables you to create a website without needing to code html


## Installing (and Starting)

### Ubuntu

#### Install using pip

Requires Python 3.9. You can see the python version by typing `python3 --version` (on Linux-based systems) or `python --version` (on Windows and MacOS)

1. `pip3 install website-generator`
2. (Optional) `echo 'export PATH="$HOME/.local/bin:$PATH"' >> .bashrc`, and then `source .bashrc`
3. Then start with: `website-gen`

#### Running from binary

*TODO*

<!--
1. [Download]() the latest file
2. Unzip and open dir
3. Launch `main`
-->

#### Running from source

1. Download the source files (tar.gz/zip) or clone, and then unzip
2. cd into the directory and run `python3 main.py`

### Windows

#### Install using pip

1. Download and install Python 3.x (Windows 7 supports up to 3.8, but not higher, so if you are using Windows 7 please make sure to download the 3.8 version rather than the latest)
2. `pip install website-generator`
3. Start using this file: {python-install-dir}/Scripts/`website-gen`

#### Running from binary

*TODO*

#### Running from source

1. Download the source files (tar.gz/zip) or clone, and then unzip
2. cd into the directory and run `python main.py`

### MacOS

*TODO* (More or less the same as for Ubuntu above)


## Usage

### Quick start

Simply run the application (as described above under "Installation"). Example content files are in place already, and a default theme will be used. The website will be generated and placed in the *output* folder (default is `public`). Then the local website files will be loaded in your browser!

### Parameters that can be given to the application

* `content-dir`
* `theme-dir`
* `output-dir`
* `force-remove-output`
* `content-url`
* `website-url`

With the `-h` flag you can get a description of all of these

The application supports using a `settings.ini` file, which can be used to store commonly used values of these parameters (so that you don't have to give them every time at the command line)

### Adding new content

1. Add `.html` and/or `.md` files - with the content you want - into the *content* dir
  * a theme template file will be used as a "frame" for your content. This template usually includes things like a header, footer and a css-file (for styling, layout, colors, fonts, etc.)
2. (Optional) If you are using any images or other resource files, add these to the `./content` dir. All files and dirs - except `.html` and `.md` files - will be copied
  * if you want to separate the resource files you can create a sub-directory starting with underscore, for example `_img` or `_res`, and then reference these files using relative links (markdown example: `![image-description](_img/my-image.png)`)

#### Creating a blog and adding blogs and posts

This works in the same way as above, with these exceptions/additions:
* All the contents of the blog is placed in a sub-directory to the *content* directory
* Each blog post will be given a date, which will be displayed and will be used to sort the posts
  * You can add a date at the start of the file name, ex: `2000-01-01_my_blog_post.md`
  * If no date is provided in the name of the file, then the application will read the modification time of the file and use that instead
* Blog posts can have *tags*, they are added by writing the name of the tag at the end of the file name, but before the suffix. For example: `my_blog_post[loving-kindness].md`. It's possible to have several tags for one post


## Directories and files

### `./main.py` file

The main file which is used to start the application and contains all the Python code

### `./themes/` dir

This is the location of the different themes that comes packaged with the application. Using the `--theme-dir` variable you can use a theme from a different directory than this one

#### `[theme-dir]/template.html` file

This file contains the template (or "frame") for each page on the website

In the middle there is a space for inserting code from the files in the `./content` directory

#### `[theme-dir]/style.css` file

CSS file used in the template (so it will be used globally for all output/public files)

### *content* dir

*TODO*

#### `.html` and `.md` files

The content that will be placed inside the template

Supports markdown and html

Html is simply copied into the template. Markdown is transformed to html

Please remember to have one file named `index.html` or `index.md`. This will be used as the home/front page

#### Other files and dirs

These are resource files, for example image files, that will be copied into the `./public` directory

### Output (default: `public`) dir

An output directory where the resulting files and will be placed


## Creating a theme

1. Copy the contents of one of the theme directories under `./themes/` (for example `./themes/clean`) into a new directory to create a base for your own theme
2. Modify the `[your-theme-dir]/template.html` file by adding/modifying header and footer content
3. Modify the `[your-theme-dir]/style.css` file

The website generator works by replacing variables inside the template with html for different pages on the website. The most important variable is `${content}` since this will be the place where (different) content is inserted for each page.

<!--
Typical things you might want to show on each page:
* Website
So typically you might want to add navigation here as well as information about who created the website

guide to how markdown is used, for newbies!
-->

### Template variables

* `content-dir` - This is the most important variable (discussed above------)
* `navigation` - This will automatically be generated from the list of files in the content dir, so that there is a link to each of the pages created for the website


## Hosting on GitLab

Normally the application is meant to be run locally but using a CI/CD system like gitlab you can trigger a job which generates/builds your website.

Please see [this directory](gitlab-website-template) for a group of files which you can copy to your own gitlab website repo.

Once you have the files in place, and a change is made in the repo, the `.gitlab-ci.yml` file is used by the gitlab servers to automatically generate the output html.


<!--
You can have a private repo and still show the contents on a website

Link for user editing of pages

Usage examples

* `edit_url` - This can be used if you want the users to be able to suggests edit to pages on the website. The base of the website content is supplied with the `--content_base_url` argument that the user can add when running `python website-gen-py`

Some tips:
* Good with defaults in `style.css` that work well with without markdown, i.e. when the user doesn't enter any classes or ids for parts of the code (which is not possible for markdown)
* Good to document `style.css` file so it's easy for users to understand

## Hosting options

#### 4a - If you want to run locally

1. Run `python website-gen.py --theme [your-theme]` (if no theme is provided a default theme will be used)
2. This will result in a directory called `./public` to be created in this (base) directory, which contains all the html files generated using the template plus content files (as well as all resource files)
3. You can then upload the `./public` dir to the web space where you want your site to be hosted

#### 4b - If you want to run on the gitlab servers

1. In the `.gitlab-ci.yml` file, edit the line `- python website-gen.py  # --theme [YOUR THEME HERE]` by removing the `#` and entering the name of your theme. (Leaving it as-is a default theme will be used)
2. Simply commit and push any changes to the code and the `.gitlab-ci-yml` file - which is located in this (base) directory - is used to start a "job" on the gitlab servers. This job will run the `website-gen.py` program and publish the results. So you just need to wait for a couple of minutes (the first time may take up to 30 minutes according to gitlab but i haven't seen wait times like this myself) for the job to complete
3. Then the page will be available in the place specified under "Settings" -> "Pages" -> "Access pages", (`https://[your-gitlab-user-name].gitlab.io/[your-gitlab-project-name]/`) --- Please note that you will not have to do any preparatory work in your project settings in gitlab. Everything should be working after having created a new project and pushing these files to that project
-->
