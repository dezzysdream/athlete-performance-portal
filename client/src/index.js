import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { ApolloProvider, ApolloClient, InMemoryCache } from '@apollo/client';

// Setup ApolloClient
const client = new ApolloClient({
  uri: 'https://athlete-performance-portal.onrender.com',   // <-- VERY IMPORTANT
  cache: new InMemoryCache(),
});

// Render App inside ApolloProvider
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>
);
