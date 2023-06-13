import redis from "redis";

const client = redis.createClient();
client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`);
});

await client.connect();
if (client.isReady) {
  console.log('Redis client connected to the server');
}

console.log(`Reply: ${await client.hSet('HolbertonSchools', 'Portland', 50)}`);
console.log(`Reply: ${await client.hSet('HolbertonSchools', 'Seatle', 80)}`);
console.log(`Reply: ${await client.hSet('HolbertonSchools', 'New York', 20)}`);
console.log(`Reply: ${await client.hSet('HolbertonSchools', 'Bogota', 20)}`);
console.log(`Reply: ${await client.hSet('HolbertonSchools', 'Cali', 40)}`);
console.log(`Reply: ${await client.hSet('HolbertonSchools', 'Paris', 2)}`);

console.log(await client.hGetAll('HolbertonSchools'))
