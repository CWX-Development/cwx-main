# Using CSS in ReactJS

Author: Thuner2007

In this tutorial, we will guide you through the process of using CSS in ReactJS.

## Prerequisites

Before we begin, ensure that you have the following:

- A React project set up in JavaScript.
- A React component.

## Step 1: Create a CSS file

Create a CSS file inside the "components" folder. You can name it whatever you like, for example, "MyComponentStyle.css".

## Step 2: Import and apply CSS

To apply CSS to your React component, import the CSS file and add the appropriate class names to your JSX elements. Here's an example:

```jsx
import React from 'react';
import './MyComponentStyle.css';

const MyComponent = () => {
  return (
    <div className="my-component">
      <h1 className="my-component-title">Hello World!</h1>
    </div>
  );
};

export default MyComponent;
```

## Step 3: Style your component

Open the CSS file you created in the previous step and add your desired styles. For example:

```css
.my-component {
  background-color: #f1f1f1;
  padding: 20px;
}

.my-component-title {
  color: #333;
  font-size: 24px;
}
```

## Step 4: Use your component

To use your component, import it into another file (e.g., App.js) and include it in your JSX code. Here's an example:

```jsx
import React from 'react';
import MyComponent from './components/MyComponent';

function App() {
  return (
    <div className="App">
      <MyComponent />
    </div>
  );
}

export default App;
```

## Conclusion

In this tutorial, you learned how to use CSS in ReactJS by creating a separate CSS file for your component and applying styles using class names.
