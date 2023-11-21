from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="ai-note-taker",
    version="0.1.3",
    author="Stefan Rummer",
    author_email="",
    description="Record audio from microphone and chat with taken notes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stefanrmmr/streamlit-audio-recorder",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        "streamlit>=0.63",
    ],
)
