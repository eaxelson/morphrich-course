# # MORPHOLOGICALLY RICH LANGUAGES WITH HFST TOOLS - LECTURE 5
#
# Topics: Twolc & xfst rewrite rules
#
# <ul>
# <li>1. <a href="#1.-Twolc-formalism">Twolc formalism</a></li>
# <li>2. <a href="#2.-Twolc-rewrite-rules-for-Olonets-Karelian">Twolc rewrite rules for Olonets Karelian</a></li>
# <li>3. <a href="#3.-Twolc-vs.-xfst-rewrite-rules">Twolc vs. xfst rewrite rules</a></li>
# </ul>

# ## 1. Twolc formalism
#
# A twol-grammar consists of five parts: `Alphabet`, `Diacritics`, `Sets`, `Definitions` and `Rules`.
# Each part contains statements that end in `;`, possibly followed by comments that begin with `!` and span to the end of the line.
# Two-level rules consist of a center, a rule-operator and contexts.
# Twolc is often used for writing phonological rules that are applied to a lexicon written in lexc.
# The rules are applied via <a href="https://github.com/hfst/python-hfst-4.0/wiki/HfstTransducer#compose_intersect-self-v-invertfalse">intersection</a>
# instead of <a href="https://github.com/hfst/python-hfst-4.0/wiki/HfstTransducer#compose-self-another">composition</a>.
#
# A minimalistic example of lexc combined with twolc:
#
# lexc script containing one entry `kaNpa`:
# ```
# LEXICON Root
# kaNpa # ;
# ```
#
# (Note that there are no multicharacter symbols in the lexc file.
# If there were, they would have to be declared with `Multichar_Symbols`.)
#
# twolc script (available in file <i>n2m.twolc</i>) that rewrites # `N` to `m` before `p`:
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

from hfst_dev import compile_twolc_script
script="""
Alphabet a k m n p N ;
Rules
"N to m"
N:m <=> _ :p ;
"""
rules = compile_twolc_script(script,verbose=True)

# The result may contain one or more rules. In this simple case, there is only one rule.
print(rules[0])

lexicon1 = lexicon.copy()
lexicon1.compose_intersect(rules)
print(lexicon1.lookup('kaNpa'))

# Plain composition would work too, as there is only one rule.
lexicon2 = lexicon.copy()
lexicon2.compose(rules[0])
print(lexicon2.lookup('kaNpa'))

print(lexicon1.compare(lexicon2))

exit(0)

# The output is (('kampa', 0.0),).
#
# For more information about twolc, see <a href="https://github.com/hfst/hfst/wiki/HfstTwolc#syntax">hfst-twolc command line tool manual page</a>.

# ## 2. Twolc rewrite rules for Olonets Karelian
#
# From the previous lecture:
#
# > ```# First, compile the lexc files:```
# > 
# > ```from hfst_dev import compile_lexc_files, HfstTransducer```
# > 
# > ```kala = compile_lexc_files(('root.lexc','kala.lexc','nouns.lexc','clitics.lexc'))
# > print(kala.lookup('kala+N+Pl+Ade'))```
# >
# > ```# Without the rules, the result is (('kala{back}^A2O>i>l', 0.0),)```
#
# Have a look at Olonets Karelian lexc files in Giella repo that we used in the previous lecture
# as well as the twolc file <i>olo-phon.twolc</i>:
#
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/stems/nouns.lexc">stems/nouns.lexc</a> (was replaced with <i>kala.lexc</i>)
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/affixes/nouns.lexc">affixes/nouns.lexc</a>
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/affixes/clitics.lexc">affixes/clitics.lexc</a>
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/phonology/olo-phon.twolc">olo-phon.twolc</a>
#
# or use a copies available in this directory. We will use a simplified test case where <i>stems/nouns.lexc</i> will be
# replaced with a single-stem file <i>kala.lexc</i> as we did in Lecture 4:
#
# ```
# LEXICON nouns
# kala+N:kala N_KALA ;
# ```
#
# Remember that multicharacter symbols and root and end lexica are listed in file <i>root.lexc</i>.

# First, compile the lexc files as we did in Lecture 4:

from hfst_dev import compile_lexc_files
kala = compile_lexc_files(('root.lexc','kala.lexc','nouns.lexc','clitics.lexc'))
print(kala.lookup('kala+N+Pl+Ade'))

