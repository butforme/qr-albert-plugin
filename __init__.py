# -*- coding: utf-8 -*-

'''Generate a QR code for the given text.

Synopsis: <trigger> <query>'''


from albert import *
import os
import qrcode

__title__ = 'QR Code Generator'
__version__ = '0.4.0'
__triggers__ = 'qr '
__authors__ = 'butforme'
__exec_deps__ = ['display']
__py_deps__ = ['qrcode', 'Pillow']
__icon__ = os.path.dirname(__file__) + '/qr.svg'

def handleQuery(query):
    results = []
    if query.isTriggered:
        os.chdir(os.path.dirname(__file__))
        if query.string:
            img = qrcode.make(query.string)
            img.save('code.svg')
            return Item(
                id = __title__,
                icon = __icon__,
                text = __title__,
                subtext = 'Generate QR Code for the query',
                actions = [                
                    ProcAction(
                        text='Displays the generated code with the display command.',
                        commandline=['display', '-title', 'QR Code ─ Albert', 'code.svg'],
                        cwd=os.path.dirname(__file__)
                    )
                ],
                completion = query.rawString
            )
        else:
            return Item(
                id = __title__,
                icon = __icon__,
                text = __title__,
                subtext = 'Generate QR Code for the query',
                completion = query.rawString
            )
    return results