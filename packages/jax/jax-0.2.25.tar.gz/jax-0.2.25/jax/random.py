# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utilities for pseudo-random number generation.

The ``jax.random`` package provides a number of routines for deterministic
generation of sequences of pseudorandom numbers.

Basic usage
-----------

>>> seed = 1701
>>> num_steps = 100
>>> key = jax.random.PRNGKey(seed)
>>> for i in range(num_steps):
...   key, subkey = jax.random.split(key)
...   params = compiled_update(subkey, params, next(batches))  # doctest: +SKIP

PRNG Keys
---------
Unlike the *stateful* pseudorandom number generators (PRNGs) that users of NumPy and
SciPy may be accustomed to, JAX random functions all require an explicit PRNG state to
be passed as a first argument.
The random state is described by two unsigned 32-bit integers that we call a **key**,
usually generated by the :py:func:`jax.random.PRNGKey` function::

    >>> from jax import random
    >>> key = random.PRNGKey(0)
    >>> key
    DeviceArray([0, 0], dtype=uint32)

This key can then be used in any of JAX's random number generation routines::

    >>> random.uniform(key)
    DeviceArray(0.41845703, dtype=float32)

Note that using a key does not modify it, so reusing the same key will lead to the same result::

    >>> random.uniform(key)
    DeviceArray(0.41845703, dtype=float32)

If you need a new random number, you can use :meth:`jax.random.split` to generate new subkeys::

    >>> key, subkey = random.split(key)
    >>> random.uniform(subkey)
    DeviceArray(0.10536897, dtype=float32)

Design and Context
------------------

Among other requirements, the JAX PRNG aims to:

(a) ensure reproducibility,
(b) parallelize well, both in terms of vectorization (generating array values)
    and multi-replica, multi-core computation. In particular it should not use
    sequencing constraints between random function calls.

The approach is based on:

1. "Parallel random numbers: as easy as 1, 2, 3" (Salmon et al. 2011)
2. "Splittable pseudorandom number generators using cryptographic hashing"
   (Claessen et al. 2013)

See also https://github.com/google/jax/blob/main/design_notes/prng.md
for the design and its motivation.
"""

# flake8: noqa: F401

# TODO(frostig): replace with KeyArray from jax._src.random once we
# always enable_custom_prng
from jax._src.prng import PRNGKeyArray as KeyArray

from jax._src.random import (
  PRNGKey as PRNGKey,
  bernoulli as bernoulli,
  beta as beta,
  categorical as categorical,
  cauchy as cauchy,
  choice as choice,
  dirichlet as dirichlet,
  double_sided_maxwell as double_sided_maxwell,
  exponential as exponential,
  fold_in as fold_in,
  gamma as gamma,
  gumbel as gumbel,
  laplace as laplace,
  logistic as logistic,
  maxwell as maxwell,
  multivariate_normal as multivariate_normal,
  normal as normal,
  pareto as pareto,
  permutation as permutation,
  poisson as poisson,
  rademacher as rademacher,
  randint as randint,
  random_gamma_p as random_gamma_p,
  rbg_key as rbg_key,
  shuffle as shuffle,
  split as split,
  t as t,
  threefry_2x32 as threefry_2x32,
  threefry2x32_key as threefry2x32_key,
  threefry2x32_p as threefry2x32_p,
  truncated_normal as truncated_normal,
  uniform as uniform,
  unsafe_rbg_key as unsafe_rbg_key,
  weibull_min as weibull_min,
)
