import React, { useEffect, useState } from 'react';

function ToDoList() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    fetch('/graphql', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify({
        query: `{
          getTodos {
            id
            title
            description
            time
            imageUrl
          }
        }`
      }),
    })
      .then(res => res.json())
      .then(data => setTodos(data.data.getTodos));
  }, []);

  return (
    <div>
      <h1>Your To-Do List</h1>
      <ul>
        {todos.map(todo => (
          <li key={todo.id}>
            <h2>{todo.title}</h2>
            <p>{todo.description}</p>
            <p>{todo.time}</p>
            {todo.imageUrl && <img src={todo.imageUrl} alt="todo" />}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ToDoList;
