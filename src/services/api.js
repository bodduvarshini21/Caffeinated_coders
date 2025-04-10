import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // Adjust the base URL as needed
});

export const uploadFile = (formData) => {
  return api.post('/api/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
};

export const analyzeStory = (story) => {
  return api.post('/api/analyze', { story });
};