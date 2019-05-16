# # MORPHOLOGICALLY RICH LANGUAGES WITH HFST TOOLS - LECTURE 3
#
# Topics: simple lexc (numerals, dates, clocks)
#
# Get acquainted with <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/transcriptions/">Olonets-Karelian</a>.
#
# ## Numerals
#
# Download transcriptor-numbers-digit2text.lexc (or use a copy available in this directory).
#

from hfst_dev import compile_lexc_file
tr = compile_lexc_file('transcriptor-numbers-digit2text.lexc')

# test cases

print(tr.lookup('111'))
print(tr.lookup('111.'))
print(tr.lookup('345678'))
print(tr.lookup('345678.'))

# Note that Uralic numerals follow a pattern different from e.g. Germanic ones
# In both language groups, numerals 1-10 must be listed individually.
#
# In Uralic (Finnish): 11-19 follow the pattern N + TOISTA (TOISTA: 'of a second')
# In Germanic (English): 11, 12, 13 separate and 14-19 N + TEEN (but e.g. five -> fifteen)
#
# In Uralic: 20-99 follow the pattern N + KYMMENTA (+ M)
# In Germanic: same pattern but 20, 30 often separate (two -> twenty, three -> thirty || zwei/zwo -> zwanzig || två -> tjugo)
#
# Also note that Uralic cardinals use singular partitive instead of (teen/zehn/ton || ty/ig/ti)
# E.g. kolmesataaneljäkymmentä, 'three of a hundred + four of a ten'
#
# Ordinal numbers:
# In Uralic: ordinality is visible in all parts: 145. -> sada*s*neljä*s*kymmene*s*viide*s*
# In Germanic: ordinality is visible only in last part: 145. -> hundred fourty-fifth
#
# In Uralic: cardinals and ordinals are inflected in case and in number (singular, plural, even dual?)
#
# 145. sadasneljäskymmenesviides
# 145. in translative: sadanneksineljänneksikymmenenneksiviidenneksi
#
# 145. in plural: sadannetneljännetkymmenennetviidennet
# 145. in plural translative: sadansiksineljänsiksikymmenensiksiviidensiksi

# ## Dates
#
# https://victorio.uit.no/langtech/trunk/langs/olo/src/transcriptions/transcriptor-date-digit2text.lexc
#

tr = compile_lexc_file('transcriptor-date-digit2text.lexc')
print(tr.lookup('1.1.'))

# ## Clocks
#
# https://victorio.uit.no/langtech/trunk/langs/olo/src/transcriptions/transcriptor-clock-digit2text.lexc
#

tr = compile_lexc_file('transcriptor-clock-digit2text.lexc')
print(tr.lookup('11:30'))
print(tr.lookup('22:15'))
