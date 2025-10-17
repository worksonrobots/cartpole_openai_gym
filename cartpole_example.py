import gymnasium as gym
import time

# Create the CartPole environment with render_mode='human' to visualize the simulation
env = gym.make("CartPole-v1", render_mode='human')

# Reset the environment to get the initial state and other info.
# The 'seed' argument is optional and used for reproducibility.
observation, info = env.reset(seed=42)

# Run the simulation for a total of 1000 time steps
for _ in range(1000):
    # Render the environment. This will display a window with the cart and pole.
    env.render()

    # Choose a random action from the environment's action space.
    # For CartPole, the actions are 0 (push cart to the left) and 1 (push cart to the right).
    action = env.action_space.sample()

    # Take the chosen action and get the results from the environment.
    # This returns:
    # 1. observation: The new state of the environment (e.g., cart position, pole angle).
    # 2. reward: The reward received for taking that action in the previous state.
    # 3. terminated: A boolean indicating if the episode has ended because a terminal state was reached (e.g., pole fell too far).
    # 4. truncated: A boolean indicating if the episode was ended for another reason (e.g., time limit).
    # 5. info: A dictionary with auxiliary diagnostic information (rarely used for simple environments).
    observation, reward, terminated, truncated, info = env.step(action)

    # Print the reward for each step to see how it accumulates.
    # In CartPole-v1, you get a +1 reward for every step the pole remains balanced.
    print(f"Reward for this step: {reward}")

    # If the episode is terminated or truncated, the simulation for this round is over.
    if terminated or truncated:
        print("Episode finished. Resetting environment.")
        # Reset the environment to start a new episode.
        observation, info = env.reset()
        # Adding a small delay to clearly see the reset in the visualization
        time.sleep(1)

# Close the environment and the rendering window.
env.close()
print("Simulation finished and environment closed.")

