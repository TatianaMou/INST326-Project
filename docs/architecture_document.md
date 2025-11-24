This project models a healthcare-oriented system using advanced object-oriented programming concepts.

The system includes:

* Medical staff behavior modeling
* Analysis engines that process the patient's data
* Composition-based registries and departments

The overall goal of this project is to build a flexible polymorphic system that models real-world healthcare relationships while demonstrating the required concepts in inheritance, ABCs, and composition.

------------------------------------------------------------

### Patient Profile Hierarchy
 PatientProfile (ABC)

 ├── PediatricPatient
 
 ├── AdultPatient
 
 └── GeriatricPatient

* All patients share attributes (name, ID, symptoms, severity, visits, allergies).
* This is a natural **is-a** relationship:
* A pediatric patient is a patient.
* A geriatric patient is a patient
* 
------------------------------------------------------------

### Medical Staff Hierarchy
  MedicalStaff (ABC)
  
 ├── Doctor
 
 ├── Nurse
 
 └── Surgeon (extends Doctor)

* Every staff member shares identity information (ID, first/last name).
* Every staff member must define `calculate_daily_tasks()`.
* Surgeon logically extends the role of a doctor with task specialization.
* This hierarchy mirrors real-world healthcare roles and responsibilities.
* 
------------------------------------------------------------

### Patient Polymorphism
The method below is abstract in the base class and implemented differently in each subclass
  ``follow_up_window_days()``

### Medical Staff Polymorphism
Every subclass implements `calculate_daily_tasks()`

The hospital department calls `member.calculate_daily_tasks()`
