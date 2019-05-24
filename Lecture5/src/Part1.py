# # MORPHOLOGICALLY RICH LANGUAGES WITH HFST TOOLS - LECTURE 5
#
# Topics:
#
# * Twolc & xfst rewrite rules
#
# TODO: demonstrate how twolc rules can be generated with hfst_dev.regex('').
#
# <ul>
# <li>1. <a href="#1.-Twolc-formalism">Twolc formalism</a></li>
# <li>2. <a href="#2.-Twolc-rewrite-rules-for-Olonets-Karelian">Twolc rewrite rules for Olonets-Karelian</a></li>
# <li>3. <a href="#3.-Xfst-rewrite-rules">Xfst rewrite rules</a></li>
# </ul>

# ## 1. Twolc formalism
#
# A twol-grammar consists of five parts: Alphabet, Diacritics, Sets, Definitions and Rules.
# Each part contains statements, that end in a ; character and comments, that begin with a ! character and span to the end of the line.
# Two-level rules consist of a center, a rule-operator and contexts.
# Twolc is often used for writing phonological rules that are applied to a lexicon written in lexc.
#
# A minimalistic example of lexc combined with twolc:
#
# lexc file:
# ```
# LEXICON Root
# kaNpa # ;
# ```
#
# twolc file (n2m.twolc):
# ```
# Alphabet a k m n p N ;
# Rules
# "N to m"
# N:m <=> _ :p ;
# ```

from hfst_dev import compile_lexc_script
lexicon = compile_lexc_script("""
LEXICON Root
kaNpa # ;
""")

from hfst_dev import compile_twolc_file, HfstInputStream
compile_twolc_file('n2m.twolc','n2m.hfst',verbose=True)
istr = HfstInputStream('n2m.hfst')
rules = istr.read_all()
istr.close()

lexicon.compose_intersect(rules)
print(lexicon.lookup('kaNpa'))

# The output is (('kampa', 0.0),).
#
# For more information about twolc, see <a href="https://github.com/hfst/hfst/wiki/HfstTwolc#syntax">hfst-twolc command line tool manual page</a>.

# ## 2. Twolc rewrite rules for Olonets-Karelian
#
# From the previous lecture:
#
# > ```# First, compile the lexc files:```
# > 
# > ```# TODO: cat root.lexc kala.lexc nouns.lexc clitics.lexc > root_kala_nouns_clitics.lexc
# > from hfst_dev import compile_lexc_file, HfstTransducer```
# > 
# > ```kala = compile_lexc_file('root_kala_nouns_clitics.lexc')
# > print(kala.lookup('kala+N+Pl+Ade'))```
# >
# > ```# Without the rules, the result is (('kala{back}^A2O>i>l', 0.0),)```
#
# Have a look at Olonetsian Karelian lexc files in Giella repo that we used in the previous lecture
# as well as the twolc file olo-phon.twolc:
#
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/stems/nouns.lexc">stems/nouns.lexc</a>
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/affixes/nouns.lexc">affixes/nouns.lexc</a>
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/affixes/clitics.lexc">affixes/clitics.lexc</a>
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/phonology/olo-phon.twolc">olo-phon.twolc</a>
#
# or use a copies available in this directory. We will use a simplified test case where stems/nouns.lexc will be
# replaced with a single-stem file kala.lexc as we did in Lecture 4:
#
# ```
# LEXICON nouns
# kala+N:kala N_KALA ;
# ```
#
# Remember that multicharacter symbols and root and end lexica are listed in file
# <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/root.lexc">root.lexc</a>.
#
# We use again the affix and clitics files as such.

# First, compile the lexc files as we did in Lecture 4:

# TODO: we have to catenate the files: cat root.lexc kala.lexc nouns.lexc clitics.lexc > root_kala_nouns_clitics.lexc

from hfst_dev import compile_lexc_file
kala = compile_lexc_file('root_kala_nouns_clitics.lexc')
print(kala.lookup('kala+N+Pl+Ade'))

# Without the rules, the result is (('kala{back}^A2O>i>l', 0.0),)

# We introduce phonological rewrite rules given in file olo-phon.twolc. Note e.g.:
#
# ```
# "a:o in the plural and preterite"
# !! __@RULENAME@__
# a:o <=> Cns: _ (%{back%}:) (%^WGStem:) %^A2O: ;
# ```

# Then compile twolc rules (TODO: result is written to file):
# This takes some time and we get verbose output (TODO: use python's stdout in hfst_dev module...):
#
# ```
# Reading alphabet.
# Reading sets.
# Reading and compiling definitions.
# Reading rules and compiling their contexts and centers.
# Compiling rules.
# Storing rules.
# ```

compile_twolc_file('olo-phon.twolc','olo-phon.hfst',verbose=True)

istr = HfstInputStream('olo-phon.hfst')
rules = istr.read_all()
istr.close()

# We get 86 rules in total:
print(len(rules))

# We compose-intersect the lexicon with the rules

kala.compose_intersect(rules)
print(kala.lookup('kala+N+Pl+Ade'))
print(kala.lookup('kala+N+Pl+Abl'))

# and get the result ```(('kalo>i>l', 0.0),)``` ('>' means morpheme boundary). Compare with test file lines:
#
# ```
# kala+N+Pl+Ade: kaloil
# kala+N+Pl+Abl: [kaloilpäi, kaloil]
# ```

for testcase in ('kala+N+Pl+Ade','kala+N+Pl+Abl'):
    results = kala.lookup(testcase)
    for res in results:
        print(res[0].replace('>',''))

# Get rid of morpheme boundary '>'.
from hfst_dev import EPSILON
kala.substitute('>',EPSILON)
kala.minimize()

# Check that each generated form produced by kala is listed
# as a possible result in yaml file (TODO: a separate function for this?):

with open ("N-kala_gt-norm.yaml", "r") as myfile:
    data=myfile.readlines()
for line in data:
    if '     ' in line:
        # kala+N+Sg+Abe: [kalata, kalattah]
        pair = line.split(': ')
        # 'kala+N+Sg+Abe'
        analysis = pair[0].replace('     ','')
        # ('kalata', 'kalattah')
        generation = pair[1].replace('\n','').replace('[','').replace(']','').split(', ')
        results = kala.lookup(analysis)
        for res in results:
            # res[0] is the output form, res[1] is the weight
            if res[0] not in generation:
                print('unknown result for analysis "' + analysis + '": "' + res[0] + '"')

# Invert the generator to get an analyser.

kala.invert()
kala.minimize()
print(kala.lookup('kaloil'))

# ## 3. Xfst rewrite rules
#
# Rewrite rules can also be written using the xfst formalism.
#
# The "N to m" rule ```# N:m <=> _ :p ;``` would be:
#
# ```
# N -> m || _ p ;
# ```
