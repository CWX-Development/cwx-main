# Documentation backend endpoints sample

## User

- **Path**
  - /user

### GET all user

- **Path**
  - /getAll
- **Get the list of all user**
- **Parameter**
  - None
- **Answer**
  - 200 OK: List of user with details (name, email, password)

### POST user

- **Path**
  - /newUser
- **Post a new user**
- **Parameter**
  - **Body**: JSON object with fields:
    - `name` (String): (optional) The name of the user.
    - `email` (String): The email of the user.
    - `password` (String): The password of the user.
  - **Answer**
    - 201 Created: The newly created user object with details.