import os
import json


def fix_library():
    appdata = os.environ.get('APPDATA', '')
    texts_dir = os.path.join(appdata, "Elgato", "CameraHub", "Texts")
    settings_path = os.path.join(appdata, "Elgato", "CameraHub", "AppSettings.json")

    if not os.path.exists(texts_dir):
        print(f"Could not find Texts folder: {texts_dir}")
        return

    if not os.path.exists(settings_path):
        print(f"Could not find AppSettings.json: {settings_path}")
        return

    # Collect all GUIDs from .json files in the Texts folder
    guids_found = []
    for i, filename in enumerate(sorted(os.listdir(texts_dir))):
        if filename.lower().endswith(".json"):
            filepath = os.path.join(texts_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                guid = data.get("GUID")
                if guid:
                    guids_found.append(guid)
                    # Fix index value to ensure uniqueness
                    data["index"] = i
                    with open(filepath, 'w', encoding='utf-8') as fw:
                        json.dump(data, fw, indent=4, ensure_ascii=False)
            except Exception as e:
                print(f"Could not read {filename}: {e}")

    print(f"Found {len(guids_found)} scripts in the Texts folder.")

    # Read AppSettings.json
    with open(settings_path, 'r', encoding='utf-8') as f:
        settings = json.load(f)

    key = "applogic.prompter.libraryList"
    current_list = settings.get(key, [])
    print(f"Scripts in libraryList before: {len(current_list)}")

    # Add any missing GUIDs
    added = 0
    for guid in guids_found:
        if guid not in current_list:
            current_list.append(guid)
            added += 1

    settings[key] = current_list
    print(f"Added {added} missing scripts to libraryList.")
    print(f"Total scripts in libraryList now: {len(current_list)}")

    # Create a backup of the original AppSettings.json
    backup_path = settings_path + ".backup"
    with open(settings_path, 'r', encoding='utf-8') as f:
        original = f.read()
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(original)
    print(f"Backup saved to: {backup_path}")

    # Save the updated AppSettings.json
    with open(settings_path, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=4, ensure_ascii=False)
    print("AppSettings.json updated successfully! Please restart Camera Hub.")


if __name__ == "__main__":
    fix_library()
