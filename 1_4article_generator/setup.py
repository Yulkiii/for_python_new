import setuptools

with open("README.md", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
  name="bullshit",
  version="0.0.1",
  author="lzjun",
  author_email="lzjun567@gmail.com",
  description="A bullshit text generator",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/lzjun567/BullshitGenerator",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)