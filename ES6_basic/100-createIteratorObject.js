export default function createIteratorObject(report) {
  // report.allEmployees obyektində bütün employee arraysini alırıq
  const allEmployees = Object.values(report.allEmployees).flat();
  // iterator qaytarırıq
  return allEmployees[Symbol.iterator]();
}

