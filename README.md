# A Scrapy Framework Powered Scraper for 3 websites 
> Scraper to crawl and take data from 3 website 

[![Python Version][python-image]][python-url]
[![Scrapy Version][scrapy-image]][scrapy-url]


Its a Scraper that self aware to take into account of any given website 
(www.wellness.com , www.healthgrades.com , www.md.com/doctors) 
and take actions depending on the website and output the data into specified csv or xlsx
format.

## Installation & Setup & Usage

OS X & Linux & Windows:

open a terminal and clone the git repo or download the repo
```bash
git clone https://github.com/PandorAstrum/Doctor-Scraper.git
```
go to the root folder of the project and on the terminal run
```
pip install requirements.txt
```
to use any scraper just supply the generated url list from the website
into the ``configure.py`` file and on terminal 
```commandline
scrapy runspider docotrs\spiders\doctordata.py
```

###Notes:
- depending on the website it will take actions to crawl on these 3 specific website
- the scraper will output the data into specified format depending the configuration
- the ```configure.py``` file is responsible to tweak or change any settings of the scraper
- all generated file can be found on ```Dump``` folder of this project upon scrapping done

## Release History

* 0.6.0
    * ADD: Instructions added for future use
* 0.5.0
    * Full Scraper ready
* 0.4.0
    * ADD: `configure.py` file created for easy tweaking of settings
* 0.3.0
    * Add: More functionality to adapt with the other two website automatically
* 0.2.0
    * The first website crawling done successfully
* 0.1.0
    * Work in progress Scrapy framework based scraper added

## Meta

Ashiquzzaman Khan – [@dreadlordn](https://twitter.com/dreadlordn)

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/PandorAstrum/Doctor-Scraper](https://github.com/PandorAstrum/Doctor-Scraper)

## Contributing

1. Fork it (https://github.com/PandorAstrum/Doctor-Scraperfork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[python-image]: https://img.shields.io/badge/Python-3.6-yellowgreen.svg?style=flat-square
[python-url]: https://www.python.org/

[scrapy-image]: https://img.shields.io/badge/Scrapy-1.5-orange.svg?style=flat-square
[scrapy-url]: https://scrapy.org/

