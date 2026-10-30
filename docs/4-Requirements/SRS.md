# Software Requirements Specification (SRS)

**Project:** Student Management System  
**Version:** 1.0  
**Date:** October 24, 2026  
**Author:** Sarah Zaheer (Product Owner)

---

## 1. Introduction

### 1.1 Purpose
The purpose of this document is to define the functional and non-functional requirements for the Student Management System. This document is intended for the development team, the Scrum Master, and the Product Owner to ensure a shared understanding of the system's capabilities.

### 1.2 Scope
The Student Management System will allow administrators to manage student records, teachers to input grades, and students to view their academic information.

---

## 2. Functional Requirements (FR)
*Functional requirements define what the system must do.*

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-01** | **User Authentication:** The system shall allow users (Admin, Teacher, Student) to log in using a unique username and password. | High |
| **FR-02** | **Admin - Student Management:** The Admin shall be able to Create, Read, Update, and Delete (CRUD) student profiles (Name, ID, DOB, Contact info). | High |
| **FR-03** | **Teacher - Grade Entry:** Teachers shall be able to input and update grades for students enrolled in their specific courses. | High |
| **FR-04** | **Student - View Grades:** Students shall be able to view their own grades and academic transcripts. | Medium |
| **FR-05** | **Course Registration:** The system shall allow students to enroll in available courses for the upcoming semester. | Medium |
| **FR-06** | **Search Function:** The Admin and Teachers shall be able to search for students by their ID or Last Name. | Low |

---

## 3. Non-Functional Requirements (NFR)
*Non-functional requirements define system properties and constraints.*

| ID | Requirement Description | Category |
| :--- | :--- | :--- |
| **NFR-01** | **Performance:** The system shall load any page or return a search query within 2 seconds. | Performance |
| **NFR-02** | **Security:** All user passwords must be encrypted using a hashing algorithm (e.g., BCrypt) before being stored in the database. | Security |
| **NFR-03** | **Usability:** The system must be accessible on standard web browsers (Chrome, Firefox, Edge) and be easy to use for non-technical staff with minimal training. | Usability |
| **NFR-04** | **Availability:** The system shall be available 99% of the time during normal university working hours (Mon-Fri, 8:00 AM - 5:00 PM). | Reliability |
| **NFR-05** | **Scalability:** The system must be able to support up to 5,000 concurrent users during peak registration periods. | Scalability |



## 4. User Requirements vs. System Requirements (Example)
*As seen in Chapter 5 of the slides, here is how you break down a requirement:*

**User Requirement (Abstract):**
> "The system should generate a report of all failing students at the end of the semester."

**System Requirements (Detailed):**
1. On the last working day of the semester, a summary of students with an average grade below 50% shall be generated.
2. The report shall be automatically generated for printing after 5:00 PM.
3. The report must list the student's ID, Name, Course, and Final Grade.
4. Access to the failing students report shall be restricted to authorized Admin users only.

---

## 5. Requirements Validation
*How did we ensure these requirements are correct? (Chapter 5)*
- [x] **Validity:** Requirements are realistic and technically feasible.
- [x] **Completeness:** All necessary features are defined.
- [x] **Consistency:** No two requirements contradict each other.
- [x] **Testability:** Every requirement can be tested (e.g., FR-01 can be tested by trying to log in).