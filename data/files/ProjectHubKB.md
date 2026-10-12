# ProjectHub — Complete User and Feature Guide

> **About this document:** A complete guide to every ProjectHub screen, button, field, dialog and rule in Synclo. Each section can be read on its own and is written for non-technical users. It is structured so a RAG (Retrieval-Augmented Generation) assistant can retrieve sections independently, and it uses terms consistently (see the Glossary).

---

## Table of Contents

1. Overview
   - 1.1 How to Set Up ProjectHub (Start Here)
   - 1.2 Super Admin Quick Guide: Which Menu Item Do I Use?
   - 1.3 ProjectHub Setup: Tab-by-Tab Guide (What Is Created, What Is On/Off)
   - 1.4 Project Member and Project Lead (Normal Employee) Guide
   - 1.5 Team Lead Guide (Role 16)
2. Glossary
3. User Roles and Permissions
4. Dashboard Menu
5. ManageCompany Menu Integration
6. Feature-by-Feature Breakdown
   - 6.1 AllProjects (Projects List)
   - 6.2 Filter Drawer (Filter Projects)
   - 6.3 ProjectCreate (Create New Project Wizard)
   - 6.4 Project (Project Detail Page)
   - 6.5 Task Detail Drawer (Task Submission and Review)
   - 6.6 Project Discussion
   - 6.7 Project Files
   - 6.8 My Tasks
   - 6.9 Team Tasks
   - 6.10 Import Projects (ProjectHub Setup Assistant)
   - 6.11 ProjectHubSetup (Company Configuration)
   - 6.12 ProjectHub Department Setup
   - 6.13 Project Templates and the Template Wizard
   - 6.14 ProjectHub Dashboard (Company)
   - 6.15 Department Projects Dashboard / Team Lead Dashboard
   - 6.16 Archived Projects
   - 6.17 ProjectHub Analytics
7. Button and Control Reference
8. Workflows and Use Cases
9. Status Reference
10. Archive and Restore Rules
11. Frequently Asked Questions
12. Known Limitations (Current Version)
13. Page and URL Reference and Feature Relationship Map
14. Project Detail, Tasks and Role-Based Behaviour (Deep Dive)

---

## 1. Overview

**ProjectHub** is the project management module in Synclo. You use it to create, plan, run, review, track and archive projects.

With ProjectHub, users can:
- **Create projects**, either blank or from a **Project Template**.
- **Plan projects**: set up milestones and tasks, set dates, assign work one task at a time or in bulk, and add task dependencies.
- **Activate projects** once the readiness checklist is complete.
- **Run projects**: start tasks, submit work (files, links, notes), and review it (approve, or revert with feedback).
- **Track issues and risks.**
- **Collaborate** through Project Discussion (messages, mentions, files, voice notes) and Project Files.
- **Monitor progress** with My Tasks, Team Tasks, dashboards and analytics.
- **Import projects** from an **Excel or CSV file**, or from **Trello**, using the **ProjectHub Setup Assistant**, guided by an assistant called **Alci**.
- **Configure ProjectHub** for the whole company and for each department.

| Area | Who uses it | Where it lives |
|------|-------------|----------------|
| Day-to-day project work | Everyone with a ProjectHub role | **Dashboard menu** |
| Setup and company-wide oversight | Super Admins (and Department Admins for department setup) | **ManageCompany menu** |

### 1.1 How to Set Up ProjectHub (Start Here)

**Question this answers:** "How do I set up ProjectHub?", "Where is ProjectHub Setup?", "What tabs does ProjectHub Setup have?"

**Answer in short:** Setting up ProjectHub is done on the **ProjectHub Setup** page. **Only a Super Admin (Company Admin, role ID 1) can open and change it.** Everyone else (Department Admin, Team Lead, Project Lead, Project Member, Employee) sees "Access Denied — Only Company Admins can access Project Management Configuration." Department Admins set up their own department on a different page, **ProjectHub Department Setup** (section 6.12).

**Where to find it (menu path):**

1. Click the **Manage Company** button on your employee profile widget (or open `/managecompany`). The sidebar switches to the **ManageCompany** menu.
2. Open **Setup & Configurations**.
3. Open **Modular Configurations** (module configuration).
4. Click **ProjectHub Setup** (opens `/projecthubsetup`).

```
ManageCompany sidebar
└── Setup & Configurations
    └── Modular Configurations
        └── ProjectHub Setup   → /projecthubsetup   (Super Admin only)
```

> ProjectHub Setup is **not** in the Business Operations → ProjectHub group, which holds the day-to-day pages (Projects, ProjectHub Dashboard, Archived Projects, Project Templates, Analytics). It is also reachable from the ProjectHub Dashboard (**ProjectHub Setup** and **View Templates** buttons). The same page also opens at `/projectmanagementconfiguration`; non-Super Admins get Access Denied.

**Tabs on the ProjectHub Setup page (in order):**

| # | Tab | What you do in this tab |
|---|-----|-------------------------|
| 1 | **General Settings** | Manage **Priority Labels** (add, edit, delete; Low, Medium, High, Critical are protected), view **Project Health Statuses** (view only), and set **Cross-Department Collaboration Rules** (allow members from other departments; require Department Administrator approval). |
| 2 | **Project Types & Categories** | Edit **Global Project Types** (Active/Inactive; for client-facing types, whether a **Client Brief Form** is required) and create **Department-Specific Categories** linked to one or more departments. |
| 3 | **Roles & Permissions** | **User Role Assignment**: give employees the **Department Administrator** or **Team Lead** ProjectHub role (Add User, Edit Role, filter by role). Changes save instantly. |
| 4 | **Project Templates** | Create and manage **Organization Wide Templates** (reusable milestone and task blueprints). See section 6.13. |
| 5 | **Archive Rules** | Set automatic archival (completed and inactive projects), restoration permissions, and the permanent-deletion rule. |

**Buttons on the page:**
- **Import Projects** (top right): opens the ProjectHub Setup Assistant (Alci) to import projects from a spreadsheet or from Trello (section 6.10).
- **Save Configuration** (bottom): saves the active tab for General Settings, Project Types & Categories and Archive Rules. It is hidden on Roles & Permissions, where changes save instantly.

**Recommended setup order for a new company:**
1. **General Settings**: review priority labels and cross-department rules.
2. **Project Types & Categories**: activate project types and add department categories.
3. **Roles & Permissions**: assign Department Administrators and Team Leads.
4. **Project Templates**: create company-wide templates.
5. **Archive Rules**: choose archive and restore behaviour.
6. Optionally **Import Projects** to bring in existing work.
7. Department Admins then complete **ProjectHub Department Setup** for their department (section 6.12).

Full details of each tab are in section 6.11.

### 1.2 Super Admin Quick Guide: Which Menu Item Do I Use?

**Question this answers:** "As a Super Admin, how do I create a project?", "Where do I see the dashboard?", "Where do I create a template?", "Why can't I pick a category for my template?"

All of these are under **Manage Company → Business Operations → ProjectHub** (ManageCompany sidebar). The sidebar items look like this (the labels such as "(All)" and "(COMPANY)" come from the Navigation settings and can differ between companies):

```
Business Operations
└── ProjectHub
    ├── Projects (All)               → /allprojects?view=superadmin
    ├── ProjectHub Dashboard (COMPANY) → /projecthub-dashboard
    ├── Archived Projects            → /archivedprojects
    ├── Project Templates            → /projecttemplates
    ├── Analytics                    → /projectanalytics
    └── ProjectHub (Standalone)      → the standalone Alci assistant view
```

| I want to... | Go to | Menu path |
|---|---|---|
| **See projects** or **create a project** | **Projects (All)** (AllProjects). Click **Create New Project** on that page. | Manage Company → Business Operations → ProjectHub → Projects |
| **See dashboard data** (company-wide numbers) | **ProjectHub Dashboard (COMPANY)** | Manage Company → Business Operations → ProjectHub → ProjectHub Dashboard |
| **See archived projects** | **Archived Projects** | Manage Company → Business Operations → ProjectHub → Archived Projects |
| **View or create a template** | **Project Templates** page (**New Template**), **or** the 4th tab of ProjectHub Setup (**Project Templates**). Both open the same Template Wizard. | Manage Company → Business Operations → ProjectHub → Project Templates; or Manage Company → Setup & Configurations → Modular Configurations → ProjectHub Setup → 4th tab |
| **Create a category** | ProjectHub Setup → **2nd tab, "Project Types & Categories"** → **Department-Specific Categories** → **Add New Category** | Manage Company → Setup & Configurations → Modular Configurations → ProjectHub Setup |
| **Assign Department Administrators / Team Leads** | ProjectHub Setup → 3rd tab, **Roles & Permissions** | same as above |

**Important order of setup before creating a template (prerequisites):**

1. **Departments must already exist** in the company. A category is linked to departments, so you need at least one department before you create a category.
2. **A category should exist before you create a template.** In the Template Wizard, Step 1 field **Available For** lists the company's existing, active categories. If none exist, it shows "No categories found". If there is no category yet: go to **ProjectHub Setup → 2nd tab (Project Types & Categories) → Add New Category**, create it, click **Save Configuration**, then return to create the template.
3. **Then create the template** (Template Wizard, section 6.13).

> A template can still be saved without a category (the field is optional), but then it is not tied to any category. Creating the category first is the recommended order.

**Only the Super Admin** can open the **Project Templates** page and **ProjectHub Setup**. Department Admins create department-level categories and templates from **ProjectHub Department Setup** (section 6.12).


### 1.3 ProjectHub Setup: Tab-by-Tab Guide (What Is Created, What Is On/Off)

**Question this answers:** "In which tab do I add a Priority Label?", "What does this switch do?", "What happens if I turn this option on?"

**Open it (Super Admin only):** Manage Company → Setup & Configurations → Modular Configurations → **ProjectHub Setup** (`/projecthubsetup`).

| I want to... | Tab |
|---|---|
| Add / edit / delete a **Priority Label** | Tab 1 **General Settings** |
| Allow people from **other departments** on projects | Tab 1 **General Settings** (switch) |
| Switch a **Project Type** on or off, or require a **Client Brief Form** | Tab 2 **Project Types & Categories** |
| Create a **Category** for departments | Tab 2 **Project Types & Categories** |
| Make someone a **Department Administrator** or **Team Lead** | Tab 3 **Roles & Permissions** |
| Create a reusable **Project Template** | Tab 4 **Project Templates** |
| Archive projects automatically, or control who can restore | Tab 5 **Archive Rules** |

**Saving:** **Save Configuration** saves only the tab you are on (tabs 1, 2 and 5). Tab 3 saves instantly; tab 4 saves from the template wizard.

The full explanation of every tab, field, switch and what happens when it is ON or OFF is in **section 6.11**. Archive rules are explained in detail in **section 10**.

---

### 1.4 Project Member and Project Lead (Normal Employee) Guide

**Question this answers:** "What does a normal employee see in ProjectHub?", "Can a Project Member or Project Lead create or import projects?", "What does a Project Lead see?"

**Project Member** and **Project Lead** are **not roles**. They are positions inside a project (section 3). An employee who only has these positions has **no ProjectHub role** and is a **normal employee** in the menu.

**Menu:** under **My Work → ProjectHub** a normal employee sees **only two entries**:

| Entry | Opens | What it is |
|---|---|---|
| **My Projects** (the sidebar label may read **All Projects**) | `/allprojects` | The projects you lead or work on (section 6.1) |
| **My Tasks** | `/mytasks` | Every task assigned to you (section 6.8) |

They do **not** see Department Projects, ProjectHub Dashboard, Department Setup, Team Tasks, Analytics or any setup page.

**What a Project Member and a Project Lead cannot do**
- They **cannot create projects**: the **Create New Project** button is not shown to them.
- They are **not meant to import projects** (Import Projects is for managers). *In the current version the Import Projects button is still displayed on the projects page for every user, but it is not intended for a Project Member or Project Lead.*
- They **cannot archive or view archived projects**, edit or delete a project from the list, or use any ProjectHub Setup page.

**The projects page for them** (`/allprojects`, heading **My Projects**, "View and manage projects you are leading or contributing to")
- A project **you lead** opens in **Project Lead** view; every other project you work on opens in **Project Member** view.
- **KPI cards:** a Project Member sees **My Active Projects**, **My Completed Projects**, **My Planning Projects**, **Overdue Tasks**. A Project Lead also sees **Projects At Risk**.
- **Filters:** **Status**, **Priority**, **Project Type**. A Project Lead (someone who leads at least one project) also gets a **Team Member** filter. There are no Department, Team Lead or Project Lead filters.
- Empty state: "No Projects Found — You haven't been assigned to any projects yet. Projects you lead or contribute to will appear here."

**Their tasks:** **My Tasks** (section 6.8): start tasks, save drafts, submit work for review, and view tasks that are Under Review or Completed.

---

### 1.5 Team Lead Guide (Role 16)

**Question this answers:** "What does a Team Lead see in ProjectHub?", "Where does a Team Lead find team projects?", "Can a Team Lead create or import projects?", "What does the Team Lead dashboard show?"

**A Team Lead has the role ID 16.** A Team Lead has two places in the sidebar:

| What the Team Lead wants | Menu path | Entries |
|---|---|---|
| **Their own** projects and tasks | **My Work → ProjectHub** | **My Projects** (the label may read **All Projects**) and **My Tasks** |
| **Their team's** projects, tasks and dashboard | **Manage My Team → ProjectHub** | **Team Lead Projects**, **Team Tasks**, **ProjectHub Dashboard** |

```
Dashboard sidebar (Team Lead)
├── My Work
│   └── ProjectHub
│       ├── My Projects / All Projects  → /allprojects
│       └── My Tasks                    → /mytasks
└── Manage My Team
    └── ProjectHub
        ├── Team Lead Projects          → /allprojects?view=teamlead
        ├── Team Tasks                  → /teamtasks
        └── ProjectHub Dashboard        → /department-projects-dashboard
```

| Entry | What it is |
|---|---|
| **Team Lead Projects** | All projects owned by the team ("Team Projects — Monitor and manage projects owned by your team."). The URL is `/allprojects?view=teamlead` (for example `https://<your-company>.synclo.com/allprojects?view=teamlead`). |
| **Team Tasks** | Supervise the team's tasks: approve, revert, reassign, edit (section 6.9). **Only Team Leads see this entry.** |
| **ProjectHub Dashboard** | The **Team Lead Dashboard** (section 6.15). It is not the company-wide dashboard. |

**A Team Lead can create and import projects.** On **Team Lead Projects** (`view=teamlead`) the buttons **Create New Project** and **Import Projects** are available (a Project Lead or Project Member does not get Create New Project). On **My Work → My Projects** a Team Lead does **not** get Create New Project; use **Team Lead Projects** instead.

**Team Lead Projects page**
- **KPI cards:** **Active Projects**, **Team Members**, **Planning Projects**, **Completed Projects**.
- **Filters:** Status, Priority, Project Type, **Project Lead** and **Team Member**. (No Department or Team Lead filter.)
- **View Archived Projects** appears only when archive restoration is allowed (section 10).
- Empty state: "No Team Projects Found — There are currently no projects assigned to your team."

**Team Tasks:** section 6.9. A Team Lead can **Approve** and **Revert with Feedback** tasks that are **Under Review**, **Reassign** and **Edit** tasks that are **To Do** or **In Progress**, and only **view** **Completed** tasks.

**Team Lead Dashboard:** section 6.15. It has **View Projects** as its only Quick Action, which opens `/allprojects?view=teamlead`.

---

## 2. Glossary

| Term | Meaning |
|------|---------|
| **Project** | A piece of work with a name, type, priority, category, team, milestones and tasks. |
| **Milestone** | A phase of a project. It has a start date and a due date, and it contains tasks. |
| **Task** | A unit of work inside a milestone. It has an assignee, dates, priority, estimated time and optional dependencies. |
| **Dependency** | A task that must be finished before another task can start. Only tasks listed above the current task can be chosen. |
| **Project Template** | A reusable blueprint of milestones and tasks. It contains no clients, dates, team members or budgets. |
| **Project Type** | A company-wide classification, for example **Internal** or **Client**. Client projects have extra client fields. |
| **Project Category** | A department-level classification, for example "Campaign". It is linked to one or more departments. |
| **Priority Label** | The priority used for projects, tasks and issues. Defaults: Low, Medium, High, Critical. |
| **Project Health** | Shows whether a project is **On Track**, **At Risk** or **Off Track**. |
| **View** | The role you are viewing as. Only three roles have a view link: SuperAdmin (1) → `view=superadmin`, DepartmentAdmin (15) → `view=departmentadmin`, TeamLead (16) → `view=teamlead`. Project Lead and Project Member have no view link; they use `/allprojects` (My Work). The view decides which projects, KPIs, filters and actions you see. |
| **My Work** | The personal projects view, used when no role view is chosen. A project you lead opens in Project Lead view; any other project opens in Project Member view. |
| **Draft** | A project or template that was saved but not finished. |
| **Submission** | Work sent for review by a task's assignee: files, working URLs and notes. Each submission is stored as a version. |
| **Revert with Feedback** | A reviewer sends a submitted task back to the assignee with comments. |
| **Alci** | The on-screen assistant in the ProjectHub Setup Assistant. |

---

## 3. User Roles and Permissions

| Role | Role ID | Code | Summary |
|------|---------|------|---------|
| **Super Admin** (Company Admin) | 1 | — | Full control across the company. |
| **Department Administrator** | 15 | `DEPARTMENT_ADMINISTRATOR` | Manages projects and ProjectHub setup for their own department. |
| **Team Lead** | 16 | `TEAM_LEAD` | Manages projects owned by their team. |
If a user has more than one role, Synclo uses the highest one by default (Super Admin > Department Administrator > Team Lead).

**Project Lead and Project Member are not roles.** They are positions inside a single project:
- **Project Lead**: the person chosen as lead of a project. Plans the work, manages the team and reviews submissions for that project.
- **Project Member**: a person added to a project's team. Works on the tasks assigned to them.

They have no role ID, are not assigned in role settings, and have no `view=` link. They always open **My Work → ProjectHub** (`/allprojects`). In that list, a project you lead opens in Project Lead view and any other project opens in Project Member view.

**Where roles are assigned:**
- **ProjectHubSetup → Roles & Permissions → User Role Assignment** (Super Admin). Only **Department Administrator** and **Team Lead** can be assigned here.
- **ProjectHub Department Setup → User Roles** (Department Admin). Only **Team Lead** can be assigned here.

### 3.1 Permission matrix

| Capability | Super Admin | Dept Admin | Team Lead | Project Lead | Project Member |
|---|:-:|:-:|:-:|:-:|:-:|
| Projects visible | All | Department | Team | Projects they lead | Projects they work on |
| Create New Project | Yes | Yes | Yes (Team Lead view only) | No | No |
| Edit project (Project Detail) | Any project | Projects they created | Projects they created | No | No |
| Edit / Delete from the project list menu | Yes | Yes | Yes | No (unless creator) | No |
| Change Project Lead | Yes | Yes | Yes | No | No |
| Manage Team | Yes | Yes | Yes | Yes | No |
| Put on Hold / Resume | Yes | Yes | Yes | Yes | No |
| Activate Project | Yes | Yes | Yes | Yes | No |
| Add or edit milestones and tasks; assign tasks | Yes | Yes | Yes | Yes | No (view only) |
| Add Issue / Add Risk | Yes | Yes | Yes | Yes | No |
| Resolve / Delete Risk | Yes | Yes | Yes | Yes | No |
| Edit Project Brief | Yes | Yes | Yes | Yes | No |
| Start a task, submit work | Assignees (PM view / My Tasks) | | | | Yes |
| Approve / Revert submitted tasks | Yes | Yes | Yes | Yes | No |
| Archive / Unarchive | See section 10 | See section 10 | See section 10 | No | No |
| Import Projects button | Yes | Yes | Yes | Yes | Yes |
| ProjectHub Dashboard | Yes | — | — | — | — |
| Department / Team Lead Dashboard | — | Yes | Yes | — | — |
| ProjectHubSetup | **Only** | No | No | No | No |
| ProjectHub Department Setup | Yes | Yes | — | — | — |
| Project Templates page | **Only** | No | No | No | No |
| Edit or delete a template or category | Any | Ones they created | Ones they created | — | — |
| Team Tasks (sidebar entry) | — | — | **Yes (only)** | — | — |
| My Tasks | Yes | Yes | Yes | Yes | Yes |

---

## 4. Dashboard Menu

### 4.1 Where ProjectHub appears
ProjectHub's everyday pages appear in the **main Dashboard sidebar**. The server loads the sidebar based on your roles, so you only see the entries your roles allow. Administrators manage the labels in the Navigation settings, so wording can differ slightly between companies.

> **About the URLs in this document:** every URL is a path on your **company's own Synclo address** (its subdomain), not `localhost`. Add the path to your company's address. For example, if your company opens Synclo at `https://<your-company>.synclo.com`, then `/allprojects?view=teamlead` is `https://<your-company>.synclo.com/allprojects?view=teamlead`.

The sidebar is split into **menu groups** (for example **My Work**, **My Employment**, **Manage My Team**). **ProjectHub** is a collapsible item inside one of these groups, and its pages are listed under it. Which group it sits in depends on your role.

#### 4.1.1 How to reach ProjectHub, by role (quick answer)

| Your role | Sidebar | Click path |
|---|---|---|
| **Employee** (including Project Lead and Project Member) | Dashboard sidebar | **My Work → ProjectHub** |
| **Department Admin** | Dashboard sidebar | **My Work → ProjectHub** (Department Projects, ProjectHub Dashboard and Department Setup are added here) |
| **Team Lead** | Dashboard sidebar | **Manage My Team → ProjectHub** |
| **Super Admin** (Company Admin) | ManageCompany sidebar | **Manage Company → Business Operations → ProjectHub** |

A user with several roles sees every path their roles allow. For example, a Team Lead also has the **My Work → ProjectHub** entry for their own projects and tasks.

**Team Tasks is shown only to Team Leads** (under **Manage My Team → ProjectHub**). Department Admins, Super Admins, Project Leads and Project Members do not see Team Tasks in the sidebar.

#### 4.1.2 Employee: My Work → ProjectHub

```
Dashboard sidebar
└── My Work
    └── ProjectHub
        ├── My Projects     → /allprojects     (the sidebar label may read "All Projects")
        └── My Tasks        → /mytasks
```

A normal employee (including a Project Lead or Project Member) sees **only these two entries** under **My Work → ProjectHub**. There is no Department Projects, ProjectHub Dashboard, Department Setup, Analytics or Configuration entry for an employee.

| Entry | Opens | What it is |
|---|---|---|
| My Projects | `/allprojects` | AllProjects in **My Work** view: the projects you lead or work on (section 6.1). |
| My Tasks | `/mytasks` | Every task assigned to you (section 6.8). |

A Project Member or Project Lead cannot create projects, and cannot archive or view archived projects (section 10). See section 1.4.

#### 4.1.3 Team Lead: Manage My Team → ProjectHub

```
Dashboard sidebar
└── Manage My Team
    └── ProjectHub
        ├── Team Lead Projects     → /allprojects?view=teamlead
        ├── Team Tasks             → /teamtasks
        └── ProjectHub Dashboard   → /department-projects-dashboard
```

| Entry | Opens | What it is |
|---|---|---|
| Team Lead Projects | `/allprojects?view=teamlead` | AllProjects in Team Lead view ("Team Projects"): projects owned by your team. A Team Lead can **Create New Project** here (section 6.1). |
| Team Tasks | `/teamtasks` | Supervise your team's tasks (section 6.9). **Only Team Leads see this entry.** |
| ProjectHub Dashboard | `/department-projects-dashboard` | The **Team Lead Dashboard** (section 6.15). This is not the company-wide ProjectHub Dashboard. |

- **Archived Projects:** Team Lead Projects → **View Archived Projects** (section 6.16).
- A Team Lead's own projects and tasks stay under **My Work → ProjectHub** (**My Projects**, **My Tasks**).

#### 4.1.4 Department Admin: My Work → ProjectHub

For a Department Admin, the department entries are added to the **My Work → ProjectHub** menu, under the personal entries.

```
Dashboard sidebar
└── My Work
    └── ProjectHub
        ├── My Projects            → /allprojects
        ├── My Tasks               → /mytasks
        ├── Department Projects    → /allprojects?view=departmentadmin
        ├── ProjectHub Dashboard   → /department-projects-dashboard
        └── Department Setup       → /projecthub-departmentsetup
```

