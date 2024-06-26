# 🗣️Project: Spartamarket 2.0
- This project is a second-hand item trading platform built with Django, allowing users to register, search, and interact with items, along with administrative management capabilities.
<br>

## 🔧 Project Update Summary
- made improvements to the profile page to display liked items. Now, users can see a list of items they have liked on their profile page.
- latest update introduces a token-based authentication system, ensuring secure user authentication during signup, login, and profile access. Additionally, we've clarified mandatory and optional fields during signup, enhanced login security, and restricted profile access to logged-in users for improved privacy.
<br>

## 👨‍🏫 Project Introduction
- This project is a platform for trading second-hand items. 
Users can register items, search for items, and view items registered by other users. 
Additionally, users can like items and follow sellers. 
Administrators have the ability to manage posts and comments. 
This allows users to conveniently participate in second-hand item transactions.
<br>

## ⏲️ Development time
- 2024.04.15(월) ~ 2023.04.19(금)
- update: ~ 2023.05.02(목)
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
### main page
![image](https://github.com/daengdaengjoa/spartamarket/assets/156053546/0ab16084-944e-4af1-847e-cbbc0c32c1b9)
### profile page
![image](https://github.com/daengdaengjoa/spartamarket/assets/156053546/8bb6c6d5-34cd-49f6-9d88-ed85f3a5f672)
### writing page
![image](https://github.com/daengdaengjoa/spartamarket/assets/156053546/85edb781-4220-4865-b609-b70e8043874e)
### Item detail page
![image](https://github.com/daengdaengjoa/spartamarket/assets/156053546/fce7b08f-a3fe-476b-9495-6c63097a2ff4)





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
