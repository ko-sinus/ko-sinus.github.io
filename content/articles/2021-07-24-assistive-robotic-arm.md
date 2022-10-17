---
layout: post
title: Assistive robotic arm for children
---

This was the first `human-computer interaction for healthcare` project I made.
It was intended for an 11 years old French child named Emilie.

Before I go into the beautiful details behind it all, here is a video promoting our success :

<iframe width="560" height="315" src="https://www.youtube.com/embed/PhL7JxOnTew" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

At the time, I was working at the [HumanLab Saint-Pierre](https://www.humanlabsaintpierre.org/)
(actually, if on their homepage you see a child holding a weird thing with a motor attached to it, this is Emilie !
I am the man behind her at her right - the man on the left is the chief research engineer of the HumanLab).
The most beautiful aspect of this project is that `it is entirely open-source` - and that is why I can share all of these details with you.


## HumanLabs ?
The open-source thing is actually a common aspect to all HumanLabs projects. If you don't know what HumanLabs are, you can find more about them [here](https://myhumankit.org/en/home/).
HumanLabs basically consist of Fablabs that are specifically dedicated to `assistive technologies`.
Their goal is to encourage people with physical disabilities to conceive and manufacture their own assistive technologies, using a classic fablab's equipment (3D printing, open-source electronics, ...).

Not only did I had the chance to work within one of them, but I actually worked in a specific one :
the HumanLab Saint-Pierre, located in the South of France, works closely with the [Institut Saint-Pierre paediatric hospital](https://www.institut-st-pierre.com/), and thus benefits from a dedicated medical team support (occupational therapists, ortho-prosthetists, doctors, ...).
This cross-disciplinary team setting was key for the success of this project, as it linked `traditional orthosis manufacturing`, `3D printing` and `electronics`.

## Short context
Emilie is a timid but lovely child who has an injured arm : `her right arm is paralysed from her shoulder to her wrist`, keeping her from any elbow motion from one side.
Before this project started, she had a traditional mechanical orthosis - she had to lock her injured arm with the other one on one specific position.
My role there was to propose a way to enable the elbow motion in the most natural way possible.
Fortunatly since she could still move her fingers to grip something on her right hand, I was able to propose `an arm positioning system using the very same injured limb`.


## Disney's magic
After reviewing some interaction technologies, I decided to use `capacitive sensing` since it also resolved the direction control problem - flexion or extension.
As this project was not 'childish' enough, I based the touch sensing technology on [Disney Research Lab's Touché project](https://la.disneyresearch.com/publication/touche-enhancing-touch-interaction-on-humans-screens-liquids-and-everyday-objects/),
mainly because of its hardware simplicity (only passive components). Hardware simplicity enables efficient scalability and reproductibility at low cost, both essential for any open-source project.
Huge thanks to Danish makers [DZL](http://blog.dzl.dk/), [Mads Hobye](http://www.hobye.dk/) and [Illutron](http://illutron.dk/) for their preliminary work on bringing Disney's research into the maker world.

The final solution I designed consists of a `touch-activated mechanism which moves a linear actuator for arm positioning` (inspiration from [Lorelei's project](https://sites.google.com/site/ourkidscandoanything/)). You can find below an early stage (*not the final control design, I insist*) proof-of-concept using a long press to move the arm, and short-clicks to control directions. *The final control commands are much more simplified* since it only uses 2 types of input : `short-click` or `long press`. A long press input moves the arm, while a short-click input defines the direction : it goes up if one short click is detected before a long press, goes down is there is no short click before a long press. Unfortunately, I just happen not to have a more recent video.

<iframe src="https://drive.google.com/file/d/1Cl-wryliRHkoRjxJLqVjsEyC7giJl1Dj/preview" width="560" height="315"></iframe>

If you want full documentation on this, you can [directly head to this link](https://wikilab.myhumankit.org/index.php?title=Projets:Orth%C3%A8se_de_Coude_Robotis%C3%A9e).
For non-french speakers, [source files are on my Github](https://github.com/ko-sinus/emilie-arm).