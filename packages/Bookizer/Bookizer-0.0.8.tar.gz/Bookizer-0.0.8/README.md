**Bookizer**

It's a quick tool to convert any number of csvs into one big calc book, being it another CSV, a XLS, XLSX or ODS.

It depends on pandas and other libraries.


* Free software: BSD license
* For Python 3.6+
* Changelog: https://github.com/JustDevZero/Bookizer/releases
* Code, issues, tests: https://github.com/JustDevZero/Bookizer


----

**HOW TO INSTALL IT?**

Make sure to dedicate a virtualenv only for Bookizer so it won't mess up with whatever you have on your system.


Create a virtualenv for python3.6 onwards, we tried with 3.9 and it worked like a charm:

```virtualenv --python /usr/bin/python3.9  ~/.virtualenvs/bookizer```

```source ~/.virtualenvs/bookizer/bin/activate```

```python -m pip install git+https://github.com/JustDevZero/bookizer.git```

Now, add symbolic link somewhere in your path *bookizer* command, for example:

```ln -s ~/.virtualenvs/bookizer/bin/bookizer ~/.local/bin/bookizer```

----

**How to use it?**

It's easy as fuck, just type from anywhere of your terminal, something like that:

```bookizer --from one.csv --from one_folder_full_of_csvs --to one_big_file.ods```

And that's it. Pretty easy.
