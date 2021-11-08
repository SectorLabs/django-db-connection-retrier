import distutils.cmd
import os
import subprocess

from setuptools import find_packages, setup


class BaseCommand(distutils.cmd.Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


def create_command(text, commands):
    """Creates a custom setup.py command."""

    class CustomCommand(BaseCommand):
        description = text

        def run(self):
            for cmd in commands:
                subprocess.check_call(cmd)

    return CustomCommand


with open(
    os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8"
) as readme:
    README = readme.read()


setup(
    name="django-db-connection-retrier",
    version="1.0",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    license="MIT License",
    description="Automatically ty re-establishing the Django database connection when it gets lost.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/SectorLabs/django-db-connection-retrier",
    author="Sector Labs",
    author_email="open-source@sectorlabs.ro",
    keywords=["django", "postgres", "extra", "hstore", "ltree"],
    install_requires=["aspectlib>=1.4.2,<2.0", "Django>=2.0"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
    ],
    cmdclass={
        "lint": create_command(
            "Lints the code",
            [
                ["flake8", "setup.py", "dbconnectionretrier", "tests"],
                ["pycodestyle", "setup.py", "dbconnectionretrier", "tests"],
            ],
        ),
        "lint_fix": create_command(
            "Lints the code",
            [
                [
                    "autoflake",
                    "--remove-all-unused-imports",
                    "-i",
                    "-r",
                    "setup.py",
                    "dbconnectionretrier",
                    "tests",
                ],
                [
                    "autopep8",
                    "-i",
                    "-r",
                    "setup.py",
                    "dbconnectionretrier",
                    "tests",
                ],
            ],
        ),
        "format": create_command(
            "Formats the code",
            [["black", "setup.py", "dbconnectionretrier", "tests"]],
        ),
        "format_verify": create_command(
            "Checks if the code is auto-formatted",
            [["black", "--check", "setup.py", "dbconnectionretrier", "tests"]],
        ),
        "format_docstrings": create_command(
            "Auto-formats doc strings", [["docformatter", "-r", "-i", "."]]
        ),
        "format_docstrings_verify": create_command(
            "Verifies that doc strings are properly formatted",
            [["docformatter", "-r", "-c", "."]],
        ),
        "sort_imports": create_command(
            "Automatically sorts imports",
            [
                ["isort", "setup.py"],
                ["isort", "-rc", "dbconnectionretrier"],
                ["isort", "-rc", "tests"],
            ],
        ),
        "sort_imports_verify": create_command(
            "Verifies all imports are properly sorted.",
            [
                ["isort", "-c", "setup.py"],
                ["isort", "-c", "-rc", "dbconnectionretrier"],
                ["isort", "-c", "-rc", "tests"],
            ],
        ),
        "fix": create_command(
            "Automatically format code and fix linting errors",
            [
                ["python", "setup.py", "format"],
                ["python", "setup.py", "format_docstrings"],
                ["python", "setup.py", "sort_imports"],
                ["python", "setup.py", "lint_fix"],
            ],
        ),
        "verify": create_command(
            "Verifies whether the code is auto-formatted and has no linting errors",
            [
                [
                    ["python", "setup.py", "format_verify"],
                    ["python", "setup.py", "format_docstrings_verify"],
                    ["python", "setup.py", "sort_imports_verify"],
                    ["python", "setup.py", "lint"],
                ]
            ],
        ),
    },
)
