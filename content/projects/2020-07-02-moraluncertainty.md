---
layout: post
title: Moral Uncertainty for AI
date: 2020-07-02
draft: false
image: /images/moralmachine.png
---

(**Update : the paper has been published !** Check it out here : [paper link](https://www.frontiersin.org/articles/10.3389/fnrgo.2023.1147211/full).)

I had the opportunity to work at [TU Delft](https://www.tudelft.nl/), the oldest technical university in The Netherlands, which also happens to be ranked among the top 10 engineering and technology universities in the world. It may sound cool, but the coolest was the proposed project : I was offered to work on the `ethical decision making` process of autonomous systems, with a focus on `autonomous vehicles`. I was there to work on the understanding and modeling of decision-making mechanisms incorporating `normative uncertainty` (uncertainty on which ethical theory is the most appropriate) for autonomous systems, and how to take `human values and credences towards ethical principles` (both at an individual and society's scales) into account when making critical decisions. How cool is that ? Well, our work was based on the very popular MIT's [Moral Machine experiment](https://www.moralmachine.net/), whose results were [published in Nature in 2018](https://www.nature.com/articles/s41586-018-0637-6). So, pretty cool.


![AiTech comic strip](https://pbs.twimg.com/media/Fd0GOYKXgAAggJ8?format=jpg&name=large "AiTech comic strip. Fun but important stuff")
| <b>Image Credits - AiTech communication</b>|

## The AiTech initiative
[AiTech](https://www.tudelft.nl/aitech) is TU Delft’s interdisciplinary research program on awareness, concepts, and design & engineering of autonomous technology under `meaningful human control`. What is meaningful human control, you ask ? Well, they defined meaningful control as a way to affect the outcome so that humans can take responsibility and act upon it. This can be pretty hard when it comes to artificial intelligence as it is closely embedded into a system and often act as a black box. The whole challenge is then about designing well-balanced human-AI systems such that meaningful human control is maintained, and humans are still responsible for the end result. It is all about keeping the benefits of automation while maintaining human responsibility and values.

![AiTech](https://d2k0ddhflgrk1i.cloudfront.net/Websections/AiTech/NEW/IMG_6254.jpg "First AiTech symposium. Clearly some hot topics.")
| <b>Image Credits - First AiTech symposium</b>|

There is a lot of involved researchers from very different backgrounds around this project : `designers`, `computer scientists`, `ethicists`, ... I personally worked under the supervision of assistant Prof. [Luciano Cavalcante Siebert](https://www.tudelft.nl/ewi/over-de-faculteit/afdelingen/intelligent-systems/interactive-intelligence/people/current-group-members/luciano-cavalcante-siebert) and Prof. [Catholjn Jonker](https://catholijnjonker.nl/) (actually, they are mentionning me [here](https://www.tudelft.nl/aitech/output#:~:text=Supervision%20of%20internship%20(student%20from%C2%A0%20IMT%20Mines%20Ales%2C%20France)%20on%20%E2%80%9CEthical%20decision%20making%20for%20autonomous%20systems%20considering%20moral%20uncertainty%E2%80%9D%20%40EEMCS%20%2D%20Luciano%2C%20Catholijn)). They have developed several approaches to contribute to the field of `machine ethics` : `predictability of humain-AI interactions`, managing one's `trust in autonomous system`, keeping `human rights in AI systems`, ... My project was about automating `decision making under moral uncertainty`.

## Moral uncertainty
Artificial agents are increasingly capable of interacting with their environment, self-learning, and making autonomous decisions. However, as they directly impact human lives, we may witness undesired consequences of their actions. In the field of autonomous vehicles, this is particularly relevant due to `non-forgiving situations`, where decisions that can irreversibly impact lives must be made in a split-second. Because we want those systems to be beneficial for individuals and society, there is a need for their decision-making process to be “good”, “right” or “fair” : in other terms, we need these systems to match our morality. The main question this reasoning rises is the following : whose morality exactly are we talking about? Who gets to decide which behaviour an artificial agent has to follow in order to be more ethical? As you guessed it, there is no universal agreement on what it means to be morally “good”. Several initiatives have proposed a converging set of ethical principles for ethical AI. However, systematic approaches to embedding these principles in autonomous systems face the challenge of disagreement between different ethical theories, i.e., `the problem of moral uncertainty`.

![The Moral Machine experiment](https://upload.wikimedia.org/wikipedia/commons/3/37/Moral_Machine_Screenshot.png "The Moral Machine experiment. Tough choice, huh ?")
| <b>Image Credits - The Moral Machine experiment, MIT</b>|

Our approach aims to contribute to the development of ethical AI that can respond to `individual moral perception`, facilitating meaningful human control to avoid responsibility gaps. We tested our method using MIT’s Moral Machine Experiment as a data source : our goal was to repurpose the well-known trolley dilemma towards means to understand and estimate `one’s credence towards normative ethical theories`. This enables us to incorporate moral uncertainty by proposing a decision-making system that combines, `via voting schemes`, different ethical theories according to predicted credence levels of human agents.

## Discussions
While the Moral Machine experiment was criticized for its improbable realness or its relevance to morality, we argue among others that the experiment results are not to be taken directly and have broader applications as they are opening discussions concerning individuals preferences or value-sensitive design processes. The main purpose of our work was not to evaluate whether such situations can happen, but rather about giving a better understanding of ethical human decision-making process and proposing an implementation of human preferences regarding ethics into autonomous systems behaviour. Our study actually showed that the use of voting schemes in order to aggregate one's preferences leads to more ethical decisions than original choices. We can therefore conclude that it is possible to make a decision that considers both a given set of ethical principles and human preferences.

There is so much things that can be further discussed here. But at the end of the day, all we want is to live in a world that is aligned with our values. AI is very new to our world, and people think there is much that remains to learn about them. While I agree with them, `I think there is much more that remains for them to learn about us`.