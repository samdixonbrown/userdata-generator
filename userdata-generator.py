import random
import string

'''
Some simple utility functions for creating pseudo random user data. 
For example these can be useful when creating test/fake users for Django applications.
See https://github.com/samdixonbrown/userdata-generator/blob/main/README.md for documentation and usage examples.
'''

def generate_username(length=None, max_length=20, include_numbers=True, include_specials=False):
    '''
    Generate a string representing a username. Optional numbers and special characters
    '''
    if length is None:
        # Skew the likely usernamename length towards shorter names
        length = int(random.triangular(2, 12, max_length))
    
    # Validate parameters
    if not isinstance(length, int) or not isinstance(max_length, int):
        raise ValueError("Length parameters must be integers")
    
    if not isinstance(include_numbers, bool) or not isinstance(include_specials, bool):
        raise ValueError("include_numbers and include_specials must be boolean True/False")
    
    if length > max_length:
        raise ValueError("Length must not be greater than max_length")

    return generate_random_string(length, include_numbers, include_specials)


def generate_email(username_length=None, domain_length=None, tld_length=None, include_specials=False):
    '''
    Generate a string representing an email address in the form `username@domain.tld`
    '''
    if username_length is None:
        username_length = random.randint(6, 10)
    
    if domain_length is None:
        domain_length = random.randint(4, 8)
    
    if tld_length is None:
        tld_length = random.randint(2, 8)
    
    # Validate parameter types
    if not isinstance(username_length, int) or not isinstance(domain_length, int) or not isinstance(tld_length, int):
        raise ValueError("Length parameters must be integers")
    
    if not isinstance(include_specials, bool):
        raise ValueError("include_specials must be boolean True/False")

    # Maximum total email address length is 254. Subtracting 1 for @ gives max 253
    if (username_length + domain_length + tld_length) > 253:
        raise ValueError("Total email address length must not be greater than 254 including @ symbol")
    
    # Username part must be between 1 and 64 chars
    if username_length < 1 or username_length > 64:
        raise ValueError("username_length must be between 1 and 64")
    
    # Given min username length of 1, @ symbol, and min tld of 2, max domain length is 250
    if domain_length < 1 or domain_length > 250:
        raise ValueError("domain_length must be between 1 and 250")
    
    # Tld must be at least 2 chars and less than 64
    if tld_length < 2 or tld_length > 64:
        raise ValueError("tld_length must be between 2 and 64")

    return f"{generate_random_string(username_length, include_numbers=True, include_specials=include_specials)}@{generate_random_string(domain_length, include_numbers=True)}.{generate_random_string(tld_length)}"


def generate_password(length=None, max_length=32, include_specials=True):
    '''
    Generate a string representing a password. Fulfils the basic requirements of:
    - 1 Uppercase letter
    - 1 Lowercase letter
    - 1 Number
    - 1 Special character (optional, enabled by default)
    '''

    if length is None:
        length = random.randint(8, max_length)
    
    # Check we're being passed an integer value for length parameters
    if not isinstance(length, int) or not isinstance(max_length, int):
        raise ValueError("Password length and max_length must be integers")
    
    # Check we're being passed a boolean value for include_specials
    if not isinstance(include_specials, bool):
        raise ValueError("include_specials must be a boolean True/False")
    
    # Length validation
    if length < 8 or length > max_length:
        raise ValueError(f"Password length must be between 8 and {max_length} characters")

    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    special_characters = "!@#$%^&*()_+[]{}|;:,.<>?~"
    numbers = string.digits

    # Determine the character set to use
    character_set = lowercase_letters + uppercase_letters + numbers
    if include_specials:
        character_set += special_characters

    # Ensure at least one character from each category
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(numbers)
    ]

    if include_specials:
        password.append(random.choice(special_characters))
    
    # Now that we have filled the basic requirements of uppercase, lowercase etc,
    # complete the rest of the password
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(character_set))

    # Shuffle the password characters
    random.shuffle(password)

    return "".join(password)


def generate_name(length=None, max_length=32):
    '''
    Generate a capitalized string representing a name
    '''

    if length is None:
        # Skew the likely name length towards shorter names
        length = int(random.triangular(2, 12, max_length))
    
    # Check we're being passed an integer value for length parameters
    if not isinstance(length, int) or not isinstance(max_length, int):
        raise ValueError("length and max_length must be integers")

    if length < 1 or length > max_length:
        raise ValueError(f"length must be between 1 and {max_length} characters")
    return generate_random_string(length).capitalize()


def generate_full_name(firstname_length=None, lastname_length=None, firstname_max_length=32, lastname_max_length=32):
    '''
    Generate a space-separated string representing a full name
    '''

    if firstname_length is None:
        # Skew the likely name length towards shorter names
        firstname_length = int(random.triangular(2, 10, firstname_max_length))
    
    if lastname_length is None:
        # Skew the likely name length towards shorter names
        lastname_length = int(random.triangular(2, 10, lastname_max_length))

    # Validate parameters
    if not isinstance(firstname_length, int) or not isinstance(lastname_length, int) or not isinstance(firstname_max_length, int) or not isinstance(lastname_max_length, int):
        raise ValueError("length parameters must be integers")

    if firstname_length < 1 or lastname_length < 1:
        raise ValueError("Name lengths must be at least 1 character")
    
    if firstname_length > firstname_max_length or lastname_length > lastname_max_length:
        raise ValueError("Name lengths must be less than max lengths")

    return f"{generate_name(firstname_length)} {generate_name(lastname_length)}"


def generate_random_string(length, include_numbers=False, include_specials=False):
    '''
    Generate a random string of lowercase ASCII letters with optional numbers and special characters
    '''

    # Validate parameters
    if not isinstance(length, int):
        raise ValueError("length parameter must be an integer")
    
    if not isinstance(include_numbers, bool) or not isinstance(include_specials, bool):
        raise ValueError("include_numbers and include_specials must be boolean True/False")

    if length < 1:
        raise ValueError("length parameter must be at least 1")

    # Form set of characters to choose from
    character_set = string.ascii_lowercase
    if include_specials:
        character_set += "!#$%&'*+-/=?^_`{|}~."
    
    if include_numbers:
        character_set += string.digits

    return ''.join(random.choice(character_set) for i in range(length))