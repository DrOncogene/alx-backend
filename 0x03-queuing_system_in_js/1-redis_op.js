import redis from "redis";

const client = redis.createClient();
client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`);
});

await client.connect();
if (client.isReady) {
  console.log('Redis client connected to the server');
}

async function setNewSchool (schoolName, value) {
  const reply = await client.SET(schoolName, value);
  console.log(`Reply: ${reply}`);
}

async function displaySchoolValue (schoolName) {
  console.log(await client.get(schoolName));
}

await displaySchoolValue('Holberton');
await setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');
