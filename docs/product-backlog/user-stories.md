# User Stories – Student Management System

**Project:** Group F – Student Management System
**Product Owner:** Sarah Zaheer
**Total Stories:** 20
**Format:** As a [role], I want [feature], so that [benefit]

---

## 👤 Actors / Roles
- **Admin** – School administrator managing the system
- **Teacher** – Instructor managing courses, grades, attendance
- **Student** – Learner accessing their academic information
- **System** – Automated system processes

---

## 📋 All 20 User Stories

### 🔐 Authentication & Access (Stories 1–4)

**US-01:** As an **Admin**, I want to **log in with my username and password**, so that **I can securely access the admin dashboard**.
*   **Acceptance Criteria:**
    *   **Given:** The admin user is on the portal login screen.
    *   **When:** They enter a valid admin username and password combination.
    *   **Then:** The system generates a valid session and opens the main admin dashboard view.

**US-02:** As a **Teacher**, I want to **log in with my credentials**, so that **I can manage my courses and student grades**.
*   **Acceptance Criteria:**
    *   **Given:** The instructor user is on the main landing screen.
    *   **When:** They enter their registered email account and secure password credentials.
    *   **Then:** The system routes them to their personalized dashboard containing assigned course sections.

**US-03:** As a **Student**, I want to **log in with my student ID and password**, so that **I can view my academic information**.
*   **Acceptance Criteria:**
    *   **Given:** The student is looking at the system authentication panel.
    *   **When:** They provide their unique student identity code and security password.
    *   **Then:** The app initializes their student interface in a secure read-only state.

**US-04:** As a **User**, I want to **log out of the system**, so that **my account stays secure when I leave**.
*   **Acceptance Criteria:**
    *   **Given:** A user holds an active, authorized login status in their browser.
    *   **When:** They select the system log out interface command option.
    *   **Then:** The backend terminates the session tokens and returns the display to the login root.

---

### 🎓 Student Management (Stories 5–9)

**US-05:** As an **Admin**, I want to **register new students** by entering their personal details, so that **their records are stored in the system**.
*   **Acceptance Criteria:**
    *   **Given:** The admin opens the official student onboarding workspace form.
    *   **When:** They fill in all requested fields with valid information parameters and click save.
    *   **Then:** The system creates a clean record index row inside the master database.

**US-06:** As an **Admin**, I want to **view a list of all registered students**, so that **I can manage student records efficiently**.
*   **Acceptance Criteria:**
    *   **Given:** The administrator selects the main user catalog section path.
    *   **When:** The database query fetches the profile indexes.
    *   **Then:** The client interface builds a clean table matrix reflecting all registered system users.

**US-07:** As an **Admin**, I want to **update a student's information** (name, contact, address), so that **records stay accurate**.
*   **Acceptance Criteria:**
    *   **Given:** The admin has loaded a targeted student profile edit template box.
    *   **When:** They adjust specific user values and hit the save updates control command.
    *   **Then:** The system overwrites the corresponding record fields instantly in the central system storage.

**US-08:** As an **Admin**, I want to **delete or deactivate a student's account**, so that **former students no longer access the system**.
*   **Acceptance Criteria:**
    *   **Given:** An active profile entry is targeted for removal or system locking.
    *   **When:** The administrator triggers the account suspension soft-delete option.
    *   **Then:** The portal drops the profile status code to inactive and rejects all subsequent logins.

**US-09:** As a **Student**, I want to **view my own profile**, so that **I can verify my personal information is correct**.
*   **Acceptance Criteria:**
    *   **Given:** A student has completed secure validation and sits on their profile page.
    *   **When:** They click into the core demographics view tab container.
    *   **Then:** The system displays their registered details inside a clean uneditable information frame.

---

### 📚 Course Management (Stories 10–13)

**US-10:** As an **Admin**, I want to **create new courses** with a name, code, and credit hours, so that **students can enroll in them**.
*   **Acceptance Criteria:**
    *   **Given:** The admin wants to establish a new academic module record.
    *   **When:** They input a valid course title, unique system code string, and credit parameter.
    *   **Then:** The element logs successfully and appears inside the active school catalog listings.

