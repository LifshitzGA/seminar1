#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 12:18:19 2020

@author: georgij
"""

import pandas as pd
import matplotlib.pyplot as plt

eq = pd.read_csv("Earthquake-database.csv")

d = pd.Index.value_counts(eq["INTENSITY"])
c = pd.Index.value_counts(eq["YEAR"])

fig, axes = plt.subplots()
plt.bar(d.index, d)
plt.ylabel('Количество землятресений')
plt.xlabel('Сила землетрясений')

fig, axes = plt.subplots()
plt.bar(c.index, c)
plt.ylabel('Количество землятресений')
plt.xlabel('Год')