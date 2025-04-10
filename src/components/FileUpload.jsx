import React, { useState } from 'react';
import axios from 'axios';
import { useDropzone } from 'react-dropzone';

const FileUpload = ({ onUpload }) => {
  const [file, setFile] = useState(null);

  const onDrop = (acceptedFiles) => {
    setFile(acceptedFiles[0]);
  };

  const { getRootProps, getInputProps } = useDropzone({
    onDrop,
    accept: '.csv',
  });

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first!");
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8000/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      onUpload(response.data);
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("Failed to upload file. Please try again.");
    }
  };

  return (
    <div>
      <div {...getRootProps()} style={{ border: '1px solid black', padding: '20px', cursor: 'pointer' }}>
        <input {...getInputProps()} />
        <p>Drag 'n' drop a CSV file here, or click to select a file</p>
      </div>
      {file && <p>Selected file: {file.name}</p>}
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default FileUpload;
