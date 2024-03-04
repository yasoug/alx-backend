import { createClient, print } from 'redis';
import { promisify } from "util";

const client = createClient().on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});
console.log('Redis client connected to the server');

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

const get = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  get(schoolName).then((res) => {
    console.log(res);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
