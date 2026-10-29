# User Stories Specification Document


**Project Reference:** Student Management System (SMS)  
**Engineering Group:** Group F  
**Product Owner:** Sarah Zaheer  
**Scrum Master:** Tamana Omar  
**Baseline Release Date:** October 10, 2026  
>>>>>>> ed36a9cd430d10b10bbc49a5497311cec903c09a

---

## 1. System Actors & Operational Roles

*   **Admin:** A high-level school administrator managing platform configurations, core user registries, and resource catalogs.
*   **Teacher:** An instructor managing specific course assignments, logging daily attendance records, and auditing student grades.
*   **Student:** A registered learner accessing individual academic schedules, monitoring personal performance history, and tracking attendance.
*   **System:** Automated backend background processes handling calculations, notifications, and security rules.

---

## 2. Master User Stories & Acceptance Criteria

### 🔐 Authentication & Access (Stories 1–4)

#### **US-01:** As an **Admin**, I want to **log in with my username and password**, so that **I can securely access the admin dashboard**.
*   **Acceptance Criteria:**
    *   *Given* an active administrator user profile exists in the database, *when* valid credentials are typed into the main login panel, *then* the platform must route the user directly to the Admin Command Center.
    *   *Given* incorrect inputs are provided, *when* the submission button is clicked, *then* the system denies access and displays a secure "Authentication Failed" alert.

#### **US-02:** As a **Teacher**, I want to **log in with my credentials**, so that **I can manage my courses and student grades**.
*   **Acceptance Criteria:**
    *   *Given* a verified teacher account exists, *when* they submit correct login data, *then* they are granted secure write access to their assigned courses.

#### **US-03:** As a **Student**, I want to **log in with my student ID and password**, so that **I can view my academic information**.
*   **Acceptance Criteria:**
    *   *Given* a registered student profile, *when* a successful login occurs, *then* the system loads their personal academic landing page in read-only view.

#### **US-04:** As a **User**, I want to **log out of the system**, so that **my account stays secure when I leave**.
*   **Acceptance Criteria:**
    *   *Given* an active authorized browser session, *when* the user hits the "Logout" control, *then* the backend must immediately clear all session tokens and direct the browser back to the main login screen.

---

### 🎓 Student Management (Stories 5–9)

#### **US-05:** As an **Admin**, I want to **register new students** by entering their personal details, so that **their records are stored in the system**.
*   **Acceptance Criteria:**
    *   *Given* a complete registration data sheet, *when* the administrator commits the form, *then* a unique record identifier is generated and safely stored in the master database.

#### **US-06:** As an **Admin**, I want to **view a list of all registered students**, so that **I can manage student records efficiently**.
*   **Acceptance Criteria:**
    *   *Given* active rows of student profiles, *when* the administrative user opens the student list panel, *then* the interface must compile a clear table with indexing tools.

#### **US-07:** As an **Admin**, I want to **update a student's information** (name, contact, address), so that **records stay accurate**.
*   **Acceptance Criteria:**
    *   *Given* an editable student profile view, *when* the admin modifies parameters and clicks "Save Changes", *then* modifications are immediately committed to the central database.

#### **US-08:** As an **Admin**, I want to **delete or deactivate a student's account**, so that **former students no longer access the system**.
*   **Acceptance Criteria:**
    *   *Given* a profile selected for removal, *when* the deactivation request is confirmed, *then* the system changes the account status to "Inactive" and instantly revokes all login permissions.

#### **US-09:** As a **Student**, I want to **view my own profile**, so that **I can verify my personal information is correct**.
*   **Acceptance Criteria:**
    *   *Given* an authorized student dashboard session, *when* the personal profile tab is opened, *then* the system renders their demographic info in a strict read-only template.

---

### 📚 Course Management (Stories 10–13)

#### **US-10:** As an **Admin**, I want to **create new courses** with a name, code, and credit hours, so that **students can enroll in them**.
*   **Acceptance Criteria:**
    *   *Given* the core structural details of a course, *when* the admin submits the setup form, *then* the unit is instantly published to the academic catalog catalog.

#### **US-11:** As an **Admin**, I want to **assign teachers to courses**, so that **each course has an instructor responsible for it**.
*   **Acceptance Criteria:**
    *   *Given* a list of open course catalogs, *when* the admin maps a specific faculty ID to a selected course section, *then* that course displays directly inside the corresponding teacher's workspace dashboard.

