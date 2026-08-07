# setup.py
from setuptools import setup, find_packages

setup(
    name="iran-free-access",
    version="0.1.0",
    description="Open-source secure internet access for people in Iran",
    author="Your Name",
    author_email="your-email@example.com",
    packages=find_packages(),
    install_requires=[
        # Add dependencies here
    ],
    entry_points={
        'console_scripts': [
            'iran-free=client:main',
        ],
    },
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
