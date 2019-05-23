# # MORPHOLOGICALLY RICH LANGUAGES WITH HFST TOOLS - LECTURE 5
#
# Topics:
#
# * Twolc & xfst rewrite rules
#
# TODO: demonstrate how twolc rules can be generated with hfst_dev.regex('').
#
# <ul>
# <li>1. <a href="#"></a></li>
# </ul>
#
# ## Twolc rewrite rules
#
# From the previous lecture:
#
# > # First, compile the lexc files:
# > #
# > # TODO: we have to catenate the files: cat root.lexc kala.lexc nouns.lexc clitics.lexc > root_kala_nouns_clitics.lexc
# > from hfst_dev import compile_lexc_file, compile_twolc_file, HfstInputStream, regex, HfstTransducer, intersect, EPSILON
# > 
# > kala = compile_lexc_file('root_kala_nouns_clitics.lexc')
# > print(kala.lookup('kala+N+Pl+Ade'))
# > 
# > # Without the rules, the result is (('kala{back}^A2O>i>l', 0.0),)
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
from hfst_dev import compile_lexc_file, compile_twolc_file, HfstInputStream, regex, HfstTransducer, intersect, EPSILON

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

# and get the result (('kalo>i>l', 0.0),)
#
# '>' means morpheme boundary

# ```
# kala+N+Pl+Ade: kaloil
# kala+N+Pl+Abl: [kaloilpäi, kaloil]
# ```

for testcase in ('kala+N+Pl+Ade','kala+N+Pl+Abl'):
    results = kala.lookup(testcase)
    for res in results:
        print(res[0].replace('>',''))

# Get rid of morpheme boundary '>'.
kala.substitute('>',EPSILON)
kala.minimize()

# Check that each generated form produced by kala is listed
# as a possible result in yaml file:

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
