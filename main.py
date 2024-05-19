import json
from pathlib import Path

MENU_OPTIONS = (
    "Ajouter une tâche",
    "Supprimer une tâche",
    "Marquer une tâche comme complétée",
    "Afficher les tâches",
    "Quitter"
)

file_task = Path("tasks.json")

def load_tasks():
    if file_task.exists():
        with file_task.open("r", encoding="UTF-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with file_task.open("w", encoding="UTF-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def display_menu():
    print("\nMenu:")
    for i, option in enumerate(MENU_OPTIONS, start=1):
        print(f"{i}. {option}")
    return input("Votre choix : ")

while True:
    print("-" * 50)
    choix_menu = display_menu()
    print("-" * 50)
    if choix_menu not in [str(i) for i in range(1, len(MENU_OPTIONS) + 1)]:
        print("Ce n'est pas un menu valide !")
        continue

    if choix_menu == "1":
        try:
            task_description = input("Entrez le nom d'une tâche à ajouter : ")
            tasks = load_tasks()
            tasks.append({"description": task_description, "completed": False})
            save_tasks(tasks)
            print(f"La tâche '{task_description}' a bien été ajoutée !")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")

    elif choix_menu == "2":
        try:
            task_description = input("Entrez le nom d'une tâche à supprimer : ")
            tasks = load_tasks()
            task_found = False
            for task in tasks:
                if task["description"] == task_description:
                    tasks.remove(task)
                    save_tasks(tasks)
                    print(f"La tâche '{task_description}' a bien été supprimée !")
                    task_found = True
                    break
            if not task_found:
                print(f"La tâche '{task_description}' n'existe pas !")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")

    elif choix_menu == "3":
        try:
            task_description = input("Entrez le nom d'une tâche à marquer comme complétée : ")
            tasks = load_tasks()
            task_found = False
            for task in tasks:
                if task["description"] == task_description:
                    task["completed"] = True
                    save_tasks(tasks)
                    print(f"La tâche '{task_description}' a bien été marquée comme complétée !")
                    task_found = True
                    break
            if not task_found:
                print(f"La tâche '{task_description}' n'existe pas !")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")

    elif choix_menu == "4":
        try:
            tasks = load_tasks()
            if not tasks:
                print("Aucune tâche à afficher.")
            else:
                for i, task in enumerate(tasks, start=1):
                    status = '[X]' if task["completed"] else '[ ]'
                    print(f"{i}. {status} {task['description']}")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")

    elif choix_menu == "5":
        print("Au revoir !")
        break
