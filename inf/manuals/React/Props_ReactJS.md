# React Props Tutorial

Author: Thuner2007

In this tutorial, we will learn the concept of props in ReactJS. Props, short for properties, are a way to pass data from a parent component to its child components. They allow for the communication and sharing of data between different parts of a React application.

## Table of Contents

1. Passing Props
2. Accessing Props
3. Default Props
4. Prop Types
5. Conclusion

## 1. Passing Props

To pass props from a parent component to a child component, you simply include them as attributes when rendering the child component. For example:

```jsx
// ParentComponent.js
import React from 'react';
import ChildComponent from './ChildComponent';

function ParentComponent() {
  const name = 'John Doe';
  const age = 25;

  return (
    <div>
      <ChildComponent name={name} age={age} />
    </div>
  );
}

export default ParentComponent;
```

## 2. Accessing Props

In the child component, you can access the props passed from the parent component by using the `props` object. For example:

```jsx
// ChildComponent.js
import React from 'react';

function ChildComponent(props) {
  return (
    <div>
      <h2>Name: {props.name}</h2>
      <h2>Age: {props.age}</h2>
    </div>
  );
}

export default ChildComponent;
```

## 3. Default Props

You can also define default values for props in case they are not provided by the parent component. This can be done using the `defaultProps` property. For example:

```jsx
// ChildComponent.js
import React from 'react';

function ChildComponent(props) {
  return (
    <div>
      <h2>Name: {props.name}</h2>
      <h2>Age: {props.age}</h2>
    </div>
  );
}

ChildComponent.defaultProps = {
  name: 'Unknown',
  age: 0,
};

export default ChildComponent;
```

## 4. Prop Types

Prop types are used to validate the type of props being passed to a component. This helps catch potential bugs and ensures that the correct data types are being used. You can define prop types using the `propTypes` property. For example:

```jsx
// ChildComponent.js
import React from 'react';
import PropTypes from 'prop-types';

function ChildComponent(props) {
  return (
    <div>
      <h2>Name: {props.name}</h2>
      <h2>Age: {props.age}</h2>
    </div>
  );
}

ChildComponent.propTypes = {
  name: PropTypes.string.isRequired,
  age: PropTypes.number.isRequired,
};

export default ChildComponent;
```

## 5. Conclusion

In this tutorial, we covered the basics of using props in ReactJS. Props are a powerful tool for passing data between components and customizing their behavior. Understanding how to pass and access props is essential for building complex React applications.

I hope you found this tutorial helpful.
