#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xc1df6cf1

# Compiled with Coconut version 1.6.0 [Vocational Guidance Counsellor]

## Coconut Header: -------------------------------------------------------------
from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:
 del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_dir)
_coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
 _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
 import __coconut__ as _coconut__coconut__
 _coconut__coconut__.__name__ = _coconut_full_module_name
 for _coconut_v in vars(_coconut__coconut__).values():
  if getattr(_coconut_v, "__module__", None) == str("__coconut__"):
   try:
    _coconut_v.__module__ = _coconut_full_module_name
   except AttributeError:
    _coconut_v_type = type(_coconut_v)
    if getattr(_coconut_v_type, "__module__", None) == str("__coconut__"):
     _coconut_v_type.__module__ = _coconut_full_module_name
 _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec
_coconut_sys.path.pop(0)
## Compiled Coconut: -----------------------------------------------------------

sys = _coconut_sys
from direct.particles.ParticleEffect import ParticleEffect
from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight
from panda3d.core import Filename
from panda3d.core import LVector3
from scipy.fftpack import fft
from scipy.io import wavfile
class setupViscloudio(ShowBase):
 '''
  A class to setup the audio visualizer.

  Attributes
  ----------
  audioFile: str
    The audio file to be played.

  Methods
  -------
  loadParticleConfig(self, filename: str) -> None:
    Loads the particle configurations from a given filename.

  setupLights(self) -> None:
    Creates an ambient light to illuminate the scene.

  setupMusic(self, file: str) -> None:
    Loads a sound file and begins looping playback.

  
  '''
 def __init__(self, audioFile# type: str
 ):
  '''
    Constructs all the necessary attributes for the scene.

    Parameters
    ----------
    audioFile: str
      The audio file to be played.
    '''
  ShowBase.__init__(self)
  (self.accept)(*('escape', sys.exit))
  base.disableMouse()
  (base.camera.setPos)(*(0, -20, 0))
  (base.camLens.setFov)(90)
  (base.setBackgroundColor)(*(0, 0, 0))
  base.enableParticles()
  self.setupLights()
  self.p = ParticleEffect()
  (self.loadParticleConfig)('../assets/shaders/steam.ptf')
  (self.setupMusic)(audioFile)
 def loadParticleConfig(self, filename# type: str
 ):
# type: (...) -> None
  '''
    Loads the particle configurations from a given filename.

    If the argument 'filename' is passed, the specified particle is loaded.

    Parameters
    ----------
    filename: str
      Filename to be loaded for use in particle emitter.

    Returns
    -------
    None
    '''
  self.p.cleanup()
  self.p = ParticleEffect()
  (self.p.loadConfig)((Filename)(filename))
  self.p.start(parent=render, renderParent=render)
 def setupLights(self):
# type: (...) -> None
  '''
    Creates an ambient light to illuminate the scene.

    Returns
    -------
    None
    '''
  ambientLight = (AmbientLight)('ambientLight')
  (ambientLight.setColor)((0.4, 0.4, 0.35, 1.0))
 def setupMusic(self, file# type: str
 ):
# type: (...) -> None
  '''
    Loads a sound file and begins looping playback.

    Returns
    -------
    None
    '''
  self.m = (base.loader.loadSfx)(file)
  self.m.play()
_coconut_call_set_names(setupViscloudio)