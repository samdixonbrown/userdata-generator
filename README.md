<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<h3 align="center">Userdata Generator</h3>

  <p align="center">
    Userdata Generator is a Python based random username, password, email address and name generator. It can be used, for example, when creating fake/test users for Django applications.
  </p>
  <p align="center">
    Userdata Generator includes a random username generator, random email address generator, random password generator and random name generator.
  </p>
  <p align="center">
    <a href="https://github.com/samdixonbrown/userdata-generator/issues">Report Bug</a>
    ·
    <a href="https://github.com/samdixonbrown/userdata-generator/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
```userdata-generator``` is written in pure Python with the only dependencies being core modules ```random``` and ```string```.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The ```userdata-generator``` module is designed to provide convenient functions for generating usernames, passwords, email addresses, and names for test users, for example in a Django application. To integrate this module into your project, follow these steps:

### Step 1: Installation

Simply download or clone the repo.

```sh
git clone https://github.com/samdixonbrown/userdata-generator.git
```

### Step 2: Integration

Copy the ```userdata-generator.py``` file into your Django project's directory or wherever else you intend to use it.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
Import the required functions into your Django views, models or any other relevant files:

```python
from userdata-generator import generate_password, generate_email, generate_username, generate_name, generate_full_name
```

The module contains 5 functions:
- [generate_username()](#generate-username)
- [generate_email()](#generate-email)
- [generate_password()](#generate-password)
- [generate_name()](#generate-name)
- [generate_full_name()](#generate-full-name)

Whilst these are randomly generated and suitable for most small-medium applications, they do not guarantee to be unique. So for very large use-cases, if you need to guarantee uniqueness you may be better using UUID or another similar approach.

Parameters can of course be passed positionally rather than explicitly but for the purposes of this documentation, the explicit form has been used for clarity.

___
### Complete Django example
```python
from myapp.models import CustomUser
from userdata-generator import generate_password, generate_email, generate_username, generate_name


user = CustomUser.objects.create_user(
    username=generate_username(), 
    password=generate_password(), 
    email=generate_email(), 
    first_name=generate_name(), 
    last_name=generate_name()
    )
```
___
<a id="generate-username"></a>

### generate_username(length=None, max_length=20, include_numbers=True, include_specials=False)
If no parameters are passed, by default the function generates a random username of 2 <= ```length``` <= ```max_length``` including numbers but excluding special characters.

```python
generate_username() # qnji1jzs2s5
```

Passing ```max_length``` with no ```length``` will return a username of random length 2 <= ```length``` <= ```max_length```

```python
generate_username(max_length=32) # rdq1jgdvpdkgq
```

Passing a ```length``` parameter will return a username of exactly that length.

```python
generate_username(length=20) # p66cro5syjkib8sabq47
```

Passing ```include_numbers``` or ```include_specials``` as booleans toggles inclusion/exclusion of numbers and special characters ```!#$%&'*+-/=?^_`{|}~.```

```python
generate_username(include_numbers=False, include_specials=True) # xxrjj_w.r{b
```

___
<a id="generate-email"></a>

### generate_email(username_length=None, domain_length=None, tld_length=None, include_specials=False)
Generate a string representing a valid email address in the form ```username@domain.tld```. 

If no parameters are passed, the function returns a random email address with 6 <= ```username_length``` <= 10, 4 <= ```domain_length``` <= 8, and 2 <= ```tld_length``` <= 8.

```python
generate_email() # e6rwjy#v?@eshh.loja
```

```username_length```, ```domain_length```, and ```tld_length``` may be optionally specified, to return an email address with the specified lengths. The function will raise ```ValueError``` if the length parameters passed will exceed 254 characters.

```python
generate_email(username_length=8, domain_length=8, tld_length=2) # 4w720f47@yto1cya0.mq
```

By default, ```include_specials``` is set to False meaning that special characters will not be included in the ```username``` portion of the email address. If you want to include special characters ```!#$%&'*+-/=?^_`{|}~.```, you can set ```include_specials=True```.

```python
generate_email(include_specials=True) # bs%tta+@ek10g0lm.jlw
```

___
<a id="generate-password"></a>

### generate_password(length=None, max_length=32, include_specials=True)
Generates a string representing a password fulfilling the basic requirements:
- 1 Uppercase letter
- 1 Lowercase letter
- 1 Number
- 1 Special character (optional, enabled by default)

If not parameters are passed, the function returns a random password of 8 <= ```length``` <= 32.

```python
generate_password() # A4dY7Ek4[sR_w@k9g~Um2cPiDb0<^
```

If ```length``` is passed, it will return a password of exactly that length.

```python
generate_password(length=12) # v<o$*DOak50{
```

Passing ```max_length``` with no ```length``` will return a password of random length 8 <= ```length``` <= ```max_length```

```python
generate_password(max_length=20) # g(A51WTj
```

You can exlude special characters using ```include_specials=False``` to produce a password with only letters and numbers.

```python
generate_password(include_specials=False) # FVyj39EjxlvA27r
```

___
<a id="generate-name"></a>

### generate_name(length=None, max_length=32)
Generate a capitalized string representing a name. If no parameters are passed, it will return a random string 2 <= ```length``` <=32.

```python
generate_name() # Vrwfsupcefgi
```

Passing ```length``` parameter will return a string of exactly that length.

```python
generate_name(length=16) # Gblemahfatjjhrbc
```

Passing ```max_length``` with no ```length``` will return a random string 2 <= ```length``` <= ```max_length```.

```python
generate_name(max_length=64) # Ywwogyghkjpecehufiecb
```

___
<a id="generate-full-name"></a>

### generate_full_name(firstname_length=None, lastname_length=None, firstname_max_length=32, lastname_max_length=32)
Generate a space-separated string representing a full name.

If no parameters are passed it will return a random string with 2 <= ```firstname_length``` <= 32 and 2 <= ```lastname_length``` <= 32.

```python
generate_full_name() # Yovnsgesshl Akga
```

Passing ```firstname_length``` or ```lastname_length``` parameters will return a string with exactly the specified lengths.

```python
generate_full_name(firstname_length=8, lastname_length=12) # Izmjoalp Uztsiiziyfui
```

Passing ```firstname_max_length``` or ```lastname_max_length``` will return a string with random name lengths between the bounds of 2 and the max lengths.

```python
generate_full_name(firstname_max_length=12, lastname_max_length=24) # Pfufsnrnj Aprcnsjrjqiakfm
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Batch creation functions with guarantee of no duplicates in each function execution


See the [open issues](https://github.com/samdixonbrown/userdata-generator/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See <a href="https://github.com/samdixonbrown/userdata-generator/blob/main/LICENSE">LICENSE</a> for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Sam Brown - [@samdixonbrown](https://twitter.com/samdixonbrown) - sambrowndeveloper@gmail.com

Project Link: [https://github.com/samdixonbrown/userdata-generator](https://github.com/samdixonbrown/userdata-generator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/samdixonbrown/userdata-generator.svg?style=for-the-badge
[contributors-url]: https://github.com/samdixonbrown/userdata-generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/samdixonbrown/userdata-generator.svg?style=for-the-badge
[forks-url]: https://github.com/samdixonbrown/userdata-generator/network/members
[stars-shield]: https://img.shields.io/github/stars/samdixonbrown/userdata-generator.svg?style=for-the-badge
[stars-url]: https://github.com/samdixonbrown/userdata-generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/samdixonbrown/userdata-generator.svg?style=for-the-badge
[issues-url]: https://github.com/samdixonbrown/userdata-generator/issues
[license-shield]: https://img.shields.io/github/license/samdixonbrown/userdata-generator.svg?style=for-the-badge
[license-url]: https://github.com/samdixonbrown/userdata-generator/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/sambrown
[Python]: https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png
[Python-url]: https://www.python.org/