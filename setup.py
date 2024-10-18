from setuptools import setup, find_packages

setup(
    name="violent_reductioniser",
    description="A tool to compress and reduce video files violently using FFmpeg.",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "violent_reductioniser = run:main",
        ]
    },
    author="Arsalan 'Aeri' Kazmi",
    license="GPL-3.0-or-later",
)
