const apiUrl = "http://127.0.0.1:5000";

async function addStudent() {
  const roll_no = document.getElementById("roll_no").value;
  const name = document.getElementById("name").value;
  const marks = document.getElementById("marks").value;

  if (!roll_no || !name || !marks) {
    alert("Please fill all fields!");
    return;
  }

  const response = await fetch(`${apiUrl}/add`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ roll_no, name, marks }),
  });

  const result = await response.json();
  alert(result.message);
}

async function getAllStudents() {
  const response = await fetch(`${apiUrl}/all`);
  const students = await response.json();

  const list = document.getElementById("studentList");
  list.innerHTML = "";

  if (students.length === 0) {
    list.innerHTML = "<p>No students found.</p>";
    return;
  }

  students.forEach((s) => {
    const card = document.createElement("div");
    card.className = "student-card";
    card.innerHTML = `<strong>Roll No:</strong> ${s.roll_no} <br>
                      <strong>Name:</strong> ${s.name} <br>
                      <strong>Marks:</strong> ${s.marks}`;
    list.appendChild(card);
  });
}

async function searchStudent() {
  const roll_no = document.getElementById("search_roll").value;
  if (!roll_no) {
    alert("Please enter a roll number!");
    return;
  }

  const response = await fetch(`${apiUrl}/search/${roll_no}`);
  const result = await response.json();

  if (result.message) {
    alert(result.message);
  } else {
    alert(`🎓 Student Found:\nRoll No: ${result.roll_no}\nName: ${result.name}\nMarks: ${result.marks}`);
  }
}

async function deleteStudent() {
  const roll_no = document.getElementById("delete_roll").value;
  if (!roll_no) {
    alert("Please enter a roll number to delete!");
    return;
  }

  const response = await fetch(`${apiUrl}/delete/${roll_no}`, { method: "DELETE" });
  const result = await response.json();
  alert(result.message);
}
