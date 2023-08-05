from setuptools import setup, find_namespace_packages


def _read(filename: str) -> str:
    """
    Reads in the content of the file.

    :param filename:    The file to read.
    :return:            The file content.
    """
    with open(filename, "r") as file:
        return file.read()


setup(
    name="wai.annotations.tf",
    description="Tensorflow format plugins for wai.annotations.",
    long_description=f"{_read('DESCRIPTION.rst')}\n"
                     f"{_read('CHANGES.rst')}",
    url="https://github.com/waikato-datamining/wai-annotations-tf",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Programming Language :: Python :: 3',
    ],
    license='Apache License Version 2.0',
    package_dir={
        '': 'src'
    },
    packages=find_namespace_packages(where='src'),
    namespace_packages=[
        "wai",
        "wai.annotations"
    ],
    version="1.2.0",
    author='Corey Sterling',
    author_email='coreytsterling@gmail.com',
    install_requires=[
        "wai.annotations.core>=0.1.1",
        "tensorflow>=2.6.0,<2.7.0",
        "numpy<1.20"
    ],
    entry_points={
        "wai.annotations.plugins": [
            # Image Object Detection Formats
            "from-tf-od=wai.annotations.tf.specifier:TFRecordsInputFormatSpecifier",
            "to-tf-od=wai.annotations.tf.specifier:TFRecordsOutputFormatSpecifier",
        ]
    }
)
