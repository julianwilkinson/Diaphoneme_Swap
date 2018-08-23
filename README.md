# Diaphoneme Swap

Diaphoneme Swap was created as a final project for the LIN 177 Computational Linguistics class in Winter 2018 at University of California, Davis. This program takes the work on systematic dialectal variation done by Phonetician John C. Wells and implements it as a Prolog program. All credit goes to Dr. Wells for his work on systematic dialectal variation as this program would not have been possible without him.

The main file to load is `diaphoneme.swipl`

The following test predicates can be used:
```Prolog
saeToOthers(SAE_Word, SAE, Realized_Word, Dialect).
wellsToOthers(Wells_Word, SAE, Realized_Word, Dialect).
```
diaphonemeSwap can be used to translate with manual input. Here's an example:
```Prolog
diaphonemeSwap([['b'],[['ɑ'],['ː']],['θ']],['rp'],Changed_Word,['sae']).
```
This will return bæθ, in addition to bɑθ, and bɑrθ as the program will map it to possible corresponding vowels in SAE.

Predicate makers written in python are also included that can be used to test other dialects or words without writing them manually in Prolog.
