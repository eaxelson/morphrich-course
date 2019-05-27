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
# In its simplest form: LEXICON Root and '#' which means no continuation lexicon:
#
# ```
# LEXICON Root
# cat # ;
# ```

from hfst_dev import compile_lexc_script
tr = compile_lexc_script("""
LEXICON Root
cat # ;
""")
print(tr.extract_paths(output='raw'))

# An example with multicharacter symbols and continuation lexica:
#
# ```
# Multichar_Symbols
#  +N # Noun
#  +V # Verb
#
# LEXICON Root
# cat NOUN ;
# mew NOUN ;
# mew VERB ;
# 
# LEXICON NOUN
# +N END ;
#
# LEXICON VERB
# +V END ;
#
# LEXICON END
# # ;
# ```

tr = compile_lexc_script("""
Multichar_Symbols
 +N # Noun
 +V # Verb

LEXICON Root
cat NOUN ;
mew NOUN ;
mew VERB ;

LEXICON NOUN
0:+N END ;

LEXICON VERB
0:+V END ;

LEXICON END
# ;
""")
print(tr.extract_paths(output='raw'))

# ## 2. Numerals
#
# # Get acquainted with <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/transcriptions/">Olonets-Karelian</a>.
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
# Below are listed numerals 1-99 for Finnish and English:
#
# * In both languages, numerals 1-10 must be listed individually.
# * Numerals 11-19:
#   * In Finnish: 11-19 follow the pattern N + TOISTA
#   * In English: 11, 12, 13 must be listed separately and 14-19 follow the pattern N + TEEN (but e.g. five -> fifteen)
# * Numerals 20-99:
#   * In Finnish: the pattern N + KYMMENTÄ (+ M)
#   * In English: same pattern but 20, 30 separate: two -> twenty, three -> thirty)
#   * cf. German zwei/zwo -> zwanzig, Swedish två -> tjugo
#
# Also note that Finnish cardinals use singular partitive, e.g. 340: kolmesataaneljäkymmentä ('three of a hundred + four of a ten').
#
# Ordinal numbers:
#
# * In Finnish: ordinality is visible in all parts: 145. -> sada*s*neljä*s*kymmene*s*viide*s*
# * In English: ordinality is visible only in last part: 145. -> hundred fourty-fifth
#
# In Finnish: cardinals and ordinals are inflected in case and in number (singular, plural). For example for the ordinal 145:
#
# * singular nominative: sadasneljäskymmenesviides
# * singular translative: sadanneksineljänneksikymmenenneksiviidenneksi
# * plural nominative: sadannetneljännetkymmenennetviidennet
# * plural translative: sadansiksineljänsiksikymmenensiksiviidensiksi

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
# * partitive: 'enzimäine päivy pakkaskuudu' ("first day of pakkaskuu")
# * genitive: 'pakkaskuun enzimäine päivy' ("pakkaskuu's first day").

# Print all names of months

for month in range(1,13):
    res = tr.lookup('1.' + str(month) + '.')
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
# <tr> <td>11:00</td> <td>'eleven'</td> </tr>
# <tr> <td>11:01 - 11:19</td> <td>'N past eleven'</td> </tr>
# <tr> <td>11:20 - 11:29</td> <td>'N to half twelve'</td> </tr>
# <tr> <td>11:30</td> <td>'half twelve'</td> </tr>
# <tr> <td>11:31 - 11:40</td> <td>'N past half twelve'</td> </tr>
# <tr> <td>11:40 - 11:59</td> <td>'N to twelve'</td> </tr>
# </table>
#
# Also try a clock aftern noon:

print(tr.lookup('22:15'))
print(tr.lookup('10:15'))
