# # MORPHOLOGICALLY RICH LANGUAGES WITH HFST TOOLS - LECTURE 1
#
# <ul>
# <li>1. <a href="#1.-Prerequisites">Prerequisites</a></li>
# <li>2. <a href="#2.-Course-material">Course material</a></li>
# <li>3. <a href="#3.-Course-overview">Course overview</a></li>
# <li>4. <a href=""></a></li>
# <li>5. <a href=""></a></li>
# <li>6. <a href=""></a></li>
# <li>7. <a href=""></a></li>
# </ul>
#
# ## HFST - Helsinki Finite-State Technology
#
# The HFST toolkit is intended for processing natural language
# morphologies. The toolkit is demonstrated by wide-coverage
# implementations of a number of languages of varying morphological
# complexity. HFST is written mainly in C++, but there is also a Python interface
# which is demonstrated on these notebooks.
#
# ## 1. Prerequisites
#
# <ul>
# <li>Foundations of general linguistics</li>
# <li>Basic knowledge on how to use a computer</li>
# <li>Some programming experience is desirable</li>
# <li>Knowledge of Natural Language Processing (NLP) is also a plus</li>
# </ul>
#
# ## 2. Course material
#
# If you want a book:
#
# <ul>
# <li>Kenneth R. Beesley and Lauri Karttunen: <a href="http://press.uchicago.edu/ucp/books/book/distributed/F/bo3613750.html">Finite State Morphology</a>, CSLI Publications, 2003</li>
# <li>Daniel Jurafsky and James H. Martin, Speech and Language Processing, Prentice Hall, second edition, 2009</li>
# </ul>
#
# Links:
#
# <ul>
# <li>HFST <a href="https://hfst.github.io">main page</a>.</li>
# <li>For installation of the HFST package for Python, see our <a href="https://pypi.org/project/hfst_dev/">PyPI pages</a>.</li>
# <li>For more information about the interface, see our <a href="https://github.com/hfst/python-hfst-4.0/wiki">Github wiki pages</a>.</li>
# </ul>
#
# First, import the package and list its contents with `help`.

import hfst_dev
help(hfst_dev)

# Then, see for more information on some of the functions, e.g. `compile_lexc_file`.

help(hfst_dev.compile_lexc_file)

# Also print the version number of the package.

print(hfst_dev.__version__)

# ## 3. Course overview
#
# <table>
# <tr> <th>Lecture</th> <th>Topics</th> </tr>
# <tr> <td>1</td> <td>Course intro, field overview, majority vs minority language technology</td> </tr>
# <tr> <td>2</td> <td>Intro to the Giella infra and a variety of finite-state tasks, stress on reusability and language independence</td> </tr>
# <tr> <td>3</td> <td>Simple lexc (numerals, dates, clocks)</td> </tr>
# <tr> <td>4</td> <td>Lexc (practices and automated documentation) (production and reuse of test materials for development of analysers/generators)</td> </tr>
# <tr> <td>5</td> <td>Twolc & xfst rewrite rules</td> </tr>
# <tr> <td>6</td> <td>Shared language-independent modeling (examples from Saamic languages, perhaps hierarchical)</td> </tr>
# </table>
