#!/usr/bin/env python3
# -*- coding: utf-8 -*


from dataclasses import make_dataclass

Position = make_dataclass("Position", ["name", "lat", "lon"])
