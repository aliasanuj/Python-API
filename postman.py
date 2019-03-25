=======================================================
Introduction to Postman for API Development:
=======================================================
Postman is an API(application programming interface) development tool which helps to build, 
test and modify APIs. Almost any functionality that could be needed by any developer is 
encapsulated in this tool

Response from server :
----------------------
The response from the server or the app, various headers are returned too with the main response
-->Connection = keep alive
-->Content-length = 1131
-->Content-type = Text/html;charset = utf-8
-->Date 
-->ETag = W/"fg-hgfhgfhgdhgf-hgfhdtrhstr-ht5t5454y5ey"
-->X-powered-By Express

=======================================
Advantage of Postman :
=======================================
1. Easily create test suites
Postman allows you create collections of integration tests to ensure your API is working as expected. 
Tests are run in a specific order with each test being executed after the last is finished. 
For each test, an HTTP request is made and assertions written in javascript are then used to verify the
integrity of your code. Since the tests and test assertions are written in JavaScript, we have freedom 
to manipulate the received data in different ways, such as creating local variables or even creating 
loops to repeatably run a test.

2. Store information for running tests in different environments
You wrote your test collection and it all works perfectly. You can run it again and again against your local 
environment and every test passes every time. But your local environment is usually configured a little 
differently than a test server. Luckily, Postman allows you to store specific information about different 
environments and automatically insert the correct environment configuration into your test. This could be a base 
URL, query parameters, request headers, and even body data for an HTTP post.

3. Store data for use in other tests
Postman also allows you to store data from previous tests into global variables. These variables can be used 
exactly like environment variables. For example, you may have an API that requires data received from another 
API. You can store the response (or part of the response, since it is JavaScript) and use that as part of a 
request header, post body, or URL for the subsequent API calls.

4. Integrates with build systems, such as Jenkins using the Newman command line tool
Postman has a command line interface called Newman. Newman makes it easy to run a collection of tests right 
from the command line. This easily enables running Postman tests on systems that don’t have a GUI, but it 
also gives us the ability to run a collection of tests written in Postman right from within most build tools. 
Jenkins, for example, allows you to execute commands within the build job itself, with the job either passing or 
failing depending on the test results.

5. Easily move tests and environments to code repositories
Postman makes it easy to share and move tests into different systems and environments by encapsulating collections 
in a "test" file and an "environment configuration" file. You can also export a test collection and use traditional 
filesharing to move it from environment to environment. This also makes it extremely simple to use code repository 
tools such as Git or SVN to manage the Postman tests and environment files, as well as maintaining version history 
in case you need to roll back changes.

6. On-the-fly testing
Any time you write some code, you’ll want to incrementally run it to make sure there aren’t any bugs or typos. 
Postman makes it easy to do just that. Postman lets you write a test without needing to put it in a collection, 
save it, or back it up. You just make a request to a URL, then see the result. Postman even parses JSON data to 
make it a little easier to read.

==================================================
Testing APIs through the CLI :
==================================================
n this post, we’ll concentrate on four parts of an API call – the URL, the HTTP verb, the headers and parameters. 
We’ll use the cURL library to send requests to the API resources through the CLI. cURL is a command line tool that 
helps in transferring data with URL syntax – supporting FTP, FTPS, HTTP, HTTPS.


curl -i -X POST -H 
    "Content-Type:application/json" 
    http://www.my-api-example.com:port/ -d 
    '{"Name":"Something"}'

The -i command stands for include, which tells the command that headers are present in the request. 
The -X option is immediately followed by the HTTP verb or method. 
-H specifies custom headers that are added to the request. 
Finally, the -d option specifies custom form data to be passed along with the request.
