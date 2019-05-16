# # MORPHOLOGICALLY RICH LANGUAGES WITH HFST TOOLS - LECTURE 4
#
# Topics:
#
# * lexc: practices and automated documentation
# * production and reuse of test materials for development of analysers/generators
#
# Have a look at the <a href="https://en.wikipedia.org/wiki/YAML">yaml</a>
# file for Olonetsian Karelian nouns.
# Download it from
# https://victorio.uit.no/langtech/trunk/langs/olo/test/src/gt-norm-yamls/N-kala_gt-norm.yaml
# or use a copy available in this directory.

# First the configuration that defines the analysis and generation transducers for hfst and xfst tools:
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
# # ```

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
