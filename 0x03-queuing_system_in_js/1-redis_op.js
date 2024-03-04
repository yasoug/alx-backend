import { createClient, print } from 'redis';

const client = createClient().on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});
console.log('Redis client connected to the server');

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, res) => {
    console.log(res);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
