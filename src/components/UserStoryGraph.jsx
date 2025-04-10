import React from 'react';
import { XYPlot, XAxis, YAxis, HorizontalGridLines, LineSeries, MarkSeries } from 'react-vis';

const UserStoryGraph = ({ data }) => {
  const { userStories, relationships } = data;

  // Generate nodes for the graph
  const nodes = userStories.map((story, index) => ({
    x: index,
    y: 0,
    label: story,
  }));

  // Generate edges for the graph
  const edges = relationships.map((rel) => ({
    x: [rel.source - 1, rel.target - 1],
    y: [0, 0],
  }));

  return (
    <div>
      <h3>User Story Impact Graph</h3>
      <XYPlot width={800} height={400}>
        <HorizontalGridLines />
        <XAxis />
        <YAxis />
        {edges.map((edge, index) => (
          <LineSeries key={index} data={[{ x: edge.x[0], y: edge.y[0] }, { x: edge.x[1], y: edge.y[1] }]} />
        ))}
        <MarkSeries
          data={nodes}
          getLabel={(d) => d.label}
          labelAnchorX="middle"
          labelAnchorY="text-after-edge"
        />
      </XYPlot>
    </div>
  );
};

export default UserStoryGraph;