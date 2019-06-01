from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadProcessor
from burp import IIntruderPayloadGenerator

import os
import binascii

class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory, IIntruderPayloadProcessor):
    
    def registerExtenderCallbacks(self, callbacks):
        # obtain an extension helpers object
        self._helpers = callbacks.getHelpers()
        
        # set our extension name
        callbacks.setExtensionName("Mad Scientist Lab - Random MD5 Generator")
        
        # register ourselves as an Intruder payload generator
        callbacks.registerIntruderPayloadGeneratorFactory(self)
        
        # register ourselves as an Intruder payload processor
        callbacks.registerIntruderPayloadProcessor(self)
    
    def getGeneratorName(self):
        return "MSL - Random MD5 Generator"

    def createNewInstance(self, attack):
        # return a new IIntruderPayloadGenerator to generate payloads for this attack
        return IntruderPayloadGenerator()
    
    def getProcessorName(self):
        return "MSL - Random MD5 Processor"

    def processPayload(self, currentPayload, originalPayload, baseValue):
        return baseValue
    

class IntruderPayloadGenerator(IIntruderPayloadGenerator):
    def __init__(self):
        pass

    def hasMorePayloads(self):
        return True

    def getNextPayload(self, baseValue):
        return binascii.hexlify(os.urandom(16))

    def reset(self):
        pass