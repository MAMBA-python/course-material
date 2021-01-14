# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 21:09:37 2019

@author: onno__000
"""

import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("Task has finished")