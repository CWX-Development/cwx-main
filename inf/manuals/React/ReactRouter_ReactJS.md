# React Router Tutorial

Author: Thuner2007

In this tutorial, we will learn how to use React Router to handle routing in a React application.

## Table of Contents

1. Introduction to React Router
2. Installation
3. Basic Routing
4. Route Parameters
5. Nested Routes
6. Redirects
7. Programmatic Navigation
8. Route Guards
9. Conclusion

## 1. Introduction to React Router

React Router is a popular library for handling routing in React applications. It allows us to create single-page applications with multiple views, each represented by a different URL.

## 2. Installation

To install React Router, we need to run the following command:

```bash
npm install react-router-dom
```

## 3. Basic Routing

In this section, we will learn how to set up basic routing in our React application using React Router.

First, we need to import the necessary components from React Router:

```jsx
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
```

Next, we can define our routes using the `Route` component. You can do this in the "index.js" file.

```jsx
<Router>
  <Routes>
    <Route index element={<Home />} />
    <Route path="/about" component={<About />} />
    <Route path="/contact" component={<Contact />} />
  </Routes>
</Router>
```

Here, we have defined three routes: one for the home page, one for the about page, and one for the contact page.

The index element is the path, that gets loaded when you are not on a page. For example: "http://localhost:3000"
in the component prop, you have to put in your component, that should load when you go on this route.
In the path prop, you have to define, what you have to put in the url, so that this route gets called. For eample if you make path="/contact" then you have to go to "http://localhost:3000/contact".

## 4. Route Parameters

Sometimes, we need to pass parameters to our routes. React Router allows us to do this easily.

To define a route with parameters, we can use the `:parameterName` syntax:

```jsx
<Route path="/users/:id" component={<User />} />
```

In the `User` component, we can access the parameter using the `useParams` hook:

```jsx
import { useParams } from 'react-router-dom';

function User() {
  const { id } = useParams();

  return <div>User ID: {id}</div>;
}
```

## 5. Nested Routes

React Router also supports nested routes, allowing us to create complex routing structures.

To define nested routes, we can nest `Route` components inside each other:

```jsx
<Route path="/products" component={<Products />}>
  <Route path="/products/:id" component={<Product />} />
</Route>
```

Here, the `Product` component will be rendered when the URL matches `/products/:id`.

## 6. Redirects

Sometimes, we need to redirect the user to a different route. React Router provides a `Redirect` component for this purpose.

To use the `Redirect` component, we can define a route with a `to` prop:

```jsx
<Route path="/old-url" render={() => <Redirect to="/new-url" />} />
```

Here, when the user visits `/old-url`, they will be redirected to `/new-url`.

## 7. Programmatic Navigation

React Router allows us to navigate programmatically using the `history` object.

To access the `history` object, we can use the `useHistory` hook:

```jsx
import { useHistory } from 'react-router-dom';

function MyComponent() {
  const history = useHistory();

  const handleClick = () => {
    history.push('/new-url');
  };

  return <button onClick={handleClick}>Go to New URL</button>;
}
```

Here, when the button is clicked, the user will be navigated to `/new-url`.

## 8. Route Guards

Route guards allow us to control access to certain routes based on certain conditions.

To implement route guards, we can use the `Route` component's `render` prop:

```jsx
const isLoggedIn = true;

<Route
  path="/protected"
  render={() => {
    if (isLoggedIn) {
      return <ProtectedPage />;
    } else {
      return <Redirect to="/login" />;
    }
  }}
/>;
```

Here, if the user is logged in (in this example isLoggedIn is true), they will be able to access the `/protected` route. Otherwise, they will be redirected to the `/login` page.

## 9. Conclusion

In this tutorial, we have learned the basics of React Router and how to use it to handle routing in a React application. We covered topics such as basic routing, route parameters, nested routes, redirects, programmatic navigation, and route guards.
