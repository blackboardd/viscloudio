import os

import pytest
from viscloudio import particles


def test_particles():
  print('Testing particles...')
  particles.setupViscloudio('../../assets/audio/drum_loop.ogg')
