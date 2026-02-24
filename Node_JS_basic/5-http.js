const http = require('http');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');

      const students = {};
      let total = 0;

      for (let i = 1; i < lines.length; i += 1) {
        const [firstname, , , field] = lines[i].split(',');

        if (firstname && field) {
          if (!students[field]) students[field] = [];

          students[field].push(firstname);
          total += 1;
        }
      }

      let output = 'This is the list of our students\n';
      output += `Number of students: ${total}\n`;

      for (const field in students) {
        if (Object.prototype.hasOwnProperty.call(students, field)) {
          output += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
        }
      }

      resolve(output.trim());
    });
  });
}

const app = http.createServer((req, res) => {
  if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });

    countStudents(process.argv[2])
      .then((data) => {
        res.end(`${data}`);
      })
      .catch(() => {
        res.end('Cannot load the database');
      });
  } else {
    res.end('Hello');
  }
});

app.listen(1245);

module.exports = app;
