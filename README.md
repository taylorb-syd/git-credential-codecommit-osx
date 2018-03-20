# git-credential-codecommit-osx
This is a script that can be used to replace the default credential helper in OS X. It makes a decision based on the provided 'host' as to which helper it should use.

It will either send the request to the default (the keychain) credential helper, or for CodeCommit repos, bypass that completely and only use the AWS CodeCommit Credential Helper.

This has an advantage to setting up the credential helper such that CodeCommit always runs before the keychain in that it will not end up populating the keychain with CodeCommit credentials.

## Installation

git-credential-codecommit-osx can be found under PyPI at [https://pypi.python.org/pypi/git-credential-codecommit-osx](https://pypi.python.org/pypi/git-credential-codecommit-osx).

To install:

    pip install git-credential-codecommit-osx

## Usage

To set this as the default system level credential helper, use the following commands:

    git config --system --unset-all credential.helper
    git config --system --add credential.helper '!git-credential-codecommit-osx $@'

## Profile

Since you may want to use specific IAM credentials for your CodeCommit integrations, to set the profile use the following command instead:

    git config --system --add credential.helper '!git-credential-codecommit-osx --profile CodeCommitProfile $@'
