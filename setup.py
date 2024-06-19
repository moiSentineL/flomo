import setuptools

AUTHOR = "Dark Circles"
VERSION = "0.0.1"
SHORT_DESCRIPTION = ""  # TODO: Add short description
AUTHOR_EMAIL = "<nibir@nibirsan.org>"
URL = "https://github.com/moiSentineL/flomo"
INSTALL_REQUIRES = [i.strip() for i in open("requirements.txt").readlines()]
PROJECT_URLS = {
    "Documentation": "https://github.com/moiSentineL/flomo#flomo",
    "Issue tracker": "https://github.com/moiSentineL/flomo/issues",
}
KEYWORDS = ["cli", "productivity", "cli-application"]
CLASSIFIERS = [
    "Development Status :: 1 - Development/Planning",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

if __name__ == "__main__":
    setuptools.setup(
        name="flomo",
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        description=SHORT_DESCRIPTION,
        long_description_content_type="text/markdown",
        long_description=LONG_DESCRIPTION,
        packages=setuptools.find_packages(),
        install_requires=INSTALL_REQUIRES,
        url=URL,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
    )
