import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
fh.close()

setuptools.setup(
    name="webhook-client",
    version="1.0.2",
    author="ElijahGives",
    author_email="elijahgives13@gmail.com",
    description="A discord webhook client written in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ElijahGives/discord-webhook",
    license="LICENSE",
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
         "Operating System :: OS Independent",
     ],
    packages=["webhook_client"],
    install_requires=[
        "requests",
        "typing"
    ]
)