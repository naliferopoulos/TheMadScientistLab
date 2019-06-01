from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadProcessor
from burp import IIntruderPayloadGenerator

import uuid

class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory, IIntruderPayloadProcessor):
    
    def registerExtenderCallbacks(self, callbacks):
        # obtain an extension helpers object
        self._helpers = callbacks.getHelpers()
        
        # set our extension name
        callbacks.setExtensionName("Mad Scientist Lab - UUID Generator")
        
        # register ourselves as an Intruder payload generator
        callbacks.registerIntruderPayloadGeneratorFactory(self)
        
        # register ourselves as an Intruder payload processor
        callbacks.registerIntruderPayloadProcessor(self)
    
    def getGeneratorName(self):
        return "MSL - UUID Generator"

    def createNewInstance(self, attack):
        # return a new IIntruderPayloadGenerator to generate payloads for this attack
        return IntruderPayloadGenerator()
    
    def getProcessorName(self):
        return "MSL - UUID Processor"

    def processPayload(self, currentPayload, originalPayload, baseValue):
        return baseValue
    

class IntruderPayloadGenerator(IIntruderPayloadGenerator):
    def __init__(self):
        pass

    def hasMorePayloads(self):
        return True

    def getNextPayload(self, baseValue):
        return str(uuid.uuid4())

    def reset(self):
        pass