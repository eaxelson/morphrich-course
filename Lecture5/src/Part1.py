# # MORPHOLOGICALLY RICH LANGUAGES WITH HFST TOOLS - LECTURE 5
#
# Topics:
#
# * Twolc & xfst rewrite rules
#
# <ul>
# <li>1. <a href="#"></a></li>
# </ul>
#
# Have a look at some Olonetsian Karelian lexc/twolc files in Giella repo:
#
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/stems/nouns.lexc">stems/nouns.lexc</a>
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/affixes/nouns.lexc">affixes/nouns.lexc</a>
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/affixes/clitics.lexc">affixes/clitics.lexc</a>
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/phonology/olo-phon.twolc">olo-phon.twolc</a>
#
# or use a copies available in this directory. We will use a simplified test case where stems/nouns.lexc will be
# replaced with a single-stem file kala.lexc.

# Multicharacter symbols and root and end lexica are listed in file
# <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/root.lexc">root.lexc</a>.

# We used a simplified one-stem version of stems/nouns.lexc named kala.lexc.
#
# ```
# LEXICON nouns
# kala+N:kala N_KALA ;
# ```

# Then, we can use the affix file as such. The most important parts are:
#
# ```
# LEXICON N_KALA !!= @CODE@ kala:kala
# !! Gradation NA
# !! Harmony: Back
# !! stem final a changes to u in Sg Par
# !! stem final a changes to o before i in Pl stem
# : ATTESTED-NOUN-STEM ;
#         N_KALA-SG  ;
#         N_KALA-PL  ;
# LEXICON N_KALA-SG
# :%{back%} NMN_KALA ;
# LEXICON N_KALA-PL
# :%{back%} NMN_KALA-PL ;
# LEXICON N-HUM_KALA
# +Sem/Hum: NMN_KALA ;
# # ```                
#
# and the continuation lexica (N_KALA-SG, N_KALA-PL, NMN_KALA, NMN_KALA-PL, N-HUM_KALA).

# The clitics file (WORD-END is defined in file root.lexc):
#
# ```
# !! Clitics
# !  --------------------
# !! Livvi clitics
# 
# LEXICON K
# +Clt/gi:%>gi WORD-END "also / -kin" ;
# !+Clt/hAi:%>h%{aä%}i WORD-END " / -hAn" ;
# +Clt/hAi:%>häi WORD-END " / -hAn" ;
# +Clt/bo:%>bo WORD-END " / -pA" ;
# +Qst:%>go WORD-END " / -kO" ;
# WORD-END ; 
#
# # ```

# We use olo-phon.lexc as such. Note e.g.:
#
# ``` 
# LEXICON NMN_KALA-PL
#  PLNOMSUF-USUALLY-WEAK ;
#  :%^A2O%>j PL-GEN/COM/APRSUF_EN ;
#  :%^A2O%>i PLPARSUF_Zero ;
#  :%^A2O%>i PLINSSUF ;
#  +Pl:%^A2O%>i OBLIQUE-CASES-NOT-GENITIVE-DERIVATIVES ;
# ```

# First, compile the lexc files:
#
# TODO: we have to catenate the files: cat root.lexc kala.lexc nouns.lexc clitics.lexc > root_kala_nouns_clitics.lexc
from hfst_dev import compile_lexc_file, compile_twolc_file, HfstInputStream, regex, HfstTransducer, intersect, EPSILON

kala = compile_lexc_file('root_kala_nouns_clitics.lexc')
print(kala.lookup('kala+N+Pl+Ade'))

# Without the rules, the result is (('kala{back}^A2O>i>l', 0.0),)

# Phonetic rules in file olo-phon.twolc, e.g.:
#
# ```
# "a:o in the plural and preterite"
# !! __@RULENAME@__
# a:o <=> Cns: _ (%{back%}:) (%^WGStem:) %^A2O: ;
# ```

# Then compile twolc rules (TODO: result is written to file):
# This takes some time and we get verbose output:
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
