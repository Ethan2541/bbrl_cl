# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#
from ._version import __version__, __version_tuple__
from gymnasium.envs.registration import register


# Continuous Acrobot
# ----------------------------------------

register(
    id="AcrobotContinuousSubspace-v0",
    entry_point="bbrl_subspaces.envs:ContinuousAcrobotSubspaceEnv",
    max_episode_steps=200,
)
register(
    id="AcrobotContinuousSubspace-v1",
    entry_point="bbrl_subspaces.envs:ContinuousAcrobotSubspaceEnv",
    max_episode_steps=500,
)


# Continuous CartPole
# ----------------------------------------

register(
    id="CartPoleContinuousSubspace-v0",
    entry_point="bbrl_subspaces.envs:ContinuousCartPoleSubspaceEnv",
    max_episode_steps=200,
)

register(
    id="CartPoleContinuousSubspace-v1",
    entry_point="bbrl_subspaces.envs:ContinuousCartPoleSubspaceEnv",
    max_episode_steps=500,
)


# Pendulum
# ----------------------------------------

register(
    id="PendulumSubspace-v0",
    entry_point="bbrl_subspaces.envs:PendulumSubspaceEnv",
    max_episode_steps=200,
)
register(
    id="PendulumSubspace-v1",
    entry_point="bbrl_subspaces.envs:PendulumSubspaceEnv",
    max_episode_steps=200,
)