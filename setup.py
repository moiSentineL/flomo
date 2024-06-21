from setuptools import setup, find_packages

AUTHOR = "Dark Circles"
VERSION = "0.0.1.0a1"
SHORT_DESCRIPTION = "A Flowmodoro CLI for producitivity enthusiasts."
AUTHOR_EMAIL = "<nibir@nibirsan.org>"
URL = "https://github.com/moiSentineL/flomo"
INSTALL_REQUIRES = ["click", "blessed", "rich"]
PROJECT_URLS = {
    "Documentation": "https://github.com/moiSentineL/flomo#flomo",
    "Issue tracker": "https://github.com/moiSentineL/flomo/issues",
}
KEYWORDS = ["cli", "productivity", "cli-application"]
CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    'License :: OSI Approved :: MIT License',
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

if __name__ == "__main__":
    setup(
        name="flomodoro",
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        description=SHORT_DESCRIPTION,
        long_description_content_type="text/markdown",
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=INSTALL_REQUIRES,
        url=URL,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        entry_points={
            "console_scripts": [
                "flomo = flomo.cli:flomo",
            ],
        },
    )
