from setuptools import setup

setup(
    name="texttoaudio",
    packages=["application"],
    description=["A simple package"],
    long_description=open("README.md").read(),
    install_requires=["pyttsx3", "trafilatura"]
)