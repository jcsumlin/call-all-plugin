# Reddit Call-All-Plugin

In short I wrote a little python script that scans posts on a subreddit you define and if there is a post that mentions someone it tags them in the comments. If there are more than three users it will create a comment thread with itself calling those users.

## Getting Started

All you need to do is edit the auth.ini.example to hold your correct credentials and ids then save that as auth.ini

### Prerequisites

All of the following packages can be installed with pip from the cmd line

```
pip install praw
pip install re
pip install configparser
```

### Installing

1. Clone/Download the repository.
2. Edit the auth.ini.example and save as auth.ini
3. run the python file!
4. DONE


The program will ask you if you want to turn on debug mode when you run it (1/0) (yes/no) all this will do is tell you when it is sleeping between checks.


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/call-all-plugin/tags). 

## Authors

* **Chat Sumlin** - *Initial work* - [jcsumlin](https://github.com/jcsumlin)

See also the list of [contributors](https://github.com/jcsumlin/call-all-plugin/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to mkgandkembafan on Reddit

