import os

def update_readme():
  with open('README.md', 'w') as readme:
    readme.write("#Update README\n")
    readme.write("This README is automatically updated for each realease. \n")

if _name_ == "_main_":
  update_readme()
