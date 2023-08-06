# 1. pysnakegym
The `pysnakegym` project provides a gym environment for developing reinforcement
learning algorithms for the game of snake.

# 2. Installation
To get started, you need to have Python 3.6+ installed. The `pysnakegym` package
can simply be installed with `pip`.

```bash
pip install pysnakegym
```

# 3. How to use
Below is an example of how to use the gym. To interface with the game of snake, the `SnakeMDP` object representing
a Markov Decision Process (MDP) is used.
```python
from pysnakegym.mdp import SnakeMDP

mdp = SnakeMDP()

state, reward, done = mdp.reset()

while not done:
    state_, reward, done = mdp.step(action=choose_action(state))
    state = state_
```

The `reset` method of the `mdp` returns a triplet consisting of the following:

* `state` **(numpy array)**: the start state of the MDP. Depending on the state representation
the shape and size will vary.
  

* `reward` **(float)**: the initial reward of the MDP.
  

* `done` **(bool)**: whether the game is finished or not. Always returns `false` for the `reset`
method.
  
---

The `step` method of the `mdp` takes an action and returns a triplet consisting of the following:
* `state` **(numpy array)**: the state of the MDP that was observed after the step
  was taken. Depending on the state representation the shape and size will vary.
  

* `reward` **(float)**: the reward observed after the step has been taken.
  

* `done` **(bool)**: whether the game is finished or not. Returns `true` if `state` is a 
final state, `false` if it is not.
  
The `step` method is a representation of the `agent-environment` interaction that
constitutes an MDP. The agent chooses an action to be taken in the environment and in return observes
a new state and a reward. 

<p align="center">
  <img width="600" height="200" src="pysnakegym/docs/img/agent_environment.svg">
</p>

# 4. State Representation
The state that the snake receives as input can be represented in many different ways. When choosing
a state representation, one must make a tradeoff between keeping the state lightweight so that
the neural network is not too complex and encoding enough information so that the snake is able
to make the right decisions for the right state. Abstracting away information means that
the set of possible states the snake can find itself in becomes smaller, however it also means
that some granularity is lost. Likewise, encoding unnecessary information blows up the set of
possible states that the snake will have to learn the correct output for.

## 4.1 Choosing Necessary Information
When selecting the information that should be included in the state representation it is helpful to think
how you as a human would play the game. Things you would want to know are the direction the snake
is currently moving in, where the obstacles are relative to the head of the snake, and where the 
food is relative to the snake's head.

## 4.2 Available States 
There are a number of state representations available to choose from:

* [boolean state representation](pysnakegym/docs/boolean_state_representation.md) 
* [grid state representation](pysnakegym/docs/grid_state_representation.md)