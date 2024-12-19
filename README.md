# Introduction
Self-Consistency is a metric that measures the accuracy of converting model generation from natural langauge to programming language and back to natural language. This metric allows the testing of a model's understanding of the code it is generating. [Paper](https://arxiv.org/pdf/2310.14053). We use this metric in order to test SemCoder_S, a new model that was recently released that's uniquely tuned on semantic reasoning. SemCoder_S is special in the fact that it uses forward and backward monologue to allow the model to understand the code each step of the way. Therefore, our hypothesis is that SemCoder_S's semantic reasoning capabilities will allow it to perform better on the self-consistency metric as it actually understands the code it is generating.

# Evaluation Results
We first evaluate SemCoder_S using IdentityChain of lengths 1 through 3 on HumanEval (164 coding questions) and get the following results:

<p align="center">
<img width="375" alt="Screenshot 2024-12-19 at 12 49 54 PM" src="https://github.com/user-attachments/assets/a3885e1a-ab3d-4559-b044-d81d9c6841e4" />
</p>

We then compare these results to the current models in the industry

<p align="center">
<img width="377" alt="Screenshot 2024-12-19 at 12 50 37 PM" src="https://github.com/user-attachments/assets/e1a7d675-8888-45d9-9c4e-2a021e36a7e8" />
</p>

We can see that SemCoder_S's semantic reasoning capabilities allow it to perform much better than other state of the art models.

# How to Use

This repo mainly contains code from the IdentityChain repo present here - https://github.com/marcusm117/IdentityChain/tree/56e1ec407ce31b5d024edec1da2f58e8f166c879 and the SemCoder-S HuggingFace files. 

The ``experiments`` folder contains scripts we run to analyze the self-consistency metric (please note: this is still a work in progress) 
- For initial start of setting up SemCoder and translating NL->PL->NL based on SemCoder README, please use ``semcoder.ipynb``
- For running IdentityChain on SemCoder based on HumanEval dataset, please use ``self-consistency-semcoder.ipynb``
     - This code only runs IdentityChain from lengths 1 to 3
- For running tests with "noisy" inputs where NL/PL prompts are polluted, please use ``semcoder_noisy_test.ipynb``

To replicate the above results, please run the the two notebooks using a GPU. 

---

*README for SemCoder Self-Consistency project: COMS E6998 Generative Models for Code*
