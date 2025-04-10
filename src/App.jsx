import React, { useState } from 'react';
import axios from 'axios';
import FileUpload from './components/FileUpload';
import UserStoryGraph from './components/UserStoryGraph';

const App = () => {
  const [data, setData] = useState(null);
  const [selectedStory, setSelectedStory] = useState(null);
  const [impactData, setImpactData] = useState(null);

  const handleFileUpload = (data) => {
    setData(data);
  };

  const handleStorySelect = async (story) => {
    setSelectedStory(story);

    try {
      const response = await axios.post('http://localhost:8000/api/analyze', { story });
      setImpactData(response.data);
    } catch (error) {
      console.error("Error analyzing story:", error);
      alert("Failed to analyze story. Please try again.");
    }
  };

  return (
    <div>
      <FileUpload onUpload={handleFileUpload} />
      {data && (
        <div>
          <h3>Select a User Story</h3>
          <ul>
            {data.userStories.map((story, index) => (
              <li key={index} onClick={() => handleStorySelect(story)}>
                {story}
              </li>
            ))}
          </ul>
        </div>
      )}
      {impactData && <UserStoryGraph data={impactData} />}
    </div>
  );
};

export default App;
