#!/usr/bin/env python3
"""Herramienta de línea de comandos para comparar followers y following de Instagram."""

import json
import sys

try:
    import tkinter as tk
    from tkinter import filedialog
except ImportError:
    tk = None

def load_usernames(filepath):
    """Devuelve un set con los usernames del archivo JSON exportado por Instagram."""
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)

    usernames = set()

    # Si el JSON viene con una estructura de diccionario
    if isinstance(data, dict):
        for key in ('relationships_following', 'relationships_followers'):
            if key in data:
                data = data[key]

    # Lista de objetos con string_list_data
    if isinstance(data, list):
        for entry in data:
            if isinstance(entry, dict) and 'string_list_data' in entry:
                string_data = entry['string_list_data']
                if isinstance(string_data, list) and string_data:
                    value = string_data[0].get('value')
                    if value:
                        usernames.add(value)

    return usernames

def ask_file(label):
    """Abre un diálogo para seleccionar archivo o solicita ruta por consola."""
    if tk:
        root = tk.Tk()
        root.withdraw()
        path = filedialog.askopenfilename(
            title=f'Seleccione {label}',
            filetypes=[('JSON files', '*.json'), ('Todos los archivos', '*.*')]
        )
        root.destroy()
        if path:
            return path
    # Fallback si no hay tkinter o se cancela
    return input(f'Ingrese la ruta al archivo {label}: ').strip()

def main():
    print('=== Instagram Comparer ===\n')

    followers_file = ask_file('followers_1.json')
    following_file = ask_file('following.json')

    try:
        followers = load_usernames(followers_file)
        following = load_usernames(following_file)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f'Error leyendo archivos: {exc}')
        sys.exit(1)

    not_following_back = following - followers
    not_followed_by_me = followers - following

    if not_following_back:
        print('🔴 Usuarios a los que seguís y que NO te siguen de vuelta:')
        for user in sorted(not_following_back):
            print('  -', user)
    else:
        print('👏 ¡Todos los que seguís te devuelven el follow!')

    if not_followed_by_me:
        print('\n🟢 Usuarios que te siguen y que VOS no seguís de vuelta:')
        for user in sorted(not_followed_by_me):
            print('  -', user)

if __name__ == '__main__':
    main()
