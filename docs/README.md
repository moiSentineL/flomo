<p align="center">
<img src="https://raw.githubusercontent.com/moiSentineL/flomo/main/docs/assets/flomo-speed.gif" width="500">
</p>

# flomo

`flomo` is a cross-platform TUI/CLI for using the Flowtime Technique a.k.a. **Flowmodoro** Technique. It is a task execution helper, or in other words, productivity booster. `flomo` allows you to work on tasks in a flow state and manage your work/break time.

## Features

-   Cross-Platform
-   Stopwatch for Flow and Timer for Breaks
-   Notification (Linux only, for now.)
-   Nice and Clean UI
-   Fairly easy-to-use, I suppose.
-   (Potential) productivity booster.

## Background

`flomo` was started as a Hackathon ([livestream](https://www.youtube.com/live/xyqQgPEozv0 "https://www.youtube.com/live/xyqQgPEozv0")) on 6 June, 2024 with [@Jonak-Adipta-Kalita](https://github.com/Jonak-Adipta-Kalita "https://github.com/Jonak-Adipta-Kalita") and [@AnubhavSC](https://github.com/AnubhavSC "https://github.com/AnubhavSC"). We wanted to create a small scale project which was fun to make and possibly helped others as well. Moreover, we all are productivity fanatics. This is a project *heavily* inspired by [pomo](https://github.com/kevinschoon/pomo "https://github.com/kevinschoon/pomo").

And when we were 2 hours in, we realised that it was harder than we thought. We spent a lot of time debugging and refactoring. [Here](https://nibirsan.org/blog/p/the-hackathon-experience/) are the things we learned from the Hackathon.

## Flow and Flowtime Technique

[Mihaly Csikszentmihalyi](https://en.wikipedia.org/wiki/Mihaly_Csikszentmihalyi "https://en.wikipedia.org/wiki/Mihaly_Csikszentmihalyi") was known for his work on **Flow Theory**. He describes "flow" as:[^1]

> "A state of being in which people become so immersed in the joy of their work or activity 'that nothing else seems to matter.'"

And as developers/creators/romantics, we experience that state of "flow" often. This "flow" can **vary** at times, meaning that it can increase *or* decrease.

This can easily be shown with a graph:

<p align="center">
<img src="https://raw.githubusercontent.com/moiSentineL/flomo/main/docs/assets/flow-graph.png" width="500">
</p>

However, we can exploit that to our advantage and work efficiently, by finding the **right time** to take a break. And that right time is when the "flow" is depleting. And this is called the Flowtime technique.

It works fairly simply: **If you work for x amount of minutes, you should take a break for x/5 amount of minutes. And repeat.**

This calls for extensive amount of discipline. Which means that you must have at least some amount of natural focus. If not, I encourage you to check the Pomodoro Technique out.

## Installation

### Pre-requisites

-   [Python](https://www.python.org/)
-   [pip](https://pip.pypa.io/en/stable/installation/)

### Instructions

#### Using PyPi package

```bash
pip install flomodoro
```

If you are on Linux, make sure you have `/home/user/.local/bin` in your `PATH`. [More info for Linux newbies](https://linuxize.com/post/how-to-add-directory-to-path-in-linux/ "https://linuxize.com/post/how-to-add-directory-to-path-in-linux/")

#### Installing from source

```bash
git clone https://github.com/moiSentineL/flomo.git
cd flomo
pip install -r requirements.txt

pip install -e .
```

## Usage

### Known Issues

-   Skip doesn't work while on break (you can just make another session).
-   Might not work if you have attention span of a goldfish.

### Getting Started

Start a flow by:

```bash
flomo s
```

Start a flow with tag `work` and `math` as session name:

```bash
flomo s -t work -n "math"
```

### Commands

```
flomo --help
    Usage: flomo [OPTIONS] COMMAND [ARGS]...

    A Flowmodoro CLI for productivity enthusiasts.

    Options:
    --help  Show this message and exit.

    Commands:
    init (i)      Initialize the required files for Flomo.
    start (s)     Start a Flowmodoro session.
    tracking (t)  Show the tracking history.
    delete (d)    Delete sessions.
    change (ch)   Change session data.
    config (cf)   Print config file path
    error (er)    Show the error log.
```

#### Pro Tip for Linux Users

If you have to repeat working on certain tags (or sessions) and don't want to keep typing the commands every time, you can create a simple script like [study.sh](https://raw.githubusercontent.com/moiSentineL/flomo/main/docs/study.sh), and set an alias to that script.

For example, with _that_ script, I can simply enter `study math` (I've set "study" as the alias) in my terminal and it will start a session with the tag `study` (in my case) with `math` as the session name.

## Roadmap

-   [x] Add sound on timer/stopwatch start
-   [x] Notification (only Linux for now)
-   [ ] Tracking data / time studied
-   [ ] Configure colors

Check our [Kanban Board](https://github.com/users/moiSentineL/projects/2 "https://github.com/users/moiSentineL/projects/2")

[^1]: : Csikszentmihalyi, M. (1990). *Flow: The Psychology of Optimal Experience*. New York: Harper and Row. p. 15 [ISBN](<https://en.wikipedia.org/wiki/ISBN_(identifier)> "ISBN (identifier)") [0-06-092043-2](https://en.wikipedia.org/wiki/Special:BookSources/0-06-092043-2 "Special:BookSources/0-06-092043-2")
