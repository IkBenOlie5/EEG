# Continuing with our project
If you wish to improve upon our project, we have several ideas on how to enhance both the EEG and software components.

## More electrodes
Firstly, consider adding more electrodes; we currently use only three, but this number could be significantly increased. This expansion allows the application of a technique called Independent Component Analysis (ICA) to eliminate artifacts. A helpful video series on ICA can be found at: [ICAnalysis - YouTube Playlist](https://www.youtube.com/playlist?list=PLXc9qfVbMMN2uDadxZ_OEsHjzcRtlLNxc). Currently, we also get noise unrelated to concentration or eye status, such as speaking and muscle activity. This noise is typically filtered out when detecting blinking, but we intentionally utilize it for playing Flappy Bird, as it produces very high peaks.

## Thought detection
With more electrodes, achievable by purchasing a pre-made EEG, you can attempt to build a neural network capable of detecting a person's thoughts. For more information, refer to this video: [Playing Video Games With Mind Control - YouTube](https://www.youtube.com/watch?v=DBYY3D1gkQ0&si=ZuJdfMcYiEgIXuje).

## Radio signal
When we playback the raw signal using Audacity, a radio station can be heard in the background (we even heard a Nivea commercial). Consider building a radio antenna and filtering out all the noise, a process similar to our noise filtering.

## Einthoven triangle
We believe that the triangle we have created (earlobe, front of head, and back of head) captures alpha waves due to the [Einthoven triangle](https://en.wikipedia.org/wiki/Einthoven%27s_triangle). Research whether this assumption is correct or not.

In Ryan Lopez's EEG project, he also mentioned some possible improvements, which are applicable to our EEG as well: [Ryan Lopez's EEG Project - Future Improvements](https://github.com/ryanlopezzzz/EEG#future-improvement).