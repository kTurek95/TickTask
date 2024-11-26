import { useState, useEffect } from "react"
import api from "../api";
import Task from "../components/Task"

const Home = () => {
    const [tasks, setTasks] = useState([]); // pusta tablica ponieważ taski to będzie lista
    const [title, setTitle] = useState(""); // pusty string ponieważ tytuł będzie stringiem
    const [description, setDescription] = useState("");
    const [deadline, setDeadline] = useState("");
    const [completed, setCompleted] = useState(false); // tutaj mamy false, ponieważ completed jest wartości boolean a domyślnie chcemy aby completed było ustawione na false

    useEffect(() => {
        getTasks()
    }, [])

    const getTasks = () => {
        api
            .get("/api/task/")
            .then((response) => response.data)
            .then((data) => {
                setTasks(data);
                console.log(data)
            })
            .catch((err) => alert(err))
    };


    const deleteTask = (id) => {
        api
            .delete(`/api/tasks/delete/${id}/`)
            .then((response) => {
                if (response.status === 204) alert("Task deleted");  // status 204 oznacza, że połączenie z serwerem przebiegło pomyślnie
                else alert("Failed to delete note");
                getTasks()  // wywołujemy tutaj funkcję getTask(), aby zadania się od razu zaktualizowały
            })
            .catch((error) => alert(error))
    };


    const createTask = (e) => {
        e.preventDefault();
        api
            .post("/api/task/", { title, description, deadline, completed })
            .then((response) => {
                if (response.status === 201) alert("task created");
                else alert("Failed to make task");
                getTasks()  // wywołujemy tutaj funkcję getTask(), aby zadania się od razu zaktualizowały
            })
            .catch((error) => alert(error))

    };


    return (
        <div>
            <div>
                <h2>Tasks</h2>
                {tasks.map((task) => (
                    <Task task={task} onDelete={deleteTask} key={task.id} />
                ))}
            </div>
            <h2>Create Task</h2>
            <form onSubmit={createTask}>
                <label htmlFor="title">Title:</label>
                <br />
                <input
                    type="text"
                    id="title"
                    name="title"
                    required
                    onChange={(e) => setTitle(e.target.value)}
                    value={title}
                />
                <br />
                <label htmlFor="description">Description:</label>
                <br />
                <textarea
                    id="description"
                    name="description"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                />
                <br />
                <label htmlFor="deadline">Deadline:</label>
                <br />
                <input
                    type="date"
                    id="deadline"
                    name="deadline"
                    required
                    onChange={(e) => setDeadline(e.target.value)}
                    value={deadline}
                />
                <br />
                <label htmlFor="completed">Completed:</label>
                <input
                    type="checkbox"
                    id="completed"
                    name="completed"
                    onChange={(e) => setCompleted(e.target.value)}
                    value={completed}
                />
                <br />
                <input type="submit" value="Submit"></input>
            </form>
        </div>
    )

}

export default Home