#### **US-12:** As a **Teacher**, I want to **view the list of students enrolled in my courses**, so that **I can manage my class rosters**.
*   **Acceptance Criteria:**
    *   *Given* an active classroom unit, *when* the assigned instructor selects their roster tab, *then* the system serves a real-time list of all students registered in that module.

#### **US-13:** As a **Student**, I want to **enroll in available courses**, so that **I can register for the classes I need**.
*   **Acceptance Criteria:**
    *   *Given* a student with zero registration blocks, *when* they opt into an open course section, *then* their identifier attaches to the class roll and the section's seat vacancy counter drops by one.

---

### 📝 Grades Management (Stories 14–16)

#### **US-14:** As a **Teacher**, I want to **enter grades for students in my courses**, so that **their academic performance is recorded**.
*   **Acceptance Criteria:**
    *   *Given* an open grade sheet, *when* numerical scores are keyed in, *then* the platform verifies entries match structural boundaries (0.00% to 100.00%) before committing to records.

#### **US-15:** As a **Teacher**, I want to **update or edit existing grades**, so that **corrections can be made when needed**.
*   **Acceptance Criteria:**
    *   *Given* a previously stored grade cell, *when* the teacher updates the cell and overrides the value, *then* the backend overwrites the previous point matrix and updates the running average calculation.

#### **US-16:** As a **Student**, I want to **view my grades for each course**, so that **I can track my academic progress**.
*   **Acceptance Criteria:**
    *   *Given* grades published by instructors, *when* a student accesses their evaluation panel, *then* a breakdown of cumulative marks is displayed alongside their target grade classifications.

---

### 📅 Attendance Tracking (Stories 17–18)

#### **US-17:** As a **Teacher**, I want to **mark attendance for students in my class**, so that **daily attendance records are maintained**.
*   **Acceptance Criteria:**
    *   *Given* an ongoing class calendar day, *when* the instructor completes checkmarks for "Present", "Absent", or "Tardy", *then* the entries are stored permanently in the attendance ledger.

#### **US-18:** As a **Student**, I want to **view my attendance history**, so that **I know how many classes I have attended**.
*   **Acceptance Criteria:**
    *   *Given* an authorized student dashboard view, *when* the user audits their participation records, *then* the system processes a live percentage calculation of their historical classroom presence.

---

### 📊 Reports & Notifications (Stories 19–20)

#### **US-19:** As an **Admin**, I want to **generate reports** (student lists, grades summaries, attendance reports), so that **I can analyze school data**.
*   **Acceptance Criteria:**
    *   *Given* complete datasets across system modules, *when* the admin triggers the report generation process, *then* the server aggregates individual records into a downloadable tabular view.

#### **US-20:** As a **Student**, I want to **receive notifications about my grades and enrollment**, so that **I stay updated on important academic events**.
*   **Acceptance Criteria:**
    *   *Given* a database update trigger (such as a published grade), *when* the record saves, *then* the system creates an automated notification banner displayed on the student’s landing view.

---

## 3. Core Matrix Data Summaries

### Matrix Table 1: Story Allocation by System Role

| Target User Role | Cumulative Volume | Associated Story Reference Identifiers |
| :--- | :--- | :--- |
| **Admin** | 8 Stories | US-01, US-05, US-06, US-07, US-08, US-10, US-11, US-19 |
| **Teacher** | 5 Stories | US-02, US-12, US-14, US-15, US-17 |
| **Student** | 6 Stories | US-03, US-09, US-13, US-16, US-18, US-20 |
| **All Users** | 1 Story | US-04 |
| **Total Backlog** | **20 Stories** | **Core Product Requirements Frozen** |

### Matrix Table 2: Story Allocation by Feature Area

| Functional Core Feature Area | Total Count |
| :--- | :--- |
| **Authentication & Access** | 4 Stories |
| **Student Management** | 5 Stories |
| **Course Management** | 4 Stories |
| **Grades Management** | 3 Stories |
| **Attendance Tracking** | 2 Stories |
| **Reports & Notifications** | 2 Stories |
| **Total Backlog** | **20 Stories** |

---

**Engineering Review Board Control Summary:**

*   **Document Status:** Baseline Requirements Finalized
*   **Author / Specification Engineer:** Sarah Zaheer (Product Owner)
*   **Quality Assurance Reviewer:** Tamana Omar (Scrum Master)
*   **Release Date:** October 10, 2026