| Entry | Opens | What it is |
|---|---|---|
| My Projects | `/allprojects` | Projects you lead or work on, in **My Work** view (section 6.1). |
| My Tasks | `/mytasks` | Every task assigned to you (section 6.8). |
| Department Projects | `/allprojects?view=departmentadmin` | AllProjects in Department Admin view: every project in your department (section 6.1). |
| ProjectHub Dashboard | `/department-projects-dashboard` | The **Department Projects Dashboard** (section 6.15). This is not the company-wide ProjectHub Dashboard. |
| Department Setup | `/projecthub-departmentsetup` | **ProjectHub Department Setup**: Team Lead roles, department categories and templates (section 6.12). The sidebar label may appear as "Departmnet Setup". |

- **Archived Projects:** Department Projects → **View Archived Projects** (section 6.16).
- A Department Admin does **not** see **Team Tasks** in the sidebar.

#### 4.1.5 All Dashboard menu entries

The table lists each entry by the page it opens.

| Entry (page) | Opens | Shown to |
|---|---|---|
| My Projects (My Work) | `/allprojects` | Everyone with a ProjectHub role |
| All Projects | `/allprojects?view=superadmin` | Super Admin |
| Department Projects | `/allprojects?view=departmentadmin` | Department Admin |
| Team Projects | `/allprojects?view=teamlead` | Team Lead |
| My Projects (Project Lead and Project Member) | `/allprojects` (no `view`) | Project Lead, Project Member |

> **Project Lead and Project Member have no role view of their own.** They always use `/allprojects` (My Work). Inside that list, a project you lead opens in Project Lead view and any other project opens in Project Member view.
| ProjectHub Dashboard (Department Projects Dashboard / Team Lead Dashboard) | `/department-projects-dashboard` | Department Admin (My Work → ProjectHub), Team Lead (Manage My Team → ProjectHub) |
| Department Setup | `/projecthub-departmentsetup` | Department Admin (My Work → ProjectHub) |
| My Tasks | `/mytasks` | Everyone with a ProjectHub role |
| Team Tasks | `/teamtasks` | **Team Lead only** (Manage My Team → ProjectHub) |
| ProjectHub Analytics | `/projecthub-analytics` | Users with All Projects access |

### 4.2 Purpose
The Dashboard menu is for **daily project work**: viewing and creating projects, planning and running them, and working on tasks. **Users who want to work on projects or tasks should use the Dashboard menu.**

### 4.3 What happens when you click it
A projects entry opens **AllProjects** (section 6.1). The heading, KPI cards, filters and buttons all adapt to the view in the link.

---

## 5. ManageCompany Menu Integration

### 5.1 Where ProjectHub appears
**ManageCompany** is the company administration area. You reach it with the **Manage Company** button on the employee profile widget, or at `/managecompany`. On ManageCompany pages, the sidebar switches to the ManageCompany navigation.

#### 5.1.1 Super Admin: Manage Company → ProjectHub

ProjectHub appears in **two places** in the ManageCompany sidebar:

```
ManageCompany sidebar
├── Business Operations
│   └── ProjectHub
│       ├── Projects               → /allprojects?view=superadmin
│       ├── ProjectHub Dashboard   → /projecthub-dashboard
│       ├── Archived Projects      → /archivedprojects
│       ├── Project Templates      → /projecttemplates
│       └── Analytics              → /projectanalytics
└── Setup & Configurations
    └── Modular Configurations
        └── ProjectHub Setup       → /projecthubsetup
```

| Entry | Click path | Opens | What it is |
|---|---|---|---|
| Projects | Manage Company → Business Operations → ProjectHub → Projects | `/allprojects?view=superadmin` | AllProjects in Super Admin view: every project in the company (section 6.1). |
| ProjectHub Dashboard | Manage Company → Business Operations → ProjectHub → ProjectHub Dashboard | `/projecthub-dashboard` | The company-wide dashboard (section 6.14). |
| Archived Projects | Manage Company → Business Operations → ProjectHub → Archived Projects | `/archivedprojects` | All archived projects (section 6.16). |
| Project Templates | Manage Company → Business Operations → ProjectHub → Project Templates | `/projecttemplates` | Create and manage templates (section 6.13). |
| Analytics | Manage Company → Business Operations → ProjectHub → Analytics | `/projectanalytics` | Project Analytics (see the note in section 6.17). |
| ProjectHub Setup | Manage Company → Setup & Configurations → Modular Configurations → ProjectHub Setup | `/projecthubsetup` | Company-wide ProjectHub configuration (section 6.11). |

#### 5.1.2 Other ManageCompany entries

| Entry (page) | Opens | Shown to |
|---|---|---|
| ProjectHub Department Setup | `/projecthub-departmentsetup` | Super Admin, Department Admin |

ProjectHub Department Setup can also be opened from the dashboard Quick Actions (sections 6.12, 6.14 and 6.15).

#### 5.1.3 Where to find each ProjectHub page, by role

| Page | Employee | Team Lead | Department Admin | Super Admin |
|---|---|---|---|---|
| Projects list | My Work → ProjectHub → My Projects | Manage My Team → ProjectHub → Team Lead Projects | My Work → ProjectHub → Department Projects | Manage Company → Business Operations → ProjectHub → Projects |
| My own projects | My Work → ProjectHub → My Projects | My Work → ProjectHub → My Projects | My Work → ProjectHub → My Projects | — |
| My Tasks | My Work → ProjectHub → My Tasks | My Work → ProjectHub → My Tasks | My Work → ProjectHub → My Tasks | `/mytasks` |
| Team Tasks | — | Manage My Team → ProjectHub → Team Tasks (**Team Lead only**) | — | — |
| Dashboard | — | Manage My Team → ProjectHub → ProjectHub Dashboard (Team Lead Dashboard) | My Work → ProjectHub → ProjectHub Dashboard (Department Projects Dashboard) | Manage Company → Business Operations → ProjectHub → ProjectHub Dashboard (company-wide) |
| Archived Projects | All Projects → View Archived Projects (when available) | Team Lead Projects → View Archived Projects | Department Projects → View Archived Projects | Manage Company → Business Operations → ProjectHub → Archived Projects |
| Analytics | — | — | — | Manage Company → Business Operations → ProjectHub → Analytics |
| Project Templates | — | — | My Work → ProjectHub → Department Setup → Project Templates | Manage Company → Business Operations → ProjectHub → Project Templates |
| ProjectHub Setup | — (Access Denied) | — | — (uses Department Setup) | Manage Company → Setup & Configurations → Modular Configurations → ProjectHub Setup |
| ProjectHub Department Setup | — | — | My Work → ProjectHub → Department Setup | ManageCompany, or ProjectHub Dashboard → Department Setup |

> **"ProjectHub Dashboard" means a different page for each role.** Department Admin → Department Projects Dashboard; Team Lead → Team Lead Dashboard (both `/department-projects-dashboard`, section 6.15); Super Admin → the company-wide ProjectHub Dashboard (`/projecthub-dashboard`, section 6.14).

### 5.2 Purpose
The ManageCompany menu is for **setting up and governing ProjectHub**: standards, categories, templates, roles, archive rules, importing projects, and the company-wide overview. **Users who want to configure ProjectHub or see the whole company should use the ManageCompany menu.**

### 5.3 How it differs from the Dashboard menu

| | Dashboard menu | ManageCompany menu |
|---|---|---|
| Focus | Doing project work | Configuring and overseeing ProjectHub |
| Users | All ProjectHub roles | Super Admin (Department Admin for department setup) |
| Data scope | Limited to your role | Company-wide or department-wide |
| Main pages | AllProjects, Project Detail, My Tasks, Team Tasks | Dashboard, Setup, Department Setup, Templates |

**How they connect:** **View All Projects** on the ProjectHub Dashboard opens AllProjects in Super Admin view. **Import Projects** on AllProjects and on ProjectHubSetup opens the same Setup Assistant.

---

## 6. Feature-by-Feature Breakdown

### 6.1 AllProjects (Projects List)

**What it is:** The main page for browsing and managing projects.

**How to access it:**
- The Dashboard menu projects entry.
- **View All Projects** on the company dashboard.
- **View Projects** on the department dashboard or a Team Lead Overview card.
- **View All** on a dashboard projects table.
- **View All Projects** on the Setup Assistant success screen.
- **Back to Projects** on Project Detail or Archived Projects.

**Headings by view:**

| View | Heading | Subtitle |
|---|---|---|
| SuperAdmin | All Projects | View and manage projects across all departments and teams. |
| DepartmentAdmin | Department Projects | Oversee and manage all projects within your department. |
| TeamLead | Team Projects | Monitor and manage projects owned by your team. |
| ProjectLead | My Projects | Manage and monitor the projects you are leading. |
| ProjectMember | My Projects | View and track the projects you are currently contributing to. |
| My Work | My Projects | View and manage projects you are leading or contributing to. |

**KPI cards by view:**

| View | Cards |
|---|---|
| SuperAdmin | Active Projects, Planning Projects, Completed Projects |
| DepartmentAdmin | Active Projects, Planning Projects, Projects At Risk |
| TeamLead | Active Projects, Team Members, Planning Projects, Completed Projects |
| ProjectLead | Active Projects, Planning Projects, Completed Projects, Projects At Risk |
| ProjectMember | My Active Projects, My Completed Projects, My Planning Projects, Overdue Tasks |
| My Work (leads at least one project) | My Active Projects, My Completed Projects, My Planning Projects, Overdue Tasks, Projects At Risk |
| My Work (member only) | My Active Projects, My Completed Projects, My Planning Projects, Overdue Tasks |

**Header buttons:** **View Archived Projects** (section 6.16), **Import Projects** (section 6.10), **Create New Project** (section 6.3).

**Toolbar:** **Search projects...**, **Filters** (section 6.2), **Sort By** (Recently Created, Alphabetical, Deadline), and the **Grid / List** toggle.

**Grid card contents:**
- Category badge.
- Project name and the ⋮ menu.
- Type badge (Internal or Client) and priority badge.
- **Project Lead** (or "Unassigned").
- "X / Y Tasks" and a progress bar: green at 60% or more, yellow at 30–59%, red below 30%.
- Due date (red when overdue) and status.
- Drafts have a dashed border.

**List columns:** Project Name (with type badge), Category, Project Lead, Timeline, Status, Priority, Progress, Actions.

**Opening a project:** Clicking a **Draft** opens the Create wizard so you can continue it. Clicking any other project opens Project Detail.

**⋮ menu:**

| Item | Shown when |
|---|---|
| **View Details** | The project is not a draft |
| **Edit Draft** / **Edit** | Viewing as SuperAdmin, DepartmentAdmin or TeamLead, or you are the creator |
| **Archive** | Viewing as SuperAdmin, DepartmentAdmin or TeamLead, and Archive Rules allow restoration |
| **Unarchive** | The project is archived and the restore rules allow it (section 10) |
| **Delete** | The same people as Edit. A confirmation appears: "Are you sure you want to delete "<name>"? This action cannot be undone." Choose **Cancel** or **Delete Project**. |

**Pagination:** 6, 12 (default), 18 or 24 per page; ‹ › to move between pages; "Showing X to Y of Z entries".

**Empty states:**
- When there are no projects at all, a role-specific message appears: "No Projects Assigned", "You're Not Leading Any Projects", "No Team Projects Found", "No Department Projects" or "No Projects Found". Managers also see **Create New Project**, and everyone sees **Import Projects**.
- When a search or filter finds nothing: "No projects found — Try adjusting your filters".

**Good to know:**
- Search, Status and Department filter across all your projects.
- Priority, Project Type, Team Lead, Project Lead, Team Member and **Sort By** only apply to the projects on the **current page**. Increase the entries per page to cover more projects.
- The Department list only shows departments of the projects already loaded.

---

### 6.2 Filter Drawer (Filter Projects)

**What it is:** A side panel titled "Filter Projects — Apply filters to narrow down your project list".

**How to access it:** AllProjects → **Filters**. A badge on the button shows how many filters are active.

**Filters:**
- **Department**
- **Project Status**: All Status, Draft, the company statuses (for example Planning, In Progress, Completed), On Hold, Archived
- **Priority**
- **Project Type**
- **Team Lead**
- **Project Lead**
- **Team Member**

**Filters shown in each view:**

| Filter | SA | DA | TL | PL | PM | My Work (SA/DA) | My Work (TL) | My Work (lead) | My Work (member) |
|---|---|---|---|---|---|---|---|---|---|
| Department | ✓ | | | | | | | | |
| Status / Priority / Type | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Team Lead | ✓ | ✓ | | | | ✓ | | | |
| Project Lead | ✓ | ✓ | ✓ | | | ✓ | ✓ | | |
| Team Member | | | ✓ | ✓ | | ✓ | ✓ | ✓ | |

**Buttons:** **Clear All** resets all filters and the search box. **Apply Filters** closes the drawer.

**Special behaviour:** Choosing Status = **Archived** opens the Archived Projects page. Any change to a filter or the search returns you to page 1.

---

### 6.3 ProjectCreate (Create New Project Wizard)

**What it is:** A four-step dialog for creating or editing a project.

**How to access it:**
- **Create New Project** (AllProjects header or empty state).
- Click a Draft card, or ⋮ **Edit Draft** / **Edit** in the list.
- Project Detail → ⋮ → **Edit Project**.

**Who:** Super Admin, Department Admin, Team Lead.

**Title:** "Create New Project" or "Edit Project". **Steps:** 1 **Structure** → 2 **Project Info** → 3 **Team** → 4 **Review**.

#### Step 1 — Structure
- **Create from Project Template** ("Start with pre-built milestones and tasks"):
  1. Choose a **Project Category \***.
  2. Choose a template under **Select Project Template \***. The list stays disabled until a category is chosen ("Select a category first..."), and it has a search box.
  3. A preview shows Milestones, Tasks and Timeline.
  - Changing the category clears the selected template.
- **Create Blank Project** ("Start from scratch with no milestones or tasks"):
  - Choose a **Project Category**. The field is labelled optional, but **Next stays disabled until a category is chosen**.
  - A note explains: "An empty project will be created. You can add milestones and tasks from the Project Detail page."
- **Editing an active project:** Step 1 shows "⚠️ Project structure cannot be modified for active projects" and is locked.

#### Step 2 — Project Info

| Field | Required | Notes |
|---|---|---|
| Project Name | Yes | Also required to save a draft |
| Description | No | |
| Project Type | Yes | The first enabled type is pre-selected |
| Priority | Yes | The first active priority is pre-selected |
| Planned Start Date | No | Defaults to today |
| Target Completion Date | No | |
| Client Organization / Client Contact | No | Shown only for the **Client** type ("Client Details") |
| Attachments | No | **Click to upload files**. Accepts PDF, Word, Excel, PowerPoint, TXT, JPG/PNG and ZIP, up to 10 MB each. Each file can have a label and can be removed with ✕. |

#### Step 3 — Team

| Field | SuperAdmin view | DepartmentAdmin view | TeamLead view |
|---|---|---|---|
| Department Admin | Shown (marked \*) | — | Shown (marked \*) |
| Project Team Lead | **Required** | **Required** | — |
| Project Lead | Optional | Optional | **Required** |
| Project Members | Optional | Optional | Optional |

- People fields are searchable (type to search). Team Leads show a "Team Lead" badge.
- **Select Whole Team** selects every available member; a counter shows how many are selected.
- The Project Lead list depends on the selected Team Lead.
- **Next** only checks the Project Team Lead (SuperAdmin and DepartmentAdmin views) or the Project Lead (TeamLead view).

#### Step 4 — Review
Shows four groups of information:
- **Project Information**: name, description, type, priority, category.
- **Project Structure**: creation method and template.
- **Project Team**: team lead, project lead, member count and names.
- **Planned Timeline.**
- **Client Details** (Client projects only).

A banner explains: "Your project will be created in **Planning** status. You can continue planning from the Project Detail page."

#### Footer buttons
- **Cancel** — asks you to confirm if you have entered data.
- **Save as Draft** — needs a name. Saves the project and opens its Planning tab.
- **Previous** / **Next** — "Step X of 4".
- **Create Project and Planning** (new project) — creates the project in Planning status and opens its **Planning** tab.
- **Update Project and Planning** (editing a Draft or Planning project) or **Update Project** (editing an active project).

**Closing with unsaved data:** "Continue without saving? You have unsaved changes. Save this project as a draft or close without saving." Choose **Yes, Close** or **Save Draft**.

---

### 6.4 Project (Project Detail Page)

**What it is:** The workspace for a single project. Section 14 covers full details by role and status.

**How to access it:**
- Click a project in AllProjects, or ⋮ **View Details**.
- Automatically after creating a project or saving a draft.
- Dashboard tables, Upcoming Milestones and Tasks Requiring Attention (these open in a new tab).
- The project link in the Task Detail drawer.
- URL: `/projectdetail?id=<id>&view=<Role>`.

#### 6.4.1 Header
- **Back button**: "Back to Projects", "Back to Team Tasks" or "Back to My Tasks", depending on where you came from. Project Leads and Members return to My Work.
- **Name and status badge.** The badge shows the first that applies: Draft, On Hold, Archived, then the actual status.
- **Project Health** (On Track, At Risk, Off Track) and **Priority**.
- **Description** with See More / See Less.
- **Project Lead, Project Type, Category, Start Date, Completion Target.**
- **Overall Progress** bar.

#### 6.4.2 Header actions

| Control | Visible when | What it does |
|---|---|---|
| **Activate Project** | Planning status; not shown to Project Members | Opens the Activate Project dialog. **Required**: Project Lead Assigned, Team Members Added. **Recommended**: All Tasks Assigned, Dependencies Verified. Confirm with **Activate Project**. While the required items are missing, the button is grey with a lock. |
| ⋮ **Edit Project** | Super Admin; Team Lead or Department Admin on projects they created. Not for Draft or Completed projects. | Opens the wizard in edit mode. |
| ⋮ **Change Project Lead** | Super Admin, Department Admin, Team Lead | Shows the **Current Project Lead**. Choose a **New Project Lead \*** ("Search or select a project lead..."), then **Change Lead**. |
| ⋮ **Manage Team** | Super Admin, Department Admin, Team Lead, Project Lead | Lists members with Team Lead, Project Lead or Team Member badges. **Add New Member**: "Select a member to add" → **Add**. Remove a member with ✕ (the Team Lead and Project Lead cannot be removed). Finish with **Save Changes**. |
| ⋮ **Put on Hold** | Same roles as Manage Team. Not for Draft, Completed or On Hold projects. | Opens "Put Project on Hold". Warning: "All project actions will be paused… disabled for everyone." Confirm with **Put on Hold**. |
| ⋮ **Resume Project** | On Hold projects | Resumes the project immediately. |
| ⋮ **Archive Project** | See section 10 | Asks for confirmation. If the project is active: "The project will be put on hold and then archived." |
| ⋮ **Unarchive Project** | Archived projects, with permission (section 10) | Restores the project. |
| **View Files** | Always | Opens Project Files (section 6.7). |
| **Project Discussion** (tab on the right edge of the screen) | Always | Opens Project Discussion (section 6.6). A red badge shows the unread count. |

Project Members never see the ⋮ menu.

#### 6.4.3 Overview tab
- **KPI cards:** Milestones Completed, Tasks Completed, High Risks.
- **Project Timeline:** Start Date, Target Completion, Current Status, Days Remaining (coloured green, yellow or red), Overall Health, Overall Progress.
- **Project Readiness** (Planning status; hidden from Project Members):
  - "X/Y Required" with a progress bar.
  - Required: Project Lead Assigned, Team Members Assigned.
  - "Recommended (not required to activate)": All Tasks Assigned, Dependencies Verified.
  - Button: **Activate Project**, or **Complete Required Items to Activate** while items are missing.
- **Pending Reviews** (outside Planning, and always for Project Members): tasks marked "Awaiting Project Lead Review", with assignees, milestone, priority and "Submitted … ago". Empty state: "No pending reviews".
- **Project Brief:**
  - **Edit** (not for Project Members) opens **Brief Description** and **Attach Files** (with labels; same file types and 10 MB limit). Save with **Save Brief**, or **Cancel**.
  - View mode shows a "Version N" badge and attachments with **Download** and the upload date.
  - **All Previous Versions** opens **Brief Versions**: each version number, a "Latest" badge, who added it and when, and **Show more/less**. **Revert to This Version** asks "Revert Brief?" before **Revert**. You can undo a revert by reverting again.
  - Empty state: "No brief description added yet. Click "Edit" to add one."
- **Team Members:** each member's role, a "Lead" crown for the project lead, task count and "% done".
- **Upcoming Milestones:** the next 3, with due date and progress.
- **Recent Activity:** the last 5 entries, with **View Full Activity** (opens the Activity tab).

#### 6.4.4 Planning / Execution tab
This tab is named **Planning** while the project is Draft or Planning, and **Execution** after activation.

**Planning mode** ("Set milestone start and end dates, add or remove tasks, assign them to project members individually or in bulk, and review the overall structure before activating the project."):
- **Add Milestone** dialog: **Milestone Name \***, Description, **Start Date \***, **Due Date \***. Save with **Add Milestone**, or **Save Changes** when editing.
- **Milestone card:**
  - Drag handle, name, status, "Due …", "X/Y tasks" and progress %.
  - All milestones are expanded.
  - ⋮ menu: **Edit Milestone** / **Delete Milestone**.
- **Drag** milestones to reorder them, and drag tasks to reorder them or move them between milestones.
- **Inside a milestone:** "Tasks (N)" plus:
  - **Bulk Assign Tasks** — shows checkboxes and a bar with "N tasks selected", **Select member**, **Assign**, and ✕ to exit.
  - **Add Task.**
- **Task row:**
  - Badges for priority, versions, Suggested JD (💡) and dependencies ("N deps", ✓ when verified).
  - Description, "Due …" or "No due date", and estimated time.
  - Assignee, or **Unassigned** (click it to assign someone right there).
  - ⋮ menu: **Add Issue**, **Edit Task**, **Delete**.
  - Copy icon: **Duplicate**.
  - Issues raised on the task are listed under it.
- **Add / Edit Task dialog:**
  - **Task Name \***, Description, Milestone, Priority.
  - **Assigned To** — searchable, or Unassigned.
  - **Suggested JD** — searchable designation.
  - Start Date / Due Date — must fall within the milestone's dates, and the due date cannot be before the start date.
  - **Estimated Time** in Hours or Days. It is calculated automatically when both dates are set.
  - **Dependencies** — only tasks above this one can be chosen. A **Circular Dependency Detected** warning blocks saving.
  - Save with **Add Task** or **Save Changes**.

**Execution mode** ("Track task progress, submit completed work for review, and manage issues and risks…"):
- Only one milestone is expanded at a time.
- Each task row shows its status, priority, versions, assignee, due date (red if overdue) and progress %.
- Tasks under review show "Awaiting Project Lead Review" (member view) or "Awaiting Team Lead Review" (other views).
- Click a task to open the **Task Detail drawer** (section 6.5).

**Issues:** **Add Issue** asks for a **Title \***, Priority and Owner, then saves with **Add Issue**.

**Risks** (in both modes):
- **Add Risk** asks for a **Risk Name \***, **Impact \*** (Low, Medium, High) and **Likelihood \*** (Low, Medium, High).
- Each risk shows its impact, likelihood and status: Open (red) or Resolved (green).
- Open risks show **Resolve** and **Delete Risk** to Super Admins, Department Admins, Team Leads and Project Leads.
- Empty state: "No risks defined".

Project Members can only view this tab.

#### 6.4.5 Activity tab
A full timeline grouped by date. Each entry shows an icon, description, relative time and exact date-time. Empty state: "No Activity Yet".

---

### 6.5 Task Detail Drawer (Task Submission and Review)

**What it is:** A side drawer for a single task. Section 14.11–14.12 shows the exact behaviour for each role and status.

**How to access it:** Click a task in Execution mode, in My Tasks, or in Team Tasks.

**Header:** task name, status (To Do, In Progress, Under Review, Completed), a **Revision Requested** badge if the task was sent back, priority, **Due:** date, the project name link (opens the project), milestone, and a progress bar.

**Task Overview:** Description, Dependencies, Estimated Hours, Start Date, Due Date, Assigned By.

