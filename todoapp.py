import firebase_admin
from firebase_admin import credentials, db, auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\Eli\OneDrive\Desktop\Hello World\Cloud Databases\todo-f907b-firebase-adminsdk-qk6qd-08294ba60d.json")  # Update path
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://todo-f907b-default-rtdb.firebaseio.com/'
})

# Function to sign up a new user with email and password
def sign_up(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        print(f"Successfully created user with email: {user.uid}")
        return user
    except Exception as e:
        print(f"Error creating user: {e}")
        return None

# Function to sign in an existing user with email and password
def sign_in(email, password):
    try:
        user = auth.get_user_by_email(email)
        print(f"Successfully signed in user: {user.uid}")
        return user
    except Exception as e:
        print(f"Error signing in user: {e}")
        return None

# Function to sign out the current user
def sign_out():
    try:
        user = auth.current_user
        print(f"Successfully signed out user: {user.uid}")
    except Exception as e:
        print(f"Error signing out user: {e}")

# Function to add a task for the current user
def add_task(user, content):
    try:
        if user:
            ref = db.reference(f'tasks/{user.uid}')
            new_task_ref = ref.push({'content': content})
            print(f'Task added: {content}')
        else:
            print("User not signed in.")
    except Exception as e:
        print(f"Error adding task: {e}")

# Function to get tasks for the current user
def get_tasks(user):
    try:
        if user:
            ref = db.reference(f'tasks/{user.uid}')
            tasks = ref.get()
            if tasks:
                print("Tasks:")
                for task_id, task in tasks.items():
                    print(f"{task_id}: {task['content']}")
            else:
                print("No tasks found")
        else:
            print("User not signed in.")
    except Exception as e:
        print(f"Error getting tasks: {e}")

# Function to delete a task for the current user
def delete_task(user, task_id):
    try:
        if user:
            ref = db.reference(f'tasks/{user.uid}')
            ref.child(task_id).delete()
            print(f'Task deleted: {task_id}')
        else:
            print("User not signed in.")
    except Exception as e:
        print(f"Error deleting task: {e}")

# Main function
def main():
    user = None  # Initialize user variable

    while True:
        print("\n1. Sign Up")
        print("2. Sign In")
        print("3. Sign Out")
        print("4. Add Task")
        print("5. View Tasks")
        print("6. Delete Task")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = sign_up(email, password)
        elif choice == '2':
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = sign_in(email, password)
        elif choice == '3':
            sign_out()
            user = None  # Reset user variable after sign out
        elif choice == '4':
            if user:
                content = input("Enter task content: ")
                add_task(user, content)
            else:
                print("User not signed in.")
        elif choice == '5':
            if user:
                get_tasks(user)
            else:
                print("User not signed in.")
        elif choice == '6':
            if user:
                task_id = input("Enter task ID to delete: ")
                delete_task(user, task_id)
            else:
                print("User not signed in.")
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()