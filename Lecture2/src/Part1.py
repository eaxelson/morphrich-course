# # MORPHOLOGICALLY RICH LANGUAGES WITH HFST TOOLS - LECTURE 2
#
# <ul>
# <li>1. <a href="#1.-Prerequisites">Prerequisites</a></li>
# <li>2. <a href="#2.-Course-material">Course material</a></li>
# <li>3. <a href="#3.-Course-overview">Course overview</a></li>
# <li>4. <a href="#6.-Majority-vs-minority-language-technology">Majority vs. minority language technology</a></li>
# </ul>
#
# Intro to the Giella infra and a variety of finite-state tasks
# 
# * stress on reusability and language independence
# 
# Reading material:
# 
# * <a href="https://github.com/mhulden/foma/blob/master/foma/docs/simpleintro.md">Foma Simple Intro</a>
# * <a href="http://emmtee.net/oe/nodalida13/conference/43.pdf">Building an open-source development infrastructure for language technology projects</a>
# 
# Exercises: **install foma or hfst**
# 
# * <a href="https://fomafst.github.io/">foma</a>
# * <a href="https://github.com/hfst/hfst/wiki/Download-And-Install">hfst</a>
# 
# ## The Giella infra
# 
# From the previous lecture:
# 
# > The Giella infrastructure specifically is built to support scaling in two dimensions:
# > 
# > * adding new languages
# > * adding support for new tools and features
# > 
# > This makes it possible for a new language community to get a head start, saving both in time and costs:
# > 
# > * all basic setup is done
# > * all integration work is done
# > * ⇒ you can start directly on the linguistic work, concentrate on that, and rest assured that the final tools will work in LibreOffice, MS Office, and on Windows, Linux and macOS, and so forth
# 
# Now let us look at the infrastructure in more detail.
# 
# On the top level we have the following directories (plus a few more that I have removed for clarity):
# 
# ```
# .
# ├── experiment-langs
# ├── external-langs
# ├── giella-core         # required tools and scripts
# ├── giella-libs         # precompiled libraries for spellers and other tools
# ├── giella-shared       # shared linguistic resources
# ├── giella-templates    # templates for new languages
# ├── keyboards
# ├── langs
# ├── startup-keyboards
# ├── startup-langs
# ├── techdoc             # technical documentation = divvun.no/doc/
# └── words
# 
# ```
# 
# Within all `*langs` and `*keyboards` dirs there are directories named according to their language content using ISO 639-3 codes:
# 
# ```
# startup-keyboards $ tree -d -L 1
# .
# ├── ces     # Czech
# ├── grn     # Guarani
# ├── hak     # etc.
# ├── ine
# ├── izh
# ├── kon
# ├── lin
# ├── nch
# ├── nds
# ├── rcf
# └── rom
# ```
# 
# Each language dir within `*langs/` has the following directory structure (the keyboard dirs have a much simpler structure):
# 
# ```
# .
# ├── am-shared               # language independent build commands
# ├── devtools                # tools useful for development, not need to build
# ├── doc                     # language-specific documentation
# ├── misc
# ├── src                     # the core source files
# │   ├── filters
# │   ├── hyphenation         # hyphenation rules
# │   ├── morphology          # lexical stems, inflection, derivation, compounding
# │   ├── orthography         # 
# │   ├── phonetics           # phonetic rules, e.g. useful for TTS processing
# │   ├── phonology           # (morpho)phonology
# │   ├── syntax              # syntactic descriptions (Constraint Grammar files)
# │   ├── tagsets
# │   └── transcriptions
# ├── test                    # most testing is defined within this dir
# │   ├── data
# │   ├── src
# │   └── tools
# └── tools                   # most tools are built inside this dir
#     ├── data
#     ├── grammarcheckers
#     ├── hyphenators
#     ├── mt
#     ├── shellscripts
#     ├── spellcheckers
#     └── tokenisers
# ```
# The `test/` and `tools/` dirs have further subdirs not included here for clarity.
# 
# ### Scalability
# 
# * for languages:
#     * template for all resources needed
# * for tools:
#     * add support for a new tool to the template, and propagate it to all existing languages
# * core design principle:
#     * separate language independent processing from language-specific processing
# 
# The templating system and the split between language independent and specific code ensures that we can add as many languages as we want, and easily add support for new tools and technologies.
# 
# #### Templates
# 
# ```
# giella-templates $ tree -d -L 1
# .
# ├── keyboards-templates
# └── langs-templates
# ```
# 
# `langs-templates` is the basis for all `*langs/` dirs:
# 
# ```
# $ tree -d -L 2
# .
# ├── am-shared
# ├── devtools
# ├── doc
# ├── misc
# ├── src
# │   ├── filters
# │   ├── hyphenation
# │   ├── morphology
# │   ├── orthography
# │   ├── phonetics
# │   ├── phonology
# │   ├── syntax
# │   ├── tagsets
# │   └── transcriptions
# ├── test
# │   ├── data
# │   ├── src
# │   └── tools
# └── tools
#     ├── data
#     ├── grammarcheckers
#     ├── hyphenators
#     ├── mt
#     ├── shellscripts
#     ├── spellcheckers
#     └── tokenisers
# ```
# 
# To start work on a new language, we essentially just copy this dir.
# 
# To enhance or change existing languages, we edit the template and *merge* the changes with all language dirs (using the `svn merge` function).
# 
# The cost for this operation is tremendeously lower than having to edit each language, and is also much less error prone. It is the heart of the scalability of the infrastructure.
# 
# It does require that all language independent changes are done via the templates, and *only there*. Otherwise you will get `svn` conflicts when merging, and the cost increases very fast.
# 
# ### Testing
# 
# 
# Systematic testing is essential, and the infrastructure supports several types of tests:
# 
# * classes of words/inflections/alternations
# * lemmas
# * in-source test data
# 
# Example test data:
# 
# ```
# Tests:
# 
#   Verb - båetedh: # verb I, stem -ie, root vowel -åe-
#     båetedh+V+IV+Inf: båetedh
#     båetedh+V+IV+Ind+Prs+Sg1: båatam
#     båetedh+V+IV+Ind+Prs+Sg2: båatah
#     båetedh+V+IV+Ind+Prs+Sg3: båata
#     båetedh+V+IV+Ind+Prs+Du1: båetien
#     båetedh+V+IV+Ind+Prs+Du2: [båeteden, båetiejidien]
#     båetedh+V+IV+Ind+Prs+Du3: båetiejægan
#     båetedh+V+IV+Ind+Prs+Pl1: [båetebe, båetiejibie]
#     båetedh+V+IV+Ind+Prs+Pl2: [båetede, båetiejidie]
#     båetedh+V+IV+Ind+Prs+Pl3: båetieh
# ```
# 
# This can be used both as a development gold standard, and as regression testing later.
# 
# 
# There is more about testing <a href="http://divvun.no/doc/infra/infraremake/AddingMorphologicalTestData.html">here</a>. (todo: fix link)
# 
# ### Keyboards in the Giella infra
# 
# We use a very simple syntax (mobile keyboard shown) to specify the keyboard layout, essentially typing out the keyboard as we want it in a text file:
# 
# ```
# modes:
#   mobile-default: |
#     á š e r t y u i o p ŋ
#     a s d f g h j k l đ ŧ
#        ž z č c v b n m
#   mobile-shift: |
#     Á Š E R T Y U I O P Ŋ
#     A S D F G H J K L Đ Ŧ
#        Ž Z Č C V B N M
# ```
# This text file corresponds to the following mobile keyboard:
# 
# <a href="img/sme-ios.png">North Sámi on iOS</a>
# 
# As can be seen, the on-screen keyboard matches the layout definition exactly.
# 
# We use the exact same setup for desktop keyboards. The infrastructure / build commands will take the above text definition of the keyboard, and turn it into an iOS app, an Android app, a Windows keyboard installer and so on.
# 
# ## Install Hfst / Foma, optionally the full giella infra
# 
# * <a href="https://fomafst.github.io/">foma</a>
# * <a href="https://github.com/hfst/hfst/wiki/Download-And-Install">hfst</a>
# * <a href="http://divvun.no/doc/infra/infraremake/GettingStartedWithTheNewInfra.html#Only+the+GT+core+and+the+wanted+language%28s%29">The Giella infra</a>
# 
# ## Some finite-state tasks
# 
# We run through (some of) the excercises here:
# 
# * <a href="https://github.com/mhulden/foma/blob/master/foma/docs/simpleintro.md">Foma Simple Intro</a>
