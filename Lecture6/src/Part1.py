# # MORPHOLOGICALLY RICH LANGUAGES WITH HFST TOOLS - LECTURE 6
#
# Topics: Shared language-independent modeling
#
# <ul>
# <li>1. <a href="#1.-...">...</a></li>
# <li>2. <a href="#2.-...">...</a></li>
# <li>3. <a href="#3.-...">...</a></li>
# </ul>

# ## 1. Inflection in Uralic languages
#
# * concatenative: e.g. Finnish koivu - koivujen
# * vowel change: e.g. Finnish kala - kalojen
# * gradation + wovel change: e.g. Olonets-Karelian meččy - mečän
# * gradation + diphtongisation: e.g. Olonets-Karelian pata - puan
# * multiple gradations: e.g. Finnish ajatella - ajattelen
# * diphtong change + consonant gradation: e.g. Skolt Sámi ǩeäʹdǧǧ -> ǩiẹˈʹđjstes
#
# Inflection can be present in two parts of a word: e.g. Olonets-Karelian(?) otti-lähti - ota-lähde.
# There is a long-distance dependency. Features that must be the same are
# Act/Pass, Tempus, Numerus, Person, Modus (sometimes even Inf/Fin), making a total of
# 2 x 4 x 2 x 3 x 4 (x 2) = 64 x 3 = 192 (x 2) combinations. If these are modeled by
# simply listing all possible word-forms, the model gets big. Alternative solution:
# flag diacritics. EXAMPLE???
#
# Sometimes we want to keep the incorrect forms in the model but mark them wrong.
# This can be useful in spellchecking or pedagogically.
# The learner of a language can be informed that they have used the wrong kind of paradigm
# instead of interpreting their answer as a typing error.
# E.g. Finnish auto -> audon, suo -> suoita.
# Allow over-generation and mark wrong forms with "Err/Orth", see e.g. vro language in giella infra. EXAMPLE???
#
# Is it the stem or ending that is altered? Where should the flag/filter/trigger be placed?
# E.g. Finnish singular illative: käsi - käteen. Is it käte+Vn, kätee+n, kät+een? EXAMPLE??? WHERE IS THE WORD DEFINED?
#
# Another example: do Estonian nouns and adjectives follow the same pattern?
# Do we want to have separate paradigms, or use the same (with some exceptions such as 'nen'-endings)?
#
# ```
# ls fin/src/morphology/affixes/
#   abbreviations.lexc  acronyms.lexc  adjectives.lexc  adv.lexc  codifieds.lexc  digits.lexc  nouns.lexc  numerals.lexc
#   particles.lexc  pp.lexc  prefix.lexc  pron.lexc  propernouns.lexc  symbols.lexc  verbs.lexc
#
# ls est/src/morphology/affixes/
#   declinations.lexc  gi.lexc  symbols.lexc  verbs.lexc
# ```
#
# How productive should the model be? E.g. Finnish numerals: yhdesti ('once'), kahdesti ('twice'), kolmesti ('thrice'), neljästi ('four times'),
# kymmenesti ('ten times'), kahdestitoista ('twelve times'), sadasti ('hundred times'), tuhannesti ('thousand times'), miljoonasti ('million times')?
#
# fin/src/morphology/stems/adverbs.lexc:
#
# ```
# yhdesti+Adv+Der/sti:yhdesti  PCLE_TYHMÄSTI  ;
# yhdesti+Adv:yhdesti  ADV_FRONT_CLIT_OPT  ;
# yhdesti+Pcle:yhdesti  ADV_TYHMÄSTI  ;
# ```
#
# Numbers only from yhdesti to kymmenesti, but not yhdestitoista etc. However:
#
# ```
# sadasti+Adv+Der/sti:sadasti  PCLE_NOPEASTI  ;
# sadasti+Adv:sadasti  ADV_BACK_CLIT_OPT  ;
# sadasti+Pcle:sadasti  ADV_NOPEASTI  ;
#
# ...
#
# tuhannesti+Adv+Der/sti:tuhannesti  PCLE_NOPEASTI  ;
# tuhannesti+Adv:tuhannesti  ADV_BACK_CLIT_OPT  ;
# tuhannesti+Pcle:tuhannesti  ADV_NOPEASTI  ;
# ```
#
# "Tuhannesti" is used in fixed expressions, such as "Tuhannesti kiitoksia!" (~ 'thousand times thanks').
#
# Also: Ingrian numerals. EXAMPLE???

# ## 2. Adding a language
#
# E.g. in Giella infra, Veps and Olonets exist, Ludian must be added.
# In Ludian, diphtongs are changed to a single vocal, last vowel drops. Cf. Finnish sauna -> Estonian saun.
#
# <table>
# <tr><th>vep</th><th>lud</th><th>olo</th><th>en</th></tr>
# <tr><td>hein</td><td>hein</td><td>heiny</td><td>hay</td></tr>
# <tr><td>marʼ</td><td>muarʼ</td><td>muarju</td><td>berry</td></tr>
# <tr><td>ma</td><td>mua</td><td>mua</td><td>land, earth</td></tr>
# </table>
