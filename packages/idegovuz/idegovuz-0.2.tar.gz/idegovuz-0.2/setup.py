import setuptools

setuptools.setup(
    name='idegovuz',
    version='0.2',
    license='MIT',
    author="Shukrullo Turgunov",
    author_email="sh@turgunov.uz",
    description="id.egov.uz provider for django-allauth",
    keywords=['id.egov.uz', 'id', 'allauth', 'provider'],
    url="https://github.com/vodiylik/allauth-idegovuz",
    packages=setuptools.find_packages(),
    install_requires=['django', 'django-allauth'],
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