**US-11:** As an **Admin**, I want to **assign teachers to courses**, so that **each course has an instructor responsible for it**.
*   **Acceptance Criteria:**
    *   **Given:** An open curriculum section entry has no instructor reference mapped.
    *   **When:** The admin binds an instructor account ID to that target course sequence item.
    *   **Then:** The item registers automatically in the target faculty member's private course sheet.

**US-12:** As a **Teacher**, I want to **view the list of students enrolled in my courses**, so that **I can manage my class rosters**.
*   **Acceptance Criteria:**
    *   **Given:** An instructor user views an assigned classroom project section box.
    *   **When:** They toggle open the class roster layout grid.
    *   **Then:** The system runs a relational search query and surfaces all student keys enrolled.

**US-13:** As a **Student**, I want to **enroll in available courses**, so that **I can register for the classes I need**.
*   **Acceptance Criteria:**
    *   **Given:** A student profile carries zero enrollment limitations, and a class has open space.
    *   **When:** The student hits the course entry registration link trigger.
    *   **Then:** Their unique identifier binds to the class matrix array and class vacancy counts reduce.

---

### 📝 Grades Management (Stories 14–16)

**US-14:** As a **Teacher**, I want to **enter grades for students in my courses**, so that **their academic performance is recorded**.
*   **Acceptance Criteria:**
    *   **Given:** The professor opens the digital grade book grid matrix cell sheet.
    *   **When:** They enter numeric score inputs into target columns and save.
    *   **Then:** The application updates rows while running boundaries checks to reject data out of a 0-100 range.

**US-15:** As a **Teacher**, I want to **update or edit existing grades**, so that **corrections can be made when needed**.
*   **Acceptance Criteria:**
    *   **Given:** A previously finalized assignment grade value is saved in the record table.
    *   **When:** The teacher edits that target field cell and updates it with an adjusted score entry.
    *   **Then:** The software replaces the numerical element data and triggers active grade average routines.

**US-16:** As a **Student**, I want to **view my grades for each course**, so that **I can track my academic progress**.
*   **Acceptance Criteria:**
    *   **Given:** An authenticated student is active inside their study portal session.
    *   **When:** They navigate directly into their evaluation record overview window component.
    *   **Then:** The system displays a structured layout detailing individual module scores and running GPA marks.

---

### 📅 Attendance Tracking (Stories 17–18)

**US-17:** As a **Teacher**, I want to **mark attendance for students in my class**, so that **daily attendance records are maintained**.
*   **Acceptance Criteria:**
    *   **Given:** An instructor launches the daily attendance checker layout screen asset.
    *   **When:** They check off Present, Absent, or Tardy boxes for the row listings and save.
    *   **Then:** The system appends a historical record map linked to the current calendar date stamp.

**US-18:** As a **Student**, I want to **view my attendance history**, so that **I know how many classes I have attended**.
*   **Acceptance Criteria:**
    *   **Given:** A student runs their active application metrics widget.
    *   **When:** They call the personal participation repository page request link.
    *   **Then:** The client interface presents a dynamic running ratio of their classroom presence metric.

---

### 📊 Reports & Notifications (Stories 19–20)

**US-19:** As an **Admin**, I want to **generate reports** (student lists, grades summaries, attendance reports), so that **I can analyze school data**.
*   **Acceptance Criteria:**
    *   **Given:** The admin enters the main database compilation panel folder path.
    *   **When:** They check an aggregation report archetype and initiate the collection query loop.
    *   **Then:** The server builds a clean data table structure and exports a copy file stream.

**US-20:** As a **Student**, I want to **receive notifications about my grades and enrollment**, so that **I stay updated on important academic events**.
*   **Acceptance Criteria:**
    *   **Given:** A major data edit action executes inside the course evaluation pipeline.
    *   **When:** The user enters the primary application space.
    *   **Then:** The software dynamically injects a top-tier alert banner box matching the change status.

---

## 📊 Story Summary by Role

| Role | Number of Stories | Story IDs |
| :--- | :---: | :--- |
| Admin | 8 | US-01, US-05, US-06, US-07, US-08, US-10, US-11, US-19 |
| Teacher | 5 | US-02, US-12, US-14, US-15, US-17 |
| Student | 6 | US-03, US-09, US-13, US-16, US-18, US-20 |
| All Users | 1 | US-04 |
| **Total** | **20** | — |

## 📊 Story Summary by Feature Area

| Feature Area | Story Count |
