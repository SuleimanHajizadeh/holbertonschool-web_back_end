const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8').trim().split('\n');

    const students = {};
    let totalStudents = 0;

    for (let i = 1; i < data.length; i += 1) {
      if (!data[i]) continue;

      const [firstname, , , field] = data[i].split(',');

      if (firstname && field) {
        if (!students[field]) {
          students[field] = [];
        }

        students[field].push(firstname);
        totalStudents += 1;
      }
    }

    console.log(`Number of students: ${totalStudents}`);

    for (const field in students) {
      if (Object.prototype.hasOwnProperty.call(students, field)) {
        console.log(
          `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`
        );
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
