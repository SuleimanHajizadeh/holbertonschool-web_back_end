export default function taskBlock(trueOrFalse) {
  let task = false;     // block scoped
  let task2 = true;     // block scoped

  if (trueOrFalse) {
    let task = true;    // yalnız bu if blokunda mövcuddur
    let task2 = false;  // yalnız bu if blokunda mövcuddur
  }

  return [task, task2]; // əsas dəyişənlər dəyişməz qalır
}

