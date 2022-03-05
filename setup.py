from setuptools import setup, find_packages

# Setting up
setup(
        name='altair_reveal', 
        version='0.0.3',
        author='Soo Oh',
        author_email='soh@revealnews.org',
        description='Reveal theme for Altair library',
        long_description='Reveal theme for the Altair statistical visualization library.',
        long_description_content_type='text/x-rst',
        url='http://www.github.com/cirlabs/altair-theme-reveal',
        license='MIT',
        packages=find_packages(),
        install_requires=['altair'],
        keywords=['python', 'altair', 'theme', 'cir', 'reveal', 'investigative'],
        classifiers= [
            'Development Status :: 4 - Beta',
            'Intended Audience :: Other Audience',
            'Programming Language :: Python :: 3',
            'Operating System :: MacOS :: MacOS X',
            'License :: OSI Approved :: MIT License',
        ]
)