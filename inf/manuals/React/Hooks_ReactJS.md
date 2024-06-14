# React Hooks Tutorial

Author: Thuner2007

In this tutorial, we will learn the concept of React Hooks and how they can be used to enhance your ReactJS applications.

## What are React Hooks?

React Hooks are functions that allow you to use state and other React features in functional components.

## Why use React Hooks?

Using React Hooks can simplify your code by eliminating the need for class components and providing a more functional approach to managing state and side effects.

## Basic Hooks

React provides several built-in hooks that cover common use cases. Here are some of the most commonly used ones:

1. `useState`: This hook allows you to add state to your functional components. It returns a state variable and a function to update that variable.

2. `useEffect`: This hook enables you to perform side effects in your components, such as fetching data from an API or subscribing to events. It runs after every render and can be used to handle component lifecycle events.

3. `useContext`: This hook allows you to access the value of a context provider from any component within its subtree.

## Custom Hooks

Apart from the built-in hooks, you can also create your own custom hooks. Custom hooks are reusable functions that summarize common logic and can be shared across multiple components.

To create a custom hook, simply start the function name with the prefix `use`. This convention tells React that it's a hook and allows you to use other hooks inside it.

## Examples of React Hooks

Let's dive into some examples of how to use React Hooks in your applications.

### Example 1: useState

```jsx
import React, { useState } from 'react';

const Counter = () => {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
    </div>
  );
};

export default Counter;
```

In this example, we initialize the `count` state variable to 0 using the `useState` hook. We also get a function `setCount` to update the `count` value. When the "Increment" button is clicked, the `increment` function is called, which updates the `count` value by adding 1.

### Example 2: useEffect

```jsx
import React, { useState, useEffect } from 'react';

function DataFetcher() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://api.example.com/data')
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div>
      {data ? (
        <ul>
          {data.map((item) => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      ) : (
        <p>Loading data...</p>
      )}
    </div>
  );
}

export default DataFetcher;
```

In this example, we use the `useEffect` hook to fetch data from an API and update the `data` state variable. The empty dependency array `[]` ensures that the effect runs only once, similar to the `componentDidMount` lifecycle method in class components.

### Example 3: custom hook

```jsx
import { useState } from 'react';

const useLocalStorage = (key, initialValue) => {
  const [value, setValue] = useState(() => {
    const storedValue = localStorage.getItem(key);
    return storedValue ? JSON.parse(storedValue) : initialValue;
  });

  const updateValue = (newValue) => {
    setValue(newValue);
    localStorage.setItem(key, JSON.stringify(newValue));
  };

  return [value, updateValue];
};

export default useLocalStorage;
```

In this example, we create a custom hook called `useLocalStorage` that allows us to store and retrieve values from the browser's local storage. It takes in a `key` and an `initialValue` as parameters. The hook uses the `useState` hook to manage the value state, initializing it with the value retrieved from local storage or the provided initial value. The `updateValue` function is used to update the value state and store the updated value in local storage. The hook returns an array with the current value and the `updateValue` function.

### Example 4: using the useLocalStorage hook

```jsx
import React from 'react';
import useLocalStorage from './useLocalStorage';

const MyComponent = () => {
  const [name, setName] = useLocalStorage('name', '');

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  return (
    <div>
      <label htmlFor="name">Name:</label>
      <input type="text" id="name" value={name} onChange={handleNameChange} />
      <p>Hello, {name}!</p>
    </div>
  );
};

export default MyComponent;
```

In this example, we import the `useLocalStorage` hook and use it in a functional component called `MyComponent`. We initialize the `name` state variable using the `useLocalStorage` hook, providing a key of `'name'` and an initial value of `''`. We also define a `handleNameChange` function that updates the `name` value when the input field changes. The current `name` value is displayed in a paragraph element. This way, the `name` value will be persisted in the browser's local storage and retrieved when the component is rendered again.
