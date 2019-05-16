# # MORPHOLOGICALLY RICH LANGUAGES WITH HFST TOOLS - LECTURE 5
#
# Topics:
#
# * Twolc & xfst rewrite rules
#
# Have a look at some Olonetsian Karelian lexc files.
#
# Download them from:
#
# * https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/stems/nouns.lexc
# * https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/affixes/nouns.lexc
# * https://victorio.uit.no/langtech/trunk/langs/olo/src/morphology/affixes/clitics.lexc
# * https://victorio.uit.no/langtech/trunk/langs/olo/src/phonology/olo-phon.twolc
#
# or use a copies available in this directory. We will use a simplified test case.

# First, the file kala.lexc (one-stem version of stems/nouns.lexc):
#
# ```
# LEXICON Root
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
# and the continuation lexica (...).

# We modify the clitics file by adding lexicon WORD-END
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
# LEXICON WORD-END
# # ;
# 
# ! vim: set ft=xfst-lexc:
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
