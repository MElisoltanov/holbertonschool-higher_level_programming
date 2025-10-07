# Task 1: Consume Data from an API Using Command Line Tools (curl)

## 1. Installing and Basic Interaction with `curl`

- To install `curl`:
  - On Linux/Mac: Usually pre-installed. Otherwise, use `sudo apt-get install curl` or `brew install curl`.
  - On Windows: Use Windows Subsystem for Linux (WSL) or download from [curl.se](https://curl.se/).

- Confirm installation:
  ```sh
  curl --version
  ```
  This will display the installed version and supported protocols.

- Fetch the content of a webpage:
  ```sh
  curl http://example.com
  ```
  This retrieves and displays the HTML of the page.

---

## 2. Fetching Data from an API

- Use `curl` to retrieve posts from JSONPlaceholder:
  ```sh
  curl https://jsonplaceholder.typicode.com/posts
  ```
  - The output will be a JSON array of posts, each with attributes like `userId`, `id`, `title`, and `body`.

---

## 3. Using Headers and Other Options with `curl`

- Fetch only the headers of a response:
  ```sh
  curl -I https://jsonplaceholder.typicode.com/posts
  ```
  - This shows HTTP headers such as status code, content type, server, and date.

- Make a POST request to the same API:
  ```sh
  curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
  ```
  - This sends data to the API and typically returns the created post in JSON format, including a new `id`.

---

## 4. Hints

- The `-I` flag fetches only headers, useful for diagnosing server settings or checking status codes.
- The `-X` flag allows you to specify the HTTP method (e.g., POST, PUT, DELETE).
- The `-d` flag sends data in your request, commonly used with POST/PUT/PATCH.
- To format JSON output for readability, you can pipe to `jq`:
  ```sh
  curl https://jsonplaceholder.typicode.com/posts | jq .
  ```

---

## 5. Expected Output

- Running `curl --version` shows details about your installed version.
- Fetching posts displays a JSON array with post details.
- Using `-I` shows headers only (status, server info).
- A POST request returns a response confirming the received data, usually with a new `id`.

---

**Summary:**  
`curl` is a powerful command-line tool for interacting with APIs. You can easily fetch data, inspect headers, and send data using its options. These basic commands are crucial for testing and debugging APIs.