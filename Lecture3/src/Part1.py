# # MORPHOLOGICALLY RICH LANGUAGES WITH HFST TOOLS - LECTURE 3
#
# Topics: simple lexc (numerals, dates, clocks)
#
# <ul>
# <li>1. <a href="#1.-Lexc-formalism">Lexc formalism</a></li>
# <li>2. <a href="#2.-Numerals">Numerals</a></li>
# <li>3. <a href="#3.-Dates">Dates</a></li>
# <li>4. <a href="#4.-Clocks">Clocks</a></li>
# </ul>

# ## 1. Lexc formalism
#
# A lexc file/script consists of lexicons with one or more entries. The entries can have a continuation
# lexicon defined. There must be one lexicon named `Root` which is the root lexicon. The entries can be
# given as strings or regular expressions.
#
# Below is a lexc file with a root lexicon with one entry ('cat') that has no continuation lexicon.
# Keyword `LEXICON` defines a lexicon and `#` after an entry means that the entry has no continuation lexicon.

from hfst_dev import compile_lexc_script
tr = compile_lexc_script("""
LEXICON Root
cat # ;
""")
print(tr.extract_paths(output='raw'))

# When we compile the script, we get a transducer that recognizes the string 'cat'.

# We continue with an example that uses multicharacter symbols and continuation lexicons.
# `Multichar_Symbols` defines a set of symbols that are tokenized as single symbols in lexicon entries.
# `:` separates input and output sides in lexicon entries. `0` represents the epsilon.
# `!` starts a comment that continues until the end of line. Note that `#` can also be used
# for comments in `Multichar_Symbols` section.

tr = compile_lexc_script("""
Multichar_Symbols
 +N # Noun
 +V # Verb

LEXICON Root    ! This is a comment
cat NOUN ;
mew NOUN ;
mew VERB ;

LEXICON NOUN
0:+N END ;

LEXICON VERB
0:+V END ;

! This is another comment
LEXICON END
# ;
""")
print(tr.extract_paths(output='raw'))

# When we compile the script, we get a transducer that recognizes the following strings:
#
# <table>
# <tr> <th>Input</th> <th>Output</th> </tr>
# <tr> <td>cat</td> <td>cat+N</td> </tr>
# <tr> <td>mew</td> <td>mew+N</td> </tr>
# <tr> <td>mew</td> <td>mew+V</td> </tr>
# </table>
#
# Note that the end lexicon `END` consist of one empty entry with no continuation lexicon.

# We modify the example with regular expressions (i.e. regexps) and weights.
#
# Regexps are enclosed in angle brackets and follow the <a href="https://github.com/hfst/python-hfst-4.0/wiki/PackageHfst#regex-regexp-kwargs">xfst regexp formalism</a>.
# Note that many characters in regexps have a special meaning and must be escaped with a per cent sign to be interpreted literally.
#
# Weights can be defined in regexps (see <a href="https://github.com/hfst/python-hfst-4.0/wiki/Weights#using-weights-in-regular-expressions">weights in xfst regexps</a>)
# and for individual lexicon entries (`"weight: WEIGHT"`). The weights in this toy example are quite arbitrary. Real weights should be based on probabilities extracted from large corpora.

tr = compile_lexc_script("""
Multichar_Symbols
 +N # Noun
 +V # Verb

LEXICON Root
cat NOUN "weight: 1" ;    ! Weights defined for lexicon entries
mew NOUN "weight: 5.2" ;
mew VERB "weight: 1.4" ;

LEXICON NOUN
<0:%+N::0.5> END ;        ! Weights defined inside regexps
!  This is the same as:
!  0:+N END "weight: 0.5" ;

LEXICON VERB
<0:%+V::0.4> END ;

LEXICON END
# ;
""")
print(tr.extract_paths(output='raw'))

# When we compile the following script, we get a transducer that recognizes the following strings:
#
# <table>
# <tr> <th>Input</th> <th>Output</th> <th>Weight</th> </tr>
# <tr> <td>cat</td> <td>cat+N</td> <td>1 + 0.5 = 1.5</td> </tr>
# <tr> <td>mew</td> <td>mew+N</td> <td>5.2 + 0.5 = 5.7</td> </tr>
# <tr> <td>mew</td> <td>mew+V</td> <td>1.4 + 0.4 = 1.8</td> </tr>
# </table>
#
# Note how weights are added when we traverse through the lexicons.
# This is the case in the tropical semiring (TODO: add a link or an explanation) where weights
# are interpreted as penalties, i.e. a bigger weight means that a path is less probable.

# ## 2. Numerals
#
# Get acquainted with <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/transcriptions/">Olonets Karelian transcriptions</a>.
#
# Download <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/transcriptions/transcriptor-numbers-digit2text.lexc">transcriptor-numbers-digit2text.lexc</a>
# (or use a copy available in this directory). The file describes how digits are converted into text.
#

from hfst_dev import compile_lexc_file
tr = compile_lexc_file('transcriptor-numbers-digit2text.lexc')

# test some numerals, both cardinal and ordinal
print(tr.lookup('111'))
print(tr.lookup('111.'))
print(tr.lookup('345678'))
print(tr.lookup('345678.'))

