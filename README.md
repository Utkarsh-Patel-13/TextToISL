# Text-To-IndianSignLanguage

This repo contains code for converting english sentence to Indian Sign Language (ISL) sentences then produce the video output.


## <u>ISL</u>

### Aim
To create a translation system, form text to sign language.

Enlgish language follows Subject-Verb-Object structure and ISL follows Subject-Object-Verb structure

### Algorithm  
1. Input -> Getting input and converting it to english if it's in other language
1. Parsing -> English sentence to structured grammatical representatation
1. Conversion -> Conversion of english tree to indian sign language grammer tree
1. Removing inflections -> Applying stemming and lemmentization
1. Video Creation -> Finding the clip of the words from video dataset and merging them

