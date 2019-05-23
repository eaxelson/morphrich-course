# # MORPHOLOGICALLY RICH LANGUAGES WITH HFST TOOLS - LECTURE 4
#
# Topics:
#
# * lexc: practices and automated documentation
# * production and reuse of test materials for development of analysers/generators
#
# <ul>
# <li>1. <a href="#1.-Test-material"></a>Test material</li>
# <li>2. <a href="#2.-Lexc-formalism">Lexc formalism</a></li>
# </ul>
#

# ## 1. Test material
#
# Have a look at the <a href="https://en.wikipedia.org/wiki/YAML">yaml</a>
# file for Olonetsian Karelian nouns (N-kala_gt-norm.yaml).
# Download it from
# <a href="https://victorio.uit.no/langtech/trunk/langs/olo/test/src/gt-norm-yamls/N-kala_gt-norm.yaml">Giella repo</a>
# or use a copy available in this directory.

# First the configuration that defines the analysis and generation transducers for hfst and xfst tools (we'll get back to this later):
#
# ```
#
# Config:
#   hfst:
#     Gen: ../../../src/generator-gt-norm.hfst
#     Morph: ../../../src/analyser-gt-norm.hfst
#   xerox:
#     Gen: ../../../src/generator-gt-norm.xfst
#     Morph: ../../../src/analyser-gt-norm.xfst
#     App: lookup
#
# ```

# Then the tests that define a full paradigm for the given test word:
#
# ```
# Tests:
# 
# # todo:
# # Proofread the gold standard (below)
# # Then: run analyser, then correct.
#
#
#   Noun - kala: # Noun 'fish / kala' - full paradigm
#      kala+N+Sg+Nom: kala
#      kala+N+Sg+Gen: kalan
#      kala+N+Sg+Acc: [kala, kalan]
#      kala+N+Sg+Par: kalua
#      kala+N+Sg+Tra: kalakse
#      kala+N+Sg+Abe: [kalata, kalattah]
#      kala+N+Sg+Com: kalanke
#      kala+N+Sg+Ine: kalas
#      kala+N+Sg+Ela: [kalaspäi, kalas]
#      kala+N+Sg+Ill: kalah
#      kala+N+Sg+Ade: kalal
#      kala+N+Sg+Abl: [kalalpäi, kalal]
#      kala+N+Sg+All: kalale
#      kala+N+Sg+Ess: kalannu
#      kala+N+Sg+Ter: kalassah
#      kala+N+Sg+Apr: kalalluo
# ```

# The same in plural:
#
# ```
#      kala+N+Pl+Nom: kalat
#      kala+N+Pl+Gen: kalojen
#      kala+N+Pl+Acc: kalat
#      kala+N+Pl+Par: kaloi
#      kala+N+Pl+Tra: kaloikse
#      kala+N+Pl+Abe: [kaloita, kaloittah]
#      kala+N+Pl+Com: kalojenke
#      kala+N+Pl+Ine: kalois
#      kala+N+Pl+Ela: [kaloispäi, kalois]
#      kala+N+Pl+Ill: kaloih
#      kala+N+Pl+Ade: kaloil
#      kala+N+Pl+Abl: [kaloilpäi, kaloil]
#      kala+N+Pl+All: kaloile
#      kala+N+Pl+Ess: kaloinnu
#      kala+N+Pl+Ins: kaloin
#      kala+N+Pl+Apr: kalojelluo
# ```

# The same with clitic gi:
#
# ```
#      kala+N+Sg+Nom+Clt/gi: kalagi
#      kala+N+Sg+Gen+Clt/gi: kalangi
#      kala+N+Sg+Acc+Clt/gi: [kalagi, kalangi]
#      kala+N+Sg+Par+Clt/gi: kaluagi
#      kala+N+Sg+Tra+Clt/gi: kalaksegi
#      kala+N+Sg+Abe+Clt/gi: [kalatagi, kalattahgi]
#      kala+N+Sg+Com+Clt/gi: kalankegi
#      kala+N+Sg+Ine+Clt/gi: kalasgi
#      kala+N+Sg+Ela+Clt/gi: [kalaspäigi, kalasgi]
#      kala+N+Sg+Ill+Clt/gi: kalahgi
#      kala+N+Sg+Ade+Clt/gi: kalalgi
#      kala+N+Sg+Abl+Clt/gi: [kalalpäigi, kalalgi]
#      kala+N+Sg+All+Clt/gi: kalalegi
#      kala+N+Sg+Ess+Clt/gi: kalannugi
#      kala+N+Sg+Ter+Clt/gi: kalassahgi
#      kala+N+Sg+Apr+Clt/gi: kalalluogi
#      kala+N+Pl+Nom+Clt/gi: kalatgi
#      kala+N+Pl+Gen+Clt/gi: kalojengi
#      kala+N+Pl+Acc+Clt/gi: kalatgi
#      kala+N+Pl+Par+Clt/gi: kaloigi
#      kala+N+Pl+Tra+Clt/gi: kaloiksegi
#      kala+N+Pl+Abe+Clt/gi: [kaloitagi, kaloittahgi]
#      kala+N+Pl+Com+Clt/gi: kalojenkegi
#      kala+N+Pl+Ine+Clt/gi: kaloisgi
#      kala+N+Pl+Ela+Clt/gi: [kaloispäigi, kaloisgi]
#      kala+N+Pl+Ill+Clt/gi: kaloihgi
#      kala+N+Pl+Ade+Clt/gi: kaloilgi
#      kala+N+Pl+Abl+Clt/gi: [kaloilpäigi, kaloilgi]
#      kala+N+Pl+All+Clt/gi: kaloilegi
#      kala+N+Pl+Ess+Clt/gi: kaloinnugi
#      kala+N+Pl+Ins+Clt/gi: kaloingi
#      kala+N+Pl+Apr+Clt/gi: kalojelluogi
# ```

# If there are hundreds or thousands of forms, best to list them alphabetically...
# See <a href="https://victorio.uit.no/langtech/trunk/langs/olo/test/src/gt-norm-yamls/V-suvaija_gt-norm.yaml">verb inflection</a>.
# There are 141 forms listed but there are even more forms.


# Compare e.g. with <a href="https://victorio.uit.no/langtech/trunk/langs/nds/test/src/gt-norm-yamls/V-waien_gt-norm.yaml">Low German verb inflection</a>:
#
# ```
#   Verb - waien: # Verb 'to blow (of wind)' - full paradigm
#      waien+V+Ind+Prs+Sg1: waie
#      waien+V+Ind+Prs+Sg2: waist
#      waien+V+Ind+Prs+Sg3: wait
#      waien+V+Ind+Prs+Pl: [waiet, waien]
# 
#      waien+V+Ind+Prt+Sg1: waide
#      waien+V+Ind+Prt+Sg2: waidest
#      waien+V+Ind+Prt+Sg3: waide
#      waien+V+Ind+Prt+Pl: waiden
# 
#      waien+V+Inf:  waien
#      waien+V+PrfPrc:  waid
#      waien+V+PrsPrc:  waien
# 
#      waien+V+Imprt+Sg2:  wai
#      waien+V+Imprt+Pl2:  waiet
# ```

# ## 2. Lexc formalism
#
# Have a look at some Olonetsian Karelian lexc files in Giella repo:
#
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/stems/nouns.lexc">stems/nouns.lexc</a>
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/affixes/nouns.lexc">affixes/nouns.lexc</a>
# * <a href="https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/affixes/clitics.lexc">affixes/clitics.lexc</a>
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
#
# Concatenative morphology is not enough, we need phonological rules.
# We will get back to them in the next lecture.
