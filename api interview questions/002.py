========================
API Questions :
========================
1) What is your understanding of what are RESTful web services?
Just like SOAP (Simple Object Access Protocol), which is used to develop web services by XML method, 
RESTful web services use web protocol i.e. HTTP protocol method. They have the feature like scalability, 
maintainability, help multiple application communication built on various programming languages etc.
RESTful web service implementation defines the method of accessing various resources which are required 
by the client and he has sent the request to the server through the web browser. The important aspects 
of this implementation include:
Resources
Request Headers
Request Body
Response Body
Status codes

2) Name the protocol which is used by RESTful web services.
RESTful web services use a famous web protocol i.e. HTTP protocol. 
This serves as a medium of data communication between client and server. 
HTTP standard methods are used to access resources in RESTful web service architecture.

3) Explain the term ‘Addressing’ with respect to RESTful WEB service.
Just like we require address with postal code to reach any person, in the same way,
‘Addressing’ locates resources that are present on the server for the purpose of hosting 
web services. This is usually done with URI i.e. Unified Resource Identifier.

4) Enlist features of RESTful web services.
Every RESTful web services should have following features and characteristics that are enlisted below:
-Based on the Client Server representation.
Use of HTTP protocol for performing functions like fetching data from the web service, retrieving resources, 
execution of any query, etc.
-The communication between the server and client is performed through the medium known as ‘messaging’.
-Addressing of resources available on the server through URIs.
-Based on the concept of statelessness where every client request and the response is independent of the 
other with complete assurance of providing required information.
-Uses the concept of caching.
-Works on Uniform interface.

5) Explain messaging technique.
Messages are the mode of exchanging data for any type of communication to take place.
In the same way, HTTP protocol plays the role of message communication between the client and server 
through HTTP Request and Response methods. HTTP request is sent by the client who contains information 
about the data and in turn, receives HTTP Response from the server.
Messages are the collection of information about the data i.e. Metadata.

6) What are the core components of HTTP request and HTTP response?
The core components that come under HTTP Request are:
Verb: Includes methods like GET, PUT, POST, etc.
Uniform Resource Identifier for identifying the resources available on the server.
HTTP Version for specifying the HTTP version.
HTTP Request header for containing the information about the data.
HTTP Request body that contains the representation of the resources in use.
The core components that come under HTTP Response are:
Request Code: This contains various codes which determine the status of the server response.
HTTP Version for specifying the HTTP version.
HTTP Response header for containing the information about the data.
HTTP Response body that contains the representation of the resources in use.

7) Explain the term ‘Statelessness’ with respect to RESTful WEB service.
In REST, ST itself defines State Transfer and Statelessness means complete isolation.
This means, the state of the client’s application is never stored on the server and is passed on. 
In this process, the clients send all the information that is required for the server to fulfill 
the HTTP request that has been sent. Thus every client request and the response is independent of 
the other with complete assurance of providing required information.
Every client passes a ‘session identifier’ which also acts as an identifier for each session.

8) Enlist advantages and disadvantages of ‘Statelessness’.
In the above question, we have understood the meaning of statelessness with respect to the client-server
communication. Now, let us see some of its advantages and disadvantages.
Advantages:
-Every method required for communication is identified as an independent method i.e. there are no 
dependencies to other methods.
-Any previous communication with the client and server is not maintained and thus the whole process 
is very much simplified.
-If any information or metadata used earlier in required in another method, then the client sends 
again that information with HTTP request.
-HTTP protocol and REST web service, both shares the feature of statelessness.
Disadvantages:
-In every HTTP request from the client, the availability of some information regarding the client 
state is required by the web service.

10) What is a ‘Resource’?
Just like the ‘Object’ instance, we have learned in object orient programming Language, in the same way, ‘Resource’ is defined as 
an object of a type which can be an image, HTML file, text data, and any type of dynamic data. There are varieties of representation 
formats available in order to represent a resource.
Some most common are enlisted below:
JSON
YAML
XML
HTML

11) Why proper representation of Resource is required?
Representation is very important because it determines the easy identification of resources. 
With proper representations of resource in the proper format, allows the client to easily understand the format.

