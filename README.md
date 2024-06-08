## Still in-the-making

# flomo

`flomo` is a TUI/CLI for using the Flowtime Technique a.k.a. **Flowmodoro** Technique. It is a task execution helper, or in other words, productivity booster. `flomo` allows you to work on tasks in a flow state, track and manage your work/break time. 

## Background

`flomo` was started as a Hackathon ([livestream](https://www.youtube.com/live/xyqQgPEozv0)) on 6 June, 2024 with [@Jonak-Adipta-Kalita](https://github.com/Jonak-Adipta-Kalita) and [@AnubhavSC](https://github.com/AnubhavSC). We wanted to create a small scale project which was fun to make and possibly helped others as well. Moreover, we all are productivity fanatics. This is a project *heavily* inspired by [pomo](https://github.com/kevinschoon/pomo).

And when we were 2 hours in, we realised that it was harder than we thought. We spent a lot of time debugging and refactoring. And we're still working on it.
## Flow and Flowtime Technique

[Mihaly Csikszentmihalyi](https://en.wikipedia.org/wiki/Mihaly_Csikszentmihalyi) was known for his work on **Flow Theory**. He describes "flow" as[^1]:

> "A state of being in which people become so immersed in the joy of their work or activity 'that nothing else seems to matter.'"

And as developers/creators/romantics, we experience that state of "flow" often. This "flow" can **vary** at times, meaning that it can increase _or_ decrease.

This can easily be shown with a graph:
<p align="center">
    <img src="https://github.com/moiSentineL/flomo/blob/main/assets/flow-graph.png" width="500">
</p>

However, we can exploit that to our advantage and work efficiently, by finding the **right time** to take a break. And that right time is when the "flow" is depleting.
And this is called the Flowtime technique.

It works fairly simply:
**If you work for x amount of minutes, you should take a break for x/5 amount of minutes. And repeat.**

This calls for extensive amount of discipline. Which means that you must have at least some amount of natural focus. If not, I encourage you to check the Pomodoro Technique out.

<!--
## Installation
```bash
pip install -e flomo
```
### Source

 ```bash
git clone https://github.com/moiSentineL/flomo.git
cd flomo
pip install -r requirements.txt

# copy pomo somewhere on your $PATH
cp bin/flomo ~/bin/
 ```

## Usage
### Getting Started

Once `flomo` is installed you need to initialize it's database.

``` bash
flomo init
```

Start a flow with tag "work" and "write some code" as session name:
```bash
flomo start -t work -n "write some code"
```
### Commands
```bash
flomo --help
	start, s       starts a flow session
	init           initialises database
	track, t       track statistics
	config, cf     display current configuration
```
-->

## Roadmap
Check our [Kanban Board](https://github.com/users/moiSentineL/projects/2)

[^1]: : Csikszentmihalyi, M. (1990). _Flow: The Psychology of Optimal Experience_. New York: Harper and Row. p. 15 [ISBN](<https://en.wikipedia.org/wiki/ISBN_(identifier)> "ISBN (identifier)") [0-06-092043-2](https://en.wikipedia.org/wiki/Special:BookSources/0-06-092043-2 "Special:BookSources/0-06-092043-2")
