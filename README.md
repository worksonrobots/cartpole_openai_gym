# cartpole_openai_gym

Getting Started with OpenAI Gymnasium for Reinforcement Learning

This repository provides a foundational setup for running reinforcement learning experiments using Gymnasium (the maintained fork of OpenAI's Gym).

It includes a step-by-step guide to installing the necessary libraries on Linux and a starter script for the classic CartPole-v1 environment to demonstrate the core API. The goal is to provide a launchpad for you to explore and create your own RL agents.

🚀 Installation and Setup (Linux)

Follow this guide to configure a clean, isolated Python environment for your projects.

Step 1: Update Your System

Ensure your system's package manager has the latest list of available software.

sudo apt-get update
sudo apt-get upgrade


Step 2: Install Python Essentials

The script requires Python 3. We also need pip (the Python package installer) and venv (for creating virtual environments). Most modern Linux distributions come with these pre-installed, but it's good to run this command to be sure.

sudo apt-get install python3 python3-pip python3-venv -y


Step 3: Create a Virtual Environment

Using a virtual environment is a crucial best practice. It isolates your project's dependencies from your system-wide Python installation, preventing conflicts.

# Create and navigate into your project directory
mkdir my-rl-project
cd my-rl-project

# Create a virtual environment named 'env'
python3 -m venv env

# Activate the virtual environment
source env/bin/activate


You'll know the environment is active when (env) appears at the start of your terminal prompt.

Step 4: Install Gymnasium

Install the gymnasium library with the Box2D extra, which includes many classic control environments like CartPole and LunarLander.

pip install "gymnasium[box2d]"


🤖 Understanding the Core Gymnasium API

The key to Gymnasium is the standardized agent-environment loop. The cartpole_example.py script demonstrates this loop.

gym.make(...): This is the universal entry point to create an environment. You pass the ID of the environment you want to use (e.g., "CartPole-v1"). The render_mode='human' argument is essential for creating a pop-up window to visualize the simulation.

env.reset(): This function is called to start a new "episode." It returns the initial observation of the environment's state.

env.step(action): This is the core of the interaction. Your agent provides an action, and the environment executes it. The function returns five crucial pieces of information:

observation: The new state of the environment after the action.

reward: The numerical feedback signal for the action taken.

terminated: A boolean (True/False) indicating if the episode ended because a terminal state was reached (e.g., pole fell, agent crashed).

truncated: A boolean indicating if the episode ended due to a time limit.

info: A dictionary for auxiliary debugging information.

env.action_space.sample(): A helper function to select a random valid action. It's great for testing an environment without a trained agent.

env.close(): Shuts down the environment and closes the visualization window.

🏆 The Reward System in CartPole

In reinforcement learning, the reward is the signal the agent tries to maximize. For CartPole-v1, the system is simple: the agent receives a reward of +1 for every timestep the pole remains balanced. The episode terminates if the pole's angle exceeds 12 degrees or the cart moves 2.4 units from the center. A perfect agent is one that maximizes its total reward by balancing the pole for as long as possible.

🧪 Running Your Own Experiments

The real power of Gymnasium is its vast collection of environments. It's incredibly easy to switch from one experiment to another.

Step 1: Find a New Environment

Explore the official Gymnasium website to find a list of available environments. Each has a unique ID, like LunarLander-v2 or Acrobot-v1.

Step 2: Modify the Code

To run a new experiment, you only need to change the ID string in the gym.make() function. For example, to switch from CartPole to Lunar Lander, you would change this line:

From:
env = gym.make("CartPole-v1", render_mode='human')

To:
env = gym.make("LunarLander-v2", render_mode='human')

The rest of the agent-environment loop code remains the same! You can save this as a new Python file (e.g., lunar_lander_test.py) and run it.

python3 lunar_lander_test.py


🛠️ Customizing Rewards and Punishments

While using default rewards is great, you often want to customize them to encourage or discourage specific behaviors. The standard way to do this is with a RewardWrapper, which intercepts and modifies the reward signal without changing the original environment code.

Example: Adding Punishments and New Rewards to CartPole

The provided custom_reward_example.py script shows how to create a wrapper that:

Adds a large punishment (negative reward) when the pole falls over.

Adds a small positive reward to encourage the agent to keep the cart centered.

To run it, simply execute the script:

python3 custom_reward_example.py


How It Works:

Create a Wrapper Class: We define a class that inherits from gymnasium.core.RewardWrapper.

Override the reward Method: This is the core of the wrapper. This method is called automatically on every step. It receives the original_reward and must return a new_reward.

Access Environment State: Inside the reward method, you can access the environment's current state (like cart_position or terminated status) using self.env.unwrapped. This allows you to create reward logic based on the situation.

Apply the Wrapper: You first create the standard environment with gym.make() and then wrap it with your custom class: wrapped_env = CustomRewardWrapper(env). You then use wrapped_env for all subsequent interactions (.step(), .reset(), etc.).

This technique is extremely powerful for "reward shaping"—guiding your agent to learn more complex behaviors.
