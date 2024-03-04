import { createClient } from 'redis';

const client = createClient().on('error', (err) =>
  console.log('Redis client not connected to the server:', err.message)
);
console.log('Redis client connected to the server');
