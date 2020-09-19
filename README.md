

<p align="center">
    <img src="https://github.com/Jimut123/CAPTCHA/blob/master/captcha.png">
</p>

***

<p align="center">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat">
     <img src="https://img.shields.io/badge/first--timers--only-friendly-blue.svg">
</p>

# CAPTCHA 


We have build many models to solve some of the difficult open sourced CAPTCHAs that are available on the internet. We have obtained about more than 99.5% accuracy on most of the models, which converges at about 5 epochs. The ``generators`` folder have some of the modified codes that we have used to generate the data to feed into the model. The ``pyfiles`` folder section have all of the models and their corresponding python codes. 

## Results

| CAPTCHA name| CAPTCHA  img| Algorithm used  | Accuracy Obtained | Try out in Google Colab|
| :------------ | :------------: |:---------------:| :-----:| -----:|
| JAM CAPTCHA | ![img](https://github.com/Jimut123/CAPTCHA/blob/master/pyfiles/JAM/1%2B7.png)| kNN | 99.53% | [![img](https://github.com/Jimut123/CAPTCHA/blob/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/JAM/cleaned_3/JAM_KNN.ipynb) |
| CNN_c4l_16x16_550 | ![img](https://github.com/Jimut123/CAPTCHA/blob/master/pyfiles/c4l_16x16_550/c4l_ex.png) | CNN - modified CIFAR 10 | 99.91% | [![img](https://github.com/Jimut123/CAPTCHA/blob/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/c4l_16x16_550/CNN_c4l_16x16_550.ipynb)|
| captcha-1L | ![img](https://github.com/Jimut123/CAPTCHA/blob/master/pyfiles/captcha-1L/2a2aa.png)  | Own CNN model - multilabel classification | 99.67% | [![img](https://github.com/Jimut123/CAPTCHA/blob/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/captcha-1L/images_1L_processed.ipynb) |
| captcha_4_letter | ![img](https://github.com/Jimut123/CAPTCHA/blob/master/pyfiles/captcha_4_letter/c4l.png) | LSTM model - multilabel classification | 99.87% | [![img](https://github.com/Jimut123/CAPTCHA/blob/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/captcha_4_letter/captcha_4_letter_v1_drive.ipynb) |
| captcha_v2 | ![img](https://github.com/Jimut123/CAPTCHA/blob/master/pyfiles/captcha_v2/captcha_v2.png) | Own CNN - multilabel classification | 90.102% | [![img](https://github.com/Jimut123/CAPTCHA/blob/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/captcha_v2/captcha_v2_1_drive.ipynb) |
| circle_captcha | ![img](https://github.com/Jimut123/CAPTCHA/blob/master/pyfiles/circle_captcha/circle_captcha.png) | Alex Net with multilabel classification | 99.99% | [![img](https://github.com/Jimut123/CAPTCHA/blob/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/circle_captcha/circle_captcha.ipynb) |
| faded | ![img](https://github.com/Jimut123/CAPTCHA/blob/master/pyfiles/faded/captcha_faded.png) | Alex Net with multilabel classification | 99.44% | [![img](https://github.com/Jimut123/CAPTCHA/blob/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/faded/faded_captcha.ipynb) |
| fish_eye | ![img](https://github.com/Jimut123/CAPTCHA/blob/master/pyfiles/fish_eye/fish_eye.png) | Alex Net with multilabel classification | 99.46% | [![img](https://github.com/Jimut123/CAPTCHA/blob/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/fish_eye/fish_eye.ipynb) |
| mini_captcha  | ![img](https://github.com/Jimut123/CAPTCHA/blob/master/pyfiles/mini_captcha/10epochs/mini_captcha.png) | Alex Net with multilabel classification        | 97.25% | [![img](https://github.com/Jimut123/CAPTCHA/blob/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/mini_captcha/10epochs/mini_captcha.ipynb) |
| multicolor | ![img](https://github.com/Jimut123/CAPTCHA/blob/master/pyfiles/multicolor/mc_full.png) | Alex Net with multilabel classification | 95.69% | [![img](https://github.com/Jimut123/CAPTCHA/blob/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/multicolor/mc_50per_saved_model_20e.ipynb) |
| railway_captcha | ![img](https://github.com/Jimut123/CAPTCHA/blob/master/pyfiles/railway_captcha/3_letter/604_1.png) | Own CNN model | 99.94% | [![img](https://github.com/Jimut123/CAPTCHA/blob/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/railway_captcha/4_letter/railway_captcha_4.ipynb)|
| sphinx | ![img](https://github.com/Jimut123/CAPTCHA/blob/master/pyfiles/sphinx/sphinx.png) | Alex Net with multilabel classification | 99.62% | [![img](https://github.com/Jimut123/CAPTCHA/blob/master/colab.png)](https://colab.research.google.com/github/Jimut123/CAPTCHA/blob/master/pyfiles/sphinx/sphinx_33_10e_9873.ipynb) |


## Documentation

[[Thesis - Deceiving computers in Reverse Turing Test through Deep Learning](https://arxiv.org/abs/2006.11373)] | [[Slides](https://jimut123.github.io/files/JBP_SCRIPTS/JBP_021.pdf)]


## Advisor 

* [Dripta Mj](http://www2.eng.ox.ac.uk/civil/efm/people/dripta-sarkar)

## Acknowledgements 

* [nlACh](https://github.com/nlACh)
* [41x3n](https://github.com/41x3n)

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

