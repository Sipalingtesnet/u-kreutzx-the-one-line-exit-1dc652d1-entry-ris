# The One-Line Exit

![The One-Line Exit](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)
![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/Sipalingtesnet/u-kreutzx-the-one-line-exit-1dc652d1-entry-ris/rank.svg)
![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/Sipalingtesnet/u-kreutzx-the-one-line-exit-1dc652d1-entry-ris/reward.svg)

Bounty: [The One-Line Exit](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)

## The letter

> I'm resigning from the hotel front desk, effective Friday, because I said 'my pleasure' to a man on fire, and then I said it again.

131 characters, one line, ending on a period.

## Why it is funny

A resignation letter has a shape everyone already knows: the job, the date, the
reason. This one keeps the job and the date, then spends its only real line of
reasoning on something nobody has ever written to an employer: the desk script
fired at a man who was on fire. The surprise is not that a bad night happened
at work. It is where the sentence turns, which is inward. The speaker is not
complaining about the fire, or the manager, or the hours, or the pay. The
speaker is reporting that the reflex went off, and then went off again.

That last clause is the whole joke, and it arrives where the reader has already
decided what kind of story this is. Set up as an incident report, the line
turns into a confession: it happened twice, which means the second time was not
panic, it was habit. Nobody resigns over a fire. People resign over what they
heard themselves say while the fire was happening, and over the discovery that
they would say it again with the same warmth. That is the unexpected turn, and
it is also the true part — anyone who has worked a service counter knows the
small horror of the script coming out of your own mouth at the exact wrong
moment, and coming out sincere.

It also has to work as a letter rather than a bit, which is why the first half
is deliberately dull: an actual resignation, plainly dated, addressed to
whoever reads it. The politeness of "I'm resigning" and "effective Friday"
makes the second half land harder, because the voice never breaks. No
exclamation mark, no apology, no list of grievances. A colleague could forward
this. A colleague would.

## What the program does

`main.py` writes the letter to the path in the `ENTRY_OUT` environment
variable, falling back to `/output/entry.txt`. It writes the bytes with no
trailing newline, checks the 1–140 character gate and the single-line rule
before writing, and uses the Python 3.13 standard library only. No network, no
environment secrets, nothing read from outside this repository.

```sh
env ENTRY_OUT=/tmp/entry.txt python3 main.py
wc -c /tmp/entry.txt   # 131, no trailing newline
```

## Licence

MIT. See [LICENSE](LICENSE).