13) What is Caching?
-Caching is the process in which server response is stored so that a cached copy can be used when required and
there is no need of generating the same response again. This process not only reduces the server load but in 
turn increase the scalability and performance of the server. Only the client is able to cache the response 
and that too for a limited period of time.
-Mentioned below are the header of the resources and their brief description so that they can be identified 
for the caching process:
-Time and Date of resource creation
-Time and date of resource modification that usually stores the last detail.
-Cache control header
-Time and date at which the cached resource will expire.
-The age which determines the time from when the resource has been fetched.

14) Explain Cache-control header.
A standard Cache control header can help in attaining cache ability.
Enlisted below is the brief description of various cache control header:
-Public: Resources that are marked as the public can be cached by any intermediate components between the client and server.
-Private: Resources that are marked as private can only be cached by the client.
No cache means that particular resource cannot be cached and thus the whole process is stopped.

15) What are the best practices that are to be followed while designing RESTful web services?
To design a secure RESTful web service, there are some best practices or say points that should be considered. These are explained as 
follows:
-Every input on the server should be validated.
-Input should be well formed.
-Never pass any sensitive data through URL.
-For any session, the user should be authenticated.
-Only HTTP error messages should be used for indicating any fault.
-Use message format that is easily understood and is required by the client.
-Unified Resource Identifier should be descriptive and easily understood.

16) What is Payload?
The request data which is present in the body part of every HTTP message is referred as ‘Payload’.  
In Restful web service, the payload can only be passed to the recipient through POST method.
There is no limit of sending data as payload through POST method but the only concern is that more 
data with consuming more time and bandwidth. This may consume much of user’s time also.

17) Enlist some of the HTTP methods with description.
Mentioned below is the list of HTTP methods with their descriptions:
-GET: This is a read only operation which fetches the list of users on the server.
-PUT: This operation is used for the creation of any new resource on the server.
-POST: This operation is used for updating an old resource or for creating a new resource.
-DELETE: As the name suggests, this operation is used for deleting any resource on the server.
-OPTIONS: This operation fetches the list of any supported options of resources that are available on the server.

18) What is the difference between PUT method and POST method?
The major difference between the PUT and POST method is that the result generated with
PUT method is always same no matter how many times the operation is performed. On the other 
hand, the result generated by POST operation is always different every time

19) What is your understanding about JAX-RS?
JAX-RS is defined as the Java API for RESTful web service.
Among multiple libraries and framework, this is considered as the most suitable 
Java programming language based API which supports RESTful web service.

20) What are HTTP status codes? Enlist few with meaning.
HTTP status codes basically are the representation of the status of the task that has been performed 
on the server, with the mode of some codes. Every code has their own meaning.
Some of the HTTP status codes with their meaning are as follows:
-Code 200: This indicates success.
-Code 201: This indicates resource has been successfully created.
-Code 204: This indicates that there is no content in the response body.
-Code 404: This indicates that there is no method available.

=================================================
=================================================
1. What is REST?
REST is an architectural style for developing web services which exploit the ubiquity of HTTP protocol 
and uses the HTTP method to define actions. It revolves around resource where every component being a 
resource that can be accessed through a shared interface using standard HTTP methods.
In REST architecture, a REST Server provides access to resources and REST client accesses and makes these 
resources available. Here, each resource is identified by URIs or global IDs, and REST uses multiple ways 
to represent a resource, such as text, JSON, and XML. XML and JSON are nowadays the most popular 
representations of resources.

2. What is a RESTFul Web Services?
Mostly, there are two kinds of Web Services which should be remembered in your next API testing interview:
-SOAP (Simple Object Access Protocol): An XML-based method to expose web services.
-REST (Representational State Transfer): Web services developed in the REST style are referred to as RESTful 
web services. These web services use HTTP methods to implement the concept of REST architecture. 
A RESTful web service usually defines a URI, Uniform Resource Identifier a service, provides 
resource representation like JSON and a set of HTTP methods.

