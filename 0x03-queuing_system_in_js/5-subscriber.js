import { createClient } from "redis";

const client = createClient();
client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

await client.connect();

await client.subscribe('holberton school channel', async (message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    await client.unsubscribe('holberton school channel');
    await client.quit();
  }
});
