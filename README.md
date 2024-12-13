---
license: mit
---
This is the README for the COMS6998: COMS E6998 Generative Models for Code class. 

This repo mainly contains code from the IdentityChain repo present here - https://github.com/marcusm117/IdentityChain/tree/56e1ec407ce31b5d024edec1da2f58e8f166c879 and the SemCoder-S HuggingFace files. 



The ``experiments`` folder contains scripts we run to analyze the self-consistency metric (please note: this is still a work in progress) 


``semcoder.ipynb`` is the file that contains code for setting up SemCoder and code for translating NL to PL and PL to NL. These experiments are based on the details in the SemCoder readme. 

``self-consistency-semcoder.ipynb`` is the file that contains NL to PL to NL code based on the [IdentityChain framework](https://github.com/marcusm117/IdentityChain) and conducts experiments using the [HumanEval dataset](https://github.com/openai/human-eval).

To replicate the above results, please run the the two notebooks using a GPU. 
