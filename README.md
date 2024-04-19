# 🗣️Project: Spartamarket
#### This project is a second-hand item trading platform built with Django, allowing users to register, search, and interact with items, along with administrative management capabilities.
<br>

## 👨‍🏫 Project Introduction
This project is a platform for trading second-hand items. 
Users can register items, search for items, and view items registered by other users. 
Additionally, users can like items and follow sellers. 
Administrators have the ability to manage posts and comments. 
This allows users to conveniently participate in second-hand item transactions.
<br>

## ⏲️ Development time
- 2024.04.15(월) ~ 2023.04.19(금)
- 기능구현
<br>

## 🧑‍🤝‍🧑 Development member
- **김준수**
<br>

## 💻 Development Environment
- **Programming Language** : Python 3.x
- **Web Framework** : Django
- **Template Engine** : Django template
- **Database** : SQLite (for development and testing)
- **IDE** : Visual Studio Code
- **Version Control** : Git, GitHub
<br>

## ⚙️ Technology Stack
- **Frontend** : HTML, CSS, JavaScript
- **Backend** : Django
- **Database ORMR** : Django ORM
- **Idea Brainstorming Tools and Environments** : Slack, Zep, Notion, figma
<br>

## 📝 Project Architecture
![image](https://github.com/daengdaengjoa/spartamarket/assets/156053546/7c839299-8dc0-4c2c-a4a4-741d5dd3945f)

<br>

## 📌 Key Features

### 1. Item CRUD Operations
-Users can create new items for sale and view all items listed on the platform.
-Items can be edited or deleted by their respective owners on the item detail view page.
### 2. User Profile
-Each user has a profile page displaying their personal information, including username, registration date, and statistics such as the number of items listed, liked items, followers, and following count.
### 3. Sorting Items
-Users can sort items on the main page by popularity, newest listings, and most liked items.
### 4. Item Detail View
-Detailed information about each item is displayed on its individual detail page, including title, description, owner, price, number of likes, and other relevant details.
### 5. Like Feature
-Users can like items they are interested in on the item detail view page.
-The 'Like' button toggles to 'Unlike' upon clicking and can be undone, allowing users to like an item only once.
### 6. Follow Users
-Users can follow other users on the platform to stay updated with their listings and activities.
-Followed users' items appear on the follower's main page for easy access.
### 7. Authentication and Authorization
-User authentication is required for creating, editing, or deleting items, as well as accessing certain features like user profiles.
-Administrators have special permissions to manage user accounts and listings, ensuring platform integrity.
### 8. User Interaction
-Users can interact with each other through likes, follows, and comments on items and user profiles, fostering a sense of community within the platform.
     

<br> 

## ✒️ API

| Endpoint                 | Method | Description                        | Request Body                           | Response Body                          |
|--------------------------|--------|------------------------------------|----------------------------------------|----------------------------------------|
| `/api/items/`            | GET    | Get all items                      | N/A                                    | Array of item objects                  |
| `/api/items/<item_id>/`  | GET    | Get details of a specific item     | N/A                                    | Item object                            |
| `/api/items/`            | POST   | Create a new item                  | JSON object with item details          | Created item object                    |
| `/api/items/<item_id>/`  | PUT    | Update details of a specific item  | JSON object with updated item details  | Updated item object                    |
| `/api/items/<item_id>/`  | DELETE | Delete a specific item             | N/A                                    | Success message                        |
| `/api/users/`            | GET    | Get all users                      | N/A                                    | Array of user objects                  |
| `/api/users/<user_id>/`  | GET    | Get details of a specific user     | N/A                                    | User object                            |
| `/api/users/`            | POST   | Create a new user                  | JSON object with user details          | Created user object                    |
| `/api/users/<user_id>/`  | PUT    | Update details of a specific user  | JSON object with updated user details  | Updated user object                    |
| `/api/users/<user_id>/`  | DELETE | Delete a specific user             | N/A                                    | Success message                        |

- API 명세서 : <>
