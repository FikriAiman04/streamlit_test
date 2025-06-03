// App.jsx
import React, { useState } from "react";

function App() {
  const [repos, setRepos] = useState([
    { id: 1, name: "example-repo", description: "My first project." },
  ]);
  const [newRepo, setNewRepo] = useState("");

  const addRepo = () => {
    if (!newRepo) return;
    setRepos([...repos, { id: Date.now(), name: newRepo, description: "New project." }]);
    setNewRepo("");
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      {/* Mercedes-Benz Link */}
      <div className="mb-6 bg-gray-100 p-4 rounded-lg shadow">
        <a
          href="https://www.mercedes-benz.com.my/passengercars/models.html"
          target="_blank"
          rel="noopener noreferrer"
          className="text-blue-600 hover:underline text-lg font-semibold"
        >
          🚘 View All Mercedes-Benz Car Models
        </a>
      </div>

      <h1 className="text-3xl font-bold mb-4">My GitHub Clone</h1>

      <div className="mb-4">
        <input
          className="border px-2 py-1 w-full"
          placeholder="New repository name"
          value={newRepo}
          onChange={(e) => setNewRepo(e.target.value)}
        />
        <button className="bg-blue-500 text-white px-4 py-1 mt-2" onClick={addRepo}>
          Add Repository
        </button>
      </div>

      <ul>
        {repos.map((repo) => (
          <li key={repo.id} className="mb-2 border-b pb-2">
            <h2 className="text-xl font-semibold">{repo.name}</h2>
            <p className="text-sm text-gray-600">{repo.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;