**Work Submission** (changes with the task status):
- **To Do**: "Click "Start Task" below to begin working on this task." If a revision was requested, it shows the reviewer's feedback (Reviewer, Reviewer Comments) and the last submission.
- **In Progress** (assignee): a form with:
  - **Upload Files** — any type, with an optional label for each file.
  - **Working URL(s)** — a Label plus https://…, with **Add another URL**.
  - **Submission Notes.**
- **In Progress** (manager view): "This task is currently in progress. The assignee will submit their work for review when ready."
- **Under Review**: "This submission is currently awaiting review. No edits allowed." Shows Submitted By, Submitted Date, Notes, Files and Working URLs.
- **Completed**: "✅ Submission Approved" (click to see the history). Shows Approved By, Approval Date, Notes and Files.
- "N submissions available · **View history**" opens **Submission History**. Each version shows its status (Approved, Rejected, Awaiting … Review), date, submitter, files, URLs, notes, reviewer and comment.

**Bottom action bar:**

| Status | Assignee (member view / My Tasks) | Managers (Team Tasks, or TeamLead / ProjectLead / DepartmentAdmin / SuperAdmin view) |
|---|---|---|
| To Do | **Start Task** (moves the task to In Progress) | **Reassign Task**, **Edit Task** |
| In Progress | **Save Draft**, **Submit for Review** (needs at least one file, URL or note) | **Reassign Task**, **Edit Task** |
| Under Review | — | **Revert with Feedback**, **Approve** |
| Completed | "Read-only view — no actions available" | Same |

- **Approve** opens "Approve Task". An **Approval Comment \*** is required. **Confirm Approval** marks the task Completed.
- **Revert with Feedback** requires a **Feedback Comment \***. **Revert Task** sends the task back to the assignee marked "Revision Requested".
- **Edit Task** opens the Add/Edit Task dialog.
- Closing with unsaved submission data shows "Unsaved Changes" with **Keep Editing** or **Discard & Close**.

---

### 6.6 Project Discussion

**Question this answers:** "What is Project Discussion?", "What can I send?", "How do I mention someone?", "How do I send a voice note or a file?", "Can I react, reply or delete?", "Who can see and use it?", "What does the unread badge mean?"

**What it is:** A real-time chat space for **one project**, like a group chat. It lives in a side drawer on the Project Detail page. Everyone on the project writes in the same thread space.

**How to open it:** On Project Detail, click the vertical **Project Discussion** tab fixed on the **right edge** of the screen (blue tab with a speech-bubble icon). The drawer slides in from the right (about 440 px wide); close it with **X**. A **red badge** on the tab shows the number of unread messages (up to **99+**); the badge is hidden while the drawer is open.

**Who can use it:** **Everyone who can open the project**: Super Admin, Department Admin, Team Lead, Project Lead and Project Member, in **every** project status (Draft projects open in the wizard, so they have no discussion). The drawer itself has no role or status check. There is no private or role-limited discussion: all team members see the same messages.

#### What is on the drawer (top to bottom)

| Part | What it shows |
|---|---|
| **Header** | "Project Discussion", a **thread count** badge ("N threads"), and **X** to close |
| **Participants** | The project team's avatars (the first 4, then "+N") and **View all**. **View all** opens **Discussion Participants** ("N members in this discussion") with each person's photo, name, email and role. |
| **Messages area** | Messages in order, **oldest at the top and newest at the bottom** (like WhatsApp). Each message is a **thread** that can have replies. |
| **Composer** (bottom) | A text box "Write a comment... use @ to mention", a paperclip (**Attach file**), a microphone (**Record voice note**) and **Send** |

If there are no messages yet, it says **"No comments yet. Start the discussion!"**. While loading, it says "Loading...".

#### What you can send

| You can send | How |
|---|---|
| **Text** | Type in the box. **Enter** sends; **Shift+Enter** adds a new line; or click **Send**. |
| **A @mention of one person** | Type **@** and start the name; pick the person from the list (see below). |
| **@all** | Type **@** and choose **All** ("Mention everyone"): everyone on the team is mentioned. |
| **Files** | Click the paperclip and choose **Document** (.pdf, .doc, .docx, .txt, .xls, .xlsx, .ppt, .pptx), **Photo** (images), **Video** or **Audio File**. You can select **several files at once**. |
| **A voice note** | Click the microphone (see below). |
| **Text + files + a voice note together** | Yes, in one message. |

**Send is disabled** while a recording is running, or when the box is empty and nothing is attached. You can send a message with **only** a file or **only** a voice note (no text).

**Attachments before sending:** each chosen file shows its name and size (KB) with an **X** to remove it. There is no file size limit in the screen itself.

#### Mentions

- Typing **@** opens a list: **All** (first, "Mention everyone"), then team members. Keep typing to filter by name. **Click** a person to insert `@Name`. (The arrow keys and Enter do not pick from the list; click the person.)
- Mentions are highlighted: **green** if it is **@all** or **you**, **blue** for someone else.
- A message that **mentions you** gets a **green left border**.
- The mentioned people are notified; **@all** mentions every project team member.
- A mention only works if the text matches a team member's exact name, followed by a space or punctuation.

#### Voice notes

1. Click the microphone. The browser may ask for **microphone permission**.
2. The bar shows **"Recording... m:ss"** with **Cancel** (throw away) and **Stop**.
3. After **Stop**, a preview appears: play or pause it, watch the progress, delete it with **X**, or click **Add to Message**.
4. Click **Send**. If you forgot **Add to Message**, a finished recording is still included when you click Send.
5. **One voice note fits in one message.** If you add more, each extra voice note is sent as its **own message**, in order.
- The recording is saved as **audio/mp4** when the browser supports it, otherwise **audio/webm**. A recording is at least 1 second.
- The microphone button is disabled while recording or while a recorded clip is waiting.
- Errors: **"Microphone access denied."** with "Please allow microphone access in your browser settings."; **"No microphone found."** with "Please connect a microphone..."; or a general "Unable to access microphone" message.
- Voice notes in the chat have a **play/pause** button, a progress bar and the duration.

#### Replies (threads)

- Click **Reply** under a message. A reply box opens: "Write a reply... use @ to mention".
- A reply can have **text, @mentions, files and a voice note**, the same as a message, and **Cancel** / **Reply** buttons. **Enter** sends the reply.
- Replies are shown **indented under the message** they belong to, newest first inside the thread.
- **Replies are one level only**: you cannot reply to a reply, and the **Reply** button is not shown on a message that is still sending.

#### Reactions (emoji)

- Click the **smiley** under a message to open the emoji list. The emojis come from the system's list of **reaction types**.
- **One reaction per person per message.** Choosing the **same** emoji again **removes** your reaction; choosing a **different** emoji **replaces** your old one.
- Reactions are shown under the message with a count. Your own reaction has a blue outline. Click your own to remove it. Click someone else's reaction (or right-click any) to open **Reactions**: tabs per emoji with the people who reacted; in that list you can click your own emoji to remove it.
- **Reactions are added on the main messages.** Replies show the reactions they already have, but the smiley picker is only on the main message.
- You cannot react to a message that is still sending.

#### Delete

- You can delete **only your own** messages and replies.
- **Hover** over your message, click the small **arrow** that appears at its top right, and choose **Delete message**.
- Confirm in **"Delete message?"** — "This message will be deleted for everyone. This cannot be undone." — **Cancel** or **Delete**.
- There is **no edit** for a sent message, and nobody (not even a manager) can delete someone else's message.

#### Opening files from the chat

- Files appear as blue paperclip links with the file name. Click one to open it.
- PDFs, pictures, videos, audio and text files **open in a new browser tab**. Other file types (for example Word or Excel) are **downloaded**.
- If it cannot be opened: **"Unable to open file — Please try again."**
- Files shared in the discussion also appear in **Project Files**, under the **Discussion** source (section 6.7).

#### Message status ticks

Every message shows small ticks at its right:
- **One grey tick:** still **sending**.
- **Two grey ticks:** sent (**Delivered**).
- **Two blue ticks:** **Read**.
While a message is sending it appears at once (grey, no Reply button), then it is replaced by the saved copy.

If sending **fails**, the message disappears from the chat, your text and files come back into the composer, and a message **"Failed to send"** appears so you can try again.

#### Real-time updates and unread count

- New messages, replies, mentions and reactions from other people appear **instantly** (no refresh needed) while the project page is open.
- When someone sends a message with a **file or voice note**, you may first see **"Uploading attachment..."** in italics; it fills in automatically (the screen retries a few times over about 30 seconds).
- The **unread badge** comes from the project data and is refreshed about every 30 seconds and when messages arrive. When you **open** the drawer, all loaded messages are **marked as read**. When you **close** it, the counts refresh.

#### Long conversations

- The drawer loads **20 threads** at a time. It opens scrolled to the **newest** messages.
- Scroll **up** near the top to load **older** messages ("Loading older messages..."). When the oldest message is reached on a long discussion you see **"You've reached the start of this discussion"**.
- The header counts **threads** (top-level messages), not replies.

#### Quick answers

- **Can a Project Member write in Project Discussion?** Yes. Every team member can write, reply, react, attach files and send voice notes.
- **Can I mention everyone?** Yes: **@all**.
- **Can I edit a message?** No. You can only delete your own message.
- **Can I reply to a reply?** No; replies are one level under a message.
- **Can I send a voice note and text together?** Yes, in one message; extra voice notes become separate messages.
- **Where do shared files go?** They are listed in **View Files → Discussion**.
- **Do I need to refresh to see new messages?** No, they arrive live.

---

### 6.7 Project Files

**What it is:** A drawer listing every file in the project, newest first.

**How to access it:** Project Detail → **View Files**.

**Contents:**
- The file count.
- **Search files...**
- Source filter chips: **All**, **Brief**, **Task Submission**, **Discussion**, **Project Document**.
- Each file: icon, name, source badge, task (for submissions), uploader, date, size, and **View** / **Download**.
- Empty state: "No files found".

---

### 6.8 My Tasks

**Question this answers:** "What is My Tasks?", "How do I start a task?", "How do I submit my work?", "Can I drag tasks between columns?", "What can I do in each status?", "Why can't I edit a task that is Under Review?"

**What it is:** Every task assigned to **you**, across all projects. It is used by every ProjectHub user, including a **Project Member** and a **Project Lead**.

**How to access it:** Dashboard menu → **My Work → ProjectHub → My Tasks** (`/mytasks`). Subtitle: "View, manage, and track all tasks assigned to you across your projects".

#### Page layout

