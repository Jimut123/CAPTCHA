

<p align="center">
    <img src="https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/captcha.png">
</p>

***

<p align="center">
    <img src="https://github.com/pytorch/examples/workflows/Run%20Examples/badge.svg">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat">
    <img src="https://img.shields.io/badge/first--timers--only-friendly-blue.svg">
    <a href="https://doi.org/10.5281/zenodo.4041154"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.4041154.svg" alt="DOI"></a>
    <img src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/deceiving-computers-in-reverse-turing-test/captcha-detection-on-jam-captcha">
    <a href="https://arxiv.org/abs/2006.11373"><img src="http://img.shields.io/badge/arXiv-2006.11373-B31B1B.svg"></a>
    
</p>

# CAPTCHA 

## Abstract

It is increasingly becoming difficult for human beings to work on their day to day life without going through the process of reverse Turing test, where the Computers tests the users to be humans or not. Almost every website and service providers today have the process of checking whether their website is being crawled or not by automated bots which could extract valuable information from their site. In the process the bots are getting more intelligent by the use of Deep Learning techniques to decipher those tests and gain unwanted automated access to data while create nuisance by posting spam. Humans spend a considerable amount of time almost every day when trying to decipher CAPTCHAs. The aim of this investigation is to check whether the use of a subset of commonly used CAPTCHAs, known as the text CAPTCHA is a reliable process for verifying their human customers. We mainly focused on the preprocessing step for every CAPTCHA which converts them in binary intensity and removes the confusion as much as possible and developed various models to correctly label as many CAPTCHAs as possible. We also suggested some ways to improve the process of verifying the humans which makes it easy for humans to solve the existing CAPTCHAs and difficult for bots to do the same. 

#### Note:

We have build many models to solve some of the difficult open sourced CAPTCHAs that are available on the internet. We have obtained about more than 99.5% accuracy on most of the models, which converges at about 5 epochs. The ``generators`` folder have some of the modified codes that we have used to generate the data to feed into the model. The ``pyfiles`` folder section have all of the models and their corresponding python codes. 

## Results

