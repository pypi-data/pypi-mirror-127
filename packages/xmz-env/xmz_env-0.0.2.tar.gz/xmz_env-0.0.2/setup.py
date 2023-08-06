import setuptools
from  pathlib import Path

setuptools.setup(
          name='xmz_env',
          version='0.0.2',
          description="just for fun",
          long_description=Path("README.md").read_text(),
          long_description_content_type="text/markdown",
          packages=setuptools.find_packages(include="xmz_env*"),
          install_requires=['gym']
)