- **KPI cards:** **Open Tasks**, **Due Today**, **Due This Week**, **Overdue Tasks**.
- **Search:** "Search tasks..." (searches as you type, after a short pause).
- **Filters** button (a number badge shows how many filters are active). **Filter Tasks** drawer ("Apply filters to narrow down your task list"):
  - **Project** (any project you have tasks in), **Priority** (the company's Priority Labels), **Status** (To Do, In Progress, Under Review, Completed), **Due Date** (Due Today, Due This Week, Overdue).
  - The drawer closes automatically after each choice. Buttons: **Clear All**, **Close**.
- **View switch:** **Board** (default, grid icon) or **List** (list icon).
- **Empty states:** "No Tasks Assigned — You're all caught up! New tasks assigned to you will appear here." or, when a search or filter finds nothing, "No Tasks Found" with **Clear Filters**.

#### The task status flow

Every task moves through the statuses **one step at a time**:

```
To Do  →  In Progress  →  Under Review  →  Completed
```

| Status | Who moves it | How |
|---|---|---|
| **To Do → In Progress** | The assignee (you) | **Start Task** in the task drawer, or drag the card to the In Progress column |
| **In Progress → Under Review** | The assignee | **Submit for Review** in the task drawer (after you add your work) |
| **Under Review → Completed** | The reviewer (Project Lead, Team Lead, Department Admin or Super Admin) | **Approve** (with a comment) |
| **Under Review → To Do** (sent back) | The reviewer | **Revert with Feedback**. The task returns to **To Do** marked **Revision Requested**, with the reviewer's feedback |

**A task cannot jump from To Do straight to Under Review or Completed, and it cannot go from Under Review straight to Completed by you.** Each step has to be done in order. A Project Member or Project Lead working on their own tasks can **not** approve their own task from My Tasks: the **Approve** and **Revert** buttons are not shown there.

#### Board view

Four columns with a task count each: **To Do**, **In Progress**, **Under Review**, **Completed**.

Each card shows: task name, project name, **priority** badge, a **review stage** badge (only in Under Review, for example "Awaiting Project Lead Review"), a **progress** bar, the **due date** (red if overdue, amber if due today), and attachment and comment counts when there are any. **Click a card** to open the task drawer.

**Drag and drop (Board view):**
- **To Do → In Progress** — drag the card to In Progress. This starts the task, the same as **Start Task**.
- **In Progress → To Do** — also allowed (puts the task back).
- **In Progress → Under Review** — the board also allows this drag, but the proper way is **Submit for Review** in the drawer, which sends your files, links and notes with it.
- **Under Review** and **Completed** cards **cannot be dragged** from My Tasks.
- Any other move shows the message **"This transition is not allowed."** (for example To Do → Under Review, To Do → Completed, or In Progress → Completed). Dropping a card in its own column does nothing.
- After a successful drag a message shows "Task status updated successfully" (or the server's message) and the list refreshes.

#### List view

Columns: **Task**, **Project**, **Priority**, **Status**, **Review Stage**, **Due Date**, **Progress**, **Last Updated**, and a **View** button. Clicking a row (or **View**) opens the task drawer. There is **no drag and drop** in list view.

#### The Task Detail drawer (click a task)

A side drawer opens for the task. It has three parts:

1. **Header:** task name; **status** badge (To Do, In Progress, Under Review, Completed); a red **Revision Requested** badge if the reviewer sent it back; **priority**; **Due:** date; the **project name** (click it to open the project; from My Tasks it opens the project in Project Member view); the **milestone**; and a **progress** bar.
2. **Task Overview:** **Description**, **Dependencies** (tasks that must finish first), **Estimated Hours**, **Start Date**, **Due Date**, **Assigned By**.
3. **Work Submission** area and a **bottom action bar** that **change with the task's status**:

| Status | Work Submission area | Bottom buttons (your own tasks in My Tasks) |
|---|---|---|
| **To Do** | "Click **Start Task** below to begin working on this task." If the task was sent back (**Revision Requested**), it also shows the reviewer's feedback (**Reviewer**, **Reviewer Comments**) and your last submission, and says "Click Start Task below to begin, then submit your revised work." | **Start Task** — moves the task to **In Progress** |
| **In Progress** | The **submission form** (see below). You can work and submit here. | **Save Draft** and **Submit for Review**. **Submit for Review** stays disabled until you add at least one file, one working URL or some notes. |
| **Under Review** | **Read only.** "This submission is currently awaiting review. No edits allowed." Shows who submitted, the date, the notes, the files and the working URLs. | **No buttons.** You can only view. |
| **Completed** | **Read only.** "✅ Submission Approved". Shows **Approved By**, approval date, notes, files. | "Read-only view — no actions available" |

**The submission form (In Progress only):**
- **Upload Files** — any file type; you can add a label for each file.
- **Working URL(s)** — a **Label** and a link (https://…); **Add another URL** adds more rows.
- **Submission Notes** — free text.
- **Save Draft** keeps what you typed without sending it for review ("Draft saved successfully").
- **Submit for Review** sends the work to the reviewer ("Work submitted for review successfully"). The task moves to **Under Review** and the form becomes read only.

**Other things in the drawer**
- **Submission history:** when a task has submissions the drawer shows "N submissions available · **View history**". **Submission History** lists each version with its status (Approved, Rejected, Awaiting … Review), date, submitter, files, URLs, notes, reviewer and comment.
- **Unsaved Changes:** if you close the drawer while the submission form has content, a dialog warns "You have unsaved work in the submission form" with **Keep Editing** or **Discard & Close**.
- **Revision loop:** if the reviewer clicks **Revert with Feedback**, your task goes back to **To Do** with **Revision Requested** and the feedback. Click **Start Task** again, fix the work, and **Submit for Review** again.

**Short rules for a Project Member and a Project Lead in My Tasks**
- **To Do:** you can **start** it (button or drag). Nothing else.
- **In Progress:** you can **save a draft** and **submit for review**.
- **Under Review:** **view only**. Wait for the reviewer.
- **Completed:** **view only**.
- You never see **Approve**, **Revert with Feedback**, **Reassign Task** or **Edit Task** in My Tasks. Managers use those in **Team Tasks** (section 6.9) or in Project Detail.

---

### 6.9 Team Tasks

**Question this answers:** "What is Team Tasks?", "Who can see Team Tasks?", "What can a Team Lead do with a team member's task?", "How do I approve or revert a task?", "How do I reassign or edit a task?", "What filters does Team Tasks have?"

**What it is:** A page where a **Team Lead** supervises the tasks of the people in their team, across all of the team's projects.

**Who sees it:** **Only a Team Lead (role ID 16).** It is not shown to Department Admins, Super Admins, Project Leads or Project Members.

**How to access it:** **Manage My Team → ProjectHub → Team Tasks** (`/teamtasks`). Subtitle: "Monitor, manage, and supervise task execution across your team".

Team Tasks looks like My Tasks (section 6.8) with the same KPI cards, board and list views and task drawer, but it shows **your team's tasks** and gives you **manager actions**.

#### Page layout

- **KPI cards:** **Open Tasks**, **Due Today**, **Due This Week**, **Overdue Tasks** (for the team).
- **Search:** "Search team tasks..." (searches as you type, after a short pause).
- **Filters** button (a number badge shows how many filters are active). **Filter Team Tasks** drawer ("Apply filters to narrow down your team's task list"):

| Filter | Options |
|---|---|
| **Team Member** | All Members, or one person from your team |
| **Project** | All Projects, or one of your team's projects |
| **Project Lead** | All Project Leads, or one Project Lead |
| **Priority** | All Priorities, or one of the company's Priority Labels (Low, Medium, High, Critical and any you added) |
| **Status** | All Status, To Do, In Progress, Under Review, Completed |
| **Due Date** | All Dates, Due Today, Due This Week, Overdue |
| **Revision Requested** | All Tasks, Revision Requested, No Revision |
| **Overdue** | All Tasks, Overdue Only, Not Overdue |

  Buttons: **Clear All** (resets every filter and the search) and **Apply Filters** / **Close**. A filter takes effect as soon as you choose it, and the drawer closes after each choice. All filters and the search combine.
- **View switch:** **Board** (default) or **List** (same as My Tasks).
- **Empty states:** "No Tasks Found" with **Clear Filters** when a search or filter finds nothing.

#### Board and list

The **Board** has four columns: **To Do**, **In Progress**, **Under Review**, **Completed**. The **List** has the columns Task, Project, Priority, Status, Review Stage, Due Date, Progress, Last Updated and **View**. **Click a task** (card or row) to open the **Task Detail drawer**. Cards can be dragged between To Do and In Progress, and from In Progress to Under Review or back to To Do; Under Review and Completed cards cannot be dragged (same rules as My Tasks, section 6.8).

#### The Task Detail drawer in Team Tasks (what a Team Lead can do, by status)

| Task status | What the drawer shows | Team Lead buttons |
|---|---|---|
| **To Do** | Task details; "Click Start Task…" area is shown read only (a Team Lead does not do the member's work) | **Reassign Task** and **Edit Task** |
| **In Progress** | The assignee's work area is **read only**: "This task is currently in progress. The assignee will submit their work for review when ready." Shows any draft submission details | **Reassign Task** and **Edit Task** |
| **Under Review** | The submission to review: who submitted, date, notes, files, working URLs, and submission history | **Revert with Feedback** and **Approve** |
| **Completed** | The approved submission ("✅ Submission Approved": Approved By, date, notes, files) | **Read only** — "Read-only view — no actions available" |

**Approve (Under Review)**
1. Click **Approve**. The dialog **Approve Task** opens.
2. Enter the **Approval Comment \*** (required).
3. Click **Confirm Approval**. The task becomes **Completed** ("Task approved successfully").

**Revert with Feedback (Under Review)**
1. Click **Revert with Feedback**. The dialog **Revert with Feedback** opens.
2. Enter the **Feedback Comment \*** (required).
3. Click **Revert Task**. The task goes back to the assignee marked **Revision Requested**, with your feedback ("Task reverted with feedback"). The assignee starts it again and resubmits. You can then find these tasks with the **Revision Requested** filter.

**Reassign Task (To Do or In Progress)**
1. Click **Reassign Task**. The dialog **Reassign Task** opens ("Select a new team member for this task."). If the task has no assignee it is titled **Assign Task**.
2. **Current Assignee** shows who has it now.
3. In **Reassign To \*** open the list (search "Search member..."), choose the new person from the project and department members, and click **Reassign**.
4. *Current version note:* confirming currently shows the message **"Reassign functionality coming soon"**, so the change of assignee is **not saved yet** (the dialog and the member list work).

**Edit Task (To Do or In Progress)**
1. Click **Edit Task**. The **Edit Task** dialog opens.
2. You can change: **Task Name \*** (required), **Description**, **Milestone**, **Priority**, **Assigned To** (the person doing the task), **Start Date** and **End Date**, **Estimated Time** (hours or days), and **Dependencies** (tasks that must finish first).
3. Save. The task is updated ("Task updated successfully").

**Other things**
- The **project name** in the drawer header opens the project in **Team Lead view**; the back button returns you to Team Tasks.
- **Change due date** is not available yet ("Change due date functionality coming soon").
- A Team Lead does **not** submit work in Team Tasks. Submitting work happens in **My Tasks** for tasks assigned to the Team Lead personally.

**Short rules for a Team Lead in Team Tasks**
- **To Do / In Progress:** **Reassign Task** and **Edit Task**.
- **Under Review:** **Approve** (comment required) or **Revert with Feedback** (comment required).
- **Completed:** view only.

---

### 6.10 Import Projects (ProjectHub Setup Assistant)

**Question this answers:** "How do I import my existing projects?", "How do I import projects from a file?", "Can I upload a spreadsheet?", "Can I import from Trello?", "What are mapped and unmapped people?", "What happens if I click Import Projects?", "What does 'No, I'll do it manually' do?"

**What it is:** A guided assistant, led by **Alci** (with short videos), that brings existing projects, tasks and team members into ProjectHub. It opens as a pop-up window titled **Welcome to ProjectHub**.

> **Current version: you can import from a spreadsheet (XLSX or CSV) or from Trello.** File upload is the bulk-file path. Trello is available on the Welcome screen. monday.com, ClickUp, Asana, Atlassian / Jira and Notion are greyed out (**Coming soon**).

**Users who want to move existing project data into Synclo from a file or from Trello should use Import Projects.**

**How to open it**
- **ProjectHub Setup** page (Manage Company → Setup & Configurations → Modular Configurations → ProjectHub Setup) → **Import Projects** button (top right).
- **AllProjects** page → **Import Projects** button (header, and in the empty state).
- It also opens **automatically every time the ProjectHub Setup page loads** in the current version (the source marks this as a "Testing" behaviour).

#### Step 1 — Welcome ("How would you like to bring in your data?")

Alci says: "Hi! I'm Alci. I'll help you set up ProjectHub. Choose how you'd like to bring in your data — import from an existing tool, upload a spreadsheet, or set things up manually."

| Option | What it is | What happens when you click it |
|---|---|---|
| **Upload a spreadsheet** (under "Or you can bulk upload a file") | **XLSX or CSV** with projects and tasks. **This is the file-import path.** | Opens **Upload Project Data** (File path, Step 2). |
| **Trello** ("Import boards, tasks, and members.") | Migrate data from Trello. | Opens the **Connect Trello** window (Trello path). |
| **monday.com**, **ClickUp**, **Asana**, **Atlassian / Jira**, **Notion** | Other tools | Greyed out, **Coming soon**. They cannot be clicked. |
| **No, I'll do it manually** (bottom of the window) | Skip the import | See below. |

The **X** button (top right of the window) closes the assistant at any time.

#### What happens if you click "No, I'll do it manually"

- The assistant window **closes**. **Nothing is imported** and no data is created or changed.
- You stay on the same page (ProjectHub Setup or AllProjects).
- You then create your data yourself: Super Admin → **Manage Company → Business Operations → ProjectHub → Projects → Create New Project** (or use a Project Template). Categories, Priority Labels, roles and templates are set up in **ProjectHub Setup** (section 6.11).
- On the ProjectHub Setup page the assistant opens again the next time the page loads. You can also reopen it yourself with **Import Projects**.

---

### File path — import from an XLSX or CSV file

**Use this when the question is "how do I import projects from a file?" or "how do I upload a spreadsheet?"**

#### File Step 2 — Upload Project Data

1. On Welcome, click **Upload a spreadsheet** ("XLSX or CSV · projects and tasks").
2. The **Upload Project Data** screen opens. Alci says: "Upload an XLSX or CSV file with your projects and tasks. I'll analyze it and map everything into ProjectHub."
3. Drag and drop the file, or click the dashed box to browse. Only **.xlsx** and **.csv** are accepted.
4. When a file is selected, its name is shown and you can click again to replace it.
5. Click **Analyze File** (disabled until a file is chosen). **Back** returns to Welcome.

#### File Step 3 — Analyzing your file

The screen **Analyzing your file** runs while Alci reads the spreadsheet. Progress steps:

1. Analyzing uploaded data… → File analyzed
2. Identifying projects… → N project(s) found
3. Identifying tasks… → N task(s) found
4. Matching employees… → N of M person/people matched
5. Validating information… → Information validated (or N validation issue(s) found)

If analysis **fails**, an error toast is shown and you are returned to **Upload Project Data** so you can pick another file.

#### File Step 4 — Review ("Your data is ready"): mapped and unmapped people

Alci tells you: "A few people from your file couldn't be matched automatically. Map them to your Synclo employees so their tasks stay assigned, then complete the import."

The heading is **Your data is ready**. Summary cards show what was found: **Projects**, **Tasks**, **People**, **Files**.

**How people are matched.** ProjectHub compares names in the file with your Synclo employees:

| Group | Meaning | What you do |
|---|---|---|
| **Mapped (matched) people** | The system found the matching Synclo employee automatically. | Nothing. Their tasks are assigned to that employee. They are not listed on the screen. |
| **Unmapped (unmatched) people** | No Synclo employee could be matched automatically. | Choose a Synclo employee for each, or leave them unmapped. They are listed under **Needs Your Attention**. Unmapped people are listed **once** even if they appear in more than one project. |

**Needs Your Attention** ("N people couldn't be matched to employees in Synclo. X resolved · Unmapped users' tasks will remain unassigned."). Each unmatched person appears **once** as a card (name, and if available email or role and project count):

- **Who is <name> in Synclo?** → opens a searchable employee list ("Search employee…", shows department and designation). Click an employee. The card turns **green: "Mapped to <employee name>"**.
- **Do Not Map This User** (at the bottom of the list) → the card turns **amber: "Do not map — tasks stay unassigned"**. That person's tasks are imported without an assignee.
- **Change** → undoes your choice for that person.

**Import Now**
- If **everyone is resolved**, the data is imported at once (projects, milestones, tasks and team links are created in ProjectHub).
- If **some people are still unmapped**, a **Pending Resolution** dialog appears: "N people are still unmapped. Their tasks will remain unassigned in ProjectHub. Do you want to continue without resolving?" Choose **Go Back** (to map them) or **Continue Without Resolving** (import anyway).
- The button shows **Importing...** while saving. If saving fails, an **Error** message is shown and you can try again.

The import does **not** create new employees. It only links names from the file to **existing** Synclo employees.

#### File Step 5 — Creating your ProjectHub workspace

A short progress screen: **Creating your projects → Setting up milestones and tasks → Linking employees → Finalizing ProjectHub**.

#### File Step 6 — "ProjectHub is ready"

Shows three counters: **Projects Imported**, **Tasks Created**, **Team Members Mapped**. Click **View All Projects** to open the imported projects in AllProjects (the list is refreshed; from ProjectHub Setup it opens `/allprojects?view=superadmin`; from AllProjects it keeps the view you were on).

---

### Trello path — import from Trello

#### Trello Step 2 — Connect Trello

1. Click **Trello**. The **Connect Trello** window opens ("Trello Sign In — Sign in to your Trello account").
2. Click **Continue to Trello**. A **pop-up browser window** (about 600 × 700 px) opens on the Trello / Atlassian sign-in page. The Connect Trello window shows **Authorizing ProjectHub… Complete authorization in the popup window.** (Allow pop-ups in your browser, or the window will not open.)
3. In the pop-up, sign in to Trello and click **Allow** to give ProjectHub **read** access to your boards and projects, tasks and assignments, due dates and labels, and member information. ProjectHub never stores your Trello password ("Secure OAuth").
4. The window shows **Connected Successfully — Linked to <workspace name>** and moves on automatically after about 1.6 seconds. (If the Trello page returns to `/allprojects?trelloConnected=true&connectionId=...` instead, the assistant reopens on AllProjects and goes straight to the next step.)

Messages you may see: **Authorization cancelled. Please try again.** (you closed the pop-up before finishing), **Trello authorization failed. Please try again.**, **Failed to start Trello authorization.**

#### Trello Step 3 — Importing from Trello (sync)

ProjectHub starts a sync of your Trello data **on the server** and checks its progress every 3 seconds. The screen **Importing from Trello** shows these steps with a progress bar:

1. Connecting to your Trello workspace… → Workspace connected
2. Reading projects and boards… → Projects read
3. Importing tasks… → Tasks read
4. Matching team members… → Team members read
5. Validating your data… → Data validated

When the server reports **Completed**, the assistant moves to Review. If the sync **fails**, an error toast shows the server message (or "Trello sync failed. Please try again.") and the assistant goes back about 3 seconds later.

#### Trello Step 4 — Review ("Your Trello data is ready")

Same mapping controls as the file path (**Who is <name> in Synclo?**, **Do Not Map This User**, **Change**, **Import Now**, **Pending Resolution**). Summary cards show Trello boards, cards, members and attachments. Auto-matched Trello members are applied in the background; unmatched people are listed under **Needs Your Attention**. Then **Creating your ProjectHub workspace** and **"ProjectHub is ready"** work the same as the file path.

---

#### Quick answers

- **How do I import projects from a file?** **Import Projects** → **Upload a spreadsheet** → choose an **XLSX or CSV** file → **Analyze File** → map unmatched people if asked → **Import Now** → **View All Projects**.
- **Which sources can I import from?** **Spreadsheet (XLSX/CSV)** and **Trello**. monday.com, ClickUp, Asana, Atlassian / Jira and Notion are "Coming soon".
- **What if I click "No, I'll do it manually"?** The assistant closes, nothing is imported, and you create projects yourself with **Create New Project**.
- **What is a mapped person?** A name from the file (or a Trello member) matched to a Synclo employee (automatically, or by you on the Review screen). Their tasks stay assigned to that employee.
- **What is an unmapped person?** A name with no matching Synclo employee. If you do not map them, their tasks are imported **unassigned**; assign them later on the project's Planning tab.
- **Does the import create employees?** No. It only links people to **existing** Synclo employees.
- **Can I close it halfway?** Yes, with **X**. Project data is created when you click **Import Now** on the Review step.
- **Why does the Trello window not open?** Your browser is blocking pop-ups. Allow pop-ups for the Synclo site and click **Continue to Trello** again.

---

### 6.11 ProjectHubSetup (Company Configuration)

> Full tab-by-tab guide to the **ProjectHub Setup** page. Written from `src/pages/ProjectManagementConfiguration.jsx` and the tab components in `src/components/project-config/`. Each part can be read on its own.

**What it is:** the company-level configuration page for ProjectHub. Heading **ProjectHub Setup**: "Define company-level standards, role permissions, templates, and retention policies". It has **five tabs** and an **Import Projects** button.

| # | Tab | One-line purpose |
|---|-----|------------------|
| 1 | **General Settings** | Priority Labels, Project Health Statuses (view only), cross-department collaboration rules |
| 2 | **Project Types & Categories** | Switch project types on or off, and create department Categories |
| 3 | **Roles & Permissions** | Give employees the Department Administrator or Team Lead ProjectHub role |
| 4 | **Project Templates** | Create company-wide, reusable project templates (milestones and tasks) |
| 5 | **Archive Rules** | Automatic archiving and restore rules |

#### How to open it (menu path)

Super Admin, ManageCompany sidebar:
1. Click **Manage Company** on your employee profile widget (or open `/managecompany`).
2. Open **Setup & Configurations**.
3. Click **Modular Configurations**.
4. Click **ProjectHub Setup** (`/projecthubsetup`).

Other ways in: ProjectHub Dashboard → **ProjectHub Setup** or **View Templates**; or the direct address `/projectmanagementconfiguration` (same page; non-Super Admins get Access Denied). It is **not** under Business Operations → ProjectHub.

#### Who can use it

**Only a Super Admin (role ID 1).** Everyone else sees **Access Denied — Only Company Admins can access Project Management Configuration.** with **Back to Dashboard**. Department Administrators use **ProjectHub Department Setup** (section 6.12) instead.

#### Page buttons

| Element | What it does |
|---|---|
| **Import Projects** (top right) | Opens the Setup Assistant (Alci). See "Import Projects" below. |
| **Tab bar** | Five tabs; the selected one is blue. |
| **Save Configuration** (bottom right) | Saves the **active tab only**. Hidden on Roles & Permissions. Shows "Saving...". Success toast shows the server message; failure shows "Failed to save configuration". |

#### How saving works (read this first)

**Save Configuration saves only the tab you are on.** Click it before you change tabs, or the change is lost.

| Tab | How changes are stored |
|---|---|
| 1. General Settings | **Save Configuration**. (Deleting a saved Priority Label is immediate.) |
| 2. Project Types & Categories | **Save Configuration**. (Deleting a Category is immediate.) The in-card **Save Changes** buttons only keep the change on the page. |
| 3. Roles & Permissions | Instant on **Add User** / **Save Role**. No Save Configuration. |
| 4. Project Templates | Saved by the Template Wizard. Delete is immediate. |
| 5. Archive Rules | **Save Configuration**. |

#### Tab 1 — General Settings

Purpose: company-wide standards used by every project, task and issue. Three cards.

**Priority Labels** — "Company-wide priority levels used for projects and tasks across all departments."

Add: **Add Priority Label** → dialog fields:

| Field | Required? | Details |
|---|---|---|
| **Name** | **Required** | e.g. "High Priority". Button disabled until entered. |
| **Description** | Optional | "Optional description". |
| **Color** | Optional (default blue `#3B82F6`) | Colour picker with a live **Preview** badge. |

Click **Add Priority Label**, then **Save Configuration** (a new label is stored only after that). Edit: pencil → **Save Changes** → Save Configuration. Delete: trash icon; an unsaved new label is removed at once; a saved label asks "Delete Priority Label" and is deleted **immediately**. **Low, Medium, High, Critical** show a **Default** badge: editable, **not deletable**. Priority Labels are used for the Priority of projects, tasks and issues, and in the Template Wizard task dialog.

**Project Health Statuses** — "Default health indicators used throughout dashboards and reporting." **View only** (e.g. On Track, At Risk, Off Track). No add, edit or delete.

**Cross-Department Collaboration Rules** — "Control how departments collaborate on projects." Two switches, **both default Off**; click **Save Configuration** after changing.

| Switch | If ON | If OFF |
|---|---|---|
| **Allow members from other departments** ("Team members can be assigned to projects outside their department") | People from other departments can be assigned to a project. | Members stay within the project's own department. |
| **Require Department Administrator approval for cross-department collaboration** ("Department Administrators must approve cross-department assignments") | Cross-department assignments need Department Administrator approval. | No approval step. |

The page only saves these (`allowCrossDepartment`, `requireDepartmentAdministratorApproval`); the assignment checks run on the server.

#### Tab 2 — Project Types & Categories

Purpose: classify projects. Two cards. Store changes with **Save Configuration**.

**Global Project Types** — "Company-wide project types available to all departments." Built in (e.g. **Internal**, **Client**-facing types). **You cannot add or delete types; you can only switch them on or off.** Each card shows an **Active** or **Inactive** badge; click the pencil to edit.

**Normal type (e.g. Internal):** inline editor with one switch.

| Control | If ON | If OFF |
|---|---|---|
| **Active** | Type is available. | Type is hidden where users pick a project type (e.g. the type filter on AllProjects). Existing projects are not deleted. |

Click **Save Changes**, then **Save Configuration**.

**Client-facing type (name contains "Client"):** dialog **Edit <type>** ("Configure permissions for the client-facing project type") with two switches.

| Switch | If ON | If OFF |
|---|---|---|
| **Active / Inactive** ("Enable or disable this project type") | Type available; badge **Active**. | Type hidden from selection; badge **Inactive**. |
| **Require Client Brief Form** ("Client brief form templates can be set up separately") | Card shows **Brief Form Required**; client projects of this type need a brief form. | No brief form required. |

Click **Save Changes**, then **Save Configuration**.

**Department-Specific Categories** — "Categories assigned to one or more departments for targeted project classification."

Prerequisite: the company must already have **departments**. If there are none, **Applicable Departments** is empty.

Add: **Add New Category** → dialog:

| Field | Required? | Details |
|---|---|---|
| **Category Name** | **Required** | e.g. "Campaign". **Add Category** is disabled until entered. |
| **Description** | Optional | "Optional description". |
| **Applicable Departments** | Optional in the form, **recommended** | Searchable multi-select ("Search departments..."). Pick one or more. With none selected the card shows "No departments". |

Click **Add Category**, then **Save Configuration**. Cards show name, description, department badges and project count. Edit: pencil → **Save Changes** → Save Configuration. Delete: trash icon → "Delete Category", runs **immediately**, and is **blocked when projects use the category** ("Cannot delete this category... Please reassign or remove those projects before deleting."). Only the **Super Admin and the creator** can edit or delete; others see a lock ("No Edit Permission"). A Category is what a Template is linked to (wizard step 1, **Available For**), so create Categories **before** Templates.

#### Tab 3 — Roles & Permissions

Purpose: decide who gets a **ProjectHub role**. One sub-tab, **User Role Assignment**. The Permission Matrix is commented out in the code, so there are **no on/off switches** here. Super Admin always has every permission.

Roles assigned here: **Department Administrator** and **Team Lead**. Project Lead and Project Member are positions inside one project, not roles assigned here.

- **Stats cards** (click to filter): **Total Users**, **Dept Administrators**, **Team Leads**. A **Filtered by:** badge with ✕ clears the filter.
- **Employee Role Assignments** table: Employee (photo, name, code), Department (and designation), Assigned Role (badges or "No roles"), Status (Active), Actions (⋮). **Filter by role** dropdown. Pagination: 5, 10, 20 or 50 per page. Empty state: "No ProjectHub users found".
- **Add User** → **Add ProjectHub User**:

| Field | Required? | Details |
|---|---|---|
| **Select Employee \*** | **Required** | Type at least 2 characters (name, employee code or designation). Click a result; ✕ clears. "No employees found" if none. |
| **ProjectHub Role** | **Required** (at least one) | Toggle role buttons; you may pick more than one. |

Click **Add User**; it saves immediately ("User added successfully").
- ⋮ **Edit Role** → **Edit ProjectHub Roles** (employee name read only) → toggle roles → **Save Role** ("Role updated successfully"), immediate.

#### Tab 4 — Project Templates

Purpose: create **Organization Wide Templates** ("General project management templates to use across the organization"): reusable milestones and tasks, with no clients, dates, team members or budgets. Same list as the **Project Templates** page (`/projecttemplates`).

On the tab: search box ("Search templates by name or description..."), **Create Template**, and template cards showing name, **Draft** or **Active**, **In Use**, **System Default**, category, milestone and task counts, timeline, projects created, last updated, created by. ⋮ menu: **Edit**, **Delete** (**Delete (Locked)** when projects use it). Only the **Super Admin or creator** can edit or delete (others see a lock). Empty state: **Create Your First Template**. No switches; Save Configuration is not used.

Prerequisites: departments exist, and an **active Category** exists (otherwise **Available For** shows "No categories found").

**Template Wizard** (**Create Project Template** / **Edit Project Template**), 4 steps, footer "Step N of 4":

| Step | Required to go on | Optional |
|---|---|---|
| **1. Basic Info** | **Template Name \*** | **Description**; **Available For** (one active Category; empty = not tied to a Category) |
| **2. Milestones** | **At least one milestone** with a name. Days default 5, minimum 1. | Milestone description; drag to reorder |
| **3. Tasks** | **Task Name \*** for each task you add. Adding tasks is **not enforced** (you can click Next with none). | Task Description; **Priority** (default Medium, from your Priority Labels); **Estimated Time** (Hours or Days, 1 day = 8 hours); **Task Dependencies** (only tasks above the current task) |
| **4. Review & Create** | Template name and at least one milestone | Nothing to fill; shows Milestones, Total Tasks, Est. Timeline, Est. Hours, Name, Description, Category |

Footer buttons: **Previous**; **Save Draft** (new templates only); **Next**; on step 4 **Create Template** / **Update Template**. Created = **Active**; Save Draft = **Draft**.

- **Step 2:** type name, days and optional description, then **Add** (or Enter). Edit inline, drag to reorder, delete with the trash icon (confirmation; also removes its tasks). Total duration is shown.
- **Step 3:** tasks live inside milestones (**Add Task**). Edit, duplicate, delete, drag between milestones; **Expand All / Collapse All**; rename a milestone. A warning appears if a task estimate is longer than its milestone.
- **Warnings:** **Leave without saving?** (**Save Draft** or **Close without saving**); **Cyclic Dependency Detected** (blocks, **Go Back & Fix**); **Task Dependencies Detected** (new templates only: dependencies are **not saved**; choose **Go Back & Remove Dependencies** or **Proceed Anyway**; add them later by editing).

Required vs optional: Required = Template Name, at least one named milestone, a Task Name per task added. Everything else is optional.

#### Tab 5 — Archive Rules

Purpose: when projects are archived and who may restore them. Save with **Save Configuration**. Archiving moves a project to **Archived Projects**; it does not delete it. **The complete explanation of every option, examples and the permission table is in section 10.** Summary:

| # | Item | Control | Default |
|---|---|---|---|
| 1 | **Enable automatic archival** | Switch | Off |
| 2 | **Archive completed projects** (only if 1 is On) | **Immediately** or **After X days** (default 30, min 1) | Immediately |
| 3 | **Archive inactive projects after X days** (only if 1 is On) | Number, min 1 | 60 |
| 4 | **Allow archived project restoration** | Switch | Off |
| 5 | **Allow Department Administrators to restore archived projects** | Switch | Off |
| 6 | **Require Super Admin approval for permanent deletion** | Switch, **Always On**, locked | On |

Item 4 OFF: nobody can archive or restore from AllProjects, and **View Archived Projects** is hidden. Item 5 ON (with 4 ON): Department Administrators can restore in their department. Draft projects are never archived automatically.

#### Import Projects (Setup Assistant)

**Import Projects** (top right) opens the **ProjectHub Setup Assistant** (Alci). In the current version you can **upload an XLSX or CSV spreadsheet**, import from **Trello**, or click **No, I'll do it manually** to close it without importing. The complete step-by-step guide, including mapped and unmapped people, is in **section 6.10**. (The assistant also opens automatically on every page load of this page; the source marks this as "Testing".)

#### Recommended setup order

1. General Settings: review Priority Labels; set the two cross-department switches.
2. Project Types & Categories: set types Active or Inactive; create Categories linked to departments; **Save Configuration**.
3. Roles & Permissions: add Department Administrators and Team Leads.
4. Project Templates: create templates (after Categories).
5. Archive Rules: choose archival and restore rules; **Save Configuration**.
6. Optional: **Import Projects**.
7. Department Administrators finish **ProjectHub Department Setup**.

#### ProjectHub Setup quick answers

- **Where do I add a Priority Label?** Tab 1 → Priority Labels → **Add Priority Label** → Save Configuration.
- **Where do I create a Category?** Tab 2 → Department-Specific Categories → **Add New Category** → Save Configuration.
- **Why can't I choose a Category in a Template?** No active Category exists; create one in Tab 2.
- **Where do I make someone Team Lead or Department Administrator?** Tab 3 → **Add User** or ⋮ → **Edit Role**.
- **Where do I turn off a project type?** Tab 2 → Global Project Types → pencil → Active off → Save Changes → Save Configuration.
- **Where do I turn on automatic archiving?** Tab 5 → **Enable automatic archival** → Save Configuration.
- **Where do I allow other departments on projects?** Tab 1 → **Allow members from other departments**.
- **Why did my change disappear?** You switched tab without **Save Configuration**.
- **Can I delete Low, Medium, High, Critical?** No (editable only). **A Category with projects?** No. **A used Template?** No (**Delete (Locked)**).

#### Not shown in the current version

Commented out in the code and **not** on the page; do not describe it to users: the **Permission Matrix** sub-tab in Roles & Permissions.

#### Developer reference

Page `src/pages/ProjectManagementConfiguration.jsx` (routes `/projecthubsetup`, `/projectmanagementconfiguration`). Each saving tab exposes `save()` via a ref; `handleSave` calls the active tab's ref. API base `/api/projecthub` (`src/api/projectHubConfigurationApi.js`):

| Tab | Components | Endpoints |
|---|---|---|
| General Settings | `GeneralSettingsTab.jsx`, `PriorityLabelsSection.jsx` | GET `/ProjectGeneralSettings`; POST `/ProjectGeneralSettings/save`; POST `/ProjectGeneralSettings/priority-label` (delete) |
| Project Types & Categories | `ProjectTypesCategoriesTab.jsx` | GET `/projecttypescategories`; POST `.../save`; POST `.../delete-category`; departments `/api/company-onboarding/department` |
| Roles & Permissions | `RolePermissionsTab.jsx`, `UserRoleAssignmentTab.jsx` | GET/POST `/ProjectHubUser`; POST `/ProjectHubUser/update` |
| Project Templates | `ProjectTemplatesTab.jsx`, `template-wizard/*` | GET/POST `/ProjectTemplate`; `get-template-by-Id`; `delete-template`, `delete-template-milestone`, `delete-template-task` |
| Archive Rules | `ArchiveRetentionTab.jsx` | GET `/ProjectArchiveRules/get-all-archive-rules`; POST `/ProjectArchiveRules/update-archive-rule` |

Archive payload: `enableAutomaticArchival`, `archiveCompletedProjectsTypeId` (1 = Immediately, 2 = After X days), `archiveProjectsAfterDays` (0 when Immediately), `archiveInActiveProjectsAfterDays`, `allowArchivedProjectRestoration`, `allowDepartmentAdministratorsToRestore`, `requireSuperAdminApprovalForPermanentDeletion` (always `true`).

---

### 6.12 ProjectHub Department Setup

**Question this answers:** "How do I set up my department in ProjectHub?", "Where is Department Setup?", "What tabs does Department Setup have?", "How do I create a Team Lead?", "How do I create a Category for my department?", "How do I create a Template for my department?"

**What it is:** **ProjectHub Department Setup** is the department-level setup page. Heading: "ProjectHub Department Setup — Configure ProjectHub settings scoped to the <department> department". It is the Department Administrator's version of ProjectHub Setup: the same kind of settings, but only for **their own department**.

**Who can use it:** the **Super Admin** and anyone who has the **Department Administrator** role. Team Leads, Project Leads, Project Members and normal employees do not get this page.

> **Department Setup versus ProjectHub Setup:** **ProjectHub Setup** (section 6.11) is company-wide and only the Super Admin can use it. **Department Setup** is for one department and is used by the Department Administrator. A Department Administrator does **not** use ProjectHub Setup.

#### How to open it (Department Administrator)

A user's **My Work → ProjectHub** menu depends on their role:

| Role | What the user sees under **My Work → ProjectHub** |
|---|---|
| **Normal employee** (also Project Lead and Project Member) | Only **My Projects** and **My Tasks** |
| **Department Administrator** | **My Projects**, **My Tasks**, plus **Department Projects**, **ProjectHub Dashboard** and **Department Setup** (the sidebar label may read "Departmnet Setup") |

```
Dashboard sidebar (Department Administrator)
└── My Work
    └── ProjectHub
        ├── My Projects            → /allprojects
        ├── My Tasks               → /mytasks
        ├── Department Projects    → /allprojects?view=departmentadmin
        ├── ProjectHub Dashboard   → /department-projects-dashboard
        └── Department Setup       → /projecthub-departmentsetup
```

**So if a Department Administrator asks "How do I set up my department?"** the answer is: open **My Work → ProjectHub → Department Setup** (`/projecthub-departmentsetup`). If you do **not** see **Department Setup** in that menu, you do not have the Department Administrator role: ask your Super Admin to assign it (ProjectHub Setup → Roles & Permissions, section 6.11).

Other ways in: the **ProjectHub Dashboard** (Department Projects Dashboard) Quick Actions **View Templates**, **Department Configuration** and **Assign Roles** all open Department Setup; for the Super Admin, ProjectHub Dashboard → **Department Setup**.

#### Tabs

Department Setup has **three tabs**. There is **no Save Configuration button**: each tab saves its own changes at once.

| # | Tab | What it is for |
|---|-----|----------------|
| 1 | **User Roles** | Mark which people in your department are **Team Leads** |
| 2 | **Project Categories** | Create the Categories your department uses for its projects |
| 3 | **Project Templates** | Create reusable project templates for your department |

#### Tab 1 — User Roles (mark Team Leads)

**Purpose:** decide who is a **Team Lead**. **Marking Team Leads here is required** so that projects can be assigned to Team Leads and appear on their Team Lead views.

- Stats cards (click to filter): **Total Users** and **Team Leads**.
- **Employee Role Assignments** table: Employee (name and code), Department (and designation), Assigned Role (for example **Team Lead** or **Department Administrator**), Status, Actions (⋮). **Filter by role** dropdown. Pagination: 5, 10, 20 or 50 per page.
- **Only the Team Lead role can be assigned** on this page. The Department Administrator and Super Admin roles are not assignable here (the Super Admin assigns Department Administrators in ProjectHub Setup).

**To mark someone as Team Lead:**
1. Click **Add User** (the screen may also label it **Assign Role**).
2. **Select Employee \*** — type at least **2 characters** (name, employee code or designation) and click the person. The search covers the whole employee directory.
3. **ProjectHub Role \*** — choose **Team Lead**. At least one role must be selected; otherwise nothing is saved.
4. Click **Add User**. The person is added immediately ("User added successfully").

**To change or remove the Team Lead role:** on the employee's row click ⋮ → **Edit Role** → toggle **Team Lead** → **Save Role** ("Role updated successfully").

#### Tab 2 — Project Categories

**Purpose:** "Department Project Categories — Manage project categories for your department." A **Category** classifies your department's projects (for example "Campaign"). Create Categories **before** Templates, because a Template is linked to a Category.

**Create a Category:** click **Create Category** → dialog **Create Category**:

| Field | Required? | Details |
|---|---|---|
| **Category Name \*** | **Required** | Placeholder "e.g., Campaign". The **Create** button stays disabled until a name is entered. |
| **Description** | Optional | "Brief description of this category..." |

> **No department selection here.** Unlike the Super Admin's Category form in ProjectHub Setup (which has **Applicable Departments**), the Department Setup form has only **Category Name** and **Description**. You do **not** pick a department, because the Category belongs to the Department Setup you are working in and is shown for your department.

Click **Create**. The Category is saved at once ("Category created successfully") and is shown in the list.

**The Category list**
- **Grid** or **table** view (toggle with the two icons).
- Each Category shows its **name**, **description**, **Active Projects** (number of projects) and a **status** (**Active** or **Archived**). The table view has columns Category Name, Description, Active Projects, Status, Actions.
- ⋮ menu (or action buttons in table view):
  - **Edit** — change name and description (**Save Changes**).
  - **Archive** — hides the Category from active use. An archived Category appears faded with the status **Archived**.
  - **Restore** — shown for archived Categories; makes the Category **Active** again.
  - **Delete** — asks "Are you sure you want to delete the category...? This action cannot be undone." If the Category has projects, a red warning says "This category has N active project(s)". The server may refuse to delete a Category that is in use.
- **Who can edit, archive or delete a Category:** the **Super Admin** and the **person who created it**. Everyone else sees a lock icon ("No Edit Permission").
- Empty state: "No categories yet".

#### Tab 3 — Project Templates

**Purpose:** "Department Templates" — department-specific templates tailored to your department's workflows. Same engine as the company Template tab (section 6.13).

- **Search templates by name or description...** box.
- **Create Template** button → opens the **Template Wizard** (Basic Info → Milestones → Tasks → Review & Create). See section 6.13 for every step and which fields are required (**Template Name \***, at least one milestone with a name, and a **Task Name \*** per task you add; everything else is optional).
- **Grid** or **table** view toggle.
- Template cards show Draft or Active, category, milestones, tasks and timeline. ⋮ menu: **Edit**, **Delete** (**Delete (Locked)** if projects already use it).
- Only the **creator or a Super Admin** can edit or delete a template; others see a lock.
- In step 1 of the wizard, **Available For** lists the Categories — create your Category (Tab 2) first.

#### Recommended order for a Department Administrator

1. **User Roles:** mark your **Team Leads**.
2. **Project Categories:** create your department's Categories.
3. **Project Templates:** create templates linked to those Categories.
4. Then create and run projects from **Department Projects** (`/allprojects?view=departmentadmin`).

#### Department Setup quick answers

- **Where do I set up my department?** My Work → ProjectHub → Department Setup.
- **I don't see Department Setup.** You are not a Department Administrator. Only the Super Admin can give you that role.
- **What tabs are there?** User Roles, Project Categories, Project Templates.
- **Is it required to mark Team Leads?** Yes. Do it in the **User Roles** tab so Team Leads can own and see projects.
- **Do I choose a department when I create a Category?** No. Only Category Name (required) and Description (optional).
- **Do I need Save Configuration?** No. Each action saves immediately.
- **What does a normal employee see in the ProjectHub menu?** Only My Projects and My Tasks.

---

### 6.13 Project Templates and the Template Wizard

**Where templates are managed:**
- ProjectHubSetup → Project Templates ("Organization Wide Templates").
- Department Setup → Project Templates ("Department Templates").
- The **Project Templates** page (**Manage Company → Business Operations → ProjectHub → Project Templates**, `/projecttemplates`, Super Admin only): "Create and manage reusable project templates", with **New Template**.

**Where templates are used:** ProjectCreate → Step 1 → **Create from Project Template**.

**Template card:**
- Name and badges: **System Default** (built in), **In Use** (used by projects), **Draft** / **Active**.
- Category.
- Milestones, Tasks, and Timeline (days).
- Projects created, Last updated, and Created by (or Updated by for system defaults).

**Card actions:**
- ⋮ menu: **Edit**, **Delete**. In-use templates show **Delete (Locked)**.
- Only the creator or a Super Admin can edit or delete; others see a lock ("No Edit Permission").
- Delete asks for confirmation ("Delete Template").
- Search: "Search templates by name or description...".
- Empty state: **Create Your First Template**.

**Template wizard** ("Create Project Template" or "Edit Project Template"). Steps: **Basic Info → Milestones → Tasks → Review & Create**.
1. **Basic Info:**
   - **Template Name \***, Description.
   - **Available For**: one category, or leave it empty for all categories.
   - Note: "A Project Template defines the reusable structure… It does not include clients, dates, team members, or budgets."
2. **Milestones:**
   - Add a milestone with its name, duration in days and an optional description, then **Add** (or press Enter).
   - Edit milestones inline, drag to reorder, or delete. Deleting asks for confirmation and also removes the milestone's tasks.
   - The total duration is shown.
   - At least one milestone is required.
3. **Tasks ("Default Tasks"):**
   - **Expand All** / **Collapse All**; **Rename** a milestone.
   - **Add Task** fields:
     - **Task Name \*** and Task Description.
     - Priority.
     - Estimated Time in Hours or Days (1 day = 8 hours).
     - Task Dependencies (earlier tasks only).
   - A warning appears if a task's estimate is longer than its milestone.
   - Edit, duplicate or delete tasks (delete asks for confirmation). Drag tasks to reorder them or move them between milestones.
4. **Review & Create:** Milestones, Total Tasks, Est. Timeline, Est. Hours, Template Name, Description, Available Category.

**Footer:** **Previous**, **Save Draft** (new templates only), **Next**, **Create Template** / **Update Template**.

**Template Wizard: step-by-step requirements (what is required and what is optional)**

Prerequisite: create a **Category** first (ProjectHub Setup → 2nd tab, Project Types & Categories). Categories need departments, so departments must exist first.

| Step | Name | Required to move on | Optional |
|---|---|---|---|
| 1 | **Basic Info** | **Template Name \*** (the **Next** button stays disabled until a name is entered) | **Description**; **Available For** (choose one active category; if left empty the template is not tied to a category) |
| 2 | **Milestones** | **At least one milestone**, each with a **Milestone name** (**Next** is disabled until one milestone exists). **Days** defaults to 5 and is at least 1. | Milestone **Description**; reorder by drag and drop; total duration is calculated for you |
| 3 | **Tasks** | **Task Name \*** for every task you add. Adding tasks is **not enforced**: you can click **Next** with zero tasks, though a template normally has tasks. | **Task Description**; **Priority** (default Medium; choices come from the Priority Labels in General Settings); **Estimated Time** (Hours or Days, 1 day = 8 hours); **Task Dependencies** (only tasks above the current task) |
| 4 | **Review & Create** | Template Name and at least one milestone (checked again before **Create Template** is enabled) | Nothing to fill in; this step only shows Milestones, Total Tasks, Est. Timeline, Est. Hours, Name, Description and Available Category |

Notes for each step:
- **Step 1** — the category list shows only **active** categories. If it says "No categories found", create a category first.
- **Step 2** — milestones are the phases of the project. Tasks are added inside milestones in Step 3, so create milestones first.
- **Step 3** — the dialog warns if a task's estimated time is longer than its milestone duration. On **Next** the wizard checks for **cyclic dependencies** (blocking) and, for **new** templates, warns that **dependencies are not saved** until the template exists.
- **Step 4** — click **Create Template** (or **Update Template** when editing) to save. A saved template is **Active**; a template saved with **Save Draft** is **Draft**.
- **Save Draft** (new templates only) is available on any step and keeps the work without finishing the wizard. If you close the wizard with unsaved data it asks "Leave without saving?".

**Required vs optional at a glance (Template):** Required = Template Name, at least one milestone (with a name), and a Task Name for each task you add. Everything else (description, category, milestone description, task description, priority, estimated time, dependencies) is optional.

**Required vs optional at a glance (Category):** Required = Category Name. Optional = Description. Applicable Departments is optional in the form, but you should select at least one department so the category is usable by that department.

**Warnings:**
- **Leave without saving?** → **Save Draft** or **Close without saving**.
- **Cyclic Dependency Detected** → **Go Back & Fix**.
- **Task Dependencies Detected** (new templates only): dependencies are **not** saved for a new template, so add them after creating it. Choose **Go Back & Remove Dependencies** or **Proceed Anyway (Dependencies Won't Save)**.

---

### 6.14 ProjectHub Dashboard (Company)

**Question this answers:** "What does the ProjectHub Dashboard show?", "What filters does it have?", "What happens when I click a card, row or button?"

**What it is:** **ProjectHub Dashboard** — "Operational overview across all company projects." It is the company-wide dashboard for the **Super Admin** (the page always loads data in the SuperAdmin view). Department Admins and Team Leads have a different page (section 6.15).

**How to access it:** **Manage Company → Business Operations → ProjectHub → ProjectHub Dashboard** (`/projecthub-dashboard`, also `/projecthubdashboard`). The sidebar label may read "ProjectHub Dashboard (COMPANY)".

**Loading and errors:** while data loads, grey placeholder blocks are shown. If loading fails the page shows **Failed to load dashboard data** with the server message. Any card with no data shows **No Data Found**.

#### Page layout (top to bottom)

| # | Section | What it shows |
|---|---|---|
| 1 | Header | Title and description |
| 2 | **KPI cards** | Company-level numbers |
| 3 | **Quick Actions** | Four shortcut buttons |
| 4 | **Company Projects** | Searchable, filterable table of projects |
| 5 | **Team Lead Overview** | Cards per Team Lead (carousel) |
| 6 | **Resource Allocation** | Workload chart |
| 7 | **Upcoming Milestones** | Milestones due across projects |
| 8 | **Cross-Dept Requests** | Pending cross-department requests |
| 9 | **Tasks Requiring Attention** | Overdue, blocked, revision, unassigned tasks |
| 10 | **Recent Company Activity** | Activity feed |

#### 1. KPI cards

Cards are display only (clicking does nothing).

| Card | Meaning |
|---|---|
| **Active Projects** | Number of active projects in the company. |
| **Projects at Risk** | Number of projects whose health is At Risk. |
| **Resource Utilization** | Company-wide utilization, shown as a percentage. |

#### 2. Quick Actions

| Button | What happens when you click it |
|---|---|
| **View All Projects** | Opens **AllProjects** in Super Admin view (`/allprojects?view=SuperAdmin`). |
| **View Templates** | Opens **ProjectHub Setup** (`/projecthubsetup`), where templates are managed in the **Project Templates** tab. |
| **Department Setup** | Opens **ProjectHub Department Setup** (`/projecthub-departmentsetup`). |
| **ProjectHub Setup** | Opens **ProjectHub Setup** (`/projecthubsetup`). |

#### 3. Company Projects table

Heading **Company Projects**, sub-text "All active projects across the company (N)", where N is the number of projects matching the current search and filters.

**Controls**

| Control | What it does |
|---|---|
| **Search projects...** | Filters the table as you type. It matches the **project name**, the **Team Lead name** and the **Project Lead name**. |
| **Filters** button | Opens the **Filters** side panel (below). A number badge on the button shows how many filters are active. |
| **View All** | Opens AllProjects in Super Admin view. |

**Table columns** (click a column header to sort; click again to reverse the order)

| Column | Shows |
|---|---|
| **Project Detail** | Project name and a type badge (for example Internal, Client). |
| **Team Lead & Project Lead** | Team Lead name (top) and Project Lead name (below); "—" if none. |
| **Progress** | Progress bar and percentage. Bar colour: below 30% amber, 30–69% blue, 70% and above green. |
| **Due Date & Health** | Due date (for example "Dec 31, 2026") and a health badge (**Healthy**, **At Risk**, **Delayed**). |
| **Status** | Project status badge (**Planning**, **In Progress**, **On Hold**, **Completed**, **Cancelled**). |

**Click on a row:** opens that project's **Project Detail** page (`/projectdetail?id=<id>&view=SuperAdmin`) in the same tab.
The table shows the first **8** projects that match the search and filters. Use **View All** to see every project.

**Filters panel** ("Filter projects by department, team lead, category, status, health, and type")

| Filter | Options come from | Notes |
|---|---|---|
| **Department** | All company departments | Choosing a department also reloads the **Team Lead** list for that department and resets Team Lead to "All Team Leads". |
| **Team Lead** | Team Leads of the selected department (or of your own department if none is selected) | |
| **Category** | The company's Categories (ProjectHub Setup, tab 2) | |
| **Status** | Project statuses (Planning, In Progress, On Hold, Completed, Cancelled...) | |
| **Project Health** | Project Health Statuses (ProjectHub Setup, tab 1) | |
| **Project Type** | Project types that are **Active** (ProjectHub Setup, tab 2) | An Inactive type does not appear here. |

Buttons: **Clear All** (resets every filter, clears the department choice and applies at once) and **Apply Filters** (applies the choices and closes the panel). Filters apply to the **Company Projects table only**, not to the cards below it. All filters and the search are combined (a project must match all of them). Choices stay as "All ..." until you click **Apply Filters**.

#### 4. Team Lead Overview

"Operational summaries for each Team Lead across the company". Shows **3** Team Leads at a time. Use the round **‹** and **›** arrows (top right) to move one Team Lead at a time; an arrow is disabled at the start or end of the list.

Each Team Lead card shows:

| Item | Meaning |
|---|---|
| Name, photo, "Team Lead" | The Team Lead |
| **Team Size** | People in the team |
| **Active Projects** | Active projects the Team Lead owns |
| **Open Tasks** | Tasks not yet finished |
| **Overdue Tasks** | Late tasks (red when above 0) |
| **Utilization** | Percentage with a label and bar (see below) |
| **At Risk** | Projects at risk (red when above 0) |

Utilization label and bar colour: **Available** (below 60%, green), **Moderate** (60–79%, blue), **Fully Allocated** (80–95%, orange), **Overallocated** (above 95%, red).

**View Projects** button on a card: opens AllProjects in Super Admin view. (It does not filter by that Team Lead.)

#### 5. Resource Allocation

"Workload overview across all teams." A bar chart with four bars: **Available**, **Moderate**, **Fully Allocated**, **Overallocated**. Each bar shows the share (%) of team members in that group.

| Group | Utilization | Bar colour |
|---|---|---|
| Available | below 60% | green |
| Moderate | 60–80% | blue |
| Fully Allocated | 80–95% | orange |
| Overallocated | above 95% | red |

Hover over a bar to see a tooltip with the group name, **Count**, **Percentage** and the label. A bar at 0% is grey. A legend below the chart lists the four groups and their ranges.

#### 6. Upcoming Milestones

"Milestones due across company projects." Scrollable list. Each card shows the milestone name, project name, a status badge (**On Track**, **At Risk**, **Delayed**, **Overdue**), the Team Lead, the due date and a progress bar with a percentage. **Overdue** milestones have a red card and a red progress bar.

**Click on a milestone:** opens that project's Project Detail **in a new tab**.

#### 7. Cross-Dept Requests

"Pending collaboration requests across departments." In the current version this card always shows **No Data Found**; it is a placeholder.

#### 8. Tasks Requiring Attention

"Overdue, blocked, revision, and unassigned tasks." Scrollable list. Each card shows the task name, a status badge (**Overdue**, **Under Review**, **Blocked**, **Revision**, **Unassigned**), the project name, the assignee ("Unassigned" if none), the Team Lead ("TL: ...") and the due date.

**Click on a task:** opens that project's Project Detail **in a new tab**.

#### 9. Recent Company Activity

"Chronological activity feed." A timeline, newest first, of what happened across all projects, for example **Project Created**, **Project Updated**, **Team Member Added**. Each entry has an icon, a title, a description and how long ago it happened ("22 hours ago"). Entries are not clickable.

#### What each click does (summary)

| You click | Result |
|---|---|
| KPI card | Nothing (display only) |
| **View All Projects** / **View All** / a Team Lead's **View Projects** | AllProjects, Super Admin view |
| **View Templates** / **ProjectHub Setup** | ProjectHub Setup page |
| **Department Setup** | ProjectHub Department Setup page |
| A row in **Company Projects** | Project Detail (same tab) |
| A milestone or a task card | Project Detail (new tab) |
| Column header in Company Projects | Sorts the table |
| **Filters** → **Apply Filters** | Filters the Company Projects table |

#### Notes

- Search and filters change **only** the Company Projects table. The KPI cards, Team Lead Overview, Resource Allocation, milestones, tasks and activity always show company-wide data.
- Only a **Super Admin** should use this page. Department Admins and Team Leads use the **Department Projects Dashboard / Team Lead Dashboard** (section 6.15).
- If a section says **No Data Found**, there is nothing to show yet (for example no projects, no milestones due, or no activity).

---

### 6.15 Department Projects Dashboard / Team Lead Dashboard

**Question this answers:** "What does the Department Admin see on the dashboard?", "What filters does the dashboard have?", "What happens when I click Assign Roles, View Templates, Department Configuration, View All or View Projects?"

**What it is:** One page (`/department-projects-dashboard`) that shows a different dashboard depending on the user's role:
- **Department Administrator** → **Department Projects Dashboard** ("Operational overview for your department").
- **Team Lead** → **Team Lead Dashboard** ("Overview of your team's projects and tasks").
- If a user has **both** roles, the **Department Administrator** version is shown.

**How to open it**
- **Department Administrator:** **My Work → ProjectHub → ProjectHub Dashboard**.
- **Team Lead:** **Manage My Team → ProjectHub → ProjectHub Dashboard**.
- In both sidebars the entry is labelled **ProjectHub Dashboard**, but it opens this department or team page, **not** the company-wide dashboard (that one is for the Super Admin only, section 6.14).

| | Department Admin | Team Lead |
|---|---|---|
| Heading | Department Projects Dashboard | Team Lead Dashboard |
| Sub-heading | "Operational overview for your department" | "Overview of your team's projects and tasks" |
| Quick Actions | View Projects, View Templates, Department Configuration, Assign Roles | View Projects only |
| Projects table | "Department Projects" ("All active projects within your department") | "Team Projects" ("Projects assigned to your team") |
| Resource Allocation chart | Shown | Hidden |
| Cross-Dept Requests | Not shown | Not shown |

The rest of this section describes the **Department Administrator** dashboard. The Team Lead dashboard has the same cards, with the differences in the table above.

**Loading and errors:** while loading, grey placeholder blocks are shown. If loading fails the page shows **Failed to load dashboard data** with the server message. A card with no data shows **No Data Found**.

#### Page layout (top to bottom)

| # | Section | What it shows |
|---|---|---|
| 1 | Header | Title and description |
| 2 | **KPI cards** | Three numbers for your department |
| 3 | **Quick Actions** | Shortcut buttons |
| 4 | **Department Projects** | Searchable, filterable table of your department's projects |
| 5 | **Team Lead Overview** | Cards per Team Lead in the department |
| 6 | **Resource Allocation** (Department Admin only) | Workload chart |
| 7 | **Upcoming Milestones** | Milestones due across department projects |
| 8 | **Tasks Requiring Attention** | Overdue, blocked, revision and unassigned tasks |
| 9 | **Recent Department Activity** | Activity feed |

#### 1. KPI cards

Display only (clicking does nothing).

| Card | Meaning |
|---|---|
| **Active Projects** | Number of active projects in your department |
| **Projects at Risk** | Number of projects whose health is At Risk |
| **Resource Utilization** | Utilization of your department's people, as a percentage |

#### 2. Quick Actions (Department Administrator)

| Button | What happens when you click it |
|---|---|
| **View Projects** | Opens **Department Projects** (AllProjects in Department Admin view): `/allprojects?view=DepartmentAdmin` (for example `https://<your-company>.synclo.com/allprojects?view=DepartmentAdmin`). |
| **View Templates** | Opens **ProjectHub Department Setup** (`/projecthub-departmentsetup`). The page opens on its first tab, **User Roles**; click the **Project Templates** tab (tab 3) to see and create templates. |
| **Department Configuration** | Opens **ProjectHub Department Setup** (`/projecthub-departmentsetup`). |
| **Assign Roles** | Opens **ProjectHub Department Setup** (`/projecthub-departmentsetup`), which opens on the **User Roles** tab, where you mark Team Leads. |

All three setup buttons open the same page, **Department Setup**, with its three tabs: **User Roles**, **Project Categories**, **Project Templates** (section 6.12). A **Team Lead** sees only **View Projects**.

#### 3. Department Projects table

Heading **Department Projects**, sub-text "All active projects within your department (N)", where N is the number of projects matching the current search and filters.

**Controls**

| Control | What it does |
|---|---|
| **Search projects...** | Filters as you type. Matches the **project name**, the **Team Lead name** and the **Project Lead name**. |
| **Filters** button | Opens the **Filters** side panel (below). A number badge shows how many filters are active. |
| **View All** | Opens **Department Projects**: `/allprojects?view=DepartmentAdmin`. |

**Columns** (click a header to sort; click again to reverse)

| Column | Shows |
|---|---|
| **Project Detail** | Project name and a type badge (for example Internal, Client) |
| **Team Lead & Project Lead** | Team Lead name (top), Project Lead name (below); "—" if none |
| **Progress** | Progress bar and percentage (below 30% amber, 30–69% blue, 70% and above green) |
| **Due Date & Health** | Due date (for example "Sep 24, 2026") and a health badge (**Healthy**, **At Risk**, **Delayed**) |
| **Status** | **Planning**, **In Progress**, **On Hold**, **Completed** or **Cancelled** |

**Click on a row:** opens that project's **Project Detail** (`/projectdetail?id=<id>&view=DepartmentAdmin`) in the same tab. The table shows the first **8** matching projects; use **View All** for all of them. If nothing matches it says **No projects found**.

**Filters panel** ("Filter projects by team lead, category, status, health, and type")

| Filter | Options come from |
|---|---|
| **Team Lead** | Team Leads of **your department** |
| **Category** | The company's Categories |
| **Status** | Project statuses (Planning, In Progress, On Hold, Completed, Cancelled...) |
| **Project Health** | The Project Health Statuses (Healthy, At Risk, Delayed...) |
| **Project Type** | Project types that are **Active** (an Inactive type does not appear) |

There is **no Department filter** here, because the table already shows only your department. Buttons: **Clear All** (resets every filter and applies at once) and **Apply Filters** (applies and closes the panel). Choices stay as "All ..." until you click **Apply Filters**. All filters and the search combine (a project must match all of them). Filters change the **Department Projects table only**, not the cards below it.

#### 4. Team Lead Overview

"Operational summaries for each Team Lead in the department." Shows **3** Team Leads at a time; use the round **‹** and **›** arrows to move one at a time (an arrow is disabled at the start or end of the list).

Each card shows: name, photo and "Team Lead"; **Team Size**; **Active Projects**; **Open Tasks**; **Overdue Tasks** (red when above 0); **Utilization** (percentage, label and bar); **At Risk** (red when above 0).

Utilization label and colour: **Available** (below 60%, green), **Moderate** (60–79%, blue), **Fully Allocated** (80–95%, orange), **Overallocated** (above 95%, red).

**View Projects** on a card opens `/allprojects?view=DepartmentAdmin` (the Department Projects list). It does not filter by that Team Lead.

#### 5. Resource Allocation (Department Administrator only)

"Workload overview across all teams." A bar chart with four bars: **Available**, **Moderate**, **Fully Allocated**, **Overallocated** (short names AV, MD, FA, OA). Each bar is the share (%) of people in that group.

| Group | Utilization | Colour |
|---|---|---|
| Available | below 60% | green |
| Moderate | 60–80% | blue |
| Fully Allocated | 80–95% | orange |
| Overallocated | above 95% | red |

Hover a bar for a tooltip (group, **Count**, **Percentage**, label). A legend under the chart lists the four groups and ranges. A Team Lead does not see this card.

#### 6. Upcoming Milestones

"Milestones due across department projects." Scrollable list. Each card shows the milestone name, project name, a status badge (**On Track**, **At Risk**, **Delayed**, **Overdue**), the Team Lead, the due date and a progress bar with a percentage. **Overdue** milestones have a red card.

**Click on a milestone:** opens that project's Project Detail **in a new tab**.

#### 7. Tasks Requiring Attention

"Overdue, blocked, revision, and unassigned tasks." Each card shows the task name, a status badge (**Overdue**, **Under Review**, **Blocked**, **Revision**, **Unassigned**), the project name, the assignee ("Unassigned" if none), the Team Lead ("TL: ...") and the due date. **Click on a task:** opens that project's Project Detail **in a new tab**.

#### 8. Recent Department Activity

"Chronological activity feed." A timeline, newest first, of what happened in your department's projects, for example **Project Updated**, **TeamMember Added**, **Project Created**. Each entry has an icon, a title, a description and how long ago it happened ("2 weeks ago"). Entries are not clickable.

#### What each click does (summary)

| You click | Result |
|---|---|
| KPI card | Nothing (display only) |
| **View Projects** (Quick Actions), **View All**, a Team Lead's **View Projects** | Department Projects list: `/allprojects?view=DepartmentAdmin` |
| **Assign Roles** | Department Setup (opens on the **User Roles** tab) |
| **View Templates** | Department Setup (then use the **Project Templates** tab) |
| **Department Configuration** | Department Setup |
| A row in the projects table | Project Detail (same tab) |
| A milestone or a task card | Project Detail (new tab) |
| A column header | Sorts the table |
| **Filters** → **Apply Filters** | Filters the Department Projects table |

#### Notes

- Search and filters change **only** the Department Projects table. The KPI cards, Team Lead Overview, Resource Allocation, milestones, tasks and activity always show department-wide data.
- Only a **Department Administrator** (or a Team Lead for the team version) sees this page in the menu. The **Super Admin** uses the company-wide dashboard (section 6.14).
- **No Data Found** on a card means there is nothing to show yet.

#### Team Lead Dashboard in detail (Team Lead, role 16)

A Team Lead who opens **Manage My Team → ProjectHub → ProjectHub Dashboard** sees the **Team Lead Dashboard** ("Overview of your team's projects and tasks").

- **Quick Actions:** only one button, **View Projects**. Clicking it opens **Team Lead Projects**: `/allprojects?view=teamlead`.
- **Projects table:** **Team Projects** ("Projects assigned to your team"). The same search, sortable columns and row click as the Department Projects table. A row opens the project's Project Detail in Team Lead view.
- **View All** (table header) and **View Projects** (on a Team Lead Overview card) both open `/allprojects?view=teamlead`.
- **Filters** (the **Filters** button on the table; panel "Filter projects by team lead, category, status, health, and type"): **Team Lead**, **Category**, **Status**, **Project Health**, **Project Type**, with **Clear All** and **Apply Filters**. Filters change the projects table only.
- **KPI cards**, **Team Lead Overview**, **Upcoming Milestones**, **Tasks Requiring Attention** and **Recent Activity** work as described above. **Resource Allocation** is **not** shown to a Team Lead, and the Upcoming Milestones card uses the full width.
- A user who is both a Team Lead and a Department Administrator sees the **Department Administrator** version instead.


---

### 6.16 Archived Projects

**How to access it:**
- Super Admin: **Manage Company → Business Operations → ProjectHub → Archived Projects**.
- AllProjects → **View Archived Projects**. This appears in the SuperAdmin, DepartmentAdmin and TeamLead views, only when restoration is allowed.
- Filter Drawer → Status → **Archived**.
- `/archivedprojects?view=<Role>`. If the view is missing, your highest role is used.

**Page:** "Archived Projects — View and manage your archived projects", with **Back to Projects** (returns you to where you came from).

**Controls:**
- **Search archived projects...**
- **Filters** ("Filter Archived Projects"): Department, Category, Priority. Buttons: **Clear All**, **Apply Filters**.
- Grid or list view, and pagination.

**To restore a project:** open it and choose ⋮ → **Unarchive Project** on Project Detail (section 10). Empty state: "No Archived Projects Found".

---

### 6.17 ProjectHub Analytics

**How to access it:** `/projecthub-analytics`. Heading: "ProjectHub Analytics — Analyze project delivery performance, milestone execution, team outcomes, and project risks."

**Controls:**
- **Export Report** downloads `projecthub-analytics-report.csv`.
- **Filters** ("Filter Report"):
  - Date Range: Last 30 Days, Last 3 Months, Last 6 Months (default), Last Year, All Time.
  - Department, Project Type, Project Category, Team Lead, Project Lead.
  - Buttons: **Clear All**, **Apply Filters**.

| Tab | KPIs | Charts / lists |
|---|---|---|
| Project Performance | Projects Completed, On-Time Completion Rate, Average Schedule Variance, Average Project Duration | Planned vs Actual Completion & Schedule Variance; Project Performance List |
| Milestone Performance | Total Milestones, On-Time Completion %, Overdue Milestones %, Average Delay | Milestone Outcomes Over Time; Milestone Performance by Project |
| Department Performance | Company Avg Completion Rate, Company Avg On-Time Delivery, Company Avg Schedule Variance | Department Comparison (choose a metric); Department Summary |
| Project Lead Performance | Active Project Leads, Average On-Time Delivery, Average Review Turnaround, Average Milestone Completion | Projects Managed vs On-Time Delivery; Project Lead List |
| Issues & Risks | Switch between Issues and Risks. Issues: Raised, Resolved, Resolution Rate, Average Resolution Time. Risks: Identified, Open, Mitigated, High / Critical Risk % | Trends and breakdowns |

> This page currently shows **sample data**. An older page, "Project Analytics" (`/projectanalytics`), also exists for Company Admins and Reporting Authorities. The sidebar **Analytics** entry opens `/projectanalytics`: Super Admin → **Manage Company → Business Operations → ProjectHub → Analytics**. Normal employees do not see an Analytics entry.

---

## 7. Button and Control Reference

### 7.1 AllProjects
| Button | Location | Action | Who |
|---|---|---|---|
| Create New Project | Header; empty state | Opens the wizard | SA, DA, TL (Team Lead view) |
| Import Projects | Header; empty state | Opens the Setup Assistant | Everyone |
| View Archived Projects | Header | Opens Archived Projects | SA, DA and TL views, when restoration is allowed |
| Search / Filters / Sort By / Grid–List | Toolbar | Search, filter, sort, change layout | Everyone |
| ⋮ View Details / Edit / Edit Draft / Archive / Unarchive / Delete | Card or row | See 6.1 | By role |
| Entries per page, ‹ › | Bottom | Pagination | Everyone |

### 7.2 Filter Drawer
| Button | Location | Action | Who |
|---|---|---|---|
| Filter dropdowns | Body | Set filter values | By view (6.2) |
| Clear All | Footer | Reset filters and search | Everyone |
| Apply Filters | Footer | Close and apply | Everyone |

### 7.3 ProjectCreate wizard
| Button | Location | Action | Who |
|---|---|---|---|
| Create from Project Template / Create Blank Project | Step 1 | Choose the structure | Creators |
| Click to upload files | Step 2 | Add attachments | Creators |
| Select Whole Team | Step 3 | Select all members | Creators |
| Cancel / Save as Draft / Previous / Next | Footer | Move between steps or save | Creators |
| Create Project and Planning / Update Project (and Planning) | Step 4 | Save the project | Creators and editors |
| Yes, Close / Save Draft | Unsaved-changes dialog | Discard or save | Creators |

### 7.4 Project Detail
| Button | Location | Action | Who |
|---|---|---|---|
| Back to Projects / Team Tasks / My Tasks | Top left | Go back | Everyone |
| Activate Project | Header; Readiness widget | Activate the project | Everyone except PM; Planning only |
| ⋮ Edit Project, Change Project Lead, Manage Team, Put on Hold, Resume Project, Archive / Unarchive Project | Header | See 6.4.2 | By role |
| View Files | Beside the tabs | Opens Project Files | Everyone |
| Project Discussion | Right edge of the screen | Opens the discussion | Everyone |
| Overview / Planning (Execution) / Activity | Tabs | Switch section | Everyone |
| Edit, Save Brief, All Previous Versions, Revert to This Version | Project Brief | Manage the brief | Everyone except PM (anyone can view versions) |
| View Full Activity | Recent Activity | Opens the Activity tab | Everyone |
| Add Milestone; ⋮ Edit Milestone / Delete Milestone | Planning tab | Manage milestones | Editors |
| Bulk Assign Tasks, Add Task, Unassigned (inline assign), ⋮ Add Issue / Edit Task / Delete, Duplicate | Milestones and task rows | Manage tasks | Editors (Planning) |
| Select member, Assign, ✕ | Bulk Assign bar | Bulk-assign tasks | Editors |
| Add Risk, Resolve, Delete Risk | Risks section | Manage risks | Editors |

### 7.5 Task Detail drawer
| Button | Location | Action | Who |
|---|---|---|---|
| Project name link | Header | Opens the project | Everyone |
| Start Task | Bottom bar | Moves the task to In Progress | Assignee |
| Save Draft / Submit for Review | Bottom bar | Save or submit work | Assignee |
| Add another URL / Click to upload files | Submission form | Add work items | Assignee |
| View history | Submission section | Opens Submission History | Everyone |
| Approve → Confirm Approval | Bottom bar | Completes the task | Reviewers |
| Revert with Feedback → Revert Task | Bottom bar | Sends the task back | Reviewers |
| Reassign Task / Edit Task | Bottom bar | Reassign (coming soon) / edit | Managers |
| Keep Editing / Discard & Close | Unsaved-changes dialog | Keep or discard edits | Assignee |

### 7.6 My Tasks / Team Tasks
| Button | Location | Action | Who |
|---|---|---|---|
| Search tasks... / Search team tasks... | Toolbar | Search | Everyone |
| Filters → Clear All / Close | Toolbar / drawer | Filter tasks | Everyone |
| Board / List | Toolbar | Change view | Everyone |
| Drag a card | Board | Change status (allowed moves only) | Everyone |
| View | List row | Opens the task | Everyone |
| Clear Filters | Empty state | Reset filters | Everyone |

### 7.7 Project Discussion and Files
| Button | Location | Action | Who |
|---|---|---|---|
| Send / Enter | Composer | Send a message | Team |
| Paperclip (Document, Photo, Video, Audio File) | Composer | Attach a file | Team |
| Microphone, Stop, Cancel, Add to Message | Composer | Record a voice note | Team |
| Reply, reactions | Message | Respond | Team |
| Delete message | Your own message | Delete it for everyone | Author |
| View all | Discussion header | See participants | Team |
| Search files..., source chips, View, Download | Files drawer | Find and open files | Everyone |

### 7.8 Setup Assistant
| Button | Location | Action | Who |
|---|---|---|---|
| Upload a spreadsheet / Trello / No, I'll do it manually | Welcome | Import from a file or Trello, or skip the import | Assistant users |
| Analyze File / Back | Upload Project Data | Analyze the XLSX or CSV file, or return to Welcome | Assistant users |
| Continue to Trello | Connect Trello | Open the Trello sign-in pop-up | Assistant users |
| Who is <name> in Synclo? / Do Not Map This User / Change | Review | Map people | Assistant users |
| Import Now / Go Back / Continue Without Resolving | Review | Submit the import | Assistant users |
| View All Projects | Success | Opens AllProjects | Assistant users |
| X | Top right | Close | Assistant users |

### 7.9 Setup pages and templates
| Button | Location | Action | Who |
|---|---|---|---|
| Import Projects / Save Configuration | ProjectHubSetup | Import / save the current tab | SA |
| Add Priority Label | General Settings | Add a priority | SA |
| Pencil on a project type | Project Types | Active / Brief Form settings | SA |
| Add New Category | Project Types & Categories | Add a category | SA |
| Add User / Edit Role / Save Role | Role Assignment | Assign roles | SA; DA (Team Lead only) |
| Create Category; Edit, Archive, Restore, Delete | Department Categories | Manage categories | DA, SA |
| Create Template / New Template / Create Your First Template | Template lists | Open the template wizard | SA; DA |
| Edit / Delete / Delete (Locked) | Template card | Manage a template | Creator or SA |
| Previous / Save Draft / Next / Create Template / Update Template | Template wizard | Move between steps or save | Template authors |
| Archive Rules toggles | Archive Rules | Set the policy | SA |

### 7.10 Dashboards and Analytics
| Button | Location | Action | Who |
|---|---|---|---|
| View All Projects / View Templates / Department Setup / ProjectHub Setup | Company Quick Actions | Navigate | SA |
| View Projects / View Templates / Department Configuration / Assign Roles | Department Quick Actions | Navigate | DA (View Projects also TL) |
| Search, Filters, View All, column sort, row click | Projects table | Explore projects | Dashboard users |
| ‹ › and View Projects | Team Lead Overview | Browse team leads | Dashboard users |
| Export Report / Filters | Analytics | Export CSV / filter | Analytics users |

---

## 8. Workflows and Use Cases

### 8.1 Create a project (SA, DA, TL)
1. Open your projects page and click **Create New Project**.
2. **Structure:** choose a template or a blank project, then a **Category** (and the template, if using one). Click **Next**.
3. **Project Info:** enter the **Name**, **Type** and **Priority**, plus any optional fields. Click **Next**.
4. **Team:** choose the **Project Team Lead** (SA and DA views) or the **Project Lead** (TL view), and add members. Click **Next**.
5. **Review:** click **Create Project and Planning**. The project opens on its Planning tab.

### 8.2 Plan a project (SA, DA, TL, PL)
1. On the Planning tab, click **Add Milestone** and enter a name and dates.
2. In each milestone, click **Add Task** and enter the name, assignee, dates, estimate and dependencies.
3. Assign any remaining tasks with **Unassigned**, or with **Bulk Assign Tasks** → **Select member** → **Assign**.
4. Drag to reorder. Add the **Project Brief** and any **Risks**.

### 8.3 Activate a project
1. Make sure a Project Lead (⋮ **Change Project Lead**) and team members (⋮ **Manage Team**) are assigned.
2. Check **Project Readiness** on the Overview tab.
3. Click **Activate Project** and confirm. The tab changes to **Execution**.

### 8.4 Do a task (assignee)
1. Open the task from **My Tasks**.
2. Click **Start Task**, or drag the card from To Do to In Progress.
3. Add files, URLs and notes. Use **Save Draft** to save your progress.
4. Click **Submit for Review**.
5. If the task is reverted, read the feedback, start it again and resubmit.

### 8.5 Review a task (SA, DA, TL, PL)
1. Open the task from **Team Tasks**, **Pending Reviews** or the Execution tab (in a manager view).
2. Check the submission and **View history**.
3. Either **Approve** (add a comment, then **Confirm Approval**) or **Revert with Feedback** (add feedback, then **Revert Task**).

### 8.6 View all projects
- SA: **All Projects**
- DA: **Department Projects**
- TL: **Team Projects**
- PL / PM: **My Projects**

### 8.7 Filter projects
Click **Filters**, choose your values, then **Apply Filters**. **Clear All** resets them. Increase the entries per page to filter more projects at once.

### 8.8 Set up ProjectHub for the company (SA)
1. Go to ManageCompany → **ProjectHub Setup**.
2. In the assistant, either import your data or choose **No, I'll do it manually**.
3. **General Settings** → **Save Configuration**.
4. **Project Types & Categories** → **Save Configuration**.
5. **User Role Assignment** → **Add User** for each Department Admin, Team Lead, Project Lead and Member.
6. **Project Templates** → **Create Template**.
7. **Archive Rules** → **Save Configuration**.
8. Ask each Department Admin to complete Department Setup.

### 8.9 Set up a department (DA)
1. Open **ProjectHub Department Setup**.
2. **User Roles**: assign Team Leads.
3. **Project Categories**: create and manage the department's categories.
4. **Project Templates**: create department templates.

### 8.10 Import existing projects
**From a file (XLSX or CSV):**
1. **Import Projects** → **Upload a spreadsheet**.
2. Choose an **.xlsx** or **.csv** file → **Analyze File**.
3. On the Review screen map each unmatched person, or choose **Do Not Map This User**.
4. **Import Now** → **View All Projects**.

**From Trello:**
1. **Import Projects** → **Trello** → **Continue to Trello**.
2. Sign in to Trello in the pop-up and click **Allow**.
3. Wait for the sync to finish, then on the Review screen map each unmatched person, or choose **Do Not Map This User**.
4. **Import Now** → **View All Projects**.

### 8.11 Assign ProjectHub roles
**Add User** → search for the employee → select roles → **Add User**. To change roles later: ⋮ **Edit Role** → **Save Role**.

### 8.12 Put a project on hold, resume, archive or restore it
- ⋮ **Put on Hold** → confirm.
- ⋮ **Resume Project.**
- ⋮ **Archive Project** → confirm.
- To restore, open the archived project → ⋮ **Unarchive Project** (section 10).

### 8.13 Change the project lead or team
- ⋮ **Change Project Lead** → choose the new lead → **Change Lead**.
- ⋮ **Manage Team** → **Add New Member** → **Add** → **Save Changes**.

### 8.14 Revert the brief
**All Previous Versions** → **Revert to This Version** → **Revert**.

### 8.15 Discuss a project
Open **Project Discussion**, type your message (use @ to mention people), attach files or a voice note, then **Send**.

### 8.16 Find files
**View Files** → search or filter by source → **View** / **Download**.

### 8.17 Create a template
**Create Template** → Basic Info → Milestones (at least one) → Tasks → **Create Template**.

### 8.18 Delete a project
⋮ **Delete** → **Delete Project**. This is permanent.

---

## 9. Status Reference

| Project status | Meaning | Second tab |
|---|---|---|
| Draft | Saved, not yet created | Planning |
| Planning | Created and being planned | Planning |
| In Progress | Activated | Execution |
| On Hold | Paused; project actions are disabled | Execution |
| Completed | Finished (set automatically by Synclo) | Execution |
| Archived | Stored away | — |

```
(new) --Save as Draft--> Draft --Create/Update--> Planning --Activate--> In Progress --> Completed
                                                                 |  ^
                                                    Put on Hold  v  | Resume
                                                               On Hold
Any non-draft --Archive (if allowed)--> Archived --Unarchive (if allowed)--> restored
```

**Other statuses:**
- **Task:** To Do → In Progress → Under Review → Completed. A reverted task returns to the assignee marked "Revision Requested".
- **Project Health:** On Track, At Risk, Off Track.
- **Risk:** Open, Resolved. Impact and Likelihood are each Low, Medium or High.
- **Template:** Draft or Active, plus the System Default and In Use badges.
- **Department category:** Active or Archived.

---

## 10. Archive and Restore Rules

**Question this answers:** "What are the Archive Rules?", "What happens if I choose Immediately / After X days?", "What happens if I turn this switch on or off?", "Who can archive or restore a project?"

**Where to set them:** Manage Company → Setup & Configurations → Modular Configurations → **ProjectHub Setup** → **5th tab, Archive Rules** (Super Admin only). Click **Save Configuration** at the bottom to store changes. (See section 1.3 for the other tabs.)

**What "archive" means:** Archiving moves a project out of the active project list into **Archived Projects** so dashboards stay clean. Archived projects are still searchable and can be restored if the rules allow it. Archiving does **not** delete a project.

#### 10.1 All Archive Rules at a glance

There are **six** items on the Archive Rules tab. Their default values when the company has no rule saved yet are shown (all switches Off, completed mode "Immediately", inactive days 60).

| # | Rule (exact label) | Control | Values | Short effect |
|---|---|---|---|---|
| 1 | **Enable automatic archival** | Switch | On / Off | Master switch for rules 2 and 3 (automatic archiving by the system). |
| 2 | **Archive completed projects** | Radio (pick one) | **Immediately** / **After X days** | When a Completed project is archived automatically. |
| 3 | **Archive inactive projects after X days** | Number | 1 or more, default 60 | When a project with no activity is archived automatically. |
| 4 | **Allow archived project restoration** (setting **A**) | Switch | On / Off | Controls whether people can archive manually, see archived projects and restore them. |
| 5 | **Allow Department Administrators to restore archived projects** (setting **B**) | Switch | On / Off | Lets Department Administrators restore archived projects. |
| 6 | **Require Super Admin approval for permanent deletion** | Switch, locked | **Always On** | Permanent deletion always needs Super Admin approval. Cannot be changed. |

Rules 2 and 3 are only visible when rule 1 is On.

#### 10.2 What each option does

**Rule 1 — Enable automatic archival**
- **ON:** the system archives projects by itself using rules 2 and 3. The two rule cards appear under the switch, plus a note: "Draft projects are excluded from automatic archival. Only projects in Completed, In Progress, or On Hold statuses are evaluated."
- **OFF:** no project is archived automatically, and rules 2 and 3 are hidden (their values are not used). Projects can still be archived by hand, if rule 4 allows it.

**Rule 2 — Archive completed projects** (shown only when rule 1 is On; the two options are mutually exclusive)

| Option you select | What happens | Extra field |
|---|---|---|
| **Immediately** | "Archive projects the moment their status changes to Completed." As soon as a project becomes **Completed**, it is archived. | None (saved as 0 days) |
| **After X days** | "Delay archival until a specified number of days after completion." A Completed project stays visible for X days, then it is archived. | **days after completion**: a number, minimum 1, default **30**. The box appears only when this option is selected. |

**Rule 3 — Archive inactive projects after X days** (shown only when rule 1 is On)
- Enter a number of days (default **60**, minimum 1).
- A project that has had **no activity** for that many days is archived. "Activity" means task updates, comments or status changes.
- Only projects in **Completed, In Progress or On Hold** are checked. **Draft** projects are never archived automatically.
- Example: set to 60. A project On Hold with no task update, comment or status change for 60 days is archived.

**Rule 4 (A) — Allow archived project restoration**
- **ON:** Super Admin, Department Administrator and Team Lead (in their own project views) can use the **Archive** action on the AllProjects ⋮ menu, see the **View Archived Projects** button, and restore (unarchive) archived projects. Department Administrators can restore only if rule 5 is also On.
- **OFF:** in AllProjects nobody can archive from the ⋮ menu or restore, and **View Archived Projects** is hidden. (Project Detail still lets a **Super Admin** archive, see table in 10.4.)
- Project Lead and Project Member are never allowed to archive or restore, whatever this switch says.

**Rule 5 (B) — Allow Department Administrators to restore archived projects**
- **ON** (and A also ON): Department Administrators can restore archived projects **in their department** without Super Admin approval. The Unarchive action appears for them.
- **OFF:** Department Administrators cannot unarchive. Super Admin still can.
- This switch has no effect on Team Leads (a Team Lead can unarchive in AllProjects only when A is On, and never on Project Detail).

**Rule 6 — Require Super Admin approval for permanent deletion**
- Always On and greyed out ("Always On"; "This is a mandatory security policy and cannot be disabled").
- Archiving and restoring are reversible; **permanent deletion** of an archived project always needs a Super Admin.

#### 10.3 Common choices (what happens in practice)

| What you set | Result |
|---|---|
| Rule 1 **Off**, A **On** | Nothing is archived automatically. Managers archive and restore by hand. |
| Rule 1 **On**, Completed = **Immediately**, inactive = 60 | Completed projects are archived straight away. Projects with no activity for 60 days are archived. |
| Rule 1 **On**, Completed = **After X days** (30), inactive = 90 | Completed projects stay in the list for 30 days, then are archived. Inactive projects are archived after 90 days. |
| A **Off** | No manual archiving or restoring from AllProjects, and **View Archived Projects** is hidden. Use this to lock archived projects. |
| A **On**, B **Off** | Super Admin and Team Lead can restore. Department Administrators cannot. |
| A **On**, B **On** | Super Admin, Team Lead and Department Administrator can all restore. |

> Automatic archiving itself (the nightly or scheduled check against rules 1 to 3) runs on the **server**. This guide describes the options you can set on the page; the exact schedule and timing of the automatic run is decided by the backend.

#### 10.4 Who can archive and restore (permission table)

Use A = "Allow archived project restoration" and B = "Allow Department Administrators to restore archived projects".

| Action | Where | Super Admin | Department Admin | Team Lead | PL / PM |
|---|---|---|---|---|---|
| See **View Archived Projects** | AllProjects header | If A | If A | If A | Never |
| **Archive** | AllProjects ⋮ | If A | If A | If A | Never |
| **Archive Project** | Project Detail ⋮ | Always | If A | If A | Never |
| **Unarchive** | AllProjects ⋮ | If A | If A **and** B | If A | Never |
| **Unarchive Project** | Project Detail ⋮ | Always | If B | Never | Never |
| Permanent deletion | — | Always needs Super Admin approval | | | |
| **Unarchive** | Archived Projects page | Always | If B | Never | Never |

> The rules for AllProjects and for Project Detail are slightly different for the Super Admin: on **Project Detail** a Super Admin can always archive and unarchive; on the **AllProjects** ⋮ menu the Super Admin follows setting **A**. If A is Off and a Super Admin cannot archive from the list, open the project and use ⋮ on **Project Detail**.

**Where to see archived projects:** Super Admin → Manage Company → Business Operations → ProjectHub → **Archived Projects**; others → AllProjects → **View Archived Projects** (only when A is On). See section 6.16.

---

## 11. Frequently Asked Questions

**How do I open ProjectHub as an Employee?**
In the Dashboard sidebar, go to **My Work → ProjectHub**. You will see **All Projects**, **My Tasks**, **Analytics** and **Configuration** (section 4.1.2).

**How do I open ProjectHub as a Team Lead?**
In the Dashboard sidebar, go to **Manage My Team → ProjectHub**. You will see **Team Lead Projects**, **Team Tasks** and **ProjectHub Dashboard** (the Team Lead Dashboard). Your own projects and tasks stay under **My Work → ProjectHub** (section 4.1.3).

**How do I open ProjectHub as a Department Admin?**
In the Dashboard sidebar, go to **My Work → ProjectHub**. Besides **My Projects** and **My Tasks**, you will see **Department Projects**, **ProjectHub Dashboard** (the Department Projects Dashboard) and **Department Setup** (section 4.1.4).

**Who can see Team Tasks?**
Only Team Leads, under **Manage My Team → ProjectHub → Team Tasks**. Department Admins, Super Admins, Project Leads and Project Members do not have Team Tasks in the sidebar.

**How do I open ProjectHub as a Super Admin?**
Click **Manage Company**, then **Business Operations → ProjectHub**. ProjectHub Setup is under **Setup & Configurations → Modular Configurations → ProjectHub Setup** (section 5.1.1).

**Where is the ProjectHub Dashboard?**
It depends on your role. Super Admin: **Manage Company → Business Operations → ProjectHub → ProjectHub Dashboard** (company-wide, section 6.14). Department Admin: **My Work → ProjectHub → ProjectHub Dashboard** (Department Projects Dashboard). Team Lead: **Manage My Team → ProjectHub → ProjectHub Dashboard** (Team Lead Dashboard). See section 6.15.

**Where are Archived Projects?**
Super Admin: **Manage Company → Business Operations → ProjectHub → Archived Projects**. Other roles: open the projects list and click **View Archived Projects** (section 6.16).

**Where is ProjectHub Analytics?**
Super Admin: **Manage Company → Business Operations → ProjectHub → Analytics** (section 6.17). Normal employees do not see an Analytics entry.

**Where are Project Templates?**
Super Admin: **Manage Company → Business Operations → ProjectHub → Project Templates**. Department Admin: **ProjectHub Department Setup → Project Templates** (section 6.13).

**I clicked Configuration under My Work → ProjectHub and see Access Denied. Why?**
Configuration opens ProjectHub Setup, which only Super Admins can use. Department Admins use ProjectHub Department Setup instead.

**Why can't I see Create New Project?**
Only Super Admins, Department Admins and Team Leads can create projects. Team Leads see the button only in **Team Projects**.

**Why can't I open ProjectHub Setup?**
It is for Super Admins only. Department Admins use **ProjectHub Department Setup** instead.

**Why is Activate Project locked?**
A Project Lead must be assigned and at least one Team Member must be added.

**Why can't I click Next on Structure for a blank project?**
You need to choose a Project Category first.

**Why can't I edit the project structure?**
The structure can only be changed while the project is Draft or Planning.

**Why can't I submit my task?**
Click **Start Task** first, then add at least one file, URL or note.

**Why can't I drag a card to Completed?**
A reviewer must use **Approve** instead.

**Why is a category or template locked?**
Only its creator or a Super Admin can change it. In-use templates and categories with projects cannot be deleted.

**Why don't I see archive options?**
See section 10.

**What happens to tasks of people I didn't map during an import?**
They stay unassigned. Assign them on the Planning tab.

**How do I import projects from a file?**
**Import Projects** → **Upload a spreadsheet** → choose an **XLSX or CSV** file → **Analyze File** → map unmatched people if asked → **Import Now**. See section 6.10.

**Can I import from Jira, Asana, ClickUp, monday.com or Notion?**
Not yet. Those cards are "Coming soon". You can import from a **spreadsheet (XLSX/CSV)** or from **Trello**.

**Why does the Setup Assistant open every time I visit ProjectHub Setup?**
That is the current behaviour. Close it with **X** or choose **No, I'll do it manually**.

**Why do some filters seem to miss projects?**
Some filters and sorting only apply to the current page (see 6.1).

---

## 12. Known Limitations (Current Version)

- **Import Projects:** **XLSX/CSV file upload** and **Trello** work. monday.com, ClickUp, Asana, Atlassian / Jira and Notion are marked "Coming soon".
- **Reassign Task:** shows "Reassign functionality coming soon". There is no way to change a task's due date.
- **Manage Team:** removing members is not saved yet (adding members works).
- **Deleting on the Planning tab:** **Delete Milestone** and task **Delete** happen immediately, with no confirmation.
- **Analytics:** ProjectHub Analytics shows sample data, and Cross-Dept Requests always shows "No Data Found".
- **Templates:** dependencies added while creating a new template are not saved. Department Templates show the same list as Organization Wide Templates.
- **Filter badge:** on My Tasks and Team Tasks, the **Filters** badge does not show the number of active filters.
- **Archived Projects:** the card menu has no Unarchive option. Restore the project from Project Detail.
- **On Hold and Archived projects:** the screen does not block any buttons. The server decides which actions are allowed.

---

## 13. Page and URL Reference and Feature Relationship Map

All URLs below are paths on your company's Synclo subdomain (for example `https://<your-company>.synclo.com/allprojects`), never `localhost`.

| Page | URL | Menu | Users |
|---|---|---|---|
| AllProjects (My Work) | `/allprojects` | Dashboard | All |
| AllProjects (Employee / My Work) | `/allprojects` | My Work → ProjectHub | Employee (and everyone, for their own projects) |
| AllProjects (Department Admin) | `/allprojects?view=departmentadmin` | My Work → ProjectHub → Department Projects | DA |
| AllProjects (Team Lead) | `/allprojects?view=teamlead` | Manage My Team → ProjectHub → Team Lead Projects | TL |
| AllProjects (Super Admin) | `/allprojects?view=superadmin` | Manage Company → Business Operations → ProjectHub → Projects | SA |
| AllProjects (Project Lead / Project Member) | `/allprojects` (same as Employee; there is no separate view) | My Work → ProjectHub | PL, PM |
| Project Detail | `/projectdetail?id=<id>&view=<Role>` | From lists | All |
| Archived Projects | `/archivedprojects?view=<Role>` | From AllProjects; ManageCompany → Business Operations → ProjectHub | SA, DA, TL |
| Project Analytics | `/projectanalytics` | ManageCompany → Business Operations → ProjectHub → Analytics | SA |
| Configuration (same as ProjectHub Setup) | `/projectmanagementconfiguration` | Direct address (same page as ProjectHub Setup) | SA (others: Access Denied) |
| My Tasks | `/mytasks` | Dashboard | All |
| Team Tasks | `/teamtasks` | Manage My Team → ProjectHub | TL only |
| Department / Team Lead Dashboard ("ProjectHub Dashboard" in the sidebar) | `/department-projects-dashboard` | DA: My Work → ProjectHub; TL: Manage My Team → ProjectHub | DA, TL |
| ProjectHub Analytics | `/projecthub-analytics` | Dashboard | All Projects access |
| ProjectHub Dashboard | `/projecthub-dashboard` | ManageCompany | SA |
| ProjectHub Setup | `/projecthubsetup` | ManageCompany | SA |
| ProjectHub Department Setup | `/projecthub-departmentsetup` | ManageCompany | SA, DA |
| Project Templates | `/projecttemplates` | ManageCompany | SA |

**How the features connect:**
- **ProjectCreate** opens from AllProjects (Create New Project, Edit, Edit Draft, clicking a draft) and from Project Detail (Edit Project). After saving, it goes to Project Detail → Planning.
- **Filter Drawer** opens from AllProjects → Filters. Status = Archived goes to Archived Projects.
- **Project Detail** opens from AllProjects, Archived Projects, the dashboards, My Tasks, Team Tasks and the Task Detail drawer.
- **Task Detail drawer** opens from Execution mode, My Tasks and Team Tasks.
- **Import Projects** opens from AllProjects and ProjectHubSetup, and ends on AllProjects.
- **ProjectHubSetup** controls:
  - priorities, types and categories, which are used in ProjectCreate and the filters;
  - roles, which decide the views, buttons and menus each user gets;
  - templates, which are used in ProjectCreate → Structure;
  - archive rules, which control the archive and restore actions.

---

## 14. Project Detail, Tasks and Role-Based Behaviour (Deep Dive)

### 14.1 Roles in this section

| Short name | Who it means |
|---|---|
| **SA** | Super Admin (SuperAdmin view) |
| **DA** | Department Admin (DepartmentAdmin view) |
| **TL** | Team Lead (TeamLead view) |
| **PL** | Project Lead (ProjectLead view). In My Work, a project you lead always opens in this view. |
| **PM** | Project Member (ProjectMember view). In My Work, a project you don't lead always opens in this view. |
| **Editors** | SA, DA, TL and PL. Everyone except PM. |
| **Creator** | The person who created the project. |

> Your rights inside a project depend on the **view** you opened it in (`&view=...` in the link). The view comes from the menu you used (for example, Team Projects means TL) or from My Work (PL if you lead the project, otherwise PM).

### 14.2 What is inside Project Detail

1. **Back button**: Back to Projects, Team Tasks or My Tasks.
2. **Header card**:
   - Name, status, Project Health and Priority.
   - Description.
   - Project Lead, Type, Category, Start Date and Completion Target.
   - Overall Progress.
3. **Header actions**:
   - **Activate Project** (Planning only).
   - **⋮ menu**: Edit Project, Change Project Lead, Manage Team, Put on Hold / Resume Project, Archive / Unarchive Project.
4. **Tabs**: **Overview**, **Planning** (renamed **Execution** after activation), **Activity**.
5. **View Files**: the Project Files drawer.
6. **Project Discussion**: a tab on the right edge of the screen, with an unread count.
7. **Task Detail drawer**: opens when you click a task in Execution mode.

**Overview tab**

| Block | What it shows | Who sees it |
|---|---|---|
| KPI cards | Milestones Completed, Tasks Completed, High Risks | Everyone |
| Project Timeline | Start, Target Completion, Current Status, Days Remaining, Overall Health, Overall Progress | Everyone |
| Project Readiness | Activation checklist and **Activate Project** | Planning only; hidden from PM |
| Pending Reviews | Tasks waiting for review | Shown when not in Planning; PM always sees it |
| Project Brief | Brief text, attachments, versions | Everyone can read; Editors can **Edit** |
| Team Members | Role, Lead crown, task count, % done | Everyone |
| Upcoming Milestones | The next 3 | Everyone |
| Recent Activity | The last 5, plus **View Full Activity** | Everyone |

**Planning / Execution tab**

| Block | Planning mode | Execution mode |
|---|---|---|
| Heading | "Planning" | "Project Execution" |
| Add Milestone | Yes (Editors) | No |
| Milestones | All expanded; drag to reorder; ⋮ Edit / Delete | One expanded at a time; no ⋮ |
| Task rows | Editable: inline assign, ⋮ Add Issue / Edit Task / Delete, Duplicate | Read-only; click to open the Task Detail drawer |
| Add Task / Bulk Assign Tasks | Yes (Editors) | No |
| Drag tasks (reorder or move between milestones) | Yes (Editors) | Yes (Editors) |
| Risks and **Add Risk** | Yes (Editors) | Yes (Editors) |
| PM | View only | View only; can open the task drawer |

**Activity tab:** the full history, grouped by day, with relative and exact times.

### 14.3 Who can do what inside a project

| Action | SA | DA | TL | PL | PM | Where |
|---|:-:|:-:|:-:|:-:|:-:|---|
| Activate Project | ✓ | ✓ | ✓ | ✓ | ✗ | Header / Readiness (Planning only) |
| Edit Project | ✓ any | Creator | Creator | ✗ | ✗ | ⋮ (not for Draft or Completed) |
| Change Project Lead | ✓ | ✓ | ✓ | ✗ | ✗ | ⋮ |
| Manage Team | ✓ | ✓ | ✓ | ✓ | ✗ | ⋮ |
| Put on Hold | ✓ | ✓ | ✓ | ✓ | ✗ | ⋮ (not for Draft, Completed or On Hold) |
| Resume Project | ✓ | ✓ | ✓ | ✓ | ✗ | ⋮ (On Hold only) |
| Archive Project | ✓ always | If restoration is allowed | If restoration is allowed | ✗ | ✗ | ⋮ |
| Unarchive Project | ✓ always | If Archive Rules A **and** "Allow Department Administrators to restore" (B) are on | ✗ | ✗ | ✗ | ⋮ (Archived only) |
| Add / Edit / Delete Milestone | ✓ | ✓ | ✓ | ✓ | ✗ | Planning tab |
| Add / Edit / Delete / Duplicate Task | ✓ | ✓ | ✓ | ✓ | ✗ | Planning tab |
| Assign tasks (inline or bulk) | ✓ | ✓ | ✓ | ✓ | ✗ | Planning tab |
| Reorder or move tasks | ✓ | ✓ | ✓ | ✓ | ✗ | Planning and Execution |
| Add Issue | ✓ | ✓ | ✓ | ✓ | ✗ | Task row ⋮ (Planning) |
| Add Risk | ✓ | ✓ | ✓ | ✓ | ✗ | Risks section |
| Resolve / Delete Risk | ✓ | ✓ | ✓ | ✓ | ✗ | Risk row (Open risks) |
| Edit Project Brief / Revert version | ✓ | ✓ | ✓ | ✓ | ✗ | Overview |
| View Files, Discussion, Activity | ✓ | ✓ | ✓ | ✓ | ✓ | Everywhere |
| Start Task / Submit for Review | — | — | — | — | ✓ (assignee) | Task drawer (14.11) |
| Approve / Revert with Feedback | ✓ | ✓ | ✓ | ✓ | ✗ | Task drawer (Under Review) |
| Reassign Task / Edit Task (drawer) | ✓ | ✓ | ✓ | ✓ | ✗ | Task drawer (To Do, In Progress) |

### 14.4 What happens in each project status

**Draft**
- **What it is:** saved with **Save as Draft** but not yet created.
- **Opening it:** clicking it in the list opens the **Create wizard** so you can finish it.
- **Actions:** no ⋮ menu and no Activate in the header. In the list, ⋮ shows **Edit Draft**, Archive (if allowed) and Delete.
- **Next step:** finish the wizard and click **Update Project and Planning**. The project becomes **Planning**.

**Planning**
- **Header:**
  - SA / DA / TL: Edit Project (SA or the creator), Change Project Lead, Manage Team, Put on Hold, Archive (if allowed).
  - PL: Manage Team, Put on Hold.
  - PM: nothing.
- **Activate Project** is visible to everyone except PM. It stays locked until the requirements are met (14.5).
- **Overview:** Project Readiness (PM sees Pending Reviews instead).
- **Planning tab:** full editing — milestones, tasks, assignment, bulk assignment, issues, risks and reordering.
- **Task drawer:** clicking a task does **not** open it. Use **Edit Task** on the row.
- **Edit Project:** the Structure step can still be changed.

**In Progress (Active)**
- **Header:**
  - SA / DA / TL: Edit Project (SA or the creator), Change Project Lead, Manage Team, Put on Hold, Archive (if allowed).
  - PL: Manage Team, Put on Hold.
  - PM: nothing.
  - Activate is gone.
- **Overview:** **Pending Reviews** replaces Readiness.
- **Execution tab:**
  - No longer available: Add Milestone, Add Task, Bulk Assign, Edit/Delete Milestone, and task-row Edit / Delete / Duplicate / Add Issue.
  - Editors can still drag tasks, and use **Add Risk**, **Resolve** and **Delete Risk**.
  - Click a task to open the **Task Detail drawer**. People start and submit work there, managers review it, and managers can **Edit Task**.
- **Edit Project:** the Structure step is locked ("Project structure cannot be modified for active projects"). Info and team details can still be edited.

**On Hold**
- **What it is:** paused with **Put on Hold**. "All project actions will be paused… disabled for everyone." The badge reads "On Hold".
- **Header:**
  - SA / DA / TL: Edit Project (SA or the creator), Change Project Lead, Manage Team, **Resume Project**, Archive (if allowed).
  - PL: Manage Team, **Resume Project**.
- **To continue:** ⋮ **Resume Project**.

**Completed**
- **What it is:** finished. Synclo sets this status itself; there is no "Mark Complete" button.
- **Header:**
  - SA / DA / TL: Change Project Lead, Manage Team, Archive (if allowed).
  - PL: Manage Team.
  - No **Edit Project** or **Put on Hold**.
- **Tasks:** read-only ("Read-only view — no actions available").
- **Archiving:** Archive Rules may archive the project automatically.

**Archived**
- **What it is:** stored away. It is hidden from the normal list and shown in Archived Projects.
- **Header:** Edit Project (SA or the creator) and **Unarchive Project** (SA always; DA if allowed; never TL).
- **Archiving an active project** puts it on hold first.

### 14.5 How to activate a project (requirements and steps)

**Who:** SA, DA, TL, PL. Not PM.

| Item | Required? | How to complete it |
|---|---|---|
| **Project Lead Assigned** | **Required** | Choose a Project Lead in the Create wizard (Team step), or use ⋮ **Change Project Lead** |
| **Team Members Assigned / Added** | **Required** | Choose members in the wizard (or **Select Whole Team**), or ⋮ **Manage Team** → Add New Member → Add → Save Changes |
| All Tasks Assigned | Recommended | Assign every task (**Unassigned** inline, or **Bulk Assign Tasks**) |
| Dependencies Verified | Recommended | Always ticked |

> Milestones and tasks are **not** required. A project with no milestones can still be activated, but planning first is strongly recommended.

**Steps:**
1. Open the project. It must be in **Planning**.
2. Check the "X/Y Required" counter on **Overview → Project Readiness**.
3. Assign whatever is missing: Project Lead (⋮ **Change Project Lead**) and members (⋮ **Manage Team**).
4. Optionally, plan and assign all tasks.
5. Click **Activate Project** in the header or in the Readiness widget. While items are missing, the button reads **Complete Required Items to Activate** and is locked.
6. Review the checklist in the **Activate Project** dialog, then click **Activate Project**.

**Result:**
- The status becomes **In Progress**, and the Planning tab becomes **Execution**.
- Planning-only editing turns off.
- Pending Reviews replaces Readiness.
- The structure is locked.

### 14.6 Milestones: add, edit, delete, reorder

**Who:** Editors. **When:** Planning only.

| Action | How | Details |
|---|---|---|
| **Add Milestone** | Planning tab → **Add Milestone** (top right) | **Milestone Name \*** (e.g. "Discovery & Requirements"), Description, **Start Date \***, **Due Date \*** (not before the start date). Click **Add Milestone**. Message: "Milestone added successfully". |
| **Edit Milestone** | Milestone ⋮ → **Edit Milestone** | Same fields. Click **Save Changes**. Message: "Milestone updated successfully". |
| **Delete Milestone** | Milestone ⋮ → **Delete Milestone** | Deleted **immediately**, with no confirmation. Message: "Milestone deleted successfully". |
| **Reorder** | Drag the ⋮⋮ handle | Message: "Milestone order updated successfully". |

A milestone card shows its name, status, "Due …", "completed/total tasks" and progress %. Template projects start with the template's milestones; blank projects start with none.

### 14.7 Tasks: add, edit, delete, duplicate, assign, move

**Who:** Editors. **When:** Planning, unless the table says otherwise.

| Action | How | Details |
|---|---|---|
| **Add Task** | In a milestone → **Add Task** | **Task Name \***, Description, Milestone, Priority, **Assigned To**, **Suggested JD**, Start / Due Date (within the milestone's dates), **Estimated Time** in Hours or Days (calculated automatically when both dates are set), **Dependencies** (earlier tasks only; a circular dependency is blocked). Click **Add Task**. |
| **Edit Task** | Task row ⋮ → **Edit Task** (Planning), or the Task drawer → **Edit Task** (managers, To Do / In Progress) | Same fields. Click **Save Changes**. |
| **Delete Task** | Task row ⋮ → **Delete** | Deleted **immediately**, with no confirmation. Message: "Task deleted successfully". |
| **Duplicate Task** | Copy icon at the bottom right of the row | Message: "Task duplicated successfully". |
| **Assign one task** | Click **Unassigned** on the row and choose a member | Message: "Task assigned successfully". |
| **Bulk assign** | **Bulk Assign Tasks** → tick tasks → in the bar ("N tasks selected"), **Select member** → **Assign** (✕ exits) | Message: "N task(s) assigned successfully". |
| **Reorder or move** | Drag within a milestone, or to another milestone | Works in Planning and Execution. Message: "Task order updated successfully". |
| **Reassign** (after activation) | Task drawer → **Reassign Task** | Currently shows "Reassign functionality coming soon". |

**Task row badges:** priority, "N versions", 💡 Suggested JD, 🔗 "N deps" (✓ when verified), due date or "No due date", estimated time, assignee, and any issues.

### 14.8 Add Issue

- **What it is:** a problem or blocker recorded against a task.
- **Who:** Editors.
- **Where:** Planning tab → task row ⋮ → **Add Issue**.
- **Fields:** **Title \***, **Priority**, **Owner**.
- **Save:** **Add Issue**. Message: "Issue created successfully".
- **Display:** issues appear in orange under the task, with the title, priority, owner and date-time.

### 14.9 Risks: add, resolve, delete

- **What a risk is:** something that may hurt the project. This is different from **Project Health "At Risk"**, which Synclo works out automatically. The **High Risks** KPI counts high risks.
- **Who can add:** Editors. PM can only view.
- **Where:** Risks section → **Add Risk**. This is available in every status.
- **Fields:** **Risk Name \***, **Impact \*** (Low, Medium, High), **Likelihood \*** (Low, Medium, High).
- **Save:** **Add Risk**. Message: "Risk added successfully".
- **Status:** **Open** (red) or **Resolved** (green). Each risk shows "Impact: … • Likelihood: …".
- **Resolve** (open risks): message "Risk resolved successfully".
- **Delete Risk** (open risks, bin icon): message "Risk deleted successfully".
- **Empty state:** "No risks defined — Define any risks that you feel may impact the project".

### 14.10 Header actions in detail

**Manage Team** (SA, DA, TL, PL)
- Opens with ⋮ → **Manage Team**: "Add or remove team members for '<project>'".
- Lists members with their email and a badge (**Team Lead**, **Project Lead** or **Team Member**).
- **To add:** under **Add New Member**, use "Select a member to add" (searchable, showing department, designation and a Team Lead badge) → **Add** → **Save Changes**. Message: "N team member(s) added successfully".
- **To remove:** ✕ on a Team Member. The Team Lead and Project Lead cannot be removed. *Removals are not saved yet.*

**Change Project Lead** (SA, DA, TL)
- ⋮ → **Change Project Lead** shows the **Current Project Lead**.
- Choose a **New Project Lead \*** ("Search or select a project lead...") → **Change Lead**. Message: "Project lead changed successfully".
- This also completes the "Project Lead Assigned" activation requirement.

**Edit Project** (SA on any project; TL or DA on projects they created)
- Not available for Draft or Completed projects.
- Opens the Create wizard with the saved data. The structure is locked after activation.

**Put on Hold / Resume Project** (SA, DA, TL, PL)
- **Put on Hold:** confirm in "Put Project on Hold".
- **Resume Project:** one click. Message: "Project resumed successfully".

**Archive Project / Unarchive Project**
- **Archive:** confirm in "Archive Project". An active project is put on hold first.
- **Unarchive:** one click. Message: "Project unarchived successfully".
- **Who:** see section 10.

### 14.11 What happens in each task status (Task Detail drawer)

The drawer always shows:
- **Header:** name, status, **Revision Requested** badge (if any), priority, Due date, project link, milestone, progress.
- **Task Overview:** Description, Dependencies, Estimated Hours, Start Date, Due Date, Assigned By.
- **Work Submission** section, which changes with the status.
- **Bottom action bar**, which changes with the status **and** with your rights (14.12).

**To Do**

| Who | Work Submission | Buttons |
|---|---|---|
| Assignee (PM view or My Tasks) | "Click 'Start Task' below to begin working on this task." If the task was sent back: reviewer feedback (Reviewer, Reviewer Comments), the last submission, and the form | **Start Task** (moves it to In Progress) |
| Managers (TL/PL/DA/SA view, or Team Tasks) | The same information, read-only. Team Tasks shows "This task requires revision. The assignee will submit updated work when ready." | **Reassign Task**, **Edit Task** |

**In Progress**

| Who | Work Submission | Buttons |
|---|---|---|
| Assignee | Form with **Upload Files** (optional label each), **Working URL(s)** (Label + https://…, **Add another URL**) and **Submission Notes**. Reviewer feedback is shown if the task was reverted. | **Save Draft** ("Draft saved successfully"); **Submit for Review** (needs at least one file, URL or note; "Work submitted for review successfully"; moves the task to **Under Review**) |
| Managers | Team Tasks: "This task is currently in progress. The assignee will submit their work for review when ready." plus the last submission | **Reassign Task**, **Edit Task** |

**Under Review**

| Who | Work Submission | Buttons |
|---|---|---|
| Assignee | "This submission is currently awaiting review. No edits allowed." Submitted By, Submitted Date, Notes, Files, Working URLs | None (wait for the review) |
| Reviewers (TL/PL/DA/SA view, or Team Tasks) | The same details | **Approve**: "Approve Task", **Approval Comment \*** (required), **Confirm Approval** → the task becomes **Completed**. **Revert with Feedback**: **Feedback Comment \*** (required), **Revert Task** → the task goes back to the assignee marked **Revision Requested**. |

Review badges: "Awaiting Project Lead Review" in PM view, "Awaiting Team Lead Review" in other views.

**Completed**

| Who | Work Submission | Buttons |
|---|---|---|
| Everyone | "✅ Submission Approved" (click to see the history), Approved By, Approval Date, Notes, Files | None. "Read-only view — no actions available" |

**Always available:**
- **View history** opens **Submission History**. Each version (Version 1, 2, …) shows its status (Approved, Rejected, Awaiting … Review), date, submitter, files, URLs, notes, reviewer and comment.
- Closing with unsaved submission data shows "Unsaved Changes": **Keep Editing** or **Discard & Close**.

```
To Do --Start Task--> In Progress --Submit for Review--> Under Review --Approve--> Completed
                          ^                                   |
                          +------ Revert with Feedback -------+   (task marked "Revision Requested")
```

### 14.12 Task Detail drawer: buttons by where you open it

| Where you open the drawer | Role / view | To Do | In Progress | Under Review | Completed |
|---|---|---|---|---|---|
| **My Tasks** | Anyone (your own tasks) | Start Task | Save Draft, Submit for Review | No buttons (no reviewing here) | Read-only |
| **Team Tasks** | TL (only Team Leads have Team Tasks in the sidebar) | Reassign Task, Edit Task | Reassign Task, Edit Task | **Approve**, **Revert with Feedback** | Read-only |
| **Project Detail (Execution)** | PM view | Start Task | Save Draft, Submit for Review | No buttons | Read-only |
| **Project Detail (Execution)** | TL, PL, DA, SA view | Reassign Task, Edit Task | Reassign Task, Edit Task | **Approve**, **Revert with Feedback** | Read-only |
| **Project Detail (Planning)** | — | The drawer does not open; use Edit Task on the row | | | |

> **To review work**, use **Team Tasks**, or open the project in a manager view (Team, Department or All Projects, or My Work for a project you lead). **To do your own work**, use **My Tasks**.

### 14.13 My Tasks (full detail)

- **Opens from:** Dashboard menu → **My Tasks** (`/mytasks`).
- **Who:** everyone with a ProjectHub role. Shows only tasks **assigned to you**.
- **KPI cards:** Open Tasks, Due Today, Due This Week, Overdue Tasks.
- **Search:** "Search tasks...".
- **Filters:**
  - Project, Priority, Status (To Do, In Progress, Under Review, Completed), Due Date (Due Today, Due This Week, Overdue).
  - The drawer closes after each choice. Buttons: **Clear All**, **Close**.
- **Board view** (default): columns **To Do, In Progress, Under Review, Completed**, each with a count.
  - **Drag rules:** To Do → In Progress ✓; In Progress → To Do ✓; In Progress → Under Review ✓. Anything else shows "This transition is not allowed." Under Review and Completed cards are locked.
  - **Cards** show the task, project, priority, review stage, progress, and due date (red if overdue, amber if due today).
- **List view:** Task, Project, Priority, Status, Review Stage, Due Date, Progress, Last Updated, **View**.
- **Clicking a task** opens the drawer with the **assignee** buttons (14.12).
- **Project link:** opens the project in **PM view**. **Back to My Tasks** returns here.
- **Empty states:** "No Tasks Assigned — You're all caught up!", or "No Tasks Found" with **Clear Filters**.

### 14.14 Team Tasks (full detail)

- **Opens from:** **Manage My Team → ProjectHub → Team Tasks** (`/teamtasks`). Only Team Leads see this entry.
- **Who:** Team Leads (and SA, DA, PL). Shows your team members' tasks.
- **KPI cards:** the same as My Tasks.
- **Search:** "Search team tasks...".
- **Filters:** **Team Member**, Project, **Project Lead**, Priority, **Revision Requested** (Revision Requested / No Revision), Status, **Overdue** (Overdue Only / Not Overdue), Due Date.
- **Board and list:** the same as My Tasks, with the same drag rules.
- **Clicking a task** opens the drawer with **manager / reviewer** buttons (14.12):
  - To Do and In Progress: Reassign / Edit Task.
  - Under Review: **Approve** / **Revert with Feedback**.
  - The submission section is read-only.
- **Project link:** opens the project in **Team Lead view**. **Back to Team Tasks** returns here.
- **Messages:** "Task approved successfully", "Task reverted with feedback", "Task status updated successfully".

### 14.15 Project Discussion (full detail)

The complete guide to Project Discussion is in **section 6.6**. In short:

- **Where:** the vertical **Project Discussion** tab on the right edge of Project Detail, with a red unread badge (up to 99+).
- **Who:** everyone on the project, in every view and every status (Project Member, Project Lead, Team Lead, Department Admin, Super Admin).
- **What you can send:** text, @name and @all mentions, files (Document, Photo, Video, Audio File), and voice notes. Replies can have the same.
- **Reactions:** one emoji per person per message; the same emoji again removes it, a different one replaces it.
- **Delete:** your own messages only ("This message will be deleted for everyone."). No edit.
- **Live:** new messages, mentions and reactions appear instantly; ticks show Sending, Delivered and Read.
- **History:** 20 threads at a time; scroll up for older ones.
- Files shared here also appear in **Project Files → Discussion**.

### 14.16 Project Files (full detail)

- **Where:** Project Detail → **View Files**. Everyone can use it.
- **Contents:** every project file, newest first, with a total count.
- **Search:** "Search files...".
- **Source filters:** All, Brief, Task Submission, Discussion, Project Document.
- **Each file:** icon, name, source, task (for submissions), uploader, date, size, and **View** / **Download**.

### 14.17 Quick answers

| Question | Answer |
|---|---|
| Who can activate a project? | SA, DA, TL, PL (not PM), and only in Planning. |
| What is needed before activating? | A Project Lead must be assigned and at least one Team Member must be added. |
| Who can add or edit milestones and tasks? | SA, DA, TL, PL, in Planning only. |
| Can I add a task after activation? | Not from Project Detail. Managers can change existing tasks with **Edit Task** in the drawer. |
| Who can delete a task or milestone? | Editors, in Planning. The delete is immediate, with no confirmation. |
| Who can add an issue? | Editors, from the task row ⋮ in Planning. |
| Who can add or resolve a risk? | Editors (SA, DA, TL, PL), in any status. |
| Who can start or submit a task? | The assignee, from My Tasks or in PM view. |
| Who can approve or revert a task? | TL, PL, DA, SA, from Team Tasks or a manager view. |
| Who can change the project lead? | SA, DA, TL. |
| Who can manage the team? | SA, DA, TL, PL. |
| Who can put a project on hold or resume it? | SA, DA, TL, PL. |
| Who can edit project details? | SA on any project; TL or DA on projects they created. Not for Draft or Completed projects. |
| Who can use Project Discussion and Files? | Everyone on the project. |

### 14.18 Project Detail: What Each Role Can Do (Role-by-Role Guide)

**Question this answers:** "What can a Project Member do on Project Detail?", "What can a Project Lead do?", "What can a Team Lead, Department Admin or Super Admin do?", "Which actions show in the ⋮ menu for my role and the project's status?", "Who can Add Milestone, Add Task, Add Risk?"

> **How the page knows your role:** Project Detail reads the **view** in its link (`/projectdetail?id=<id>&view=<Role>`). The view comes from the menu you used: **All Projects** = SuperAdmin, **Department Projects** = DepartmentAdmin, **Team Lead Projects** = TeamLead. In **My Work → My Projects**, a project you **lead** opens as **ProjectLead** and every other project opens as **ProjectMember**.

#### 14.18.1 Project status shown in the header

The header badge shows the **first** of these that applies: **Draft**, then **On Hold**, then **Archived**, then the real status (**Planning**, **In Progress**, **Completed**). All the rules below use this badge value.

#### 14.18.2 The header ⋮ menu: by role and by status

A dash means the item is not shown. "Creator" means the person who created the project. "If A" means Archive Rules item **Allow archived project restoration** is On (section 10).

| Item in the ⋮ menu | Project Member | Project Lead | Team Lead / Department Admin | Super Admin |
|---|---|---|---|---|
| **Edit Project** | — | — | Only on projects **they created** | **Any** project |
| **Change Project Lead** | — | — | Yes | Yes |
| **Manage Team** | — | Yes | Yes | Yes |
| **Put on Hold** / **Resume Project** | — | Yes | Yes | Yes |
| **Archive Project** | — | — | Only **If A** | **Always** |
| **Unarchive Project** | — | — | Department Admin: **If A and** "Allow Department Administrators to restore" is On. Team Lead: never. | **Always** |

| Project status | What the ⋮ menu shows (for a role that is allowed) |
|---|---|
| **Draft** | **No ⋮ menu at all** (for every role). A Draft is finished from the Create wizard (Edit Draft in the list). |
| **Planning** | Edit Project, Change Project Lead, Manage Team, **Put on Hold**, Archive Project |
| **In Progress** | Edit Project, Change Project Lead, Manage Team, **Put on Hold**, Archive Project |
| **On Hold** | Edit Project, Change Project Lead, Manage Team, **Resume Project** (instead of Put on Hold), Archive Project |
| **Completed** | Change Project Lead, Manage Team, Archive Project. **No Edit Project** and **no Put on Hold.** A Project Lead sees only **Manage Team**. |
| **Archived** | Only **Edit Project** (if allowed) and **Unarchive Project** (if allowed). Nothing else is shown. |

The separator line in the menu comes before **Archive Project** / **Unarchive Project**.

**Activate Project button** (next to the ⋮ menu): shown to **Super Admin, Department Admin, Team Lead and Project Lead** (never to a Project Member), and **only while the project is in Planning**. It is **locked** (grey, with a lock) until a **Project Lead** and at least one **team member** are assigned. A Draft, On Hold, In Progress, Completed or Archived project has no Activate button.

#### 14.18.3 Change Project Lead, Manage Team, Put on Hold, Archive: what happens

| Action | Steps and result |
|---|---|
| **Change Project Lead** (Super Admin, Department Admin, Team Lead) | The dialog shows the **Current Project Lead**. Choose a **New Project Lead \*** (required, searchable list "Search or select a project lead...") and click **Change Lead** (disabled until one is chosen). Message "Project lead changed successfully". This also fulfils the "Project Lead Assigned" activation requirement. |
| **Manage Team** (Super Admin, Department Admin, Team Lead, Project Lead) | Shows the team with badges (**Team Lead**, **Project Lead**, **Team Member**). **Add:** pick a person in **Add New Member** ("Select a member to add"; the list shows the project's and the department's people) → **Add** → **Save Changes**. Message "N team member(s) added successfully". **Remove (✕):** the Team Lead and Project Lead cannot be removed; removing a Team Member only changes the list on screen and is **not saved yet**. |
| **Put on Hold** (Super Admin, Department Admin, Team Lead, Project Lead) | Confirm in "Put Project on Hold". "Once on hold, all project-level actions will be disabled for everyone." No reason is asked. The badge becomes **On Hold**. |
| **Resume Project** (same roles; only On Hold) | One click, no dialog. Message "Project resumed successfully". |
| **Archive Project** | Confirm in "Archive Project". "The project will be put on hold and then archived. All project actions will be disabled." |
| **Unarchive Project** | One click. Message "Project unarchived successfully". |

#### 14.18.4 What each role does on Project Detail

**Project Member (PM)**
- Sees the Overview, the Planning/Execution tab, Activity, **View Files** and **Project Discussion**. All planning blocks are **view only**.
- **No header menu and no Activate button.**
- Cannot add or edit milestones or tasks, assign tasks, add issues or risks, edit the Project Brief, or approve work.
- On an active project they can **open a task** (Execution tab). In the task drawer, **their own** task shows **Start Task** (To Do) and **Save Draft / Submit for Review** (In Progress). **Under Review** and **Completed** are view only (section 14.11).
- Can use Project Discussion and Project Files.

**Project Lead (PL)** — for the projects they lead
- Everything a PM can see, plus **editing rights** ("Editors").
- **Header:** **Activate Project** (Planning), and the ⋮ menu with **Manage Team** and **Put on Hold / Resume Project**. No Edit Project, Change Project Lead or Archive.
- **Planning tab** (project in Planning): **Add Milestone**, edit / delete / reorder milestones, **Add Task**, edit / delete / duplicate tasks, assign tasks (inline or **Bulk Assign Tasks**), **Add Issue**, drag tasks.
- **Any status:** **Add Risk**, **Resolve** and **Delete** an open risk; edit the **Project Brief**.
- **Execution tab** (project active): **Approve** and **Revert with Feedback** for tasks Under Review; **Reassign Task** and **Edit Task** for To Do and In Progress tasks (Reassign is not saved yet).
- Cannot create projects or change the project lead.

**Team Lead (TL), Department Admin (DA) and Super Admin (SA)**
- All the Project Lead abilities, plus:
  - **Change Project Lead.**
  - **Edit Project** — **SA** on any project; **TL and DA** only on projects **they created**. Not for Draft or Completed.
  - **Archive Project** — **SA always**; **TL and DA** only if **Allow archived project restoration** is On. **Unarchive:** SA always; DA only with both archive switches On; TL never.
- **Create New Project** and **Import Projects** are on the projects list, not on Project Detail (section 6.1).

#### 14.18.5 What can be added or changed, by project status

"Editors" are PL, TL, DA and SA. A Project Member never edits.

| Action | Draft | Planning | In Progress | On Hold | Completed | Archived |
|---|---|---|---|---|---|---|
| Open the project | Opens the Create wizard | Yes | Yes | Yes | Yes | Yes |
| **Add Milestone** | — | Editors | — | — | — | — |
| Edit / Delete / Reorder Milestone | — | Editors | — | — | — | — |
| **Add Task**, Edit / Delete / Duplicate Task on the row | — | Editors | — | — | — | — |
| **Assign Task** (inline) and **Bulk Assign Tasks** | — | Editors | — | — | — | — |
| **Add Issue** (task row ⋮) | — | Editors | — | — | — | — |
| Drag tasks (reorder or move between milestones) | — | Editors | Editors | Editors | — | — |
| **Add Risk** / **Resolve** / **Delete** risk | — | Editors | Editors | Editors | Editors | Editors |
| Edit Project Brief | — | Editors | Editors | Editors | Editors | Editors |
| Open the **Task Detail drawer** | — | No (use Edit Task on the row) | Yes | Yes | Yes (read only) | Yes |
| **Start Task** / **Save Draft** / **Submit for Review** | — | — | The task's assignee | The screen does not block it; the server decides | — | — |
| **Approve** / **Revert with Feedback** | — | — | Editors (task Under Review) | Same as above | — | — |
| **Reassign Task** / **Edit Task** (in the drawer) | — | — | Editors (task To Do or In Progress) | Same as above | — | — |
| **Activate Project** | — | Editors, once Lead and members exist | — | — | — | — |

> **On Hold and Archived projects:** the screen does **not** hide the planning and task buttons; the server decides which actions are allowed. The archived and on-hold badge tells users the project is paused.

#### 14.18.6 Quick answers

- **Who can Add Task and Add Milestone?** Editors (PL, TL, DA, SA), **only while the project is in Planning**.
- **Who can Add Risk?** Editors, in any status.
- **Who can Add Issue?** Editors, from the task row ⋮ menu in Planning.
- **Who can change the Project Lead?** SA, DA, TL (not the Project Lead).
- **Who can manage the team?** SA, DA, TL, PL.
- **Who can archive?** SA always; TL and DA when archive restoration is allowed. PL and PM never.
- **Why do I see no ⋮ menu?** You are a Project Member, or the project is a Draft, or no action is available for your role in this status.

### 14.19 Create Project and Edit Project (CreateProjectWizard): rules by role, status and template

**Question this answers:** "Which steps does Create Project / Edit Project have?", "What is required on each step?", "Whom must I mark: Department Admin, Team Lead or Project Lead?", "Do I need a category for a template project and for a blank project?"

**Create Project and Edit Project use the same wizard** (`CreateProjectWizard`). Title: **Create New Project** or **Edit Project**. Four steps: **1 Structure → 2 Project Info → 3 Team → 4 Review** ("Step N of 4").

**Where each opens**
- **Create New Project:** projects list header (Super Admin, Department Admin, Team Lead views only). Project Lead and Project Member do not see it.
- **Edit Project:** Project Detail ⋮ → **Edit Project**, or ⋮ **Edit** / **Edit Draft** on the projects list. In edit mode the wizard loads the saved data.

#### Step 1 — Structure (how the project is built)

You must choose one of two modes (**Next** stays disabled until you do):

| | **Create from Project Template** | **Create Blank Project** |
|---|---|---|
| Meaning | "Start with pre-built milestones and tasks" | "Start from scratch with no milestones or tasks" |
| **Project Category** | **Required** (\*). Only **active** Categories are listed. | **Required to continue.** The field says "Select a category (optional)", but **Next is disabled until a category is chosen.** |
| **Project Template** | **Required** (\*). The list stays disabled until a Category is chosen ("Select a category first..."). It then shows only the templates of that Category, with a search box and a preview (milestones, tasks, timeline). | Not used |
| Changing the Category | Clears the chosen template | — |
| Result | The project starts with the template's milestones and tasks | An empty project; add milestones and tasks later on the Planning tab |

**Template mode needs both the Category and the Template; blank mode needs only the Category.**

**Edit rule for Step 1:** it can be changed only while the project is a **Draft** or in **Planning**. For **In Progress, On Hold, Completed** (and Archived) projects, Step 1 is **locked**: the fields are greyed out and the header says "Project structure cannot be modified for active projects".

#### Step 2 — Project Info

| Field | Required? |
|---|---|
| **Project Name** | **Required** |
| **Project Type** | **Required** (the first enabled type is pre-selected) |
| **Priority** | **Required** (the first active Priority Label is pre-selected) |
| Description, Start Date (defaults to today), Target Completion Date | Optional |
| Client Organization, Client Contact | Optional; shown for the **Client** type |
| Attachments | Optional (files with labels, up to 10 MB each) |

#### Step 3 — Team: who must be marked (this depends on the view you use)

| You are using the... view | **Department Admin** field | **Project Team Lead** field | **Project Lead** field | **Project Members** |
|---|---|---|---|---|
| **Super Admin** (All Projects) | Shown, marked \*, but **not checked** by Next | **Required** | Optional | Optional |
| **Department Admin** (Department Projects) | Not shown (you are the Department Admin; your own ID is sent) | **Required** | Optional | Optional |
| **Team Lead** (Team Lead Projects) | Shown, marked \*, but **not checked** by Next | Not shown (you are the Team Lead) | **Required** | Optional |

- **Next on Step 3 stays disabled until the required person is chosen:** the **Project Team Lead** for Super Admin and Department Admin, or the **Project Lead** for Team Lead.
- The **Project Lead** list depends on the chosen Team Lead. **Select Whole Team** selects every available member; a counter shows how many.
- These rules are the same for **Create** and **Edit**; in Edit they follow the view in the Project Detail link.
- **Project Lead and at least one member are not needed to create** a project when you are Super Admin or Department Admin, but they **are needed to Activate** it (section 14.5).

#### Step 4 — Review

Shows Project Information, Project Structure, Project Team, Planned Timeline and (Client projects) Client Details. A banner says the project will be created in **Planning** status.

#### Footer buttons

| Button | Notes |
|---|---|
| **Cancel** | Asks to confirm if you entered data: "Continue without saving?" → **Yes, Close** or **Save Draft** |
| **Save as Draft** | Needs only a **Project Name**. No other step is checked. Saves the project as a **Draft**. |
| **Previous** / **Next** | **Next** is disabled until the current step is valid (above) |
| **Create Project and Planning** (new project) | Creates the project in **Planning** and opens its Planning tab |
| **Update Project and Planning** (editing a **Draft** or **Planning** project) | Saves the changes |
| **Update Project** (editing an active, On Hold or archived project) | Saves the changes (Step 1 stays locked) |

#### Summary: what is required

| To... | Required |
|---|---|
| **Save as Draft** | Project Name |
| **Pass Step 1** | Template mode: Category **and** Template. Blank mode: Category. |
| **Pass Step 2** | Project Name, Project Type, Priority |
| **Pass Step 3** | SA / DA: Project Team Lead. TL: Project Lead |
| **Activate the project later** | A Project Lead and at least one team member |
