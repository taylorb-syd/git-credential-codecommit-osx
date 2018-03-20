from distutils.core import setup

setup(
    name = 'git-credential-codecommit-osx',
    version = '0.1.0',
    description = 'OS X specific Git Credential Helper',
    long_description = 'Forwards onto either the CodeCommit Credential Helper or the OS X Keychain Credential Helper depending on URL',
    url = 'https://github.com/NightKhaos/git-credential-codecommit-osx',
    author = 'Taylor Bertie',
    author_email = 'nightkhaos@gmail.com',
    license = 'MIT',
    download_url = 'https://github.com/NightKhaos/git-credential-codecommit-osx/archive/0.1.0.tar.gz',
    keywords = [ 'codecommit', 'credential', 'osx', 'mac', 'keychain' ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    packages = [ '' ],
    install_requires = [
        'argparse>=1.4',
        'six>=1.11'
    ],
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, <4',
    scripts = [ 'bin/git-credential-codecommit-osx']
)
