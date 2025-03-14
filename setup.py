from setuptools import setup, find_packages

setup(
    name='chbencode',
    version='1.0.0',
    author='SimonB',
    author_email='py.simonbolivar@gmail.com',
    description='Encode string data by zlib, base64 invert',
    url='https://github.com/SimonBolivarPy',
    packages=find_packages(),
    install_requires=[
        # Здесь перечислите зависимости вашего пакета, например:
        # 'requests>=2.25.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
