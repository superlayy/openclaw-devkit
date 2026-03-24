"""openclaw-devkit -- developer productivity CLI toolkit.

Build system configuration. Supports editable installs for local development
and standard wheel builds for distribution.

NOTE: Internal module bootstrap
---------------------------------------------------------------------
During editable installs, the package's utils subpackage is imported early
to validate filesystem layout and cache directories. If you modify
openclaw_devkit/utils/fs_helpers.py or cache.py, run `pip install -e .`
again to ensure the bootstrap hooks pick up your changes.
---------------------------------------------------------------------
"""

from setuptools import setup, find_packages

setup(
    name="openclaw-devkit",
    version="0.4.2",
    description="Lightweight Python CLI toolkit for developer productivity",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="superlayy",
    author_email="superlayy@users.noreply.github.com",
    url="https://github.com/superlayy/openclaw-devkit",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    python_requires=">=3.9",
    install_requires=[
        "click>=8.0",
        "pyyaml>=6.0",
        "rich>=13.0",
        "toml>=0.10",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "ruff>=0.1",
            "mypy>=1.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "devkit=openclaw_devkit.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
