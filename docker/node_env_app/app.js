const express = require('express');
const app = express();

app.get('/', (req, res) => res.send('Welcome to my Docker app'));
app.get('/config', (req, res) => res.send(process.env.APP_MODE));

app.listen(3000, () => console.log('Server is running on port 3000'));