# Note that Uralic numerals follow a pattern different from e.g. Germanic ones.
# Numerals 1—99 are listed below for Finnish and English:
#
# * In both languages, numerals 1—10 must be listed individually.
# * Numerals 11—19:
#   * In Finnish: 11—19 follow the pattern N + TOISTA ('N of a second')
#   * In English:
#     * 11, 12, 13 must be listed separately (eleven, twelve, thirteen)
#     * 14—19 follow a pattern similar to Finnish N + TEEN
#     * but phonological/ortographical changes in five &#8658; fifteen and eight &#8658; eighteen
# * Numerals 20—99:
#   * In Finnish: the pattern N + KYMMENTÄ (+ M) ('N of a ten (M)')
#   * In English:
#     * similar pattern N + TY (+ M)
#     * but 20 and 30: two &#8658; twenty, three &#8658; thirty (cf. German zwei/zwo &#8658; zwanzig, Swedish två &#8658; tjugo)
#     * also phonological/ortographical changes in five &#8658; fifty and eight &#8658; eighty
#
# Also note that Finnish cardinals use singular partitive, e.g. 340: kolmesataaneljäkymmentä ('three of a hundred four of a ten').
#
# Ordinal numbers:
#
# * In Finnish: ordinality is visible in all parts: 145. &#8658; sada<b>s</b>neljä<b>s</b>kymmene<b>s</b>viide<b>s</b>
# * In English: ordinality is visible only in the last part: 145. &#8658; hundred fourty-fif<b>th</b>
#
# In Finnish: cardinals and ordinals are inflected in case and in number (singular, plural). For example for the ordinal 145:
#
# * singular nominative: sada<b>s</b>neljä<b>s</b>kymmene<b>s</b>viide<b>s</b>
# * singular translative: sada<b>nneksi</b>neljä<b>nneksi</b>kymmene<b>nneksi</b>viide<b>nneksi</b>
# * plural nominative: sada<b>nnet</b>neljä<b>nnet</b>kymmene<b>nnet</b>viide<b>nnet</b>
# * plural translative: sada<b>nsiksi</b>neljä<b>nsiksi</b>kymmene<b>nsiksi</b>viide<b>nsiksi</b>

# ## 3. Dates
#
# Download <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/transcriptions/transcriptor-date-digit2text.lexc">transcriptor-date-digit2text.lexc</a>
# (or use a copy available in this directory). The file describes how dates are converted into text.
#
# Ordinals and month names are both needed. Since there are only 31 ordinals, they can be listed individually.

tr = compile_lexc_file('transcriptor-date-digit2text.lexc')
print(tr.lookup('1.1.'))

# Result is (('enzimäine päivy pakkaskuudu', 0.0), ('Pakkaskuun+Use/NG enzimäine päivy', 0.0), ('pakkaskuun+Use/NG enzimäine päivy', 0.0))
#
# Date can be expressed with:
#
# * partitive: 'enzimäine päivy pakkaskuudu' ("first day of Pakkaskuu")
# * genitive: 'pakkaskuun enzimäine päivy' ("Pakkaskuu's first day").

# Print all names of months

for month in range(1,13):
    # use first day of month
    res = tr.lookup('1.' + str(month) + '.')
    # use first result, ignore weight and perform some simple replaces to get the name of the month
    print(res[0][0].replace('enzimäine päivy ','').replace('du',''))

# Result: pakkaskuu, tuhukuu, kevätkuu, sulakuu, oraskuu, kezäkuu, heinykuu, elokuu, syvyskuu, ligakuu, kylmykuu, talvikuu
#
# * cf. Finnish: tammikuu, helmikuu, maaliskuu, huhtikuu, toukokuu, kesäkuu, heinäkuu, elokuu, syyskuu, lokakuu, marraskuu, joulukuu
# * cf. Estonian: jaanuar, veebruar, märts, aprill, mai, juuni, juuli, august, september, oktoober, november, detsember
# * cf. English: January, February, March, April, May, June, July, August, September, October, November, December
  
# ## 4. Clocks
#
# Download <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/transcriptions/transcriptor-clock-digit2text.lexc">transcriptor-clock-digit2text.lexc</a>
# (or use a copy available in this directory). The file describes how clocks are converted into text.
#
# Print all clocks between 11:00 and 11:59.

tr = compile_lexc_file('transcriptor-clock-digit2text.lexc')
hour = '11'
for minutes in range(0,60):
    minutes = str(minutes)
    # add missing zero to numbers 1-9
    if len(minutes) == 1:
        minutes = '0' + minutes
    clock = hour + ':' + minutes
    print(clock + '\t' + str(tr.lookup(clock)))

# The pattern is:
#
# <table>
# <tr> <th>Clock</th> <th>Translation</th> </tr>
# <tr> <td>11:00</td> <td>'eleven hours' or 'eleven sharp'</td> </tr>
# <tr> <td>11:01—11:29</td> <td>'N minutes of twelfth'</td> </tr>
# <tr> <td>11:30</td> <td>'half twelve'</td> </tr>
# <tr> <td>11:31—11:59</td> <td>'N minutes short of twelve'</td> </tr>
# </table>

# Also try clocks after noon:

print(tr.lookup('22:15'))
print(tr.lookup('10:15'))

for clocks in (('00:00','12:00'),('00:30','12:30'),('11:59','23:59'),('05:32','17:32'),('02:11','14:11')):
    assert(tr.lookup(clocks[0]) == tr.lookup(clocks[1]))
