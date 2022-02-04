
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()


def install_requirements():
    return [package_string.strip() for package_string in open('requirements.txt', 'r')]


def package_description():
    text = open('README.md', 'r').read()
    return text


setup(name='pygamerule',
      version="0.0.1a1",
      description="Base class for board game rules",
      long_description=package_description(),
      long_description_content_type='text/markdown',
      classifiers=[
          "Topic :: Games/Entertainment :: Board Games",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Software Development :: Version Control :: Git",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "License :: OSI Approved :: MIT License",
          "Intended Audience :: Developers"
      ],
      keywords="board games",
      url="https://github.com/stephenhky/PyGameRule",
      author="Kwan-Yuet Ho",
      author_email="stephenhky@yahoo.com.hk",
      license='MIT',
      packages=['pygamerule'],
      install_requires=install_requirements(),
      tests_require=[
          'unittest2',
      ],
      include_package_data=True,
      test_suite="test",
      zip_safe=False)
