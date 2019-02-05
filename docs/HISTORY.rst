Changelog
=========

3.0 (unreleased)
----------------

- Add support for Python 3

Backwards incompatible changes
++++++++++++++++++++++++++++++

* In Python 2, if you call the ``SoupStrainer`` instance with a 
  string, the result will be a string again, instead of unicode.


2.0 (2017-10-19)
----------------

Backwards incompatible changes
++++++++++++++++++++++++++++++

* Update to beautifulsoup4.

* Add a parameter ``parser`` to ``SoupStrainer`` which specifies the parser
  used by beautifulsoup4.


1.0 - 2008-11-14
----------------

* Initial release

