File Sculpt
v. 0.0.3

This python module abstracts finding and replacing certain portions of a file through regular expressions. It is a class that creates abstraction of the inner workings of opening and closing a file when finding and replacing its contents.

CLASS DEFINITION:

Sculptfile( <positional arg> tofind : re , <positional arg> replacewith : list, <positional arg> inpath : str, <optional positional arg> outpath : str)

CLASS ARGUMENTS:

tofind - is of type re or regular expression which is used to find/define portions of the file to be replaced with

See https://docs.python.org/3/howto/regex.html for more info on regular expressions

replacewith - is a list that should contain either a string or an integer. This list will be rendered in ascending order as replacement for the objects found through regex. An integer refers to the grouping order in a regex query.

For example:

If a file contains 'The quick brown fox' and after regex operations (quick,fox) is obtained, The file's contents can be replaced by assigning a replacewith list formatted as ["A ",0," yellow ",1]. The integers' 0 and 1 represent quick and fox, and when rendered 'A quick yellow fox' is obtained

inpath - is a string filepath for the file to be read

outpath - is an optional string filepath for the file to be written after operations are done. If not specified the inpath is set as the outpath and changes will overwrite the file.

CLASS METHODS:

scuttle() - opens the file specified by inpath as read and returns the regular expression findall() list of the tofind argument

sculpt() = executes the scuttle method and then executes the replacement specified by replacewith. Writes the result to the file specified in outpath

USAGE:

Define an object of class Sculptfile given the parameters above. Execute sculpt() method on the object.

EXAMPLE:

    Given a file foo.txt containing the text 'A quick brown fox jumps under the lazy dog.', we want the text to become "The quick brown fox jumps over the lazy dog"and save it to another file, foorect.txt.

    ```python

        from fileSculpt.filesculpt import Sculptfile

        a = Sculptfile(r'^(A).+',["The",0],'foo.txt','foorect.text')
        a.sculpt()

    ```

PATCHES:

v. 0.0.2 :

    - changed path keyword arguments into positional arguments.
    - fixed bug of grouping when only one group is specified in the regex by adding a default grouping at the end of the inputted regex

v. 0.0.3 :

    - fixed optional argument output path.
    - now allows paths to refer to files in the same directory without specifying the whole path
