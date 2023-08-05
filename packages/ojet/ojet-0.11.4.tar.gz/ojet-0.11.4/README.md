# Ojet package
 
### Introduction

Oracle JET is a great HTML application builder. The only flaw of this generator is the need to know both HTML and JAVASCRIPT!

This "ojet" package is a Python 3 wrapper around Oracle JET. Its aim is to hide as much as possible the complexity of the HTML and JAVASCRIPT code.

Furthurmore "ojet" can be included in a jupyter notebook in order to add sophisticated HTML views or to help to test an "ojet" application.

### License

"ojet" itself has a GNU general license, but the result of "ojet" must conform to the rules edicted by Oracle about the "Oracle JET" license.

### Installation

Install, upgrade and uninstall ojet with the following commands:

::

    $ pip3 install ojet
    $ pip3 install --upgrade ojet
    $ pip3 uninstall ojet

### Dependencies

None

### Documentation

The best way to understand the "ojet" philosophy is to see the wrapper in action within jupyter. You will learn very easily how to build sophisticated reports with a few lines of code.

The example is [here](http://gduvalsc.github.io/ojet.html).

Outside jupyter the general usage is

::

    oj = Ojet()
    jsparameters = oj.require("knockout")
    ...
    print(oj.render()) # or write the result within an HTML file or generate the page dynamically for any HTTP Python 3 server.

### Warning

"ojet" doesn't include all "HTML" or "Oracle Jet" tags. This first version built over Oracle Jet V11.1.0 is only an example of what can be done with a wrapper. The tool can be easily extended with any tags using examples provided in the package.