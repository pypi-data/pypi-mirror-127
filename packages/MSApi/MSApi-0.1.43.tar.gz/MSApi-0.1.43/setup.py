import setuptools

setuptools.setup(name='MSApi',
                 version='0.1.43',
                 description='Python API for manage MoySklad',
                 packages=setuptools.find_packages(),
                 install_requires=["requests>=2.22.0"],
                 author_email='serheos@gmail.com',
                 zip_safe=False)

