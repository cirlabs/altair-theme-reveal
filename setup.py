from setuptools import setup, find_packages

# Setting up
setup(
        name='altair_reveal', 
        version='0.0.1',
        author='Soo Oh',
        author_email='soh@revealnews.org',
        description='Reveal theme for Altair library',
        url='http://www.github.com/cirlabs/altair-theme-reveal',
        license='MIT',
        packages=find_packages(),
        install_requires=['altair'],
        keywords=['python', 'altair', 'theme', 'cir', 'reveal', 'investigative'],
        classifiers= [
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Education',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'License :: OSI Approved :: MIT License',
        ]
)