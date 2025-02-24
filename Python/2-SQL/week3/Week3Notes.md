#Client-server architecture: 

Example: WWW

Client --> requests resources to a Server 
Server --> sends a response 
*this happens over a network (ex. the Internet)

#Three-tier architecture: 

(Presentation Tier)User Client: Show me video #123 --> (Business Logic Tier) Web server/Database client --> SELECT *FROPM videos WHERE id = 123 --> (Data tier)Database Server 

Database Server sends Query Result --> Database Client --> User Client 

URL: Uniform Resource Locator 

https: (either HyperText Transfer Protocol or HyperText Transfer Protocol Secure)//www.google.com(domain name- points to the location of a google server)/search(specific resource offered by the server)?qwaffles(specifies parameters as key-value pairs)

http: uses port 80, https: uses port 443
http://username:password@example.com 

Syntax: protocol://username:password@domain.name:port/path?query=parameter&q2=p2#fragment

postgresql://postgres@localhost:5432/week3

#certain characters are not valid for URL including: space, newline, @

Invalid characters must be encoded.  Example: "blueberry waffles" has a space, which is encoded in a URL as %20.  Example:

https://www.google.com/search?q=blueberry%20waffles (percent encoding)

python: import urllib.parse (encoding library)

Raw: space Encoded: %20
Raw: @ Encoded: %40
Raw: # Encoded: %23
Raw: $ Encoded: %24
Raw: / Encoded %2F
Raw: & Encoded %26

HTTP request methods: 

Accompany URL in outgoing request from web client to web server
Should be one of several verbs as designated below
Indicate intent of request: 

GET Fetch a resource
POST Create a resource
PUT Replace a resource with edits (may create new resource if one does not exist )
PATCH Modifies existing resource
DELETE Delete resource 

Not covered in this course: HEAD, OPTIONS, TRACE, CONNECT

Request body: Useful for POST, PUT, and PATCH requests, may contain form values, file upload data
May contain data in a given format eg. JSON, XML

Request headers: 
Often used for "metadata"
Key-value pairs
May contain user authorization info
May contain content-type to describe format of request body
eg: "Auth-Token":"ER3M1D9UIP123", "Content-Type":"application/json"

REST API: 

REST --> Representational State Transfer 
API --> Application Programming Interface

JSON- JavaScript Object Notation

Interoperability: Using standards like JSON, REST, and HTTP allow networked components to communicate easily 

CRUD: 

Create, Read, Update, Delete

| Operation           |  SQL           |  HTTP          | 
-----------------------------------------------------------
| Create              |  INSERT        |  POST          |
| Read                |  SELECT        |  GET           |
| Update              |  UPDATE        |  PUT/PATCH     |
| Delete              |  DELETE        |  DELETE        |


| HTTP Verb           |  Path          |  Used For                |
--------------------------------------------------------------------
| GET                 | /photos        | Display list of photos   |
| POST                | /photos        | Create a new photo       |
| GET                 | /photos/:id    | Display a specific photo |
| PATCH/PUT           | /photos/:id    | Update a specific photo  |
| DELETE              | /photos/:id    | Delete a specific photo  | 

