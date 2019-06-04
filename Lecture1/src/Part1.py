# # MORPHOLOGICALLY RICH LANGUAGES WITH HFST TOOLS - LECTURE 1
#
# <ul>
# <li>1. <a href="#1.-Background">Background</a></li>
# <li>2. <a href="#2.-Prerequisites">Prerequisites</a></li>
# <li>3. <a href="#3.-Course-material">Course material</a></li>
# <li>4. <a href="#4.-Course-overview">Course overview</a></li>
# <li>5. <a href="#5.-Majority-vs.-minority-language-technology">Majority vs. minority language technology</a></li>
# </ul>

# ## 1. Background
#
# This web course is based on a course by Jack Rueter & Sjur Moshagen organized at the University of Helsinki
# named <i>Language Technology for Finno-Ugric Languages - Methods, Tools and Applications</i>.
# The course belongs to the MA Programme <i>Linguistic Diversity in the Digital Age</i>.
#
# This course gives an introduction to mainly rule-based language technology as used in many full-scale,
# production projects using the <a href="https://giellalt.uit.no/">GiellaLT</a> and
# <a href="https://en.wikipedia.org/wiki/Apertium">Apertium</a> infrastructures.
# The technologies and methodologies presented can be used on any language,
# although the focus is on morphologically complex ones.
#
# We use the Python interface of <a href="https://hfst.github.io/">HFST</a>
# toolkit which is intended for processing natural language morphologies
# of varying morphological complexity.  

# ## 2. Prerequisites
#
# <ul>
# <li>Foundations of general linguistics</li>
# <li>Basic knowledge on how to use a computer</li>
# <li>Some programming experience is desirable</li>
# <li>Knowledge of Natural Language Processing (NLP) is also a plus</li>
# </ul>

# ## 3. Course material
#
# If you want a book:
#
# <ul>
# <li>Kenneth R. Beesley and Lauri Karttunen: <a href="http://press.uchicago.edu/ucp/books/book/distributed/F/bo3613750.html">Finite State Morphology</a>, CSLI Publications, 2003</li>
# <li>Daniel Jurafsky and James H. Martin, Speech and Language Processing, Prentice Hall, second edition, 2009</li>
# </ul>
#
# Reading material:
#
# <ul>
# <li><a href="http://ixa2.si.ehu.es/~jipsagak/Moshagen_slides.pdf">Sustainable LT Resources</a> (Moshagen, 2012)</li>
# <li><a href="https://septentrio.uit.no/index.php/nordlyd/article/view/2474/2297">A restricted freedom of choice: Linguistic diversity in the digital landscape</a> (Trond Trosterud, University of Tromsø)</li>
# </ul>
#
# Links:
#
# <ul>
# <li>HFST <a href="https://hfst.github.io">main page</a>.</li>
# <li>For installation of the HFST package for Python, see our <a href="https://pypi.org/project/hfst_dev/">PyPI pages</a>.</li>
# <li>For more information about the interface, see our <a href="https://github.com/hfst/python-hfst-4.0/wiki">Github wiki pages</a>.</li>
# </ul>

# ## 4. Course overview
#
# <table>
# <tr> <th>Lecture</th> <th>Topics</th> </tr>
# <tr> <td>1</td> <td>Course intro, field overview, majority vs minority language technology</td> </tr>
# <tr> <td>2</td> <td>Intro to the Giella infra and a variety of finite-state tasks, stress on reusability and language independence</td> </tr>
# <tr> <td>3</td> <td>Simple lexc (numerals, dates, clocks)</td> </tr>
# <tr> <td>4</td> <td>Writing test material and applying simple concatenative morphology</td> </tr>
# <tr> <td>5</td> <td>Twolc & xfst rewrite rules</td> </tr>
# <tr> <td>6</td> <td>Shared language-independent modeling (examples from Saamic languages, perhaps hierarchical)</td> </tr>
# </table>

