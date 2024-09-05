from setuptools import find_packages, setup

AUTHOR = "Dark Circles"
VERSION = "1.1.0"
SHORT_DESCRIPTION = "A Flowmodoro Timer CLI for producitivity enthusiasts."
AUTHOR_EMAIL = (
    "<nibir@nibirsan.org>, <jonakadiptakalita@gmail.com>, <anubhavnath60@gmail.com>"
)
URL = "https://github.com/moiSentineL/flomo"
INSTALL_REQUIRES = [
    "click",
    "blessed",
    "rich",
    "playsound==1.2.2",
    "click-aliases",
]
PROJECT_URLS = {
    "Documentation": "https://github.com/moiSentineL/flomo#flomo",
    "Issue tracker": "https://github.com/moiSentineL/flomo/issues",
}
KEYWORDS = ["cli", "productivity", "cli-application"]
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
]

with open("docs/README.md", "r", encoding="utf-8") as fh:
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
        include_package_data=True,
        package_data={"flomo": ["flomo/beep.mp3"]},
    )
