import dtlpy as dl
import sys
import os


def test_login():
    env_name = 'rc'
    dl.setenv(env_name)
    if env_name in ['rc']:
        username = os.environ["TEST_USERNAME"]
        password = os.environ["TEST_PASSWORD"]
    else:
        raise ValueError('unknown env alias: {}'.format(env_name))
    dl.login_m2m(
        email=username,
        password=password
    )
    print(dl.info())
    if dl.token_expired():
        print('Token Expired')
        sys.exit(1)
    else:
        print('Success')
        sys.exit(0)


if __name__ == "__main__":
    test_login()
