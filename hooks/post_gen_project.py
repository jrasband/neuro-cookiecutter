help = """
Your project has been created!

If you have not done so already, create a conda environment for your new 
project with:

cd {{cookiecutter.repo_name}}
conda create --name {{cookiecutter.repo_name}} python=3.x
conda activate {{cookiecutter.repo_name}}
conda env export > environment.yml

Install your new project in your local conda environment with:

pip install -e .

You will need to manually add data to .gitignore to prevent it from syncing to
version control.

Don't forget to sync to GitHub. Have fun!
"""
print(help)
