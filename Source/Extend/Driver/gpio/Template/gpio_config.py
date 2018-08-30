# -*- coding: utf-8 -*-

import os

Config = {}
Config['target']     = '%s\\Source\\Extend\\Driver\\gpio\\gpio.c'%os.getcwd()
Config['template']   = '%s\\Source\\Extend\\Driver\\gpio\\Template\\gpio_template.c'%os.getcwd()
Config['config']     = '%s\\Source\\Extend\\Driver\\gpio\\Template\\gpio_config.xlsx'%os.getcwd()