import { createClient, print } from 'redis';
import { promisify } from 'util';


const client = createClient().on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});
console.log('Redis client connected to the server');

const hashObj = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (let key in hashObj) client.hmset("HolbertonSchools", key, hashObj[key], print);

client.hgetall("HolbertonSchools", (err, res) => console.log(res));
