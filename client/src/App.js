import React, { useState } from 'react';
import { useQuery, useMutation, gql } from '@apollo/client';

// GraphQL queries and mutations
const GET_WORKOUTS = gql`
  query {
    workouts {
      id
      activity
      duration
    }
  }
`;

const CREATE_WORKOUT = gql`
  mutation($activity: String!, $duration: Int!) {
    createWorkout(activity: $activity, duration: $duration) {
      id
      activity
      duration
    }
  }
`;

function App() {
  const { loading, error, data, refetch } = useQuery(GET_WORKOUTS);
  const [createWorkout] = useMutation(CREATE_WORKOUT);

  const [activity, setActivity] = useState('');
  const [duration, setDuration] = useState('');

  if (loading) return <p>Loading workouts...</p>;
  if (error) return <p>Error fetching workouts: {error.message}</p>;

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createWorkout({ variables: { activity, duration: parseInt(duration) } });
    setActivity('');
    setDuration('');
    refetch(); // Refresh the list!
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Workouts</h1>
      <form onSubmit={handleSubmit} style={{ marginBottom: '2rem' }}>
        <input
          type="text"
          placeholder="Activity"
          value={activity}
          onChange={(e) => setActivity(e.target.value)}
          required
          style={{ marginRight: '1rem' }}
        />
        <input
          type="number"
          placeholder="Duration (minutes)"
          value={duration}
          onChange={(e) => setDuration(e.target.value)}
          required
          style={{ marginRight: '1rem' }}
        />
        <button type="submit">Add Workout</button>
      </form>
      <ul>
        {data.workouts.map((workout) => (
          <li key={workout.id}>
            {workout.activity} - {workout.duration} minutes
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