# ## 5. Majority vs. minority language technology
#
# Of course there is no such thing as minority or majority language technology per se,
# but there still is some truth to the concept. First a brief historic detour:
#
# ### Short on the history of LT
#
# The history of haves and havenots...
#
# * writing (cuneiform, hieroglyphs, alphabets like runes)
#     * many of them technologically simple, you could use what you carried with you and found around you
#         * <a href="img/cuneiform.jpg">Cuneiforms</a>
#         * <a href="img/b190.jpg">Runes</a>
#     * using bible translations as a proxy, <a href="https://en.wikipedia.org/wiki/List_of_Bible_translations_by_language">roughly 1600 of the about 7000 languages of the world still doesn't have a writing system</a> at all
# * typing:
#     * Gutenberg increased production speed tremendously, and similarly reduced costs
#     * but the initial costs got much higher — now a pen or a knife or a stick was not enough anymore, you need types, lots of types, and a big machine
#     * Gutenberg <img src="img/printpress.jpg">
# * digitalisation:
#     * reducing the cost of text production dramatically once more
#     * but the initial costs and barriers again goes up, as you need:
#         * a computer to write (and potentially all your readers as well)
#         * a keyboard (soft or hard)
#         * fonts
#         * an encoding standard
#         * standards for languages, writing systems, areas, etc.
#         * operating systems that can render your text properly using all the above (and this is still not the case for some writing systems: <a href="https://en.wikipedia.org/wiki/Mongolian_script#Font_issues">«As of 2015 there are no fonts that successfully display all of Mongolian correctly when written in Unicode.»</a>, cf also Kildin Sámi and any other language forced to use combining diacritics because Unicode does not allow any new precomposed letters)
#         * Internet <img src="img/internet.jpg">
#
#
# That is just the prerequisite costs. To actually get the LT tools you expect for e.g. Finnish, you would also need:
# 
# * a speller engine
# * a language model for the speller
# * linguistic descriptions suitable for a grammar checker
# * hyphenation rules and patterns
# * dictionaries
# * machine translation resources
# * corpora
# * sound recordings and phonetic models for text-to-speech systems
# * ... and the same for speech recognition
# * and all of this integrated with and working in a multitude of operating systems
# * ... and a number of applications on each system
# * ... and then be prepared to update your tools all the time, both linguistically and technically
# 
# The costs are truly high for working LT in our society today, we just don't usually see them.
# 
# What has happened for each major technology shift is:
# 
# * the initial costs have increased dramatically
# * more languages have been getting in
# * the use of LT has more and more turned into a requirement for being a modern society of the time, or a prerequisite for the modernisation of society
# 
# ### Today
# 
# There's a hierarchy or a scale, with English on the one end,
# and the roughly 1600 languages without any writing system at all on the other end, and the rest of the languages in between.
# In terms of LT support, most languages of the world go towards the low end.
# 
# This picture is very gross.
# Even high-end languages like German do not have everything that English has, or the quality isn't as good as for English.
# 
# And there are really big languages with tens of millions of speakers with no language technology support at all,
# as documented in the article linked to for this lecture.
# 
# <img src="img/293-2067-1-PB.jpg">
# 
# #### Linguistic differences
# 
# There's a tendency that large language communities move towards a simplified grammar.
# The top three languages of the world (Mandarin, Spanish, English) all have very modest (or no) morphology.
# 
# On the other hand, often minority languages have complex to very complex grammars.
# We have worked mostly with circumpolar languages, like Uralic languages, Greenlandic and native languages in Canada.
# All of these languages have complex to very complex morphology or morphophonology (or both!).
# 
# <a href="img/gtlangs_circumpolar_names.png">International cooperation</a>
# 
# 
# #### Consequences
# 
# Combine the typological differences with the differences in economy and technology,
# and the result is that the dominating language technologies are such that linguistic analysis doesn't really matter.
# Morphology is a problem rather than a feature, and the same goes for phonology:
# the technologies basically assumes a linear string of (mostly) invariant words, and calculate statistical or other patterns from these strings.
# 
# This makes it even harder to develop tools for the languages we care about - the mainstream technology is more or less useless, at least presently.
# 
# For the minority language communities this means that:
# 
# * young people want access to technology, and if they can't get it in their mother tongue they will use another language — minority language speakers are very often bi- or multilingual
# * lack of LT is becoming a strong force in language death — a language that is not being used is a dead language
# 
# ### The alternatives
# 
# Fortunately there are still nation-state languages with complex morphology
# and with universities and research groups working on alternative technologies,
# University of Helsinki being one such place.
# 
# Using technology developed here,
# it is possible to build tools and LT solutions that will work well for in principle any language in the world.
# 
# This course is an introduction to these technologies and the tools that can be built with them, and the framework around them.
# 
# 
# #### Support for minority languages
# 
# Our work has focused on minority languages, starting out with the Sámi languages.
# 
# * rule-based technology
# * writing support, support for building a written culture
# * supporting an independent language community
# 
# This means making everything from keyboards to speech synthesis (and maybe speech recognition in the future)
# 
# <a href="img/crk-Latn.png">Plains cree keyboard menu entry</a>
# 
# So — does it make sense to talk about minority and majority LT?
# Not in itself, but because of the material basis or reality that LT must build on, and that have been presented above, it does.
# 
# #### Majority language technology (= "English" LT)
# 
# * statistical, and now also neural
# * depends on huge corpora
# * no linguists needed, only statisticians and software engineers
# 
# #### Minority language technology
# 
# * rule-based, perhaps neural in the future as a complement
# * depends on there being:
#     * mother tongue speakers
#     * ... and good grammars and dictionaries
#     * ... and linguists
# 
# As long as there are mother tongue speakers, it is always possible to build a working system.
# 
# ### Reducing the costs
# 
# Due to the huge initial costs of developing working LT solutions (independent of technology),
# a lot of our work has focused on ways to reduce that initial cost for new language communities,
# or concentrating the costs to where the language communities can afford it.
# Very much circles around the concept of reusability and grammatical work.
# 
# #### Reusable grammars
# 
# * writing rule-based descriptions of a language is labour intensive, but a well-written description can be reused in most applications
#     * by covering *and tagging* both descriptive and normative features of the grammar it can be used for both descriptive and normative tasks
#     * in general, by making all features of a grammar explicit in the linguistic analysis, one can easily modify the grammar for various purposes
# * lack of corpus material - there just isn't enough text to build statistical or neural models, if there is text at all
# * mirroring the internalized grammar of people requires just people, not huge corpora or training data
# 
# 
# #### Reusable LT tool components
# 
# The basic machinery of a speller is the same independent of language.
# At the same time it is a lot of work to develop a decent speller engine,
# and make it work with MS Office, LibreOffice, InDesign, etc
# 
# Factoring out those components,
# ensuring they are language independent, makes it possible to reuse them for any language.
# 
# The same goes for grammar checkers, hyphenators, machine translation, language learning tools, and so on.
# 
# The work we have done, and are doing,
# for the Sámi languages will thus become available and usable for any other language building on our resources.
# 
# #### Scalable infrastructure
# 
# All of the above is baked into the infrastructures we use for our LT development.
# Most of the work is done in the Giella infrastructure, and MT work is done in the Apertium infrastructure.
# Both share the same philosophy regarding reuse and support for minority languages.
# 
# The Giella infrastructure specifically is built to support scaling in two dimensions:
# 
# * adding new languages
# * adding support for new tools and features
# 
# This makes it possible for a new language community to get a head start, saving both in time and costs:
# 
# * all basic setup is done
# * all integration work is done
# * ⇒ you can start directly on the linguistic work, concentrate on that, and rest assured that the final tools will work in LibreOffice, MS Office, and on Windows, Linux and macOS, and so forth
# 
# ## Summary
# 
# * given the realities of today, it makes some sense to talk about minority language LT ⇒ but the picture is more complicated than just a minority vs. majority dichotomy
# * the up-front costs of LT is huge, leaving most languages out of even basic LT support
# * working rule-based and with reusability in mind helps reduce the costs
# * building on what has been done for other languages helps further reducing the costs
# * this course will focus on mostly minority languages from the Uralic language family
