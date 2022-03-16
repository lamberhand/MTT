## Programatic Visualisation



### When do visuals helps understand math

- Something about the result is unexpected
- Create an alternate medium of explannation



[Quaternion](https://eater.net/quaternions): 
$$
q=cos(Angle)+sin(Angle)(ai+bj+ck),\\
where (a,b,c)\ is\ unit\ vector\ representing\ the\ axis\\
usually\ f(p)=qpq^{-1}\\
if\ unlocked,\ it\ will\ be\ a\ projection\ of\ a\ hypersphere
$$




Axel • 3 years ago
Those explorable videos are revolutionary! What software / library was used to do this?
		
  Ben Eater Mod Axel • 3 years ago
Since there wasn't really anything like this yet, we built it all ourselves from a variety of existing web tools: WebGL (using threejs plus some custom shaders) for 3d stuff, raw canvas for the 2d stuff, howlerjs for handling the audio playback, and lots of React for the UI and to glue it all together. It's very much a bespoke app. In the future, I hope we'll build more of these and as we do so, the tech will evolve to something more easily generalized.