from burp import IBurpExtender
from burp import IHttpListener

class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Filter OPTIONS Method")
        callbacks.registerHttpListener(self)

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if messageIsRequest or toolFlag != 4:
            return

        requestBytes = messageInfo.getRequest()
        requestInfo = self._helpers.analyzeRequest(requestBytes)
        if requestInfo.getMethod() != "OPTIONS":
            return

        responseBytes = messageInfo.getResponse()
        responseInfo = self._helpers.analyzeResponse(responseBytes)
        responseHeaders = responseInfo.getHeaders()

        responseHeaders = [header for header in responseHeaders if not header.startswith("Content-Type: ")]
        responseHeaders.append("Content-Type: text/css; charset=UTF-8")

        responseBodyBytes = b"/* Injected by 'Filter OPTIONS Method' */"
        responseModified = self._helpers.buildHttpMessage(responseHeaders, responseBodyBytes)
        messageInfo.setResponse(responseModified)
