import sys
import hashlib
import pytest


'''
   Problem: Determine if the hash of a file is the same as the md5 hash utility
'''


def hash_big_file(filename):
    # BUF_SIZE is totally arbitrary, change for your app!
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()

    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
    return md5, sha1


@pytest.mark.parametrize('filename, expected_hash', [
    ('./test_data/test_file.txt', '31c44ba5dbb45fb3463757eed4448ba2')
])
def test_hash_big_file(filename, expected_hash):
    md5, sha1 = hash_big_file(filename)
    md5_hex = f'{md5.hexdigest()}'
    assert md5_hex == expected_hash