import React from "react";

function Task({ task, onDelete }) {
    const formattedDate = new Date(task.deadline).toLocaleDateString("en-US")
    return (
        <div>
            <p>{task.title}</p>
            <p>{task.description}</p>
            <p>{formattedDate}</p>
            <button onClick={() => onDelete(task.id)}>Delete</button>
        </div>
    )
}

export default Task