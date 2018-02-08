# IMDb Top Chart

Scraping [IMDb top chart](http://www.imdb.com/chart/top) using [Python](https://www.python.org/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to install `Python 3.x` in you local machine. Follow the link based on your OS. 

```
Python 3 is pre-installed in some distributions of Linux and Mac. 
Windows user make sure you add Python to your path. 
```

  * [Linux](https://www.google.com.np/search?ei=KE98WtSTKMr9vgS_xIWwDg&q=install+python+3+in+linux&oq=install+python+3+in+linux&gs_l=psy-ab.3..0i7i30k1l5j0j0i8i7i30k1j0i30k1j0i7i5i30k1j0i8i30k1.27508.27878.0.28549.2.2.0.0.0.0.197.387.0j2.2.0....0...1c.1.64.psy-ab..0.2.385....0.f4opmPXkmVo)
  * [Windows](https://www.google.com.np/search?ei=Ak98WsOiAYHnvgTHjYywAw&q=install+python+3+in+windows&oq=install+python+3+in+windows&gs_l=psy-ab.3..0l3j0i5i30k1j0i8i30k1.59921.60248.0.61023.2.2.0.0.0.0.181.355.0j2.2.0....0...1c.1.64.psy-ab..0.2.354...0i7i30k1j0i13k1j0i8i7i30k1j0i7i5i30k1.0.3m_2cqTXhsE)
  * [Mac](https://www.google.com.np/search?ei=L098WqDAEYXZvgSd36eIDg&q=install+python+3+in+mac&oq=install+python+3+in+mac&gs_l=psy-ab.3..0i7i30k1j0i20i263k1j0i7i5i30k1j0i8i10i30k1.26171.26641.0.27250.2.2.0.0.0.0.209.397.0j1j1.2.0....0...1c.1.64.psy-ab..0.2.397...0j35i39k1j0i5i30k1.0.5QALEmXNZxY)
  
Once Python is installed, you will need to install git in order to be able to clone the repository. Thankfully, we have a good tutorial [here](https://www.atlassian.com/git/tutorials/install-git).


###Cloning the repository

This is probably the simplest way to clone the repository to your local machine. 
```
git clone https://github.com/webscrape/IMDb_top_x.git 
```

You will see a directory named IMDb_top_x with all the files.


### Installing Libraries

You will need to install some libraries to run the script. To make it easy, we have created a requirements.txt file for you. All you need to do is naviagate into the project directory and run the following command.

```
pip install -r requirements.txt
```

In Linux and Mac, you may have both `python2` and `python3` installed. In such case, use the following command.

```
pip3 install -r requirements.txt
```

End with an example of getting some data out of the system or using it for a little demo

### Running the script

Once you have installed and setup everything, running the script is fairly simple. All you need to do is run the following command.

```
python imdb_top_x.py
```

You might need to use `python3` instead of `python` for the same reason you used `pip3` instead of `pip` to install requirements.

When you run the above command, the script will scrape the top 10 movies by default. You can also specify the number from command line. Th value should be between 1 to 250.

For example, to scrape first 50 movies
```
python imdb_top_x.py 50
```

The output will be displayed on the terminal or cmd and saved to `top.csv`