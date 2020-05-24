---
title: 'How likely that someone we know dies from COVID-19?'
date: 2020-05-24
permalink: /blog/2020/covid19-deaths/
tags:
  - COVID19
---


The pandemic caused by the SARS-CoV-2 virus continues to spread and dominate daily life in 2020. Yet, despite the alarming numbers reported ("X millions of cases!") it can feel abstract. 
<!--If it is not affecting us personally, it can be easy to write off the fear and anxiety of others as overblown. -->
As humans, we tend to care a lot more about our *tribe* than about anonymous people. With that in mind, what is the probability someone we care about dies from COVID-19?


First we need to define what caring about means: the average number of meaningful, stable social connections one can make (known as [Dumbar's number](https://en.wikipedia.org/wiki/Dunbar%27s_number)) is estimated around $150$. Even in our modern, hyperconnected world, it is hard to argue that it goes beyond $10^3$ individuals. In other words, individually we care about an *extremely* small fraction ($> 0.00001\%$) of humanity. A straightforward estimate of the probability $P$ of at least one of those contacts dying is then:

\begin{equation}
P = 1 - \left(1-\frac{K}{N}.CFR\right)^K
\end{equation}

where $K$ is the number of people we know, $N$ is the number of infected people, and $CFR$ is the **C**ase **F**atality **R**ate of the disease. Estimating both $N_I$ and $CFR$ is current extremely challenging: $N$ suffers from undersampling bias due to lack of testing, while $CFR$ depends heavily on factors such as age, hospital infraestructure, and comorbidities. See [[1](https://ourworldindata.org/mortality-risk-covid#what-do-we-know-about-the-risk-of-dying-from-covid-19)] for a comprehensive discussion. Nevertheless, using $CFR=1.38\%$ [2], we find:


Here we see that, as the disease spreads, almost surely someone we know will die from it. Knowing more people just makes it faster. For $K=150$ the threshold where $P>0.5$ (more likely to have a death than not) happens around XX cases. For $K=1000$ it is at XX cases. This helps explain why many people are not very worried about COVID-19: for many regions, numbers of cases are not high enough to be felt on a personal level. It is important to note, however, that the increase in $P$ is not linear: after this threshold in cases is reached, very quickly a death becomes almost certain. 

We can improve the analysis a bit. As mentioned, the $CFR$ depends heavily on age:

()[]
Fig. 1: Age dependency of the $CFR$, taken from [3].

A better estimate for the probability of death then takes into account both the age dependency of the $CFR$, and the age distribution (also known as *population pyramid*) of a given society. We assume that cases are spread homogeneously in the population, and that the age of the people we know follows the age distribution of the general population. With this, our expression for the probability of a death becomes:


where XXX

To calculate $P$ we need values for $CFR_i$ and $f_i$. To exemplify, we consider Brazil and Italy, which have markedly different population pyramids. We find:




In conclusion, our simple analysis suggests that 




### References:
1. [https://ourworldindata.org/mortality-risk-covid](https://ourworldindata.org/mortality-risk-covid#what-do-we-know-about-the-risk-of-dying-from-covid-19)

2. Verity et al. "Estimates of the severity of coronavirus disease 2019: a model-based analysis". The Lancet Infectious Diseases 2020. DOI: [10.1016/S1473-3099(20)30243-7](https://doi.org/10.1016/S1473-3099(20)30243-7)