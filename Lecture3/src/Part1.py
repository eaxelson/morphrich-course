# # MORPHOLOGICALLY RICH LANGUAGES WITH HFST TOOLS - LECTURE 3
#
# ## Simple lexc (numerals, dates, clocks)
#
# Get acquainted with <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/transcriptions/">Olonets-Karelian</a>.
#
# Download transcriptor-numbers-digit2text.lexc (or use a copy available in this directory).
#

from hfst_dev import compile_lexc_file
tr = compile_lexc_file('transcriptor-numbers-digit2text.lexc')

# test cases

tr.lookup('111')
tr.lookup('111.')
tr.lookup('345678')
tr.lookup('345678.')

