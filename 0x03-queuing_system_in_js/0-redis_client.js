import { createClient } from "redis";

const client = createClient();
client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`);
});

await client.connect();
if (client.isReady) {
  console.log('Redis client connected to the server');
}
