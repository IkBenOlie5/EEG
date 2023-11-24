# Continuing with our project
If you want to continue with our project, we have a few ideas on how the EEG and software can be improved.

## More electrodes
Firstly, you could add more electrodes, we currently only use three electrodes, but this number could be increased drastically. This will then allow you to use a technique called [Independant Component Analysis (ICA) to remove artifacts](https://ieeexplore.ieee.org/document/7011635). We currently also get noise unrelated to concentration or whether someones eyes are open such as speaking and muscles firing. This is usually also used to filter out the signals from blinking, but we wanted to use exactly this for playing flappy bird as it gives really high peaks.

## Thought detection
With more electrodes, which can also be achieved by simply buying a premade EEG, you can try to build a neural network that is able to detect what someone is thinking about: https://youtube.com/watch?v=DBYY3D1gkQ0&si=ZuJdfMcYiEgIXuje

## Radio signal
When we play back the raw signal using Audacity, we can hear a radio station in the background (we even heard a Nivea commercial). You could try to build a radio antenna and filter out all the noise (which is done very similarly to how we filter out the noise).

