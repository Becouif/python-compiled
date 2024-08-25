import requests
import sys
import hashlib


# use SHA1 Hash Generator is what the api is using
# and add only the first 5 characters


# this is how to make API get request call in py
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    # since if we print res we get status code
    if res.status_code != 200:
        raise RuntimeError(f'error fetching: {res.status_code}, check api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines)
    print(hashes)
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

# this function hash a string passwords
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # check password if it exist in API response
    first5_char, tail = sha1password[:5], sha1password[5:]
    # here we put the first 5 char
    response = request_api_data(first5_char)
    # print(response)
    return get_password_leaks_count(response,tail)



def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password')
        else:
            print(f'{password} was NOT found. Carry on!')

    return 'done!'


# main(sys.argv[1:])

print(pwned_api_check('hello'))

# make it be readable from text file instead of command line
# finally do sys exit too