# Without the rules, the result is (('kala{back}^A2O>i>l', 0.0),)

# Compare with Finnish, where, instead of having a trigger to cause `a:o`,
# there are three different I-triggers addressing plural, past tense and the conditional
# - i-trigger also changes to i or j.
# In Olonets-Karelian the `^A2O` trigger changes to zero and the `i:j` alteration
# is dealt with as a separate phenomenon. Separate phenomena are easier to clean up (maybe).
#
# An example of Võro language:
#
# ```
# "o2õ"
# !! __@RULENAME@__
# o:õ <=> [Cns - [m|p|b|v]] _ o: (HarmDummies:) %^OO2Õ: %> i ;
# !!€ joo%^OO2Õ%>i
# !!€ jõ00%>i
# ```

# Now back to Olonets-Karelian.
# We introduce phonological rewrite rules given in file <i>olo-phon.twolc</i>. Note e.g.:
#
# ```
# "a:o in the plural and preterite"
# !! __@RULENAME@__
# a:o <=> Cns: _ (%{back%}:) (%^WGStem:) %^A2O: ;
# ```

# Then compile twolc rules.
from hfst_dev import compile_twolc_file
rules = compile_twolc_file('olo-phon.twolc',verbose=True)

# We get 86 rules in total:
print(len(rules))

# At this point, a word about the multicharacter symbol `%^A2O` and triggers in general:
#
# * Triggers can be used for phenomena to the left and the right.
# * Be sure to sort out which direction each trigger points to, e.g. in Finnish and Olonets-Karelian vowel harmony is triggered by `%{back%}` and `%{front%}`, and the things affected lie to the right.
# * Consonant gradation, however, happens on the left.
# * Consonant gradation, as we know, happens not only in the final coda of the stem but in the penultimate coda, as well, such as:
#
# ```
# meččy:mečän
# Agjatoi:agjattoma ‘loputon’
# ajatella:ajattelee
# bringahutella+V:bringahuttel V_KUVITELLA  "heilutella" ;
# ```

# We <a href="https://github.com/hfst/python-hfst-4.0/wiki/HfstTransducer#compose_intersect-self-v-invertfalse">compose-intersect</a>
# the lexicon with the rules.

kala.compose_intersect(rules)
print(kala.lookup('kala+N+Pl+Ade'))
print(kala.lookup('kala+N+Pl+Abl'))

# and get the result `(('kalo>i>l', 0.0),)` ('>' means morpheme boundary).
# Compare the results with test file <i>N-kala_gt-norm.yaml</i> lines:
#
# ```
# kala+N+Pl+Ade: kaloil
# kala+N+Pl+Abl: [kaloilpäi, kaloil]
# ```

for testcase in ('kala+N+Pl+Ade','kala+N+Pl+Abl'):
    results = kala.lookup(testcase)
    for res in results:
        print(res[0].replace('>',''))

# Get rid of morpheme boundary '>' so we don't have to replace it every time.
# Boundary markers help writing rules when we know where one morpheme ends and the next begins,
# but they can be filtered out at this point.

from hfst_dev import EPSILON
kala.substitute('>',EPSILON)
kala.minimize()

# Check that each generated form produced by kala is listed
# as a possible result in yaml test file <i>N-kala_gt-norm.yaml</i>
# (TODO: implement a separate function for this in hfst_dev module):

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
            # TODO: maybe the result should be a class?
            if res[0] not in generation:
                print('unknown result for analysis "' + analysis + '": "' + res[0] + '"')

# Invert the generator to get an analyser.

kala.invert()
kala.minimize()
print(kala.lookup('kaloil'))

# Test the same with koivu, 'birch'.

pass # write your solution here


# ## 3. Twolc vs. xfst rewrite rules
#
# Differences between twolc and xfst formalism:
#
# * Ordering.
# * XFST has upkeep.
# * Multichar-symbols are declared differently.

# ## 4. Unexpected morphology:
#
# * Finnish 'joulumpi' ('Xmaser')
# * English 'fun, funner, funnest' ('it is fun' -> 'fun' looks like adjective)
# * English 'quickly, quicklier', and 'slowly, slowlier'
# * "German bringen is a strong verb, and it conjugates almost just like in English" -> 'bring, brang, brung'?
#
# Descriptive or prescriptive morphology?
