So the purpose of em is to create a sizing system - ie. if you want to say "this margin is this proportion of the font-size, and if the font-size changes then the margin should too", or "this heading should always be x% of the subheading size, which should always be x% of the body-text size" - using it for everything kinda implies that this isn't what you're trying to communicate, but I could be wrong.

It all depends on what the designer envisioned, really - so when implementing it's best to discuss with them why each space is what it is, what rules they used etc etc and just implement those.

As always, it's about using the right tool for the job:

% if you want to scale relative to the parent dimensions

em if you want to scale relative to the font-size

rem if you want to escape an 'em' scaling system and get back to the root size

vw, vh, dvw, dvh, vmin, vmax if you want to skip the parent and explicitly scale based on the viewport

ch if you want to make it clear that you're sizing based on number of characters

cm, mm, in, pt if you want a fixed value and are sizing for print

px if you want a fixed value and are sizing for digital

Your choice of unit describes your intent, which, in-turn, makes your code easier to maintain 👍