3. What is a “Resource” in REST?
REST architecture treats any content as a resource, which can be either text files, HTML pages, 
images, videos or dynamic business information.
REST Server gives access to resources and modifies them, where each resource is identified by URIs/ global IDs.

4. What is the most popular way to represent a resource in REST?
REST uses different representations to define a resource like text, JSON, and XML.
XML and JSON are the most popular representations of resources.

5. Which protocol is used by RESTful Web services?
RESTful web services use the HTTP protocol as a medium of communication between the client and the server.

6. What are some key characteristics of REST?
Key characteristics of REST are likely asked in a Web API Testing interview. 
So please get the answer ready in your mind with these 2 ones:
REST is stateless, therefore the SERVER has no status (or session data)
With a well-applied REST API, the server could be restarted between two calls, since all data is 
transferred to the server
Web service uses POST method primarily to perform operations, while REST uses GET for accessing resources.

7. What is messaging in RESTful Web services?
RESTful web services use the HTTP protocol as a communication tool between the client and the server. 
The technique that when the client sends a message in the form of an HTTP Request, the server sends 
back the HTTP reply is called Messaging. These messages comprise message data and metadata, that is, 
information on the message itself.

8. What are the core components of an HTTP request?
An HTTP request contains five key elements:
-An action showing HTTP methods like GET, PUT, POST, DELETE.
-Uniform Resource Identifier (URI), which is the identifier for the resource on the server.
-HTTP Version, which indicates HTTP version, for example-HTTP v1.1.
-Request Header, which carries metadata (as key-value pairs) for the HTTP Request message. 
Metadata could be a client (or browser) type, format supported by the client, format of a 
message body format, cache settings, and so on.
-Request Body, which indicates the message content or resource representation

9. What are the most commonly used HTTP methods supported by REST?
-GET is only used to request data from a specified resource. Get requests can be cached and bookmarked. 
It remains in the browser history and haS length restrictions. GET requests should never be used when 
dealing with sensitive data.
-POST is used to send data to a server to create/update a resource. POST requests are never cached and 
bookmarked and do not remain in the browser history.
-PUT replaces all current representations of the target resource with the request payload.
-DELETE removes the specified resource.
-OPTIONS is used to describe the communication options for the target resource.
-HEAD asks for a response identical to that of a GET request, but without the response body.

10. Can GET request to be used instead of PUT to create a resource?
The PUT or POST method should not be used to create a resource. You can use the GET operation which has view-only rights.

11. Is there any difference between PUT and POST operations?
PUT and POST operation are quite similar, except the terms of the result generated by them. 
PUT operation is idempotent, so you can cache the response while the responses to POST operation 
are not cacheable, and if you retry the request N times, you will end up having N resources with N 
different URIs created on server.

12. Which purpose does the OPTIONS method serve for the RESTful Web services?
The OPTIONS Method lists down all the operations of a web service supports. 
It creates read-only requests to the server.

13. What is URI? What is the main purpose of REST-based web services and what is its format?
URI stands for Uniform Resource Identifier. It is a string of characters designed for unambiguous
identification of resources and extensibility via the URI scheme. The purpose of a URI is to locate 
a resource(s) on the server hosting of the web service.
A URI’s format is <protocol>://<service-name>/<ResourceType>/<ResourceID>.

14. What is payload in RESTFul Web services?
The “payload” is the data you are interested in transporting. 
This is differentiated from the things that wrap the data for transport like the 
HTTP/S Request/Response headers, authentication, etc.

15. What is the upper limit for a payload to pass in the POST method?
<GET> appends data to the service URL. But, its size shouldn’t exceed the maximum URL length. 
However, <POST> doesn’t have any such limit.
So, theoretically, a user can pass unlimited data as the payload to POST method. 
But, if we consider a real use case, then sending POST with large payload will consume more bandwidth. 
It’ll take more time and present performance challenges to your server. Hence, a user should take action accordingly.

16. What is the caching mechanism?
Caching is just the practice of storing data in temporarily and retrieving data from a 
high-performance store (usually memory) either explicitly or implicitly.
When a caching mechanism is in place, it helps improve delivery speed by storing a copy of 
the asset you requested and later accessing the cached copy instead of the original.

