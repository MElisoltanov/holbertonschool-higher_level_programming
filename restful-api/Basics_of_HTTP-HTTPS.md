# Task 0: Basics of HTTP/HTTPS

## 1. Differences between HTTP and HTTPS

- **HTTP (Hypertext Transfer Protocol)** is the foundation for communication on the web. It transmits data in plain text, meaning anyone intercepting the traffic can read the content.
- **HTTPS (Hypertext Transfer Protocol Secure)** adds a layer of security by encrypting the data using TLS (or SSL). This makes the data unreadable to eavesdroppers and protects user information.
- **Main difference:** HTTPS encrypts all data between the client and server, providing confidentiality and integrity, while HTTP does not.

## 2. Structure of an HTTP Request and Response

### Example HTTP Request

```
GET /hello.txt HTTP/1.1
User-Agent: curl/7.63.0
Host: www.example.com
Accept-Language: en
```

### Example HTTP Response

```
HTTP/1.1 200 OK
Date: Wed, 30 Jan 2019 12:14:39 GMT
Server: Apache
Content-Type: text/plain

Hello World!
```

- **Request:** Sent from the client (browser or app) to the server, contains method, path, headers, and optionally body.
- **Response:** Sent from the server, contains status code, headers, and body.

## 3. Common HTTP Methods

| Method | Description | Typical Use Case |
|--------|-------------|------------------|
| GET    | Retrieves data from the server | Loading a web page or fetching API data |
| POST   | Sends new data to the server   | Submitting a form, creating a resource via API |
| PUT    | Updates existing data          | Editing a profile, updating a resource |
| DELETE | Removes data from the server   | Deleting an account or resource |

## 4. Common HTTP Status Codes

| Code | Description         | Scenario                                      |
|------|---------------------|-----------------------------------------------|
| 200  | OK                  | Successful request, returns requested data    |
| 201  | Created             | Resource created successfully (POST request)  |
| 404  | Not Found           | Resource does not exist on the server         |
| 403  | Forbidden           | Access denied to the requested resource       |
| 500  | Internal Server Error| Server encountered an unexpected error        |

---

**Summary:**  
HTTP is the basic protocol for web communication but lacks security. HTTPS encrypts data for safer transmission. HTTP requests and responses have a clear structure, and understanding common methods and status codes is essential for web development and API usage.