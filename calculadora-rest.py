#!/usr/bin/python

import webapp

class calculadora(webapp.webApp):
    
    resultado = "vacio"

    def parse(self, request):

        verb = request.split(' ')[0]
        resource = request.split(' ')[1][1:]
        if verb == "PUT":
            body = request.split('\r\n\r\n', 1)[1]
        else:
            body = ""

        return (verb,resource,body)

    def process(self, parsedRequest):
        
        (verb,resource,body) = parsedRequest   


        if resource == "operacion":
            if verb == "GET":
                
                httpCode = "200 OK"
                
                if self.resultado == "vacio":
                    self.resultado = "Esperando operacion"
                    httpBody = "<html><body><h1>" + self.resultado + "</h1></body></html>"

                httpBody = "<html><body><h1>" + self.resultado + "</h1></body></html>"

            elif verb == "PUT":
                
                num1 = int(body[0])
                num2 = int(body[2])
                op = body[1] 
                
                if op == '+':
                    self.resultado = str(num1) + "+" + str(num2) + "=" + str(num1+num2)                          
                elif op == '-':
                    self.resultado = str(num1) + "-" + str(num2) + "=" + str(num1-num2)
                elif op == '*':
                    self.resultado = str(num1) + "*" + str(num2) + "=" + str(num1*num2)
                elif op == '/':
                    self.resultado = str(num1) + "/" + str(num2) + "=" + str(num1/num2)
                print self.resultado
                httpCode = "200 OK"
                httpBody = "<html><body><h1> Operacion almacenada </h1></body></html>"
        else:
            httpCode = "404 Not Found"
            httpBody = "<html><body><h1> Escribir recurso: /operacion </h1></body></html>"

        return (httpCode,httpBody)

if __name__ == "__main__":
        testCalculadora = calculadora('localhost', 1234)
