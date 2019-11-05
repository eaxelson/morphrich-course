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
#
# Inflection can be present in two parts of a word: e.g. otti-lähti - ota-lähde.
# There is a long-distance dependency. Features that must be the same are
# Act/Pass, Tempus, Numerus, Person, Modus (sometimes even Inf/Fin), making a total of
# 2 x 4 x 2 x 3 x 4 (x 2) = 64 x 3 = 192 (x 2) combinations. If these are modeled by
# simply listing all possible word-forms, the model gets big. Alternative solution:
# flag diacritics.
#
# Sometimes we want to keep the incorrect forms in the model but mark them as wrong.
# This can be useful spellchecking or pedagogically.
# The learner of a language can be informed that they have used the wrong kind of paradigm
# instead of interpreting their answer as a typing error.
# E.g. Finnish auto -> audon, suo -> suoita.
# Allow over-generation and mark wrong forms with "Err/Orth", see e.g. vro language in giella infra.
#
# Stem or ending that is altered? Where should the flag/filter/trigger be placed?
# E.g. Finnish singular illative: käsi - käteen. Is it käte+Vn, kätee+n, kät+een?
#
# Another example: Estonian nouns and adjectives, +N and +A, do they follow the same pattern?
# Do we want to have separate paradigms, or use the same (with some exceptions ('nen'-endings))?
# How productive should the model be? E.g. Finnish numerals: yhdesti, kahdesti, kolmesti, neljästi,
# kymmenesti, kahdestitoista, sadasti, miljoonasti?
# Also Ingrian numerals.

# ## 2. Adding a similar language
#
# E.g. in Giella infra, Veps and Olonets exist, Ludian must be added.
# In Ludian, diphtongs are changed to a single vocal, last vowel drops. Cf. Finnish sauna -> Estonian saun.
#
# <table>
# <tr><th>vep</th><th>lud</th><th>olo</th><th>en</th></tr>
# <tr><td>hein</td><td>hein</td><td>heiny</td><td>hay</td></tr>
# <tr><td>mar'</td><td>muar'</td><td>muarju</td><td>berry</td></tr>
# <tr><td>ma</td><td>mua</td><td>mua</td><td>land, earth</td></tr>
# </table>
