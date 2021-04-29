---
title: 'Developing Qt Desktop Applications in Python'
aspectratio: 169
author: Nemanja Mićović
urlcolor: cyan
colorlinks: true
headerincludes: |
    \newcommand{\theimage}[1]{\begin{center}\includegraphics[width=1\textwidth,height=0.9\textheight,keepaspectratio]{#1}\end{center}}
    \newcommand{\en}[1]{(eng. \textit{#1})}
---

# Introduction

## About Me
\begin{columns}
    \begin{column}{0.6\textwidth}
        \begin{itemize}
            \item Teaching assistant at Faculty of Mathematics
            \item AI Research Scientist at Nordeus
            \item I like:

            \begin{itemize}
                \item Artificial Intelligence
                \item Machine Learning
                \item Education and Learning
                \item GNU/Linux and open source
                \item Python
                \item Epic and sciency fiction
                \item Video games!
            \end{itemize}
            \item My \href{http://poincare.matf.bg.ac.rs/~nemanja\_micovic/}{veb} webpage
        \end{itemize}
    \end{column}
    \begin{column}{0.4\textwidth}  %%<--- here
        \begin{center}
            \includegraphics[scale=0.2]{./images/nmicovic-katana.jpg}
        \end{center}
    \end{column}
\end{columns}

## Nordeus

\begin{center}
    \includegraphics[scale=0.2]{./images/nordeus.png}
\end{center}

- Founded over 11 years ago , now with 170+ employee from more than 20 countries
- Published games:
    - [Top Eleven](https://nordeus.com/games/top-eleven/):
        - over 230 million of registered users
        - Jose Mourinho is the face of TE
        - 11 years of being one of the most popular mobile sports games
    - [Golden Boot](https://nordeus.com/games/golden-boot/) (over 65 million players played so far)
    - [Heroic](https://nordeus.com/games/heroic/) (Unite talks: [1](https://www.youtube.com/watch?v=GEuT5-oCu_I), [2](https://youtu.be/vJZcbscZ4-o), [3](https://www.youtube.com/watch?v=_Ys7PlkKdYY&feature=youtu.be), [4](https://youtu.be/YZWKdw03Gls), [5](https://youtu.be/7mmWPtAoflI))
- ML/AI team:
    - Researches and applies AI algorithms for the needs of our games
- Visit our [ML/AI blog](https://engineering.nordeus.com/tag/ml-ai/)!
- We are hiring, check out open positions [here](https://nordeus.com/careers/)!

## Nordeus

\theimage{./images/te11.jpeg}

# Desktop Apps

## Desktop Apps

- Not easy to actually **define** :)
- But let's say these are *classical* programs that we run on our PCs and Macs
- We mostly interact through them via mouse and keyboard
- Native Desktop apps are Desktop apps created for the platform (Windows for example) in adequate technology (DotNet)
- Native apps often look very similar (due to sharing internal tech) - for example, same button style and animations
- Examples: Adobe Photoshop, Unity, GIMP, Dolphin, KDenLive...

## Web based Desktop Apps

\begin{center}
    \includegraphics[scale=0.2]{./images/electron.png}
\end{center}

- Due to rapid growth of Web technology, it's also possible to create Desktop apps
- Probably most popular framework is [Electron](https://www.electronjs.org/)
- It allows us to bundle Node based apps into packages that resemble Desktop apps
- Atom, Slack, Twitch and VSCode are great examples

## Qt

\begin{center}
    \includegraphics[scale=0.2]{./images/qt.png}
\end{center}

- C++ Framework for creating programs that support multiple platforms
- Initial releases was way back in 1995
- Current stable version is `6.0.3`
- One of the larger available frameworks for C++
- KDE organization uses Qt for lots of their projects (KDE Plasma, Konsole, Kate, KDevelop, KDenLive, Dolphin...)

## KDE Plasma

\theimage{./images/kde-plasma.jpg}

## KDevelop

\theimage{./images/kdevelop.png}

## KDenLive

\theimage{./images/kdenlive.png}

## Qt and Python

\begin{center}
    \includegraphics[scale=0.2]{./images/python.png}
\end{center}

- There are extension packages that allow you to use Qt from inside Python
- `PyQt5` is one of the most popular ones
- This is one of our goals for today!

## Deploying Python Qt based applications

- How do we **build** an app if we use Python?
- [fman](https://build-system.fman.io/) is a good solution!
- It was originally made for `fman` file browser (developed in Python nd Qt)
- You can find the tutorial [here](https://github.com/mherrmann/fbs-tutorial)

## Plan for today (live coding)

\begin{center}
    \includegraphics[scale=0.2]{./images/linus.jpg}
\end{center}

### Example 01

- Slack bot frontend
- Demonstrates how we build UI
- Demonstrates signals and slots

### Example 02

- Style GAN frontend (we shall generate dog images!)
- Demonstrates `QThread`
- Demonstrates signals and slots

## Example 01

\theimage{./images/example01.png}

## Example 02

\theimage{./images/example02.png}

## Where do I find the code and slides?

- You can find it [here](https://github.com/termNinja/pytalk2021-pyqt-desktop)
- And here: `https://github.com/termNinja/pytalk2021-pyqt-desktop`

# Thanks for your attention!

# Questions