| CAPTCHA name| CAPTCHA  img| Algorithm used  | Accuracy Obtained | Try out in Google Colab|
| :------------ | :------------: |:---------------:| :-----:| -----:|
| JAM CAPTCHA | ![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/pyfiles/JAM/1%2B7.png)| kNN | 99.53% | [![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/JAM/cleaned_3/JAM_KNN.ipynb)  [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/deceiving-computers-in-reverse-turing-test/captcha-detection-on-jam-captcha)](https://paperswithcode.com/sota/captcha-detection-on-jam-captcha?p=deceiving-computers-in-reverse-turing-test)|
| CNN_c4l_16x16_550 | ![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/pyfiles/c4l_16x16_550/c4l_ex.png) | CNN - modified CIFAR 10 | 99.91% | [![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/c4l_16x16_550/CNN_c4l_16x16_550.ipynb) [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/deceiving-computers-in-reverse-turing-test/captcha-detection-on-cnn-c4l-16x16-550)](https://paperswithcode.com/sota/captcha-detection-on-cnn-c4l-16x16-550?p=deceiving-computers-in-reverse-turing-test)|
| captcha-1L | ![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/pyfiles/captcha-1L/2a2aa.png)  | Own CNN model - multilabel classification | 99.67% | [![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/captcha-1L/images_1L_processed.ipynb) [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/deceiving-computers-in-reverse-turing-test/captcha-detection-on-captcha-1l)](https://paperswithcode.com/sota/captcha-detection-on-captcha-1l?p=deceiving-computers-in-reverse-turing-test) |
| captcha_4_letter | ![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/pyfiles/captcha_4_letter/c4l.png) | LSTM model - multilabel classification | 99.87% | [![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/captcha_4_letter/captcha_4_letter_v1_drive.ipynb) [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/deceiving-computers-in-reverse-turing-test/captcha-detection-on-captcha-4-letter)](https://paperswithcode.com/sota/captcha-detection-on-captcha-4-letter?p=deceiving-computers-in-reverse-turing-test)|
| captcha_v2 | ![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/pyfiles/captcha_v2/captcha_v2.png) | Own CNN - multilabel classification | 90.102% | [![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/captcha_v2/captcha_v2_1_drive.ipynb) [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/deceiving-computers-in-reverse-turing-test/captcha-detection-on-captcha-v2)](https://paperswithcode.com/sota/captcha-detection-on-captcha-v2?p=deceiving-computers-in-reverse-turing-test)|
| circle_captcha | ![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/pyfiles/circle_captcha/circle_captcha.png) | Alex Net with multilabel classification | 99.99% | [![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/circle_captcha/circle_captcha.ipynb) [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/deceiving-computers-in-reverse-turing-test/captcha-detection-on-circle-captcha)](https://paperswithcode.com/sota/captcha-detection-on-circle-captcha?p=deceiving-computers-in-reverse-turing-test)|
| faded | ![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/pyfiles/faded/captcha_faded.png) | Alex Net with multilabel classification | 99.44% | [![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/faded/faded_captcha.ipynb) [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/deceiving-computers-in-reverse-turing-test/captcha-detection-on-faded)](https://paperswithcode.com/sota/captcha-detection-on-faded?p=deceiving-computers-in-reverse-turing-test)|
| fish_eye | ![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/pyfiles/fish_eye/fish_eye.png) | Alex Net with multilabel classification | 99.46% | [![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/fish_eye/fish_eye.ipynb) [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/deceiving-computers-in-reverse-turing-test/captcha-detection-on-fish-eye)](https://paperswithcode.com/sota/captcha-detection-on-fish-eye?p=deceiving-computers-in-reverse-turing-test)| 
| mini_captcha  | ![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/pyfiles/mini_captcha/10epochs/mini_captcha.png) | Alex Net with multilabel classification        | 97.25% | [![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/mini_captcha/10epochs/mini_captcha.ipynb) [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/deceiving-computers-in-reverse-turing-test/captcha-detection-on-mini-captcha)](https://paperswithcode.com/sota/captcha-detection-on-mini-captcha?p=deceiving-computers-in-reverse-turing-test)|
| multicolor | ![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/pyfiles/multicolor/mc_full.png) | Alex Net with multilabel classification | 95.69% | [![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/multicolor/mc_50per_saved_model_20e.ipynb) [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/deceiving-computers-in-reverse-turing-test/captcha-detection-on-multicolor)](https://paperswithcode.com/sota/captcha-detection-on-multicolor?p=deceiving-computers-in-reverse-turing-test)|
| railway_captcha | ![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/pyfiles/railway_captcha/3_letter/604_1.png) | Own CNN model | 99.94% | [![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/railway_captcha/4_letter/railway_captcha_4.ipynb)[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/deceiving-computers-in-reverse-turing-test/captcha-detection-on-railway-captcha)](https://paperswithcode.com/sota/captcha-detection-on-railway-captcha?p=deceiving-computers-in-reverse-turing-test)|
| sphinx | ![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/pyfiles/sphinx/sphinx.png) | Alex Net with multilabel classification | 99.62% | [![img](https://raw.githubusercontent.com/Jimut123/CAPTCHA/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/sphinx/sphinx_33_10e_9873.ipynb) [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/deceiving-computers-in-reverse-turing-test/captcha-detection-on-sphinx)](https://paperswithcode.com/sota/captcha-detection-on-sphinx?p=deceiving-computers-in-reverse-turing-test)|


## Documentation

[[Thesis - Deceiving computers in Reverse Turing Test through Deep Learning (Research paper)](https://arxiv.org/abs/2006.11373)] | [[Slides](https://jimut123.github.io/files/JBP_SCRIPTS/JBP_021.pdf)]


## Advisor 

* [Dripta Mj](http://www2.eng.ox.ac.uk/civil/efm/people/dripta-sarkar)

## Acknowledgements 

* [nlACh](https://github.com/nlACh) [Help regarding data uploading]
* [41x3n](https://github.com/41x3n) [Help regarding data uploading]

<details>
<summary>
<a class="btnfire small stroke"><em class="fas fa-chevron-circle-down"></em>&nbsp;&nbsp; <bold>Frequently Asked Questions</bold> </a>    
</summary>

<ul>
<li>

Are these the only notebooks? 

- No, https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/sphinx/sphinx_33_10e_9873.ipynb  is the path for testing the notebooks in Colab, please use this format for testing other notebooks, there are some awesome visualizations too...
</li>
<li>

Do we need to download the data?

- No, it is automatically downloaded, you just need to plug and play for getting the job done in Google Collaboratory.
</li>
<li>

Training time is taking too long?

- Yes, some of the CAPTCHAs really take long time to train, (over 10 hrs for just 10 epochs even in GPUs). It is good to have multiple GPUs when you are using this on your own machine.
</li>
<li>

Found a bug? or version issue?

- PRs welcome, fork it, and send a pull request!
</li>



</ul>
</details>

## Contribution


Please feel free to raise issues and fix any existing ones. Further details can be found in our [code of conduct](https://github.com/Jimut123/CAPTCHA/blob/master/CODE_OF_CONDUCT.md).

### While making a PR, please make sure you:
- [ ] Always start your PR description with "Fixes #issue_number", if you're fixing an issue.
- [ ] Briefly mention the purpose of the PR, along with the tools/libraries you have used. It would be great if you could be version specific.
- [ ] Briefly mention what logic you used to implement the changes/upgrades.
- [ ] Provide in-code review comments on GitHub to highlight specific LOC if deemed necessary.
- [ ] Please provide snapshots if deemed necessary.
- [ ] Update readme if required.



## BibTeX and citations

```
@article{DBLP:journals/corr/abs-2006-11373,
  author    = {Jimut Bahan Pal},
  title     = {Deceiving computers in Reverse Turing Test through Deep Learning},
  journal   = {CoRR},
  volume    = {abs/2006.11373},
  year      = {2020},
  url       = {https://arxiv.org/abs/2006.11373},
  archivePrefix = {arXiv},
  eprint    = {2006.11373},
  timestamp = {Tue, 23 Jun 2020 17:57:22 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2006-11373.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

