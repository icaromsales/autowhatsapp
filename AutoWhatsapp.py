#!/usr/bin/env python3

import pywhatkit as auto
# pip install pywhatkit

hour = 16
minute = 40

auto.sendwhatmsg("+55859********",
                 "Olá, esta é uma mensagem automática!", hour, minute)
# +Country code, region code and phone number.
